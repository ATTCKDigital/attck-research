---
title: "Evidence review: How to Observe User Behavior"
---

# Evidence review: How to Observe User Behavior

Article: [How to Observe User Behavior](https://attck.com/blog/how-to-observe-user-behavior/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**In 1924 the National Research Council began a set of experiments at Western Electric's Hawthorne plant in Cicero, Illinois, to answer a narrow question: does better lighting make workers more productive?**

- [Levitt & List, NBER Working Paper 15016 (2009), published as AEJ: Applied 2011](https://www.nber.org/system/files/working_papers/w15016/w15016.pdf): “When the National Research Council initiated a set of experiments at Western Electric’s Hawthorne Plant in Cicero, Illinois in 1924, its objective was to answer a narrow question: does better lighting enhance worker productivity?”

**The popular story that spread from textbooks into management books is that every change in the light raised output, even when the room was made dimmer, so the cause had to be the attention itself.**

Confirmed against the NBER working paper and the Adair (1984) abstract.

- [Adair, Journal of Applied Psychology, 1984](https://doi.org/10.1037/0021-9010.69.2.334): “HE is inconsistently described in contemporary psychology textbooks, and there is lack of agreement on how the effect is mediated.”

**The illumination data were never formally analyzed and were thought to have been destroyed; Levitt and List found them preserved in two library archives.**

Confirmed. Izawa, French and Hedge (Human Factors, 2011) independently recovered much of the same data from a Cornell University archive.

- [Levitt & List, AEJ: Applied Economics, 2011](https://doi.org/10.1257/app.3.1.224): “were never formally analyzed and were thought to have been destroyed. Our research has uncovered these data.”

**Levitt and List's 2011 analysis concluded that the existing descriptions of remarkable data patterns were entirely fictional, with only subtler hints of an effect.**

Confirmed against the abstract (OpenAlex record; journal page paywalled) and an independent 2011 reanalysis.

- [Izawa, French & Hedge, Human Factors, 2011](https://doi.org/10.1177/0018720811417968): “Experimental results provided inconsistent evidence of an association between light levels and productivity.”

**Being asked to explain yourself is where the record gets least reliable.**

Supported for explanations of one's own choices (Nisbett and Wilson 1977; Hornbæk and Law 2007). Nisbett and Wilson also note such reports are sometimes accurate, so the wording was softened from an absolute to a comparison.

- [Nisbett & Wilson, Psychological Review, 1977](https://doi.org/10.1037/0033-295X.84.3.231): “their reports are based on a priori, implicit causal theories, or judgments about the extent to which a particular stimulus is a plausible cause of a given response.”
- [Hornbæk & Law, CHI 2007](https://doi.org/10.1145/1240624.1240722): “Measures of users' perceptions of phenomena are generally not correlated with objective measures of the phenomena.”

### Three Records From Every Session

**Jakob Nielsen's 2001 rule still holds: pay attention to what users do, not what they say, because self-reported claims and predictions about future behavior are unreliable.**

Confirmed on the NN/g page. A 73-study meta-analysis (Hornbæk and Law 2007) supports the low link between stated preference and measured performance.

- [Nielsen, First Rule of Usability? Don't Listen to Users, NN/g, 2001](https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/): “To design the best UX, pay attention to what users do, not what they say. Self-reported claims are unreliable, as are user speculations about future behavior.”
- [Hornbæk & Law, CHI 2007](https://doi.org/10.1145/1240624.1240722): “efficiency and satisfaction (e.g., preference) one of .196 ± .064”

### Four Identical Pairs of Stockings

**In a study of Nisbett and Wilson's own, run in a shop under the guise of a consumer survey, 52 passersby were shown four identical pairs of nylon stockings, asked which was the best quality, and then asked why they had chosen it.**

Confirmed against a full-text copy of the paper; the publisher page is paywalled.

- [Nisbett & Wilson, Psychological Review, 1977 (full text, CSU Long Beach copy)](https://home.csulb.edu/~cwallis/382/readings/482/nisbett%20saying%20more.pdf): “In both studies, conducted in commercial establishments under the guise of a consumer survey, passersby were invited to evaluate articles of clothing”

**Nobody mentioned position when giving reasons, and when asked directly whether it might have mattered, virtually everyone said no (quoted: 'Virtually all subjects denied it, usually with a worried glance...').**

Pull quote confirmed verbatim against the full text.

- [Johansson, Hall, Sikström & Olsson, Science, 2005](https://doi.org/10.1126/science.1111709): “while nevertheless offering introspectively derived reasons for why they chose the way they did.”

**When people report on why they did something, they often answer from an implicit theory of what should have influenced them rather than from any view of what actually did; knit and sheerness sound like reasons, position does not.**

Confirmed against the paper. A 1978 reply (Smith and Miller) and a 2025 philosophical re-examination dispute how far the thesis reaches, not the stocking result itself.

- [Nisbett & Wilson, Psychological Review, 1977](https://doi.org/10.1037/0033-295X.84.3.231): “Instead, their reports are based on a priori, implicit causal theories, or judgments about the extent to which a particular stimulus is a plausible cause of a given response.”

**The answers were sincere, and still built after the fact. Every "Why did you pick that plan?" in a usability session invites the same kind of answer. Sometimes the theory is right, as when price drove the choice, but the answer alone cannot tell you when.**

Nisbett and Wilson themselves predict that theory-based answers are accurate when the real cause is salient and plausible. The article now says 'why' answers are unverifiable on their own rather than implying they are always wrong.

- [Wilson & Schooler, Journal of Personality and Social Psychology, 1991](https://doi.org/10.1037/0022-3514.60.2.181): “Analyzing reasons can focus people's attention on nonoptimal criteria, causing them to base their subsequent choices on these criteria.”

**Saying aloud what you are attending to changes your thinking little, though it slows people down. Asking people to explain themselves as they go does change it.**

Confirmed by a 2011 meta-analysis of 94 studies (Fox, Ericsson and Best). The article now adds that thinking aloud lengthens tasks and that explanation requests, common in usability sessions, are reactive (Hertzum, Hansen and Andersen 2009).

- [Ericsson & Simon, Psychological Review, 1980](https://doi.org/10.1037/0033-295X.87.3.215): “Verbalizing information is shown to affect cognitive processes only if the instructions require verbalization of information that would not otherwise be attended to.”
- [Fox, Ericsson & Best, Psychological Bulletin, 2011](https://doi.org/10.1037/a0021663): “Findings based on nearly 3,500 participants show that the "think-aloud" effect size is indistinguishable from zero (r = -.03)”

**Nielsen calls thinking aloud possibly the single most valuable usability method, and his recipe ends with the third step 'Shut up and let the users do the talking.'**

Both quotes confirmed on the NN/g page.

- [Nielsen, Thinking Aloud: The #1 Usability Tool, NN/g, 2012](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/): “Thinking aloud may be the single most valuable usability engineering method.”

### Watch: Help Users Think Aloud

**The Kate Kaplan / NN/g 2023 video (3 min 42 s) covers how to explain thinking aloud to a participant, reinforce it, and prompt when they go quiet.**

Video metadata confirmed: NNgroup, published 31 May 2023, 3 min 42 s.

### The Same Session, Run Two Ways

**The first names the feature, so it mostly tests whether people can follow instructions. The second leaves the route to them, which is the thing you came to see.**

Uncited practitioner guidance, consistent with NN/g's published advice on writing task scenarios; a citation was added.

- [Turn User Goals into Task Scenarios for Usability Testing, NN/g](https://www.nngroup.com/articles/task-scenarios-usability-testing/): “For example, if you tell someone to click on Benefits in the main menu, you won’t learn if that menu label is meaningful to her.”

**"Why" sends people to their theories, the stocking problem. Asking what they were attending to, while it is fresh, stays closer to what Ericsson and Simon found people can report.**

Consistent with Ericsson and Simon (1980) and Fox, Ericsson and Best (2011). The wording was softened from 'stays within' to 'stays closer to', since a post-choice question is still retrospective.

- [Ericsson & Simon, Psychological Review, 1980](https://doi.org/10.1037/0033-295X.87.3.215): “From an analysis of what would be in STM at the time of report, the model predicts what can reliably be reported.”
- [Wilson & Schooler, Journal of Personality and Social Psychology, 1991](https://doi.org/10.1037/0022-3514.60.2.181): “Students who analyzed why they felt the way they did agreed less with the experts than students who did not.”

### Watching Without Steering

**Reporting what people said they would do as what they will do is an error, because stated predictions do not reliably match later behavior.**

Confirmed on the NN/g page; supported by Webb and Sheeran (2006) and the stated-preference literature.

- [Nielsen, First Rule of Usability? Don't Listen to Users, NN/g, 2001](https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/): “Definitely don't believe what people predict they may do in the future.”
- [Webb & Sheeran, Psychological Bulletin, 2006](https://doi.org/10.1037/0033-2909.132.2.249): “a medium-to-large change in intention (d = 0.66) leads to a small-to-medium change in behavior (d = 0.36).”

**Reading intent into a single session, or into cursor movement alone, is unreliable.**

Uncited but consistent with gaze-cursor research (Huang, White and Buscher 2012); a citation was added.

- [Huang, White & Buscher, CHI 2012](https://doi.org/10.1145/2207676.2208591): “findings which lead us to question the maxim that "gaze is well approximated by cursor."”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: contested

**Claim reviewed:** Being watched turns out to matter less than the Hawthorne legend claimed.

**Now reads:** The famous version of the story was wrong, but being watched still changes behavior, most clearly when silent observers sit in the room.

**Why:** Levitt and List showed that the famous Hawthorne data pattern was fiction, and a meta-analysis of 241 studies finds that merely having other people present explains only a small share of task performance. But two controlled usability-lab experiments found that silent observers in the room raised stress and lowered performance on some measures, and field studies in hospitals, homes and a clinical trial still find that people change what they do when they know they are being watched or studied. The sentence is defensible as a comparison with the legend, but in context it reads as reassurance that watching barely distorts behavior, and the evidence on that is split. Now cites [Sonderegger & Sauer, The influence of laboratory set-up in usability tests: effects on user performance, subjective ratings and physiological measures, Ergonomics 52(11), 2009](https://doi.org/10.1080/00140130903067797).

### Introduction: supported with caveats

**Claim reviewed:** Being asked to explain yourself is where the record gets unreliable (asking via surveys, interviews and feedback widgets is less reliable than observing).

**Now reads:** Being asked to explain yourself is where the record gets least reliable.

**Why:** Nisbett and Wilson, choice-blindness studies and Wilson and Schooler all show that people's explanations of their own choices are often built after the fact. But the same authors say such reports are sometimes accurate, so 'unreliable' as a blanket word is a little strong.

### Four Identical Pairs of Stockings: supported with caveats

**Claim reviewed:** The participants' answers were sincere and still built after the fact, and every 'Why did you pick that plan?' in a usability session invites the same kind of answer.

**Now reads:** The answers were sincere, and still built after the fact. Every "Why did you pick that plan?" in a usability session invites the same kind of answer. Sometimes the theory is right, as when price drove the choice, but the answer alone cannot tell you when.

**Why:** Asking 'why' after a choice does pull people toward their theories, and asking people to analyze reasons can even shift their choices. But Nisbett and Wilson predict those theory-based answers are often right when the real cause is obvious and plausible, such as price on a pricing page, so the answers are unverifiable rather than always wrong.

### Four Identical Pairs of Stockings: supported with caveats

**Claim reviewed:** Ericsson and Simon (1980) showed that saying aloud what you are attending to changes your thinking little.

**Now reads:** Saying aloud what you are attending to changes your thinking little, though it slows people down. Asking people to explain themselves as they go does change it.

**Why:** A meta-analysis of 94 studies confirms that plain thinking aloud does not change accuracy, as Ericsson and Simon predicted. It does slow people down, and the looser think-aloud most usability sessions use, with prompts and explanations, measurably changed how people navigated websites. Now cites [Fox, Ericsson & Best, Do procedures for verbal reporting of thinking have to be reactive? Psychological Bulletin 137(2), 2011](https://doi.org/10.1037/a0021663).

### Four Identical Pairs of Stockings: contested

**Claim reviewed:** That (Ericsson and Simon's finding) is why thinking aloud became the usability field's workhorse.

**Now reads:** Usability teams often cite Ericsson and Simon when they explain why thinking aloud works, though most sessions run a looser version, with more prompts and questions, than the one they studied.

**Why:** Usability writers do treat Ericsson and Simon as the theory behind thinking aloud, and the method is the field's most common one. But the practitioners who use it give practical reasons (it is fast, cheap and easy for participants), the designers who first adopted it valued the direct feedback it gave them, and surveys and experiments show that the usual usability version, with prompts and questions, does not follow Ericsson and Simon's procedure and does change behavior. So their finding is the rationale usually cited for the method, not a demonstrated cause of its popularity, and 'that is why' states the link as settled. Now cites [Boren & Ramey, Thinking aloud: reconciling theory and practice, IEEE Transactions on Professional Communication 43(3), 2000](https://doi.org/10.1109/47.867942).

### The Same Session, Run Two Ways: supported with caveats

**Claim reviewed:** A task prompt that names the feature tests whether people can follow instructions; a goal-based prompt reveals the route people would take.

**Now reads:** The first names the feature, so it mostly tests whether people can follow instructions. The second leaves the route to them, which is the thing you came to see.

**Why:** This is standard usability guidance rather than a tested finding, and NN/g's own article on task scenarios makes the same point: naming the interface element means you learn nothing about whether people would find it. 'Tests whether people can follow instructions' is a slight simplification, since people can still fail at a named step. Now cites [Turn User Goals into Task Scenarios for Usability Testing, Nielsen Norman Group](https://www.nngroup.com/articles/task-scenarios-usability-testing/).

### The Same Session, Run Two Ways: supported with caveats

**Claim reviewed:** 'Why' questions send people to their theories, while asking what they were attending to, while it is fresh, stays within what Ericsson and Simon found people can report.

**Now reads:** "Why" sends people to their theories, the stocking problem. Asking what they were attending to, while it is fresh, stays closer to what Ericsson and Simon found people can report.

**Why:** Ericsson and Simon's model favors reports of what people actually attended to, asked soon, over requests for reasons, and later work confirms that explanation requests distort. But a question asked after the choice is still a memory, and choice-blindness studies show even those can be reconstructed, so this improves the answer rather than guaranteeing it.
