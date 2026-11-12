---
title: "Evidence review: Measuring Behavioral Change Over Time"
---

# Evidence review: Measuring Behavioral Change Over Time

Article: [Measuring Behavioral Change Over Time](https://attck.com/blog/measuring-behavioral-change-over-time/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**Somewhere between 18 and 254 days. That was how long the model estimated it took participants in a study by Phillippa Lally and colleagues to reach 95% of their peak automaticity for a new daily habit, among the volunteers whose data fitted it well.**

The range covers the 39 participants with a good model fit; the longer times are projections beyond the 12-week study.

- [Lally et al. 2010, European Journal of Social Psychology (Crossref record; publisher page blocked)](https://api.crossref.org/works/10.1002/ejsp.674): “The time it took participants to reach 95% of their asymptote of automaticity ranged from 18 to 254 days”

**For participants whose data fitted the model, automaticity rose along a curve that climbed quickly and then flattened. The modeled time to reach the plateau ranged from under three weeks to about eight months, with the longer times projected past the end of the twelve-week study.**

Plateau times beyond day 84 were model projections, not observations.

### Behavior Change Has a Shape

**Measured over time, one change can rise and then fall, or fall and then recover, as novelty fades and people learn what the change is worth to them.**

Novelty and primacy effects in online experiments are documented by Sadeghi et al. (2022).

- [Sadeghi et al. 2022, Novelty and Primacy: A Long-Term Estimator for Online Experiments, Technometrics](https://api.openalex.org/works/doi:10.1080/00401706.2022.2124309): “observed treatment effects are not always stable, sometimes revealing increasing or decreasing patterns over time.”

### What Google Learned by Waiting

**Then both cohorts get the same experience, a stretch the authors call the post-period. Any difference that remains between the cohorts can be put down to what users learned during the treatment, though the gap starts to shrink as soon as the experiences match.**

The post-period gap decays as users unlearn; personalization can bias related designs.

- [Hohnhold, O'Brien, Tang 2015, KDD (Google Research PDF)](https://research.google.com/pubs/archive/43887.pdf): “Since E and C receive the same treatment in the post-period, differences between the metrics of the two cohorts in the PP can be ascribed to user behavior changes, i.e., to learning that occurred during the treatment period.”

**Few product teams have Google's traffic, but the method transfers. Hold a randomly chosen slice of users out of a change for a quarter, large enough that you could detect the effect you care about, then give both groups the same experience and keep comparing. If a gap persists past the first weeks, users learned something from the change, for better or worse. Expect the gap to narrow as the groups converge. If it is gone within days, the first-month effect was the screen itself rather than a shift in how people behave.**

The holdback design is the cited paper's post-period and lagged-start method, which the authors say applies beyond ads. Limits the paper itself names: the gap narrows as the groups converge; a small holdback has low power, so a vanishing gap can be noise; and the treatment length depends on how often users meet the change (Google estimates half the learning in 14 to 21 days for changes on every results page and a 60-day half-life for ads). Long holdouts also face cookie churn and survivorship bias (Dmitriev et al. 2016), and the related cookie-cookie-day design is biased under personalization (ACM EC 2023).

- [Allcott and Rogers 2014, American Economic Review (AEA article page; cross-field, energy conservation)](https://www.aeaweb.org/articles?id=10.1257/aer.104.10.3003): “if reports are discontinued after two years, effects are relatively persistent, decaying at 10-20 percent per year.”
- [Acland and Levy 2015, Naivete, Projection Bias, and Habit Formation in Gym Attendance, Management Science (OpenAlex record; cross-field, health economics)](https://api.openalex.org/works/doi:10.1287/mnsc.2014.2091): “We find a significant postintervention attendance increase, which we interpret as habit formation”
- [Minimax designs for causal effects in temporal experiments with treatment habituation, Biometrika 2022 (OpenAlex record; cites)](https://api.openalex.org/works/doi:10.1093/biomet/asac024): “the effects of an intervention on an experimental unit may be large when the unit is first exposed to it, but then it attenuates after repeated exposures.”

### Expect the dip, then wait it out

**The reverse also happens: a novelty bump that fades.**

Novelty effects documented by Sadeghi et al. (2022).

- [Sadeghi et al. 2022, Novelty and Primacy: A Long-Term Estimator for Online Experiments, Technometrics](https://api.openalex.org/works/doi:10.1080/00401706.2022.2124309): “Novelty describes the desire to use new technology that tends to diminish over time.”

### Keep measuring after the intervention stops

**When reports were stopped after two years, the savings proved relatively persistent, decaying at 10 to 20 percent a year, and households were slow to tune out repeated reports. Part of that persistence came from physical changes such as new appliances, which a reminder email can't leave behind.**

Persistence in Opower data is partly explained by technology adoption; habituation to repeated messages is slow, not absent.

- [Allcott and Rogers 2014, American Economic Review (AEA article page)](https://www.aeaweb.org/articles?id=10.1257/aer.104.10.3003): “if reports are discontinued after two years, effects are relatively persistent, decaying at 10-20 percent per year. Third, consumers are slow to habituate: they continue to respond to repeated treatment even after two years.”

### Tool: google/CausalImpact

**The package estimates what a metric would have done without the change, using a model built from related time series the change didn't touch, and assumes their relationship stays stable after launch. It shows how the effect evolves over the weeks that follow.**

Relies on a stable treated-control relationship after the intervention.

- [google/CausalImpact README](https://github.com/google/CausalImpact): “assumes that the outcome time series can be explained in terms of a set of control time series that were themselves not affected by the intervention.”

**Weaker than a randomized holdback and sensitive to which control series you choose, but usually better than comparing this month with last.**

Non-experimental; results depend on the choice of control series and model.

- [Gordon, Zettelmeyer, Bhargava, Chapsky 2019, Marketing Science (Crossref record)](https://api.crossref.org/works/10.1287/mksc.2018.1135): “Observational methods often fail to accurately recover the treatment effects generated from randomized advertising experiments on Facebook.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: supported with caveats

**Claim reviewed:** It took participants in Lally and colleagues' study between 18 and 254 days to reach 95% of their peak automaticity for a new daily habit.

**Now reads:** Somewhere between 18 and 254 days. That was how long the model estimated it took participants in a study by Phillippa Lally and colleagues to reach 95% of their peak automaticity for a new daily habit, among the volunteers whose data fitted it well.

**Why:** The paper reports exactly this 18 to 254 day range. But it comes from the 39 of 96 volunteers whose data fitted the model well, and times past the 84-day study were projected by the model rather than observed.

### Introduction: supported with caveats

**Claim reviewed:** For participants whose data fitted the model, automaticity rose along a curve that climbed quickly and then flattened; the modeled time to plateau ranged from under three weeks to most of a year.

**Now reads:** For participants whose data fitted the model, automaticity rose along a curve that climbed quickly and then flattened. The modeled time to reach the plateau ranged from under three weeks to about eight months, with the longer times projected past the end of the twelve-week study.

**Why:** The fast-then-flattening curve is what the paper reports. 'Most of a year' stretches 254 days (about eight months), and the long plateau times were extrapolated beyond the 12 weeks of data.

### Behavior Change Has a Shape: supported with caveats

**Claim reviewed:** A change in behavior is a curve rather than a step: people react to novelty, resist the unfamiliar, learn a feature's worth and form or drop routines, so one change can look like a win in week one, a loss in week four and a modest win in month six.

**Now reads:** Measured over time, one change can rise and then fall, or fall and then recover, as novelty fades and people learn what the change is worth to them.

**Why:** Large online-experiment studies confirm that treatment effects drift over time as users get used to a change or learn it. The specific win, loss, then modest win sequence is an illustration, not a reported finding, and the claim has no citation. Now cites [Sadeghi et al. 2022, Novelty and Primacy: A Long-Term Estimator for Online Experiments, Technometrics](https://api.openalex.org/works/doi:10.1080/00401706.2022.2124309).

### What Google Learned by Waiting: supported with caveats

**Claim reviewed:** In Google's post-period method, two cohorts receive different treatments for an extended period and then the same experience; any remaining difference can be put down to what users learned during the treatment.

**Now reads:** Then both cohorts get the same experience, a stretch the authors call the post-period. Any difference that remains between the cohorts can be put down to what users learned during the treatment, though the gap starts to shrink as soon as the experiences match.

**Why:** The method is described correctly. The paper itself warns that the remaining gap starts shrinking as soon as both groups get the same experience, and later work shows a related Google design is biased when the product personalizes.

### What Google Learned by Waiting: not supported

**Claim reviewed:** A two-week readout would have rejected the change that turned out best for users and neutral for the business.

**Now reads:** A two-week readout would have shown a substantial revenue loss set against a better user experience, with no way to tell that the loss would fade.

**Why:** The paper reports a substantial short-term revenue loss and a neutral long-term result for the mobile ad cut, but it never says what a two-week test would have decided. Its own account of the years before long-term measurement is that Google used short-term satisfaction metrics and leaned toward variants with a strong user experience, without knowing whether it was being too conservative. So the rejection is the article's inference, stated as fact. Later work agrees that short-term-only reads can lead to wrong product decisions, which supports the article's point but not this counterfactual.

### What Google Learned by Waiting: supported with caveats

**Claim reviewed:** The design transfers to teams without Google's traffic: hold a small random slice out of a change for a quarter, then give both groups the same experience; a persisting gap means users learned something, and a gap that vanishes within days means the first-month effect was the screen rather than a behavior shift.

**Now reads:** Few product teams have Google's traffic, but the method transfers. Hold a randomly chosen slice of users out of a change for a quarter, large enough that you could detect the effect you care about, then give both groups the same experience and keep comparing. If a gap persists past the first weeks, users learned something from the change, for better or worse. Expect the gap to narrow as the groups converge. If it is gone within days, the first-month effect was the screen itself rather than a shift in how people behave.

**Why:** The advice is the cited paper's own method: compare a treated cohort with a held-out cohort once both receive the same experience, and read any remaining gap as learning. The paper says the method applies outside ads, and its holdback-then-switch variant (the lagged-start measurement) is exactly the article's design, so the feature-removal limit raised in pass 4 does not apply. The article's reading of a quickly vanishing gap also follows from the paper's slow learning rates (half the learning in 14 to 21 days for changes on every results page, a 60-day half-life for ads). What the article leaves out: a small holdback has low power, so a gap that vanishes may be noise; the gap narrows on its own as the groups converge; and a quarter is Google's default for ads, not a universal length. Now cites [Dmitriev, Frasca, Gupta, Kohavi, Vaz 2016, Pitfalls of long-term online controlled experiments, IEEE BigData](https://doi.org/10.1109/bigdata.2016.7840744).

### Keep measuring after the intervention stops: supported with caveats

**Claim reviewed:** In Opower's home energy reports, the first reports set off rapid cycles of action and backsliding that faded over time; when reports stopped after two years, savings decayed at only 10 to 20 percent a year, and households kept responding to repeated reports rather than tuning them out.

**Now reads:** When reports were stopped after two years, the savings proved relatively persistent, decaying at 10 to 20 percent a year, and households were slow to tune out repeated reports. Part of that persistence came from physical changes such as new appliances, which a reminder email can't leave behind.

**Why:** The figures match the paper. 'Rather than tuning them out' overstates it: the paper says households were slow to habituate, not immune, and other energy studies find that moral-suasion messages lose force with repetition. A 2026 study of 38 experiments ties much of the lasting effect to equipment purchases, which digital prompts lack. Now cites [Do The Effects of Nudges Persist? Theory and Evidence from 38 Natural Field Experiments, Review of Economic Studies (2026)](https://doi.org/10.1093/restud/rdag012).

### Tool: google/CausalImpact: supported with caveats

**Claim reviewed:** CausalImpact estimates what a metric would have done without the change, using a model built from related time series the change didn't touch, and shows how the effect evolves over the following weeks.

**Now reads:** The package estimates what a metric would have done without the change, using a model built from related time series the change didn't touch, and assumes their relationship stays stable after launch. It shows how the effect evolves over the weeks that follow.

**Why:** The description matches the package and paper. It leaves out the key assumption that the relation between the metric and the control series stays stable after the change.

### Tool: google/CausalImpact: supported with caveats

**Claim reviewed:** CausalImpact is weaker than a randomized holdback but far better than comparing this month with last.

**Now reads:** Weaker than a randomized holdback and sensitive to which control series you choose, but usually better than comparing this month with last.

**Why:** Ranking it below a randomized holdback is well supported, including by Facebook ad studies where observational methods missed randomized results. 'Far better than comparing this month with last' is reasonable but untested, and results can change with model choices.

### A measurement plan that outlasts the launch: supported with caveats

**Claim reviewed:** Google's goals-signals-metrics process: signals should be chosen to move only when the experience gets better or worse, and metrics should be a rate or per-user average, never a raw count that grows with the user base.

**Now reads:** Metric: a rate or per-user average rather than a raw count that grows with the user base.

**Why:** The signal wording is nearly verbatim. 'Never a raw count' hardens the source, which says per-user and rate metrics are 'often more useful'.
