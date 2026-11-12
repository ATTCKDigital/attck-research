# ATTCK Research

Evidence reviews for the articles in ATTCK's
[Behavioral Science for Digital Experience Design](https://attck.com/category/behavioral-science/) series.

Each article's factual claims are checked against the sources it cites, then deliberately challenged with research
from other fields, replication attempts and meta-analyses. Where the evidence holds up, the review is published here as
an addendum and linked from the article's Sources list. Where it does not, the article is corrected first.

The addenda live in [`docs/`](docs/) and are published with GitHub Pages. Every change is recorded in this repository's
history, so anyone can see what was reviewed, when, and what changed.

## How the reviews are done

The full method is in [`.claude/skills/evidence-review/METHOD.md`](.claude/skills/evidence-review/METHOD.md). In short:

1. **Claims.** Every checkable claim in the article is listed with the source it cites.
2. **Citation check.** Each cited source is opened to confirm it says what the article says.
3. **Challenge.** Separate reviewers build the strongest case against each claim, searching three ways: studies they
   already know, later papers that cite the original work, and open searches in other fields that study the same
   mechanism.
4. **Judgment.** Each claim gets a verdict on a fixed scale (Supported, Supported with caveats, Contested, Not
   supported, Misattributed, Unverified). Doubtful claims are re-checked with a stronger model.
5. **Quote check.** A script re-fetches every source and confirms every quote. Unconfirmed quotes are never used to
   decide a verdict.

The reviews run as a Claude Code skill in [`.claude/skills/evidence-review/`](.claude/skills/evidence-review/).
Working files and the editor's private reports stay out of this repository.
