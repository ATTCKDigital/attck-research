---
title: "Evidence review: Predictive UX"
---

# Evidence review: Predictive UX

Article: [Predictive UX](https://attck.com/blog/predictive-ux/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**Starting in 1993, a team at Microsoft Research built software that tried to work out what you were stuck on before you asked.**

Horvitz's project page dates the start of Lumiere to 1993, with the first prototype finished that year; the opening now gives that date.

- [Horvitz et al., The Lumiere Project, UAI 1998 (source)](https://erichorvitz.com/lumiere.htm): “We review work on Bayesian user models that can be employed to infer a user's needs by considering a user's background, actions, and queries.”
- [Horvitz, Lumiere project page (Microsoft Research)](https://erichorvitz.com/lum.htm): “The Lumiere project at Microsoft Research was initiated in 1993 with the goal of developing methods and an architecture for reasoning about the goals and needs of software users”

**The Lumière project used Bayesian models to infer a user's needs from their background, actions and queries, and its prototypes became the basis for parts of the Office Assistant that shipped with Office 97, though the Assistant's pop-up tips ran on much simpler rules. Most people remember the Assistant by its paperclip.**

Horvitz's project page notes that the shipped Office Assistant brought itself forward using a relatively simple rule-based system on top of Lumiere's Bayesian query analysis, not Lumiere's probabilistic model of when to help.

### A Prediction Is a Default With a Confidence Score

**Three working rules follow from his principles, in our words rather than his. Every prediction needs a threshold below which it stays hidden, or at least asks before acting. A wrong guess should cost one tap, or nothing, to dismiss. And the size of what is predicted should shrink as confidence drops: a word rather than a sentence, a suggestion rather than an action.**

These rules are a design translation of Horvitz's 1999 principles, consistent with Microsoft's 2019 Guidelines for Human-AI Interaction ('Support efficient dismissal', 'Scope services when in doubt'). Horvitz's own model includes a middle option, asking the user, between acting and staying silent.

- [Horvitz, Principles of Mixed-Initiative User Interfaces, CHI 1999 (source, author copy)](https://erichorvitz.com/chi99horvitz.pdf): “Designs for services and alerts should be undertaken with an eye to minimizing the cost of poor guesses, including appropriate timing out and natural gestures for rejecting attempts at service.”
- [Amershi et al., Guidelines for Human-AI Interaction, CHI 2019](https://www.microsoft.com/en-us/research/uploads/prod/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf): “Scope services when in doubt.”

**A prediction placed in front of someone works as a default, and a search box that completes queries steers people toward the phrasings other people used.**

Treating a prediction as a default draws on default-effects research: a 2019 meta-analysis found a sizable average effect (d = 0.68) with wide variation. Experiments on search suggestions (Epstein et al. 2024) show that which suggestions appear can shift opinions.

- [Jachimowicz et al., When and why defaults influence decisions: a meta-analysis of default effects, Behavioural Public Policy 2019](https://doi.org/10.1017/bpp.2018.43): “considerable influence of defaults (d = 0.68, 95% confidence interval = 0.53–0.83), we also discover substantial variation”
- [Epstein et al., The search suggestion effect (SSE), Computers in Human Behavior 2024](https://doi.org/10.1016/j.chb.2024.108342): “differentially suppressing negative search suggestions can have a dramatic impact on the opinions and voting preferences of undecided voters”

### What Suggestions Do to the Words People Choose

**The clearest difference was in words the system had not predicted: writers used about one more of them per caption when no suggestions appeared. In this study, predictive text produced more predictable writing, though the authors caution that commercial keyboards may not have effects of the same size.**

Arnold and colleagues note that they do not claim commercial keyboards have content effects of the kind and size they measured. Later work on AI writing aids (Jakesch et al. 2023) also finds suggestions shift what people write.

- [Arnold, Chauncey & Gajos, Predictive Text Encourages Predictable Writing, IUI 2020 (source, author copy)](https://www.eecs.harvard.edu/~kgajos/papers/2020/arnold20predictive.pdf): “an average of about one additional unpredictable word was used when suggestions were Never visible compared to the Always (CI: [0.68, 1.60]) or OnlyConfident (CI: [0.46, 1.27]) conditions.”
- [Jakesch et al., Co-Writing with Opinionated Language Models Affects Users' Views, CHI 2023](https://arxiv.org/abs/2302.00560): “Using the opinionated language model affected the opinions expressed in participants' writing and shifted their opinions in the subsequent attitude survey.”

**Suggestions also reduced uncorrected typos and sped up typing in this study, though the gain shrank for faster typists, and other studies have found that reading suggestions can slow people down overall.**

The speed benefit of word suggestions is mixed across studies. Quinn and Zhai (2016) found suggestions cut keystrokes but slowed average entry, and a 37,000-person study (Palin et al. 2019) found word-prediction use correlated with slower typing. A 2025 TOCHI paper reports suggestions only improve speed when highly accurate.

**Hiding low-confidence suggestions may have softened part of the effect: captions written with suggestions always on contained about 0.78 more predictable words than those written with confident-only suggestions, a result the authors call less clear, and the drop in unpredicted words was similar in both suggestion conditions.**

The authors describe the always-on versus confident-only difference as less clear than their main result.

### Guessing Well Is Mostly Knowing When Not To

**The paperclip's trouble was never that it tried to help. It popped up often, at the wrong moments, on simple rules rather than the research team's models, and it was hard to send away.**

Horvitz writes that the shipped Assistant used simple rules to bring itself forward, and that his team had hoped for Bayesian timing and nonmodal windows that need no dismissal.

- [Horvitz, Lumiere project page (Microsoft Research)](https://erichorvitz.com/lum.htm): “coupled with designs we had demonstrated for employing nonmodal windows that do not require dismissal when they are not used.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: supported with caveats

**Claim reviewed:** In the mid-1990s a Microsoft Research team built Lumiere, which used Bayesian models to infer a user's needs from their background, actions and queries.

**Now reads:** Starting in 1993, a team at Microsoft Research built software that tried to work out what you were stuck on before you asked.

**Why:** The cited paper describes Lumiere exactly this way: Bayesian models that infer a user's needs from background, actions and queries. The only slip is the date. Horvitz's project page says the work began in 1993, so 'mid-1990s' is a little late, though the research did run through the Office 97 release. Now cites [Horvitz, The Lumiere Project page, Microsoft Research](https://erichorvitz.com/lum.htm).

### Introduction: supported with caveats

**Claim reviewed:** Lumiere's prototypes became the basis for parts of the Office Assistant that shipped with Office 97 (the paperclip).

**Now reads:** The Lumière project used Bayesian models to infer a user's needs from their background, actions and queries, and its prototypes became the basis for parts of the Office Assistant that shipped with Office 97, though the Assistant's pop-up tips ran on much simpler rules. Most people remember the Assistant by its paperclip.

**Why:** Horvitz's paper says Lumiere prototypes were the basis for components of the Office 97 Assistant, so 'parts of' is accurate. But the paragraph lets readers assume the paperclip's pop-ups were Lumiere's predictions. Horvitz's own project page says the shipped Assistant used a simple rule-based system to pop up tips, layered on the Bayesian query analysis. Now cites [Horvitz, The Lumiere Project page, Microsoft Research](https://erichorvitz.com/lum.htm).

### Introduction: supported with caveats

**Claim reviewed:** Four years later Microsoft turned the Assistant off: an April 2001 company feature announced it would be off by default in Office XP, and a product manager said Office XP was 'so easy to use that Clippy is no longer necessary, or useful.'

**Now reads:** Four years later, Microsoft switched it off by default.

**Why:** The April 11, 2001 feature confirms the date, the 'four years' and the product manager's quote word for word. 'Turned it off' is a bit stronger than the source, which says the Assistant was off by default and could be switched back on; the next sentence of the article already says 'off by default'. The quote is lighthearted PR, so it gives Microsoft's public line rather than evidence of why users disliked Clippy.

### A Prediction Is a Default With a Confidence Score: supported with caveats

**Claim reviewed:** Three working rules follow from Horvitz: every prediction needs a threshold below which it stays hidden; a wrong guess should cost one tap, or nothing, to dismiss; and the size of what is predicted should shrink as confidence drops.

**Now reads:** Three working rules follow from his principles, in our words rather than his. Every prediction needs a threshold below which it stays hidden, or at least asks before acting. A wrong guess should cost one tap, or nothing, to dismiss. And the size of what is predicted should shrink as confidence drops: a word rather than a sentence, a suggestion rather than an action.

**Why:** Horvitz does argue for a confidence threshold, cheap rejection and scaling help to uncertainty, and Microsoft's 2019 guidelines repeat those ideas. The specific rules (hide below a threshold, one tap to dismiss) are the article's own translation, and Horvitz's threshold also allows a middle step such as asking the user. Text-entry studies also show that even confidence-gated suggestions carry an attention cost, so the rules are sensible design advice rather than tested findings. Now cites [Amershi et al., Guidelines for Human-AI Interaction, CHI 2019](https://www.microsoft.com/en-us/research/uploads/prod/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf).

### What Suggestions Do to the Words People Choose: supported with caveats

**Claim reviewed:** Writers used about one more unpredicted word per caption when no suggestions appeared; predictive text produced more predictable writing.

**Now reads:** The clearest difference was in words the system had not predicted: writers used about one more of them per caption when no suggestions appeared. In this study, predictive text produced more predictable writing, though the authors caution that commercial keyboards may not have effects of the same size.

**Why:** The paper reports about one extra unpredictable word per caption without suggestions, and later studies of AI writing aids also find suggestions shift what people write. But this was a single caption-writing study on a custom keyboard, and the authors themselves say they do not claim deployed keyboards have effects of this size. One later study found that when writing became less varied, the change came from text the model contributed, not from people changing their own words.

### What Suggestions Do to the Words People Choose: supported with caveats

**Claim reviewed:** Suggestions reduced uncorrected typos and sped up typing, though the speed gain shrank for faster typists.

**Now reads:** Suggestions also reduced uncorrected typos and sped up typing in this study, though the gain shrank for faster typists, and other studies have found that reading suggestions can slow people down overall.

**Why:** The cited study did find fewer typos and faster typing, with a smaller gain for fast typists. But several other text-entry studies find the opposite on speed: reading suggestions costs time, and in a 37,000-person typing study word-prediction use went with slower typing. Speed gains seem to depend on how accurate the suggestions are and how fast the person already types, which the article only half says. Now cites [Quinn & Zhai, A Cost-Benefit Study of Text Entry Suggestion Interaction, CHI 2016](https://doi.org/10.1145/2858036.2858305).

### What Suggestions Do to the Words People Choose: supported with caveats

**Claim reviewed:** Hiding low-confidence suggestions softened the effect: captions written with suggestions always on contained about 0.78 more predictable words than those written with confident-only suggestions.

**Now reads:** Hiding low-confidence suggestions may have softened part of the effect: captions written with suggestions always on contained about 0.78 more predictable words than those written with confident-only suggestions, a result the authors call less clear, and the drop in unpredicted words was similar in both suggestion conditions.

**Why:** The 0.78 figure is right, but the authors say this contrast is 'less clear', and the article states it flatly. The confident-only condition reduced predictable words, yet writers in that condition still used about one fewer unpredictable word than with no suggestions, about the same as always-on, so hiding weak suggestions softened only part of the effect.

### What Suggestions Do to the Words People Choose: supported with caveats

**Claim reviewed:** Arnold, Gajos and Kalai found that writers read multi-word phrase suggestions as ideas about what to say, and phrases shaped content more than single-word predictions did.

**Now reads:** Longer suggestions push harder. In an earlier, smaller study, Arnold, Gajos and Adam Kalai found that writers read multi-word phrase suggestions as ideas about what to say, and those phrases shaped content more than single-word predictions did.

**Why:** The 2016 paper found exactly this: phrases were read as suggestions and shaped content more than single words. It was a small study, with the content analysis covering 61 reviews from 16 people. Later and larger studies of phrase suggestions and AI writing aids point the same way, so the direction looks sound.

### How Smart Reply Learned When to Stay Quiet: not supported

**Claim reviewed:** The feature earned that usage by holding back: staying silent on about nine messages in ten, keeping the refusal on the menu and making each option count, which is Horvitz's expected-value logic written as product rules.

**Now reads:** The design reads like Horvitz's expected-value logic written as product rules: a gate that kept the feature silent on about nine messages in ten, a refusal kept on the menu, and options that each mean something different. Only the last was measured, and a later Skype system found the same pattern, with more varied suggestions lifting click-rate by about 5%. On the gate, the authors note that slightly over-triggering might help, since an unused suggestion costs little.

**Why:** The Smart Reply paper reports the 10% usage figure as a bare metric and never credits it to restraint. It does describe the gate as a way to avoid useless suggestions, but the only design choice it measured against usage is showing three different answers (about 7.5% more clicks), and a later Skype system found the same for variety (about 5%). On the gate itself the authors lean the other way, saying slightly over-triggering may help because an unused suggestion costs little; alert-fatigue studies do show that fewer low-value prompts raise acceptance, but false-alarm research finds that effect weakest when a false alert is cheap to ignore, which is the case for a reply chip. Now cites [Budhaditya Deb, Peter Bailey, Milad Shokouhi, 'Diversifying Reply Suggestions Using a Matching-Conditional Variational Autoencoder', Proceedings of NAACL-HLT 2019, Industry Papers](https://aclanthology.org/N19-2006/).

### Guessing Well Is Mostly Knowing When Not To: supported with caveats

**Claim reviewed:** The paperclip's trouble was never that it predicted: it predicted often, at the wrong moments, and was hard to send away.

**Now reads:** The paperclip's trouble was never that it tried to help. It popped up often, at the wrong moments, on simple rules rather than the research team's models, and it was hard to send away.

**Why:** Horvitz's own account backs the diagnosis of bad timing and hard dismissal: he had hoped for windows that need no dismissal, and interruption research shows badly timed interruptions do more harm. But 'it predicted often' is loose, because the shipped Assistant's pop-ups were triggered by simple rules rather than by a prediction model. The sentence has no citation. Now cites [Horvitz, The Lumiere Project page, Microsoft Research](https://erichorvitz.com/lum.htm).
