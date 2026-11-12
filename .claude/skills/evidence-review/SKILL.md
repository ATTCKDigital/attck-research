---
name: evidence-review
description: Adversarial evidence review of articles in ATTCK's Behavioral Science series. Checks every claim against its citation, challenges it with replications, citing papers and research from other fields, judges it with a fixed rubric, re-checks every quote by script, and produces a private report with per-edit decisions. Also applies approved edits and writes the public addendum. Use for "review article 12", "run the evidence review for articles 10-17", pasted "Evidence review responses", or "write the addendum for article 4".
---

# Evidence review

Run from the root of the `attck-research` repo. The method every pass follows is in [METHOD.md](METHOD.md); give each
review agent that file's path rather than restating it. Scripts are in `scripts/` (run with `python3`, from that
folder). Private working data goes to `work/` (gitignored); only addenda in `docs/` are public.

## Setup check (once per session)

- `.env` may hold `OPENALEX_API_KEY` and `SEMANTIC_SCHOLAR_API_KEY`; never print them. Without keys the reviews still
  run: `research_api.py` stops OpenAlex list and search calls once the free daily budget ($0.10 per IP, reset at
  midnight UTC) is spent, slows keyless Semantic Scholar calls, and falls back to OpenCitations (citing papers, with
  abstracts from free OpenAlex single-paper lookups), Crossref search and Europe PMC. Say in the reply which services
  answered (`grep -ho '"source": "[a-z]*"'` over the pass3 search logs, or the agents' reports).
- `python3 scripts/fetch_article.py list` works (read-only SSH access to WordPress).

## Running reviews ("review article 12", "articles 10-17")

1. **Resume first.** `python3 scripts/state.py next 10-17`. Skip stages already `done`; restart stages left `started`.
2. **Fetch.** `state.py start NN fetch`, `fetch_article.py NN`, `state.py done NN fetch`.
3. **Passes 1–3** — one agent per article, model **opus**, up to 8 articles in parallel. Mark `claims`, `citations`
   and `challenge` started before launching and done when it returns. Prompt:
   > Run passes 1, 2 and 3 of an evidence review for one article. Read `<repo>/.claude/skills/evidence-review/METHOD.md`
   > and follow it exactly. Article folder: `<repo>/work/NN`. Write claims.json, then pass2.json, then pass3.json there
   > (valid JSON). Query research databases only through `python3 <repo>/.claude/skills/evidence-review/scripts/research_api.py`.
   > Work only in that folder. Reply with the number of claims, the pass 2 tally and the 3 strongest challenges.
4. **Pass 4 (judge)** — model **opus**, as soon as an article's pass 3 is done. Prompt: run Pass 4 from METHOD.md on
   `work/NN` (inputs article.txt, meta.json, claims.json, pass2.json, pass3.json), write pass4.json and summary.json,
   mark doubtful claims, and reply with summary.json and the doubtful ids.
5. **Pass 5 (re-check)** — model **fable**, only when pass 4 marked claims doubtful (otherwise mark `recheck` done
   immediately). Prompt: run Pass 5 from METHOD.md on `work/NN` for the doubtful ids listed in pass4.json; write
   pass5.json; rewrite summary.json if the lists change; reply with each verdict and what changed.
6. **Verify.** `verify_quotes.py NN`. If more than 10% of quotes fail, look at the failing hosts before publishing;
   blocked publishers usually need the DOI record fallback, not a different quote.
7. **Report.** `build_report.py NN`, then publish `work/reports/report-NN.html` with the Artifact tool (private, icon
   "search"). Record the URL in `work/reports/index.json` (`{"NN": url}`), mark `report` done.
8. **Finish.** `state.py summary 10-17` and reply with a table: article, minutes, quotes confirmed, verdict counts,
   must-fix count, report link.

Report findings in plain words; never claim a quote is confirmed unless verify.json says so.

## Applying edits (pasted "Evidence review responses: Article NN …")

The reply lists `Cnn [verdict]: APPLY | APPLY WITH CHANGES :: text | KEEP AS WRITTEN | DISCUSS :: text`, then any
undecided ids.

1. Save the pasted text to `work/NN/responses.txt`. Answer every DISCUSS item in chat first; those are not applied
   until the user decides.
2. `python3 scripts/apply_changes.py NN --fetch` saves the live article (read-only) to `work/NN/before.html`.
3. Draft the change set with one agent per article (model **opus**; several articles can run in parallel), giving it
   `apply/CHANGESET.md` and the article folder. It writes `changes.py`, `changes.json` and `check.py`, and `check.py`
   must pass. Review the agent's report yourself: look for edits it could not place cleanly, sources it added beyond the
   review's suggestions, and any claim where a later pass confirmed the original wording (keep the original there).
4. Show the user the change set, with the `related` group (FAQ and other sentences repeating a corrected claim) listed
   separately, and get an explicit yes. A rendered before-and-after page (private Artifact) works well for long sets.
   A standing instruction such as "apply all recommended changes" covers the approved group; say what the related
   group changed in the reply.
5. `apply_changes.py NN --dry`, then `apply_changes.py NN --write`. The write backs up the content, changes a block only
   if it still matches the drafted original, copies the hero ACF fields to the new revision, re-fetches the post and
   confirms every change landed. WP Engine allows 5 SSH connections per user, so write one article at a time.
6. For published articles, remind the user to clear the WP Engine cache.

## Addendum (after edits are applied)

`python3 scripts/build_addendum.py NN` writes `docs/<slug>.md` and adds it to `docs/index.md`. The page contains:
- "How this review works" (one paragraph, matching METHOD.md).
- "Background research": each Supported or Supported-with-caveats claim's `addendum_note`, with its confirmed
  `key_for` sources and their quotes. Contested and Not supported claims never appear as support, and unconfirmed
  quotes are never cited.
- "What changed in the article": for each applied claim, the claim reviewed, how it now reads and why.
Old citation numbers are stripped, because they change when the article is renumbered.

Hold the addendum for a scheduled article until it publishes. Once the addendum is live on GitHub Pages, add a separate
line under the article's Sources list, not a numbered source: "Evidence review for this article" linking to
`https://attckdigital.github.io/attck-research/<slug>`. Commit addenda only when the user asks; the repo is public.
