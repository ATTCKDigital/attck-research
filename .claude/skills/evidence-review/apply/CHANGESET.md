# Drafting an article change set

Turn one article's approved edits into an exact, machine-checkable change set. Drafting never writes to WordPress;
`scripts/apply_changes.py` does that, after the user has approved the change set.

## Inputs (in `work/NN/`)

- `claims.json`, `pass4.json`, `pass5.json` (overrides pass 4 per claim), `meta.json` (post id, Sources), `verify.json`.
- `responses.txt`: the user's pasted Copy Responses text. APPLY uses the claim's `suggested_edit`; APPLY WITH CHANGES
  uses the user's wording; KEEP AS WRITTEN and DISCUSS are not changed.
- `before.html`: the live article, from `python3 scripts/apply_changes.py NN --fetch` (read-only).

## Output (in `work/NN/`)

1. `changes.py`, which writes `changes.json`: a list of `{"line", "field", "old", "new", "why", "group"}`.
   - `line` is the 0-based line of `before.html` holding one block comment `<!-- wp:flexlayout/<name> {json} /-->`.
   - `field` is the attribute changed: usually `content`; quote blocks also have `contentSource` and `contentCompany`.
   - `old` is the exact current attribute value (decoded JSON string), and `new` is the replacement.
   - `group` is `approved`, `renumber` or `related`.
   - Only one change per line and field. When an approved edit and a renumbering touch the same block, combine them.
   - Name the claim ids (`C3`, `C12`) in `why`; the addendum's "What changed" section reads them from there.
2. `check.py`: re-applies `changes.json` to `before.html` in memory, asserts every invariant below and prints a
   summary line.

## Writing the edits

- Find the sentence or sentences each claim refers to, and replace them with the approved wording. Fit it into the
  surrounding paragraph so the paragraph still reads naturally.
- Keep the article's voice and HTML (`<p>`, `<strong>`, `<em>`, `<li>`), its apostrophe style, and no em dashes in new
  text.
- If a suggested edit is longer than the sentence it replaces, keep only what the claim needs and add no new ideas. If
  it can't be placed without rewriting unrelated text, keep the change minimal and say so in `why`.
- Keep existing `<sup>[n]</sup>` markers attached to the text they support.
- Some text appears twice: a book description and its mobile caption copy (class `is-style-caption2`), or a hidden
  `hide` paragraph. Change both copies identically.
- If a later review pass confirmed the original wording (for example, the exact phrase was found in the source), keep
  the original sentence and say so in `why`.

## Citations

- When the final entry has `suggested_citation`, cite it at the edited sentence. Reuse a source already in the list
  where possible.
- Confirm every new source's title, authors, venue and year from Crossref (`https://api.crossref.org/works/<doi>`) or
  the publisher's page, and never invent details. Match the existing Sources item format exactly.
- Renumber all markers in order of first appearance in the body, including book rows and quote attributions such as
  `contentCompany: "... [3]"`, and rebuild the Sources list in that order. The FAQ has no markers.
- Remove a source only if nothing cites it any more, and note that in `why`.

## Related edits (group `related`)

FAQ answers and other sentences that repeat a claim being corrected (same example, number or overstatement) are
rewritten with the same evidence and softer wording, so the article never contradicts itself. Nothing else in the FAQ
is touched. List these separately for the user, because they go beyond the clicked choices.

## Invariants `check.py` asserts

- Each `old` equals the current attribute value on its line, and each `new` differs from it.
- After applying, every `[n]` in the body is in 1..len(Sources), first appearances run 1, 2, 3, ... in order, and every
  source is cited at least once.
- New text has no em dashes, except the " — " separator inside Sources items.
- The number of block comments is unchanged.
