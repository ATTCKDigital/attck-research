---
title: "Evidence review: How to Diagnose Behavioral Problems in a Product"
---

# Evidence review: How to Diagnose Behavioral Problems in a Product

Article: [How to Diagnose Behavioral Problems in a Product](https://attck.com/blog/how-to-diagnose-behavioral-problems-in-a-product/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**In 1990, Jakob Nielsen and Rolf Molich described heuristic evaluation: give a few evaluators the design and a short list of principles, then pool what they find.**

Nielsen and Molich (1990) is the original description of heuristic evaluation.

- [Nielsen & Molich, Heuristic Evaluation of User Interfaces (CHI 1990)](https://doi.org/10.1145/97243.97281): “Heuristic evaluation is an informal method of usability analysis where a number of evaluators are presented with an interface design and asked to comment on it.”

**A single evaluator caught only 20 to 51 percent of the usability problems, but three to five evaluators working together did well.**

Later research (Hertzum and Jacobsen 2001; Nielsen and Landauer 1993) finds that results vary a lot by evaluator and that three to five is a cost-effective number rather than full coverage.

**When Susan Michie, Maartje van Stralen and Robert West reviewed the frameworks used to design behavior change programs in 2011, they counted nineteen. In setting up the review, they noted that, with few exceptions, "insufficient attention appears to be given to analysing the nature of behaviour as the starting point."**

The quoted sentence is background from the paper's introduction (citing earlier work), not a finding of the framework review itself.

- [Michie, van Stralen & West, The Behaviour Change Wheel (Implementation Science 2011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3096582/): “In general, insufficient attention appears to be given to analysing the nature of behaviour as the starting point of behaviour change interventions [ 15 ], a notable exception being intervention mapping [ 16 ].”

### What the Behaviour Change Wheel Fixed

**One line from the paper deserves a sticky note: in the COM-B model, all six components except reflective motivation are necessary for a behavior to occur.**

Michie et al. (2011) state the necessity of capability and opportunity as a premise of the COM-B model, building on a 1991 consensus of behavior theorists, rather than as an empirical result.

- [Michie, van Stralen & West, The Behaviour Change Wheel (Implementation Science 2011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3096582/): “All, apart from reflective motivation, are necessary for a given behaviour but it is possible to generate a profile of which should be targeted to achieve the behavioural target.”
- [Wood, Quinn & Kashy (2002), Journal of Personality and Social Psychology](https://doi.org/10.1037/0022-3514.83.6.1281): “When participants were engaged in habitual behavior, defined as behavior that had been performed almost daily in stable contexts, they were likely to think about issues unrelated to their behavior”

**People act without deliberating all the time.**

Wood, Quinn and Kashy (2002) found that much everyday behavior is habitual and performed while people think about other things.

### The Tax-Office Experiment

**One of the clearest examples of why the remedy has to fit the barrier comes from US college financial aid.**

Bettinger et al. (2012) compared help with the form against information alone; it shows that the remedy must match the barrier, not that a diagnosis step was tested. A 2026 meta-analysis of 51 take-up field experiments (Journal of Policy Analysis and Management) finds interventions that reduce the work of applying raise take-up by 8.31 points on average against 3.39 for information, and a 2025 French experiment and a 2025 Nature Human Behaviour childcare trial found the same pattern, which supports the article's capability-and-opportunity reading. Direct tests of diagnose-then-tailor are weaker: the 2026 Cochrane review finds tailored implementation strategies probably give a slight improvement (OR 1.49, moderate certainty), and theory-based health interventions are on average no more effective than others (Prestwich et al. 2014; Dalgetty, Miller and Dombrowski 2019).

- [Bettinger, Long, Oreopoulos & Sanbonmatsu, The Role of Application Assistance and Information in College Decisions, Quarterly Journal of Economics (2012)](https://doi.org/10.1093/qje/qjs017): “The findings suggest many other opportunities for using personal assistance to increase participation in programs that require filling out forms to become eligible.”
- [Increasing Take-Up of Social Benefits: A Meta-Analysis of Field Experiments, Journal of Policy Analysis and Management (2026), 51 field experiments, 187 effect sizes](https://doi.org/10.1002/pam.70085): “The most effective interventions are the ones reducing compliance demands, as these are estimated to increase actual take-up by 8.31 percentage points on average.”
- [Take-up of Social Benefits: Experimental Evidence from France, American Economic Journal: Economic Policy (2025), two nationwide experiments](https://doi.org/10.1257/pol.20220786): “By contrast, an online simulator that gave personalized information on benefit eligibility did not increase take-up.”
- [McHugh et al., Tailored interventions to address determinants of practice, Cochrane Database of Systematic Reviews (2026), PubMed record](https://pubmed.ncbi.nlm.nih.gov/41757603/): “Tailored implementation strategies probably result in a slight improvement in professional practice.”

### Five Steps, step 4

**Support tickets, site search terms, recordings and a handful of short interviews are often enough to rule a box in or out for a single step. If the signals disagree, gather more before you decide.**

Small samples work for narrow questions: Guest, Bunce and Johnson (2006) found the basic elements of their themes by six interviews, Guest, Namey and Chen (2020) found six to seven interviews capture most themes in a homogeneous group, and Virzi (1992) found four or five users surface about 80 percent of usability problems with the severe ones first. The number is unreliable on its own: Faulkner (2003) found random sets of five users uncovered between 55 and 99 percent of problems, Spool and Schroeder (2001) found four production web sites needed far more than five users, Alroobaea and Mayhew (2014) found no fixed number works, and Hennink et al. (2017, 2022) put code saturation at nine interviews and meaning saturation at 16 to 24. Lindgaard and Chattratichart (2007) found the number of tasks mattered more than the number of users, which favors the article's focus on one step.

- [Guest, Namey & Chen, A simple method to assess and report thematic saturation in qualitative research, PLOS ONE (2020), full text, Discussion](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0232076): “typically 6–7 interviews will capture the majority of themes in a homogenous sample”
- [Virzi, Refining the Test Phase of Usability Evaluation: How Many Subjects Is Enough? Human Factors (1992), three experiments](https://doi.org/10.1177/001872089203400407): “(a) 80% of the usability problems are detected with four or five subjects, (b) additional subjects are less and less likely to reveal new information”
- [Nielsen & Landauer (1993), INTERCHI '93](https://doi.org/10.1145/169059.169166): “For a “medium” example, we estimate that 16 evaluations would be worth their cost, with maximum benefit/cost ratio at four.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: supported with caveats

**Claim reviewed:** Michie et al. observed that "insufficient attention appears to be given to analysing the nature of behaviour as the starting point"; teams were choosing remedies before naming the problem.

**Now reads:** When Susan Michie, Maartje van Stralen and Robert West reviewed the frameworks used to design behavior change programs in 2011, they counted nineteen. In setting up the review, they noted that, with few exceptions, "insufficient attention appears to be given to analysing the nature of behaviour as the starting point."

**Why:** The quoted words are exact, but they come from the paper's introduction, where the authors summarize earlier work, not from their review of the nineteen frameworks. The same sentence names an exception, intervention mapping, which the article leaves out.

### What the Behaviour Change Wheel Fixed: supported with caveats

**Claim reviewed:** Of the six components, all except reflective motivation are necessary for a behavior to occur.

**Now reads:** One line from the paper deserves a sticky note: in the COM-B model, all six components except reflective motivation are necessary for a behavior to occur.

**Why:** The paper does say all components except reflective motivation are necessary, but it states this as a premise of the model, drawn from earlier theorists, not as a tested finding. Habit research fits the idea that people act without deliberating, yet the article presents it as a fact about behavior and then turns it into an order of checks the paper does not prescribe.

### The Tax-Office Experiment: supported with caveats

**Claim reviewed:** The clearest evidence for diagnosing first comes from the H&R Block FAFSA experiment; read through COM-B, its result points to capability and opportunity rather than reflective motivation.

**Now reads:** One of the clearest examples of why the remedy has to fit the barrier comes from US college financial aid.

**Why:** The study shows that helping families with the form worked while giving them information did not, and the newest research citing it confirms that reading: a 2026 meta-analysis of 51 take-up experiments finds that cutting the work of applying raises take-up by about 8 points against about 3 for information, and trials in France found the same pattern. So the article's point that the barrier was effort and access rather than motivation holds. But the experiment compared two remedies chosen in advance rather than testing a diagnosis step, and direct tests of diagnose-then-tailor in healthcare find only a slight improvement, so 'the clearest evidence for diagnosing first' claims more than the study shows. Now cites [Increasing Take-Up of Social Benefits: A Meta-Analysis of Field Experiments, Journal of Policy Analysis and Management (2026)](https://doi.org/10.1002/pam.70085).

### The Tax-Office Experiment: contested

**Claim reviewed:** Most "explain the value better" fixes in digital products are information-only arms, and they fail for the same reason.

**Now reads:** Many "explain the value better" fixes in digital products are information-only arms. When the real barrier is effort or access, they tend to fall short for the same reason.

**Why:** Information-only arms have failed repeatedly where the obstacle is effort or access: six EITC experiments with a million households, FAFSA nudges at scale, a French benefits simulator and a childcare trial all found little or nothing. But information is not a reliable failure either: it raised SNAP take-up on its own, a 2026 meta-analysis puts information arms at about 3.4 points against 8.3 for assistance, and school-choice, energy and financial-education studies found real effects. No study measures digital-product fixes, so 'most' and 'they fail' state a tendency as a rule. Now cites [Increasing Take-Up of Social Benefits: A Meta-Analysis of Field Experiments, Journal of Policy Analysis and Management (2026)](https://doi.org/10.1002/pam.70085).

### Five Steps, step 4: supported with caveats

**Claim reviewed:** Support tickets, site search terms, recordings and five short interviews are usually enough to rule diagnostic boxes in or out.

**Now reads:** Support tickets, site search terms, recordings and a handful of short interviews are often enough to rule a box in or out for a single step. If the signals disagree, gather more before you decide.

**Why:** Saturation studies find that about six interviews capture most themes in a homogeneous group, and Virzi found four or five users surface 80 percent of usability problems with the severe ones first, so five interviews plus tickets, search terms and recordings is a reasonable basis for ruling one box in or out at a single step. Other studies show the number is unreliable on its own: random sets of five users found between 55 and 99 percent of problems, four production web sites needed far more than five users, and code saturation took nine interviews with meaning saturation at 16 to 24. 'Usually enough' is fair for a narrow, salient barrier and too firm for anything broader or a mixed audience. Now cites [Nielsen & Landauer, A Mathematical Model of the Finding of Usability Problems (INTERCHI 1993)](https://doi.org/10.1145/169059.169166).
