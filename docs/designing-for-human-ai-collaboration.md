---
title: "Evidence review: Designing for Human–AI Collaboration"
---

# Evidence review: Designing for Human–AI Collaboration

Article: [Designing for Human–AI Collaboration](https://attck.com/blog/designing-for-human-ai-collaboration/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### A Team of Two With Unclear Roles

**Algorithm aversion is abandoning a better forecaster after watching it make a mistake.**

The definition of algorithm aversion matches the cited paper; a 2017 experiment replicated the drop in reliance on automated advice after a mistake.

- [Dietvorst, Simmons & Massey 2015 (OpenAlex abstract)](https://doi.org/10.1037/xge0000033): “We show that people are especially averse to algorithmic forecasters after seeing them perform, even when they see them outperform a human forecaster.”
- [Prahl & Van Swol 2017, Journal of Forecasting](https://doi.org/10.1002/for.2464): “However, after receiving bad advice, utilization of automated advice decreased significantly more than advice from humans.”

**Automation bias is following an aid when it is wrong, both by missing problems it failed to flag and by acting on its bad advice.**

The definition matches Parasuraman and Manzey's review.

- [Parasuraman & Manzey 2010 (OpenAlex abstract)](https://doi.org/10.1177/0018720810376055): “Automation bias results in making both omission and commission errors when decision aids are imperfect.”

**A 2010 review by Parasuraman and Manzey found automation bias in novices and experts alike, and in individuals and teams.**

Later work in law and medicine found automation bias across expertise levels, as the 2010 review reported.

- [Lyell & Coiera 2017, JAMIA](https://doi.org/10.1093/jamia/ocw105): “Contrary to the prevailing human factors view, AB was found in single tasks, typically involving diagnosis rather than monitoring, and with high verification complexity.”

**A 2010 review by Raja Parasuraman and Dietrich Manzey found it in novices and experts alike, in individuals and teams, and concluded that training or instructions cannot prevent it. Later reviews found they can reduce it, so treat training as a help, not a safeguard.**

Parasuraman and Manzey concluded training cannot prevent automation bias; a 2012 healthcare review found training and accountability reduce it.

**For a designer, the useful point is that neither failure comes down to accuracy alone. Both depend on how the person forms a picture of the system's reliability, and the interface is where much of that picture gets formed.**

The framing draws on trust-in-automation research (Lee and See 2004), now credited.

- [Lee & See 2004, Human Factors](https://doi.org/10.1518/hfes.46.1.50_30392): “Automation is often problematic because people fail to rely upon it appropriately.”

### One Visible Mistake

**Before choosing whether to tie their bonus to their own forecasts (in one study, another participant's) or to a statistical model built from the same data, participants saw the model's track record, the human's, both, or neither.**

Clarified that in most of the 2015 studies the human forecaster was the participant.

- [Dietvorst, Simmons & Massey 2015 (Wharton author PDF)](https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf): “a human judge (either themselves, in Studies 1–3, or another participant, in Study 4) or a statistical model that we built using the same data given to participants”

**The model won every study: human forecasts carried 15-29% more error in the MBA task and 90-97% more in the airline task.**

Figures match the paper.

**People who had watched the model perform were less likely to bet on it.**

Core finding confirmed; later 'algorithm appreciation' work studied people before they saw errors, so it does not undercut this result.

- [Dietvorst, Simmons & Massey 2015 (OpenAlex abstract)](https://doi.org/10.1037/xge0000033): “Participants who saw the algorithm perform were less confident in it, and less likely to choose it over an inferior human forecaster.”
- [Prahl & Van Swol 2017, Journal of Forecasting](https://doi.org/10.1002/for.2464): “However, after receiving bad advice, utilization of automated advice decreased significantly more than advice from humans.”

**Of the participants who saw both forecasters, 610 of 741 watched the model beat the human, and that group was among the least likely to choose the model.**

Count matches the paper.

**Watching the human forecaster err, who in most studies was the participant, did not significantly reduce people's willingness to bet on that human.**

Clarified that the 'human' in most studies was the participant.

**Pull quote: 'It seems that the errors that we tolerate in humans become less tolerable when machines make them.' (Dietvorst, Simmons and Massey 2015)**

Pull quote is verbatim.

**Every visible AI feature shows its errors sooner or later, so the finding is relevant to most of them, though later studies show its strength varies with the task, the user and whether people are comparing the system with their own judgment.**

Later reviews show algorithm aversion varies with task, user and comparison point.

**When participants could modify an imperfect algorithm's forecasts, they were considerably more likely to use it, even when the adjustments allowed were severely restricted, and they did better than people who relied on their own forecasts. People given that small amount of control were more satisfied and more willing to use the algorithm again. A 2023 replication confirmed this only in part, so treat it as a strong lead rather than a settled rule.**

A 2023 replication partly confirmed the 2018 'modifiable algorithm' result.

- [Dietvorst, Simmons & Massey 2018 (OpenAlex abstract)](https://doi.org/10.1287/mnsc.2016.2643): “Participants were considerably more likely to choose to use an imperfect algorithm when they could modify its forecasts, and they performed better as a result.”

**In a 2021 study, Zana Buçinca, Maja Barbara Malaya and Krzysztof Gajos found that people shown AI suggestions with explanations still followed the AI when it was wrong, as earlier studies had also found. Three designs that forced a moment of thought reduced that overreliance: asking people to decide before seeing the AI's answer, making the answer available only on request, or showing it after a delay.**

Buçinca et al. did observe overreliance in both of their explanation conditions, but their experiment had no AI-without-explanation condition, so the comparative point that explanations fail to reduce overreliance rests on earlier studies (Bansal et al. 2021; the Schemmer et al. 2022 meta-analysis) and on a 2023 clinical trial in JAMA. Later work finds explanations do reduce overreliance in some conditions: when decisions are easy (2024), when explanations are cheap to engage with relative to the task (2023), when explanations are partial (2025), and in a 2026 radiology study where chain-of-thought explanations beat bare answers. The honest summary is that explanations alone are an unreliable guard against overreliance, not that they never help.

- [Buçinca, Malaya & Gajos 2021 (arXiv full text, discussion)](https://arxiv.org/abs/2102.09692): “people frequently overrelied on the AI: they followed the suggestions of the AI even when its predictions were incorrect”
- [Buçinca, Malaya & Gajos 2021 (ACM abstract, summarizing prior work)](https://doi.org/10.1145/3449287): “Adding explanations to the AI decisions does not appear to reduce the overreliance and some studies suggest that it might even increase it.”
- [Bansal et al. 2021, CHI](https://doi.org/10.1145/3411764.3445717): “explanations increased the chance that humans will accept the AI’s recommendation, regardless of its correctness.”
- [Vasconcelos et al. 2023, CSCW (characterizing prior findings)](https://doi.org/10.1145/3579605): “Surprisingly, overreliance does not reduce when the AI produces explanations for its predictions, compared to only providing predictions.”
- [Schemmer et al. 2022, AIES meta-analysis](https://doi.org/10.1145/3514094.3534128): “we find no effect of explanations on users' performance compared to sole AI predictions.”
- [Jabbour et al. 2023, JAMA randomized clinical vignette study (457 clinicians)](https://pubmed.ncbi.nlm.nih.gov/38112814/): “commonly used image-based AI model explanations did not mitigate this harmful effect.”

**Three designs that forced a moment of thought helped: asking people to decide before seeing the AI's answer, making the answer available only on request, or showing it after a delay. Those designs reduced overreliance compared with simple explanations, though none removed it.**

Clarified that cognitive forcing reduced, but did not eliminate, overreliance.

**The cognitive forcing designs were the least liked, and they helped people who enjoy effortful thinking (high Need for Cognition) more than others.**

Matches the paper.

### Give people a dial, not a verdict

**How much people were allowed to change the forecast made relatively little difference to whether they chose the algorithm; being able to change it at all did. The desire was for some control, not a lot of it.**

Matches the 2018 paper's Study 2.

- [Dietvorst, Simmons & Massey 2018 (OpenAlex abstract)](https://doi.org/10.1287/mnsc.2016.2643): “participants’ preference for modifiable algorithms was relatively insensitive to the magnitude of the modifications they were able to make (Study 2)”

### Three Handoff Patterns

**In 2019 Amershi and colleagues at Microsoft distilled more than 150 design recommendations into 18 guidelines for human-AI interaction, tested by 49 design practitioners against 20 AI products.**

Figures match the paper.

- [Amershi et al. 2019 (OpenAlex abstract)](https://doi.org/10.1145/3290605.3300233): “a user study with 49 design practitioners who tested the guidelines against 20 popular AI-infused products.”

**Three that the study found important but still not widely implemented were making clear how well the system does what it does, explaining why it did something, and giving users global controls.**

Wording adjusted to credit the authors' analysis rather than practitioners' direct judgment.

- [Amershi et al. 2019 (Microsoft Research camera-ready PDF)](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf): “are guidelines which, despite their importance, are still not widely implemented (e.g., Guidelines 2, 11, 17)”

### Set expectations before the first error / Give people a dial

**Amershi's first two guidelines ask products to make clear what the system can do and how often it may be wrong, and another guideline asks products to support efficient correction when the system is wrong.**

Guideline content matches the paper.

- [Amershi et al. 2019 (Microsoft Research camera-ready PDF)](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf): “Help the user understand how often the AI system may make mistakes.”

### Set expectations before the first error

**A short line at the point of use ("Good at first drafts. Check names and numbers.") turns that mistake into something the person was told to expect, and in one Microsoft study, setting expectations this way made people more accepting of an imperfect assistant. Say it before the first output, not on a help page. Then keep it specific: a marker on uncertain answers, or a note on what the system couldn't check, tells people where to look, which a general disclaimer does not.**

The expectation-setting advice now credits Kocielnik, Amershi and Bennett (2019).

- [Kocielnik, Amershi & Bennett 2019, CHI](https://doi.org/10.1145/3290605.3300641): “we design expectation adjustment techniques that prepare users for AI imperfections and result in a significant increase in acceptance.”

### Ask for a judgment first where stakes are high

**Buçinca's results, from a lab task with everyday participants, say this reduces overreliance and that people will like it less. A study of radiologists found a cost as well: those who made their own call first agreed less with the AI even when it was right.**

A clinical imaging study (Fogliato et al. 2022) found judgment-first lowers agreement with both right and wrong AI advice.

- [Buçinca, Malaya & Gajos 2021 (arXiv full text)](https://arxiv.org/abs/2102.09692): “Participants in the update condition had to make the initial decision without the help of an AI (i.e., like in the no AI condition).”
- [Fogliato et al. 2022, FAccT](https://doi.org/10.1145/3531146.3533193): “participants who are asked to register provisional responses in advance of reviewing AI inferences are less likely to agree with the AI regardless of whether the advice is accurate”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### A Team of Two With Unclear Roles: supported with caveats

**Claim reviewed:** The review concluded that training or instructions cannot prevent automation bias.

**Now reads:** A 2010 review by Raja Parasuraman and Dietrich Manzey found it in novices and experts alike, in individuals and teams, and concluded that training or instructions cannot prevent it. Later reviews found they can reduce it, so treat training as a help, not a safeguard.

**Why:** The article reports the 2010 review's conclusion accurately: it says automation bias cannot be prevented by training or instructions. But a later systematic review of 74 healthcare studies lists training and accountability as factors that reduce it, so 'cannot prevent' should not be read as 'does not help'. Now cites [Goddard, Roudsari & Wyatt, Automation bias: a systematic review of frequency, effect mediators, and mitigators, JAMIA 19(1), 2012](https://doi.org/10.1136/amiajnl-2011-000089).

### A Team of Two With Unclear Roles: supported with caveats

**Claim reviewed:** Neither failure is mainly about accuracy; both are about how the person forms a picture of the system's reliability, and the interface is where that picture gets formed.

**Now reads:** For a designer, the useful point is that neither failure comes down to accuracy alone. Both depend on how the person forms a picture of the system's reliability, and the interface is where much of that picture gets formed.

**Why:** This is the article's own framing, not a cited finding. Research on trust in automation does say reliance follows people's picture of a system's reliability, shaped partly by the display, but accuracy and error patterns still matter, so 'neither failure is mainly about accuracy' overstates it. Now cites [Lee & See, Trust in Automation: Designing for Appropriate Reliance, Human Factors 46(1), 2004](https://doi.org/10.1518/hfes.46.1.50_30392).

### One Visible Mistake: supported with caveats

**Claim reviewed:** Dietvorst, Simmons and Massey ran five studies in which participants forecast MBA applicants' program performance and, in two studies, US states' ranks on departing airline passengers, then chose whether to tie their bonus to a human's forecasts or a statistical model, after seeing the model's track record, the human's, both, or neither.

**Now reads:** Before choosing whether to tie their bonus to their own forecasts (in one study, another participant's) or to a statistical model built from the same data, participants saw the model's track record, the human's, both, or neither.

**Why:** The study design is described correctly, except for one detail that matters: in Studies 1 to 3 the human forecaster was the participant, and only Study 4 used another person. Much of the aversion is a preference for one's own judgment over the model's.

### One Visible Mistake: supported with caveats

**Claim reviewed:** Watching the human err did not significantly reduce people's willingness to bet on the human.

**Now reads:** Watching the human forecaster err, who in most studies was the participant, did not significantly reduce people's willingness to bet on that human.

**Why:** The paper says seeing the human err did not significantly reduce choosing the human, and a 2017 experiment found the same asymmetry. But in most of the studies 'the human' was the participant, so this mostly shows people sticking with their own forecasts, which the article does not say.

### One Visible Mistake: supported with caveats

**Claim reviewed:** Every visible AI feature shows its errors sooner or later, so the algorithm-aversion finding applies to nearly all of them.

**Now reads:** Every visible AI feature shows its errors sooner or later, so the finding is relevant to most of them, though later studies show its strength varies with the task, the user and whether people are comparing the system with their own judgment.

**Why:** The drop in reliance after an algorithm errs has been replicated, so it is relevant to most visible AI features. But reviews of 60 to 80 studies show its strength depends on the task (subjective tasks are worse), the user, and whether people compare the system with their own judgment, so 'applies to nearly all of them' is too flat. Now cites [Mahmud, Islam, Ahmed & Smolander, What influences algorithmic decision-making? A systematic literature review on algorithm aversion, Technological Forecasting and Social Change 175, 2022](https://doi.org/10.1016/j.techfore.2021.121390).

### One Visible Mistake: supported with caveats

**Claim reviewed:** When participants could modify an imperfect algorithm's forecasts they were considerably more likely to use it, even when the adjustments allowed were severely restricted, performed better as a result, and were more satisfied and more willing to use the algorithm again.

**Now reads:** When participants could modify an imperfect algorithm's forecasts, they were considerably more likely to use it, even when the adjustments allowed were severely restricted, and they did better than people who relied on their own forecasts. People given that small amount of control were more satisfied and more willing to use the algorithm again. A 2023 replication confirmed this only in part, so treat it as a strong lead rather than a settled rule.

**Why:** The 2018 paper says exactly this, including higher satisfaction. A 2023 replication confirmed the effect only in part and raised reproducibility concerns, and 'performed better' means better than people using their own forecasts, not better than the unmodified algorithm. Now cites [Cheng & Chouldechova, Overcoming Algorithm Aversion: A Comparison between Process and Outcome Control, CHI 2023](https://doi.org/10.1145/3544548.3581253).

### One Visible Mistake: supported with caveats

**Claim reviewed:** Buçinca, Malaya and Gajos (2021) found that adding explanations to AI suggestions did not stop people over-relying on them.

**Now reads:** In a 2021 study, Zana Buçinca, Maja Barbara Malaya and Krzysztof Gajos found that people shown AI suggestions with explanations still followed the AI when it was wrong, as earlier studies had also found. Three designs that forced a moment of thought reduced that overreliance: asking people to decide before seeing the AI's answer, making the answer available only on request, or showing it after a delay.

**Why:** The full text confirms that both of the study's explanation conditions showed people following the AI when it was wrong, so the sentence's attribution holds as written: Buçinca's own participants over-relied despite explanations. Two caveats remain. The study never compared explanations against no explanations, so the comparative phrasing 'adding explanations did not stop' leans on earlier work the paper summarizes, and later studies show explanations can reduce overreliance when the task is easy, the explanation is cheap to check, or the explanation is partial, so the point should not read as settled. Now cites [Bansal et al., Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance, CHI 2021](https://doi.org/10.1145/3411764.3445717).

### One Visible Mistake: supported with caveats

**Claim reviewed:** Three designs that forced a moment of thought (deciding before seeing the AI's answer, answer on request only, answer after a delay) did stop overreliance, reducing it compared with simple explanations.

**Now reads:** Three designs that forced a moment of thought helped: asking people to decide before seeing the AI's answer, making the answer available only on request, or showing it after a delay. Those designs reduced overreliance compared with simple explanations, though none removed it.

**Why:** The three designs are described correctly and the paper reports they significantly reduced overreliance compared with simple explanations. But the paper says they did not eliminate it, and the article's 'did' implies they stopped it.

### Three Handoff Patterns: supported with caveats

**Claim reviewed:** Three guidelines that practitioners judged relevant but not widely implemented were making clear how well the system does what it does, explaining why it did something, and giving users global controls.

**Now reads:** Three that the study found important but still not widely implemented were making clear how well the system does what it does, explaining why it did something, and giving users global controls.

**Why:** The paper does name Guidelines 2, 11 and 17 as important but not widely implemented. That label is the authors' reading of where practitioners found the guidelines applied or violated, not a judgment the practitioners made themselves.

### Set expectations before the first error: supported with caveats

**Claim reviewed:** Aversion grows when the first mistake arrives as a surprise; telling people at the point of use what to expect, and marking specific uncertain answers, reduces it in a way a general disclaimer does not.

**Now reads:** A short line at the point of use ("Good at first drafts. Check names and numbers.") turns that mistake into something the person was told to expect, and in one Microsoft study, setting expectations this way made people more accepting of an imperfect assistant. Say it before the first output, not on a help page. Then keep it specific: a marker on uncertain answers, or a note on what the system couldn't check, tells people where to look, which a general disclaimer does not.

**Why:** This advice is uncited but has support: a Microsoft study found that setting expectations before use made people more accepting of an imperfect AI assistant. Evidence that specific uncertainty markers work better than a general disclaimer is thinner; confidence scores helped people calibrate trust but did not by themselves improve decisions, so 'never does' overstates it. Now cites [Kocielnik, Amershi & Bennett, Will You Accept an Imperfect AI? Exploring Designs for Adjusting End-user Expectations of AI Systems, CHI 2019](https://doi.org/10.1145/3290605.3300641).

### Ask for a judgment first where stakes are high: supported with caveats

**Claim reviewed:** For high-stakes decisions, asking for the person's call before revealing the AI's answer reduces overreliance, and people will like it less.

**Now reads:** Buçinca's results, from a lab task with everyday participants, say this reduces overreliance and that people will like it less. A study of radiologists found a cost as well: those who made their own call first agreed less with the AI even when it was right.

**Why:** Buçinca's 'decide first' condition did reduce overreliance and was liked less, but it was tested with lay participants on a food task, not money or health decisions. A study of radiologists found judgment-first also made experts agree less with the AI when it was right, a cost the article does not mention. Now cites [Fogliato et al., Who Goes First? Influences of Human-AI Workflow on Decision Making in Clinical Imaging, FAccT 2022](https://doi.org/10.1145/3531146.3533193).
