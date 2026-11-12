<?php
// Apply the approved evidence-review change set to one post (POST=<id> DIR=<folder with changes.json>). Each change replaces one block
// attribute on one line, and only if the current value still matches what the change set was drafted from.
// GROUPS limits which change groups run (comma list: approved,renumber,related). DRY=1 reports without writing.
$dir = getenv('DIR');
$id = (int) getenv('POST');
$changes = json_decode(file_get_contents("$dir/changes.json"), true);
$groups = explode(',', getenv('GROUPS') ?: 'approved,renumber,related');
$dry = getenv('DRY') === '1';

$c = get_post_field('post_content', $id);
$lines = explode("\n", $c);
$err = [];
$n = 0;
foreach ($changes as $ch) {
	if (!in_array($ch['group'], $groups, true)) continue;
	$k = $ch['line'];
	if (!preg_match('#^(<!-- wp:flexlayout/[\w-]+ )(\{.*\})( /-->)$#', $lines[$k], $m)) { $err[] = "line $k is not a block"; continue; }
	$attrs = json_decode($m[2], true);
	if (($attrs[$ch['field']] ?? null) !== $ch['old']) { $err[] = "line $k {$ch['field']} changed since the change set was drafted"; continue; }
	$attrs[$ch['field']] = $ch['new'];
	$lines[$k] = $m[1] . serialize_block_attributes($attrs) . $m[3];
	$n++;
}
if ($err) { echo "STOP, nothing written:\n" . implode("\n", $err) . "\n"; exit(1); }
$new = implode("\n", $lines);
if (serialize_blocks(parse_blocks($new)) === '') { echo "STOP: content does not parse\n"; exit(1); }
if ($dry) { echo "DRY: $n changes ready, length " . strlen($c) . " -> " . strlen($new) . "\n"; exit(0); }
@mkdir("$dir/bak");
file_put_contents("$dir/bak/$id-" . gmdate('Ymd\THis') . '.html', $c);
$r = wp_update_post(wp_slash(['ID' => $id, 'post_content' => $new]), true);
if (is_wp_error($r)) { echo 'ERROR ' . $r->get_error_message() . "\n"; exit(1); }
$rev = function_exists('acf_get_post_latest_revision') ? acf_get_post_latest_revision($id) : null;
if ($rev) foreach (['hero_image', '_hero_image', 'nav_color', '_nav_color'] as $f) update_metadata('post', $rev->ID, $f, get_post_meta($id, $f, true));
clean_post_cache($id);
echo "OK: $n changes written to post $id (" . get_post_status($id) . ")\n";
