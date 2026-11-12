---
title: "Evidence review: Turning Insights Into Experiments"
---

# Evidence review: Turning Insights Into Experiments

Article: [Turning Insights Into Experiments](https://attck.com/blog/turning-insights-into-experiments/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**The team that ran Microsoft's experimentation platform shared that only one third of the ideas tested at the company improved the metrics they were designed to improve, and joked that their job was to tell clients that their new baby is ugly.**

Confirmed in the author-hosted copy of the KDD 2012 paper. The figure first appeared in the team's 2009 paper and is restated here.

- [Kohavi et al., Five Puzzling Outcomes Explained, KDD 2012 (author-hosted PDF)](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf): “only one third of ideas tested at Microsoft improved the metric(s) they were designed to improve”

**A Bing ad-headline change needed a few days of engineering, was judged low priority and languished for more than six months; when tested it raised revenue 12%, more than $100 million a year in the US alone, without hurting key user-experience metrics.**

Confirmed in the HBR article; a separate Microsoft paper (KDD 2013) reports the same order of magnitude for small changes at Bing.

- [Kohavi & Thomke, The Surprising Power of Online Experiments, HBR 2017](https://hbr.org/2017/09/the-surprising-power-of-online-experiments): “So it languished for more than six months”
- [Kohavi et al., Online Controlled Experiments at Large Scale, KDD 2013 (author-hosted PDF)](https://exp-platform.com/Documents/2013%20controlledExperimentsAtScale.pdf): “two small changes, which took days to develop, each increased ad revenue by about $100 million annually”

**Between them, those numbers show that teams misjudge their own ideas in both directions.**

An interpretation of the two cited examples; the KDD 2013 paper from the same team supports the underestimation side more generally.

### Do's and Don'ts

**At Microsoft a 'too good to be true' alert usually signals a bug; Bing's headline result was the exception, and it was checked before anyone believed it.**

Confirmed in the HBR article. The same team's KDD 2012 paper gives a worked example of a large click effect that turned out to be a logging artifact.

- [Kohavi & Thomke, The Surprising Power of Online Experiments, HBR 2017](https://hbr.org/2017/09/the-surprising-power-of-online-experiments): “Usually, such alerts signal a bug, but not in this case.”
- [Kohavi et al., Five Puzzling Outcomes Explained, KDD 2012 (author-hosted PDF)](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf): “In reality, the click logging was simply more reliable and fewer beacon requests were lost.”

**Testing tweaks your traffic cannot see. An underpowered test that finds nothing cannot tell you the change had no effect.**

Uncited; the idea is the classic 'absence of evidence is not evidence of absence' (Altman and Bland, BMJ 1995).

- [Altman & Bland, Absence of evidence is not evidence of absence, BMJ 1995 (PubMed abstract)](https://pubmed.ncbi.nlm.nih.gov/7647644/): “It is therefore wrong and unwise to interpret so many negative trials as providing evidence of the ineffectiveness of new treatments.”
- [Power Analysis is Essential: High-Powered Tests Suggest Minimal to No Effect of Rounded Shapes on Click-Through Rates, arXiv 2025](https://arxiv.org/abs/2512.24521): “Underpowered studies (below 50% power) suffer from the winner's curse”

### An Experiment Is a Decision Written Down in Advance

**An online controlled experiment randomly splits users between the current and a changed experience; random assignment lets you read the difference as caused by the change rather than by who happened to see it.**

Confirmed in the author-hosted KDD 2007 paper. Interference between users (marketplaces, social features) is a boundary condition outside this article's scope.

- [Kohavi, Henne & Sommerfield, Practical Guide to Controlled Experiments on the Web, KDD 2007 (author-hosted PDF)](https://exp-platform.com/Documents/GuideControlledExperiments.pdf): “any differences in the OEC are inevitably the result of this assignment, establishing causality”

**Johari and colleagues note that A/B testing users are known to monitor results continuously, which makes traditional p-values and confidence intervals unreliable; their fix was a different statistic built for constant checking. Continuous checking with ordinary statistics finds winners that are not there.**

Confirmed on the KDD 2017 paper page (ACM full text blocked). Optional stopping is a well-established problem across fields.

- [Johari et al., Peeking at A/B Tests, KDD 2017 (conference paper page)](https://www.kdd.org/kdd2017/papers/view/peeking-at-ab-tests-why-it-matters-and-what-to-do-about-it): “Our methodology addresses the issue that traditional p-values and confidence intervals give unreliable inference.”
- [Simmons, Nelson & Simonsohn, False-positive psychology, Psychol Sci 2011](https://pubmed.ncbi.nlm.nih.gov/22006061/): “flexibility in data collection, analysis, and reporting dramatically increases actual false-positive rates”

### Finding 1: Early trends are mostly noise

**Their verdict: most cases of suspected primacy and novelty effects are a statistical artifact, though real ones do occur. Few users have been counted early on, so early estimates swing.**

Confirmed in the KDD 2012 paper, which also says true novelty and primacy effects exist; the trending chart it warns about came from an A/A test.

- [Kohavi et al., Five Puzzling Outcomes Explained, KDD 2012 (author-hosted PDF)](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf): “most cases of suspected Primacy and Novelty effects are not real, but just a statistical artifact.”

**In their illustration of an experiment with no real effect, day one has a 67% chance of falling outside the final 95% confidence bound, and day two a 55% chance.**

Confirmed in the KDD 2012 paper; the illustration assumes a 21-day run with no repeat users.

**In Microsoft's experiments, they could not find a single case where a statistically significant result in one direction became significant in the other because of these effects. More often, significant negatives grew more negative over time and significant positives more positive. Later industry reviews mostly agree that the sign of an effect rarely flips, but it can over months for changes to ad load, content quality and pricing, and the Google team in the next finding reads its own ad results as one such case. The practical reading is plain: fix the run length in advance and don't argue with an early chart.

Later, replace "The two findings fit together." with: The two findings mostly fit together, though the Google authors note that their ad results cut against Microsoft's no-reversal claim.**

Microsoft's no-reversal finding is quoted accurately and matches the broadest later evidence: a 2026 industry workshop found sign flips rare, Netflix's 200-test comparison found two-week and two-month readings agree about 95% of the time, and field studies of energy reports and price promotions show effects fading rather than reversing. But Google's KDD 2015 paper footnotes the Microsoft claim as 'at odds' with its ad results, and Microsoft's own 2016 paper lists price and search-quality cases where short-term gains become long-term losses. The edit scopes the claim to Microsoft's runs and names where sign flips occur.

- [Sigerson et al., Evaluating for the long term: Learnings from industry, arXiv 2608.08043 (Aug 2026)](https://arxiv.org/abs/2608.08043): “Participants largely agreed that reversals of sign from short-run to long-run treatment effects are rare”
- [Zhang et al., Evaluating the Surrogate Index Using 200 A/B Tests at Netflix, arXiv 2311.11922](https://arxiv.org/abs/2311.11922): “the statistical inferences that we would draw from using the surrogate index are ~95% consistent with those from directly measuring the long-term treatment effect”
- [Allcott and Rogers, The Short-Run and Long-Run Effects of Behavioral Interventions, American Economic Review 2014](https://www.aeaweb.org/articles?id=10.1257/aer.104.10.3003): “initial reports cause high-frequency “action and backsliding,” but these cycles attenuate over time”

### Finding 2: Some effects really do change over time

**Hohnhold, O'Brien and Tang's starting point was that the effect measured during an experiment does not always predict the effect once a product has launched and users have changed their behavior in response.**

- [Hohnhold, O'Brien & Tang, Focusing on the Long-term, KDD 2015 (Google Research PDF)](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43887.pdf): “the short-term effect is not always predictive of the long-term effect”

**Acting on the results, Google cut the ad load on its mobile search interface by 50% over a sequence of launches. The change was substantially negative for short-term revenue; their methods estimated its long-term revenue impact to be neutral, with a better experience for users.**

Confirmed in the KDD 2015 paper; the edit notes that the 50% cut came in stages and that the long-term figure is an estimate.

**The two findings fit together. Most drift in the first week is noise, and the cure is patience. Real learning takes weeks or months, and it needs a measurement designed for it, such as keeping a group of users on the change long enough to learn it.**

Adds inline citations to the two sources the paragraph summarizes. Google runs its long-term learning studies for about 90 days.

- [Evaluating for the long term: Learnings from industry, arXiv 2026](https://arxiv.org/abs/2608.08043): “there is no substitute for a well-run long-term experiment”

### Size the test before you build the variant

**At 95% confidence and 90% power, the number of users needed is about (4rσ/Δ)², where r is the number of variants, σ the standard deviation of the metric and Δ the smallest difference you care about. The authors call it deliberately conservative, so it errs toward more traffic than a standard calculator would ask for. The square is what catches teams out. Halving the effect you want to detect quadruples the traffic you need.**

The cited paper and the authors' 2009 journal version both describe this rule of thumb as an overestimate; the edit says so.

- [Kohavi, Henne & Sommerfield, Practical Guide to Controlled Experiments on the Web, KDD 2007 (author-hosted PDF)](https://exp-platform.com/Documents/GuideControlledExperiments.pdf): “The following formula approximates the desired sample size, assuming the desired confidence level is 95% and the desired power is 90%”

**Revenue per user is far noisier than a yes-or-no conversion: in the paper's example a 5% change in revenue needs over 1.6 million users; narrowing the analysis to users the change can affect, such as those who started checkout, helps too.**

Confirmed in the KDD 2007 paper. The same example inherits the conservative formula noted under C14.

**At Bing's scale, a 1% revenue improvement was worth more than $10 million a year in the US.**

- [Kohavi et al., Online Controlled Experiments at Large Scale, KDD 2013 (author-hosted PDF)](https://exp-platform.com/Documents/2013%20controlledExperimentsAtScale.pdf): “A 1% improvement to revenue equals more than $10M annually in the US”

**Most products cannot detect a 1% change in a test of normal length.**

Uncited, but it follows from the sizing formula the article gives. The edit removes 'at all', since longer runs and variance reduction can lower the threshold.

### Worked example

**These figures use the paper's conservative rule of thumb. A standard sample-size calculator will usually ask for about a third fewer users, so treat them as a safe upper estimate.**

Reviewer arithmetic confirms all four figures with the article's formula; the edit notes that the formula errs high.

- [Kohavi, Henne & Sommerfield, Practical Guide to Controlled Experiments on the Web, KDD 2007 (author-hosted PDF)](https://exp-platform.com/Documents/GuideControlledExperiments.pdf): “the number of users needed drops by a factor of 16 to 30,400”

### Expect a redesign to look good in week one

**Both argue for running whole weeks, plotting the difference between versions over time rather than only the running total, and comparing new users, who have no habits to unlearn, against everyone else.**

Confirmed in the KDD 2007 guide and the KDD 2012 paper; the edit matches the sources' wording on plotting the difference over time.

- [Kohavi, Henne & Sommerfield, Practical Guide to Controlled Experiments on the Web, KDD 2007 (author-hosted PDF)](https://exp-platform.com/Documents/GuideControlledExperiments.pdf): “Both primacy and newness concerns imply that some experiments need to be run for multiple weeks.”
- [Kohavi et al., Five Puzzling Outcomes Explained, KDD 2012 (author-hosted PDF)](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf): “generating the delta graph (between Control and Treatment) over time”

### Name the guardrails before you name the winner

**If you configured a 50/50 split and the user counts come back more uneven than chance allows, which a simple chi-square test will tell you, that sample ratio mismatch is a symptom of a data-quality problem, and ignoring it can make a bad change look good.**

Confirmed in the author-hosted KDD 2019 paper; the edit replaces 'noticeably' with a statistical check.

- [Fabijan et al., Diagnosing Sample Ratio Mismatch, KDD 2019 (author-hosted PDF)](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf): “an SRM is a symptom for a variety of data quality issues”

### Book box / Do's and Don'ts

**Trustworthy Online Controlled Experiments (Kohavi, Tang, Xu; 288 pages) is written by experimentation leaders from Google, LinkedIn and Microsoft, draws on companies that each run more than 20,000 controlled experiments a year, has a chapter on Twyman's law and trustworthiness, gives institutional memory its own chapter, and its early chapters are written for everyone.**

Confirmed on the Cambridge University Press book page, including the table of contents.

- [Kohavi, Tang & Xu, Trustworthy Online Controlled Experiments, Cambridge University Press 2020 (publisher page)](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59): “Based on practical experiences at companies that each run more than 20,000 controlled experiments a year”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Finding 1: Early trends are mostly noise: supported with caveats

**Claim reviewed:** Kohavi and colleagues conclude that most cases of suspected primacy and novelty effects are a statistical artifact: few users are counted early on, so early estimates swing.

**Now reads:** Their verdict: most cases of suspected primacy and novelty effects are a statistical artifact, though real ones do occur. Few users have been counted early on, so early estimates swing.

**Why:** The cited paper says most suspected novelty and primacy effects are a statistical artifact, for the reason the article gives. The same paper adds that real novelty and primacy effects do exist, and later Microsoft work built a method to estimate them across many experiments, so 'mostly' should stay 'mostly'.

### Finding 1: Early trends are mostly noise: supported with caveats

**Claim reviewed:** They could not find a single experiment where a statistically significant result in one direction became significant in the other because of these effects; more often significant negatives grew more negative over time and significant positives more positive.

**Now reads:** In Microsoft's experiments, they could not find a single case where a statistically significant result in one direction became significant in the other because of these effects. More often, significant negatives grew more negative over time and significant positives more positive. Later industry reviews mostly agree that the sign of an effect rarely flips, but it can over months for changes to ad load, content quality and pricing, and the Google team in the next finding reads its own ad results as one such case. The practical reading is plain: fix the run length in advance and don't argue with an early chart.

Later, replace "The two findings fit together." with: The two findings mostly fit together, though the Google authors note that their ad results cut against Microsoft's no-reversal claim.

**Why:** Microsoft's team did say this, and the broadest later evidence agrees with them for the typical test: a 2026 workshop of 26 experts from 15 platforms found sign flips rare and probably overstated in the literature, Netflix saw two-week and two-month readings agree in about 95% of 200 tests, and field studies of energy reports and price promotions show effects fading rather than reversing. But the finding is scoped to novelty and primacy within experiment-length runs; over months, reversals do happen for ad load, content quality and pricing changes, Google's 2015 paper calls Microsoft's claim at odds with its ad results, and Microsoft's own 2016 paper gives price and search-quality examples where a short-term gain becomes a long-term loss. The sentence is accurate as a report of Microsoft's finding, but 'the two findings fit together' omits that the Google authors disagree and where flips occur. Now cites [Sigerson et al., Evaluating for the long term: Learnings from industry, arXiv 2608.08043 (2026)](https://arxiv.org/abs/2608.08043).

### Finding 2: Some effects really do change over time: supported with caveats

**Claim reviewed:** Acting on the results, Google cut the ad load on its mobile search interface by 50%; the change was substantially negative for short-term revenue, but its long-term revenue impact was neutral, with a better experience for users.

**Now reads:** Acting on the results, Google cut the ad load on its mobile search interface by 50% over a sequence of launches. The change was substantially negative for short-term revenue; their methods estimated its long-term revenue impact to be neutral, with a better experience for users.

**Why:** The abstract says the 50% mobile ad-load cut was substantially negative for short-term revenue and that the long-term impact was shown to be neutral. The body adds that the cut came from a sequence of launches and that the long-term figure was a model-based estimate (one passage even says net positive), so 'cut by 50%' in one move and 'showed' slightly overstate it.

### Finding 2: Some effects really do change over time: supported with caveats

**Claim reviewed:** Most drift in the first week is noise and the cure is patience; real learning takes weeks or months and needs a measurement designed for it, such as keeping a group of users on the change long enough to learn it.

**Now reads:** The two findings fit together. Most drift in the first week is noise, and the cure is patience. Real learning takes weeks or months, and it needs a measurement designed for it, such as keeping a group of users on the change long enough to learn it.

**Why:** The paragraph is an uncited summary of the two findings. Google's paper supports 'weeks or months' (it runs long-term studies for 90 days) and the need for a designed measurement such as a long-running group. Netflix and Microsoft have since shown that short-term data or observational methods can often stand in for a long holdout, so a long holdout is one option rather than the only one.

### Size the test before you build the variant: supported with caveats

**Claim reviewed:** At 95% confidence and 90% power the number of users needed is about (4r sigma / Delta)^2; halving the effect you want to detect quadruples the traffic you need.

**Now reads:** At 95% confidence and 90% power, the number of users needed is about (4rσ/Δ)², where r is the number of variants, σ the standard deviation of the metric and Δ the smallest difference you care about. The authors call it deliberately conservative, so it errs toward more traffic than a standard calculator would ask for. The square is what catches teams out. Halving the effect you want to detect quadruples the traffic you need.

**Why:** The formula and its 95% confidence, 90% power assumptions are exactly as the cited paper gives them, and the square law is right. The same paper warns the factor of 4 may overestimate by 25% for large samples, and the authors' 2009 journal version calls it intentionally conservative; standard calculations need about a third fewer users. Now cites [Kohavi, Longbotham, Sommerfield & Henne, Controlled experiments on the web: survey and practical guide, Data Min Knowl Disc 2009](https://exp-platform.com/Documents/controlledExperimentDMKD.pdf).

### Size the test before you build the variant: supported with caveats

**Claim reviewed:** Most products cannot detect a 1% change at all.

**Now reads:** Most products cannot detect a 1% change in a test of normal length.

**Why:** No source states this, but it follows from the article's own formula: a 1% relative change on a 5% conversion rate needs millions of users per variant, more than most sites see in a month. 'At all' is too absolute, since longer runs and variance-reduction methods lower the bar.

### Worked example: supported with caveats

**Claim reviewed:** With two variants, 95% confidence, 90% power and a 5% baseline, detecting a 20% change needs about 30,400 users, a 10% change about 121,600, a 5% change just under 500,000; with 80,000 users the smallest detectable relative change is roughly 12%.

**Now reads:** These figures use the paper's conservative rule of thumb. A standard sample-size calculator will usually ask for about a third fewer users, so treat them as a safe upper estimate.

**Why:** The arithmetic is correct for the formula the article uses: the 30,400 and under-500,000 figures are in the cited paper, and 121,600 and the 12% ceiling follow from it. Because the formula is conservative, standard calculations give about a third fewer users (about 20,000 for the 20% case) and a ceiling near 10% at 80,000 users. Now cites [Kohavi, Longbotham, Sommerfield & Henne, Controlled experiments on the web: survey and practical guide, Data Min Knowl Disc 2009](https://exp-platform.com/Documents/controlledExperimentDMKD.pdf).

### Expect a redesign to look good in week one: supported with caveats

**Claim reviewed:** Kohavi, Henne and Sommerfield describe a newness bias (users clicking everywhere on a new design) and a primacy effect (experienced users slower after navigation changes); both argue for running whole weeks, plotting the daily difference rather than only the running total, and comparing new users against everyone else.

**Now reads:** Both argue for running whole weeks, plotting the difference between versions over time rather than only the running total, and comparing new users, who have no habits to unlearn, against everyone else.

**Why:** The newness and primacy descriptions, running whole weeks and comparing new users are all in the cited guide. Plotting the difference over time is in the 2012 paper, but neither source says to plot the daily difference rather than the running total; that is a reasonable reading of the paper's warning about cumulative charts. The guide says 'some experiments' need multiple weeks, not all.

### Name the guardrails before you name the winner: supported with caveats

**Claim reviewed:** If a configured 50/50 split comes back noticeably uneven, that sample ratio mismatch is a symptom of a data-quality problem, and ignoring it can make a bad change look good.

**Now reads:** If you configured a 50/50 split and the user counts come back more uneven than chance allows, which a simple chi-square test will tell you, that sample ratio mismatch is a symptom of a data-quality problem, and ignoring it can make a bad change look good.

**Why:** The cited paper calls sample ratio mismatch a symptom of data-quality problems and says ignoring it can make a bad change look good. 'Noticeably uneven' undersells the check: the paper uses a statistical test, and a mismatch that matters at large sample sizes can be too small to notice by eye.

### Do's and Don'ts: supported with caveats

**Claim reviewed:** An underpowered test that finds nothing has told you nothing.

**Now reads:** Testing tweaks your traffic cannot see. An underpowered test that finds nothing cannot tell you the change had no effect.

**Why:** The core point is standard: a null result from a test too small to detect plausible effects is not evidence of no effect. 'Told you nothing' goes too far, because the confidence interval still rules out very large effects. Now cites [Altman & Bland, Absence of evidence is not evidence of absence, BMJ 1995 (PubMed abstract)](https://pubmed.ncbi.nlm.nih.gov/7647644/).
