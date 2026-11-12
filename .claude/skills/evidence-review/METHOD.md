# Evidence review method (version 2)

ATTCK publishes a 50-article series, "Behavioral Science for Digital Experience Design". Each article gets an
adversarial evidence review, the way a demanding professor challenges a student's paper: every factual claim is checked
against its own citation, then argued against with research from other fields, replications and meta-analyses, then
judged with a fixed rubric. Every quote is re-checked by a script. This file is the method every review pass follows.

Each article folder (`work/NN/`) holds `article.txt` (full text; bracketed numbers like [3] are citation markers) and
`meta.json` (number, title, live URL, the numbered Sources list with links).

## Evidence rules (all passes)

- Every evidence item has a working URL and a verbatim quote under 40 words. No quote, no use. Never paraphrase inside
  a quote field. A script re-fetches every URL afterwards and checks every quote; unconfirmed quotes are never used to
  decide a verdict.
- Never invent studies, authors, numbers or quotes. If unsure, say "not verified".
- Never put a personal email address or other personal data in a request to any service (some APIs ask for a contact
  address; leave it out).
- Rate strength: meta-analysis | replication | experiment | observational | expert/practitioner | anecdote.
- Blocked publisher pages: use the same paper's record in OpenAlex, Crossref, Semantic Scholar, Europe PMC or PubMed,
  and say so.
- "Contradicts" and "no evidence either way" are different findings.
- Research databases: query them through `scripts/research_api.py`, which applies the API keys, throttles requests,
  retries on refusals, falls back to keyless services (OpenCitations, Crossref, Europe PMC) and shares one cache across
  all reviews. Log every query in `search_log` with the service that answered (the output's `source`); when a
  citation-graph result says `scanned_newest`, record that only that many of the newest citing papers were checked.

## Pass 1 — claims (`claims.json`)

List atomic, checkable claims: empirical, causal, numeric, attribution, case study; prescriptive claims only when the
article presents them as evidence-backed. Skip framing sentences and pure opinion. Aim for 12–22 claims.

`{"id": "C1", "section", "claim" (close to the article's wording), "cite" (source number(s) or null), "type", "note"}`

## Pass 2 — citation check (`pass2.json`)

For each claim: does the cited source say this? Open it, quote the passage, flag overreach (stretching, generalizing,
misstating, "consistently", wrong attribution). For uncited claims, name the likely uncredited source if one exists.

`{"id", "cited_source_supports": "yes"|"partly"|"no"|"uncited", "passage", "url", "overreach", "notes"}`

## Pass 3 — challenge (`pass3.json`)

Build the strongest honest case against each claim, plus the best support, found systematically rather than from
memory. Three routes, every query logged:

1. **recall** — studies the reviewer already knows (labeled as recall).
2. **citation-graph** — for cited papers with a DOI, papers that cite them (`research_api.py cites DOI TERM`),
   filtered for replication, failed to replicate, meta-analysis and boundary conditions, newest first. For web pages
   or books, search for later work that re-examines the same finding.
3. **cross-field** — state the claim's mechanism in general terms with no web-design wording; name 3–5 fields outside
   UX that study it; run open topic and database searches per field with no author names; record for / against /
   mixed / nothing found.

Keep it proportionate: interpretive or prescriptive claims need fewer fields than core empirical claims.

`{"id", "mechanism", "fields": [{"field", "result", "items": [{"finding", "source", "url", "quote", "strength", "route"}]}],
"citation_graph": {"api_used", "citing_papers_scanned", "relevant": [items]}, "challenge_strength": "none"|"weak"|"moderate"|"strong",
"search_log": [...]}`

## Pass 4 — judge (`pass4.json`, `summary.json`)

Weigh pass 2 and pass 3 per claim. Open the URL of any quote that decides a verdict and confirm it. Be even-handed:
pass 3 argued against everything, so weigh strength and directness, not volume. Cross-field evidence counts only when
the mechanism transfers.

Verdicts:
- **Supported** — the cited source says it, and no credible evidence undercuts it as written.
- **Supported with caveats** — broadly right, but the wording overstates or omits a known boundary condition.
- **Contested** — credible evidence points both ways; the article presents it as settled.
- **Not supported** — the cited source does not say it, or the best evidence contradicts it.
- **Misattributed** — the idea is sound but credited to the wrong source, or uses an uncredited source.
- **Unverified** — uncited, and no evidence either way (not the same as false).

Confidence: high | medium | low.

`{"id", "verdict", "confidence", "why" (2–3 plain sentences for a non-specialist editor), "key_for": [{"source", "url", "quote"}],
"key_against": [...], "suggested_edit" (replacement sentence(s) in the article's voice, or null), "suggested_citation": {"source", "url"} or null,
"addendum_note", "coverage": {"routes": {"recall": n, "citation-graph": n, "cross-field": n}, "fields": [{"field", "result"}]},
"doubtful": true when the verdict is Contested / Not supported / Misattributed, confidence is low, or the challenge was strong,
"notes"}`

`summary.json`: `{"counts", "must_fix", "should_fix", "fine", "headline" (2–3 sentences), "method_note"}`

Suggested edits use plain American English, no em dashes and no hype words, and keep the article's voice.

## Pass 5 — re-check of doubtful claims (`pass5.json`)

Only for claims marked doubtful, on the strongest model. Deepen the challenge (more fields, the citation graph,
newest work), confirm deciding quotes, then re-judge. Entries use the pass 4 shape plus `changed_from_pass4` (null or
one sentence). The final verdict is pass 5 when present, else pass 4. Update `summary.json` if the lists change.

## After the passes

- `verify_quotes.py` re-checks every quote in passes 2–5.
- `build_report.py` renders the private report with a decision control per suggested edit and a Copy Responses button.
- Approved edits are applied to the article, and the public addendum in `docs/` records the supporting research and
  what changed.
