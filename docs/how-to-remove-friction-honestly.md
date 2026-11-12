---
title: "Evidence review: How to Remove Friction Honestly"
---

# Evidence review: How to Remove Friction Honestly

Article: [How to Remove Friction Honestly](https://attck.com/blog/how-to-remove-friction-honestly/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**Dashboards reward the belief. Remove a field and sign-ups often rise; remove a screen and the funnel looks healthier.**

Experiments outside UX, such as Galesic and Bosnjak's survey-length study, support the general pattern that more requested effort means fewer completions, though the size of the effect varies.

- [Galesic & Bosnjak, Effects of Questionnaire Length on Participation (Public Opinion Quarterly 2009)](https://doi.org/10.1093/poq/nfp031): “As expected, the longer the stated length, the fewer respondents started and completed the questionnaire.”

**Teams that celebrate one-click sign-up often own untimed cancellation flows, so friction is removed where it costs the company and left where it costs the user.**

Sunstein's work on 'sludge' describes the same asymmetry: friction that serves the institution rather than the person, often costing more than it is worth.

- [Luguri & Strahilevitz, Shining a Light on Dark Patterns (Journal of Legal Analysis 2021)](https://doi.org/10.1093/jla/laaa006): “Hidden information, trick question, and obstruction strategies were particularly likely to manipulate consumers successfully.”

### Friction Has a Direction

**In 2016, Anna Cox and colleagues challenged the design advice that friction should always be removed to avoid frustration and disengagement.**

Later studies citing Cox et al. have tested their idea in practice, for example Grüning et al. (CHI 2024) found that short frictions before opening apps made app use more intentional.

- [Cox, Gould, Cecchinato, Iacovides & Renfree, Design Frictions for Mindful Interactions (CHI EA 2016)](https://doi.org/10.1145/2851581.2892410): “Such articles often argue that these frictions should be removed from interaction flows in order to reduce the risk of user frustration and disengagement.”

**Small intentional barriers (microboundaries) can interrupt mindless automatic interactions and prompt reflection, with benefits ranging from fewer data-entry errors to support for health-behaviour change.**

A longitudinal study of 1,039 smartphone users (Grüning et al., CHI 2024) found that short frictions before opening chosen apps reduced opening attempts. A 2026 TikTok study found heavier friction cut compulsive use but made the experience worse, a reminder to keep pauses small.

- [Grüning et al., Design Frictions to Prevent Smartphone Overuse (CHI 2024)](https://doi.org/10.1145/3613904.3642370): “the short design frictions introduced by one sec effectively reduce how often users attempt to open target apps and lead to more intentional app-openings over time.”

### Two Experiments

**High school seniors whose parents received this help were 8 percentage points more likely to have completed two years of college within three years, 36% against 28%.**

Later randomized trials point the same way: in France, in-person help applying for benefits raised take-up while an online eligibility calculator did not, and in Delhi application assistance raised applications by 41 to 70 percent.

- [Bettinger, Long, Oreopoulos & Sanbonmatsu, The H&R Block FAFSA Experiment (QJE 2012)](https://doi.org/10.1093/qje/qjs017): “In particular, high school seniors whose parents received the treatment were 8 percentage points more likely to have completed two years of college, going from 28% to 36%, during the first three years following the experiment.”
- [Take-up of Social Benefits: Experimental Evidence from France (AEJ: Economic Policy 2025)](https://doi.org/10.1257/pol.20220786): “By contrast, an online simulator that gave personalized information on benefit eligibility did not increase take-up.”

**An IRS field experiment found something similar for tax credits. Among 35,050 filers who had failed to claim $26 million despite a first notice, a second mailing produced substantial additional claims, especially when it was simpler and made the benefit more salient. Attempts to reduce the perceived stigma or cost of applying did not help.**

Linos and colleagues ran six preregistered experiments with about a million households who had not filed a tax return and found that letters and texts did not raise filing or credit claims, which suggests reminder mailings work better for people already in the system.

- [Bhargava & Manoli, Psychological Frictions and the Incomplete Take-Up of Social Benefits (AER 2015)](https://doi.org/10.1257/aer.20121493): “While the mere receipt of the mailing, simplification, and the heightened salience of benefits led to substantial additional claiming, attempts to reduce perceived costs of stigma, application, and audits did not.”

**In both studies, a simpler and clearer path to the money moved people: a shorter notice and worksheet in the IRS study, hands-on help with the form in the student-aid study. In the student-aid study, information without that help moved no one.**

The IRS mailing included the claiming worksheet; a shorter worksheet raised response from 19% to 23% and a shorter notice from 17% to 23%, with the largest gain (8 points) from showing the credit amount. A 2026 meta-analysis of 51 field experiments finds help with the application raises take-up by about 8 points on average against about 3 for information alone, and trials in France and India agree. Information alone is not always idle: a federal letter raised naturalization applications by 1 point and a free-tuition guarantee letter raised applications from 26% to 68%, while letters to EITC non-filers and a College Board campaign moved no one. The 'no one' finding belongs to the student-aid study only.

- [J-PAL evaluation summary of Bhargava & Manoli's IRS experiment (Psychological Frictions and the Incomplete Take-Up of Social Benefits in the United States)](https://www.povertyactionlab.org/print/pdf/node/2175?lang=en): “The simple notice and simple worksheet generated a 23 percent response rate. The complex informational notice generated a 17 percent response rate, a 27 percent decline compared to the simple notice.”
- [Increasing Take-Up of Social Benefits: A Meta-Analysis of Field Experiments (Journal of Policy Analysis and Management, 2026); quote confirmed in the OpenAlex record because the Wiley page refused the fetch](https://doi.org/10.1002/pam.70085): “The most effective interventions are the ones reducing compliance demands, as these are estimated to increase actual take-up by 8.31 percentage points on average.”
- [A randomized controlled trial on the effect of administrative burden and information costs on social inequalities in early childcare access in France (Nature Human Behaviour, 2025); abstract from the Europe PMC record, PMID 40935911](https://doi.org/10.1038/s41562-025-02293-4): “Results revealed that the information-only treatment had minimal impact, while adding personalized support to alleviate administrative burdens significantly bridged the SES and migration gaps in early childcare applications.”

**Prompted users posted 6% fewer offensive Tweets than control, created fewer offensive Tweets afterwards and received fewer offensive replies, while the change in total replies sent was not statistically significant.**

Work on 'accuracy prompts' in misinformation research supports the idea that a brief nudge to reconsider reduces harmful sharing, although a preregistered replication (Roozenbeek et al., 2021) found the effect smaller than first reported.

- [Katsaros, Yang & Fratamico, Reconsidering Tweets (ICWSM 2022)](https://doi.org/10.1609/icwsm.v16i1.19308): “We find that users in our treatment prompted with this intervention posted 6% fewer offensive Tweets than non-prompted users in our control.”
- [Pennycook & Rand, Accuracy prompts are a replicable and generalizable approach (Nature Communications 2022)](https://doi.org/10.1038/s41467-022-30073-5): “The magnitude of the effect did not significantly differ by content of headlines (politics compared with COVID-19 related news) and did not significantly decay over successive trials.”

**The prompts also seemed to lose force with repetition: the more prompts someone saw, the more likely they were to send the Tweet unchanged.**

Warning research supports habituation: in Vance and colleagues' three-week field study, people followed repeated security warnings less over time, and changing the warning's look reduced that effect.

- [Katsaros, Yang & Fratamico, Reconsidering Tweets (ICWSM 2022; arXiv preprint)](https://arxiv.org/pdf/2112.00773): “Across these cohorts, the send rate increases with each subsequent prompt”
- [Vance, Jenkins, Anderson, Bjornn & Kirwan, Tuning Out Security Warnings (MIS Quarterly 2018)](https://doi.org/10.25300/misq/2018/14124): “Consistent with our fMRI results, users’ warning adherence substantially decreased over the three weeks.”

### Do's and Don'ts

**Confirmation prompts on trivial actions wear out fast.**

Vance and colleagues found attention to and compliance with repeated warnings fell over three weeks, and that varying the warning's design reduced the decline.

- [Vance, Jenkins, Anderson, Bjornn & Kirwan, Tuning Out Security Warnings (MIS Quarterly 2018)](https://doi.org/10.25300/misq/2018/14124): “Consistent with our fMRI results, users’ warning adherence substantially decreased over the three weeks.”
- [Laubheimer, Confirmation Dialogs Can Prevent User Errors (If Not Overused), Nielsen Norman Group](https://www.nngroup.com/articles/confirmation-dialog/): “I say again: if you warn people too much, they stop paying attention.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: supported with caveats

**Claim reviewed:** Removing a form field makes sign-ups rise, and removing a screen makes the funnel look healthier.

**Now reads:** Dashboards reward the belief. Remove a field and sign-ups often rise; remove a screen and the funnel looks healthier.

**Why:** No source is cited, but the general direction holds: experiments in survey research show that asking for more effort lowers how many people start and finish. The sentence states it as a rule, though, and effort is not always a pure cost; some studies find visible effort can raise perceived value.

### Two Experiments: supported with caveats

**Claim reviewed:** Simpler mailings that made the benefit more salient produced substantial additional claims, while attempts to reduce the perceived stigma or cost of applying did not.

**Now reads:** An IRS field experiment found something similar for tax credits. Among 35,050 filers who had failed to claim $26 million despite a first notice, a second mailing produced substantial additional claims, especially when it was simpler and made the benefit more salient. Attempts to reduce the perceived stigma or cost of applying did not help.

**Why:** The paper credits three things for the extra claims: simply receiving a second mailing, simplification, and making the benefit more salient. The article mentions only the last two, which makes the design changes sound like the whole effect. A later set of six large experiments on similar letters found no effect on people who had not filed taxes at all, so the result has limits.

### Two Experiments: supported with caveats

**Claim reviewed:** In both studies, making the task simpler moved people; in the student-aid study, information without help moved no one.

**Now reads:** In both studies, a simpler and clearer path to the money moved people: a shorter notice and worksheet in the IRS study, hands-on help with the form in the student-aid study. In the student-aid study, information without that help moved no one.

**Why:** The student-aid half is exactly what the source says: help with the form raised college completion, information alone did not. The IRS half is looser than pass 4 allowed but not wrong: every mailing carried the claiming worksheet, and J-PAL's summary of the study shows the shorter worksheet lifted response from 19% to 23%, though the shorter notice (17% to 23%) and showing the credit amount (8 more points) did more. A 2026 meta-analysis of 51 field experiments finds help with the application raises take-up by about 8 points on average against about 3 for information alone, so the lesson is broadly right; the article should just not imply that information alone never moves anyone, because in many settings it moves a few.

### Two Experiments: supported with caveats

**Claim reviewed:** The effect faded: the more prompts someone saw, the more likely they were to send the Tweet unchanged.

**Now reads:** The prompts also seemed to lose force with repetition: the more prompts someone saw, the more likely they were to send the Tweet unchanged.

**Why:** The paper does report that people sent more Tweets unchanged with each further prompt. 'The effect faded' reads more into that than the paper does: people who get many prompts may differ from those who get few, and the paper found first-prompt responses were similar for occasional and frequent offenders. Research on security warnings does show people tune out repeated warnings.

### Tool: GOV.UK Check answers: supported with caveats

**Claim reviewed:** The GOV.UK Check answers pattern adds a single review page immediately before the confirmation screen so people get a second chance to notice and correct errors; its guidance and code are open source (MIT).

**Now reads:** For small and medium-sized transactions, the pattern adds a single review page immediately before the confirmation screen, so people get a second chance to notice and correct errors before submitting.

**Why:** GOV.UK describes the pattern this way, but recommends a single check page only for small to medium-sized transactions; for long services it suggests checking each section. GOV.UK states the error-reduction benefit as a design rationale, not a measured result.

### Tool: GOV.UK Check answers: misattributed

**Claim reviewed:** For reversible actions, an undo offered afterwards often protects people better than a confirmation question beforehand; up-front questions should be saved for irreversible actions and name the consequence in the button label.

**Now reads:** That logic extends to a second kind of protective step. For actions that can be reversed, an undo option offered afterwards often protects people better than a question asked beforehand, because it costs nothing for the person who meant it. Save the up-front question for actions that can't be taken back, and put the consequence in the button label, such as "Delete 14 projects," so the pause carries information.

**Why:** The paragraph's three points, offer undo rather than a question, keep the question for actions that cannot be undone, and name the action on the button, are exactly the guidance in Nielsen Norman Group's 2018 article on confirmation dialogs (by Jakob Nielsen) and Aza Raskin's 2007 essay 'Never Use a Warning When You Mean Undo', neither of which the article credits. The advice is sound: field studies in four fields show that routine prompts get clicked through, with 70% of Chrome's SSL warnings dismissed, half or more of drug alerts overridden and consent dialogs accepted on sight. But no experiment compares undo with a confirmation head to head, and undo only helps when the person notices the mistake, so 'often protects people better' rests on expert judgment plus the habituation evidence. Now cites [Confirmation Dialogs Can Prevent User Errors (If Not Overused) — Jakob Nielsen, Nielsen Norman Group (2018)](https://www.nngroup.com/articles/confirmation-dialog/).
