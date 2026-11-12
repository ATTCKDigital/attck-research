---
title: "Evidence review: Creating a Full Behavioral Redesign"
---

# Evidence review: Creating a Full Behavioral Redesign

Article: [Creating a Full Behavioral Redesign](https://attck.com/blog/creating-a-full-behavioral-redesign/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### The Experiment That Shapes Every Decision Here

**Karlan and List sent fundraising letters to more than 50,000 previous donors of a US nonprofit; some letters offered a matching grant and some did not.**

- [Karlan and List (2007), Does Price Matter in Charitable Giving?, American Economic Review (AEA abstract page)](https://www.aeaweb.org/articles?id=10.1257/aer.97.5.1774): “Using direct mail solicitations to over 50,000 prior donors of a nonprofit organization, we tested the effectiveness of a matching grant on charitable giving.”

**The match offer increased both the share of people who gave and the revenue per letter.**

A follow-up field experiment by Karlan, List and Shafir (2011) with about 20,000 donors to a similar organization found only weak evidence that $1:$1 or $1:$3 matches raised giving overall, with effects concentrated among recently active donors. Matching works, but less reliably than one experiment suggests.

**Larger match ratios, $2:$1 and $3:$1, added nothing over $1:$1.**

The ratio finding replicated in direction in Karlan, List and Shafir (2011), which compared $1:$1 with $1:$3.

- [Karlan, List and Shafir (2011), Small matches and charitable giving, Journal of Public Economics (author PDF)](http://s3.amazonaws.com/fieldexperiments-papers2/papers/00284.pdf): “larger match ratios are not necessarily superior to smaller match ratios.”

**Response rose from 1.8 percent without a match to 2.2 percent with one.**

- [Karlan and List (2006), NBER Working Paper 12338](https://www.nber.org/system/files/working_papers/w12338/w12338.pdf): “In addition, the match offer significantly increases the probability that an individual donates—by 22%.”

**The size of the overall matching pool and the example amount quoted in the letter made no meaningful difference.**

In a later experiment, a high example amount paired with a match below $1:$1 reduced giving (Karlan, List and Shafir 2011), so the details can matter in other setups.

**And the match worked only among donors in states that voted Republican in 2004. The charity was a liberal advocacy group, and the authors tested several explanations for the split and left it to future research.**

The organization in Karlan and List's experiment was a liberal civil-liberties group, which the authors note when discussing the red-state result. The split may say more about donors giving to a cause outside their usual politics than about matching in general.

**An average effect can hide a group that doesn't respond at all.**

A second example: in Karlan, List and Shafir (2011), recently active donors responded to a match while lapsed donors did not or gave less.

### The landing screen / The account form

**A buried call to act, and the work of setting a password before paying, are physical-opportunity barriers in COM-B terms.**

Confirmed against the COM-B definitions in Michie et al. (2011).

- [Michie, van Stralen and West (2011), The Behaviour Change Wheel, Implementation Science (Europe PMC full text; publisher page blocked)](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3096582/fullTextXML): “Opportunity is defined as all the factors that lie outside the individual that make the behaviour possible or prompt it.”

### The amount screen and the match

**The toggling pointed to psychological capability, the effort of understanding the choice: a frequency option that was easy to miss and amounts with nothing to compare them by. The fix is in the screen, which is physical opportunity, so the change targets both.**

COM-B coding of interface problems often has two readings: the strain falls on the person's capability, while the cause sits in the environment (opportunity).

- [Michie, van Stralen and West (2011), The Behaviour Change Wheel, Implementation Science (Europe PMC full text; publisher page blocked)](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3096582/fullTextXML): “psychological capability being the capacity to engage in the necessary thought processes - comprehension, reasoning”

### The commitment line

**Hesitation over an open-ended commitment is a reflective-motivation barrier in COM-B terms.**

Confirmed against the COM-B motivation definitions in Michie et al. (2011).

- [Michie, van Stralen and West (2011), The Behaviour Change Wheel, Implementation Science (Europe PMC full text; publisher page blocked)](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3096582/fullTextXML): “we distinguished between reflective processes (involving evaluations and plans) and automatic processes (involving emotions and impulses that arise from associative learning and/or innate dispositions)”

**Telling donors they can change or stop a monthly gift any time with one click reduces hesitation over an open-ended commitment.**

Direct experimental evidence on 'cancel any time' copy for recurring gifts was not found; retail survey data on return policies is the closest support. The redesign tests this line separately.

- [Baymard Institute, Cart abandonment rate statistics (survey of US online shoppers)](https://baymard.com/lists/cart-abandonment-rate): “13% Returns policy wasn't satisfactory”

### The account form

**Requiring account and password creation before payment is a major source of drop-off; moving account creation to after the gift reduces the loss.**

Baymard Institute's checkout surveys list being required to create an account among the top reasons US shoppers abandon a purchase. This is survey evidence from retail; the donation flow here is illustrative.

- [Baymard Institute, Cart abandonment rate statistics (survey of US online shoppers)](https://baymard.com/lists/cart-abandonment-rate): “18% The site wanted me to create an account”

### The amount screen and the match / Testing the Redesign

**On the match, Karlan and List's result suggests not paying for a bigger ratio. Whether a longer $1:$1 match beats a short one is our own question, not theirs. Donor experiments that varied deadline length found it made little difference, so the test plan checks it rather than assuming it.**

Karlan and List did not test match length. In Karlan, List and Shafir (2011), a randomized October versus December match deadline made no significant difference during the campaign. With 53,000 Danish donors, varying the deadline did not change the share who gave; donations came at once or not at all (Damgaard and Gravert 2017). In a charity-linked task, a one-month deadline drew the fewest responses (Knowles et al. 2021). Longer windows can also invite procrastination (Shu and Gneezy 2010), and giving fell after a match ended (Meier 2007).

- [Karlan and List (2007), Does Price Matter in Charitable Giving?, American Economic Review (AEA abstract page)](https://www.aeaweb.org/articles?id=10.1257/aer.97.5.1774): “Larger match ratios (i.e., $3:$1 and $2:$1) relative to a smaller match ratio ($1:$1) had no additional impact, however.”

### Do's and Don'ts

**Escalating an incentive by default. A bigger match may cost more and change nothing. Test the size before you pay for it.**

The evidence that bigger incentives add nothing comes from charitable match ratios. For discounts and cash bonuses, size often does change behavior, so test before assuming either way.

- [Karlan and List (2007), Does Price Matter in Charitable Giving?, American Economic Review (AEA abstract page)](https://www.aeaweb.org/articles?id=10.1257/aer.97.5.1774): “Larger match ratios (i.e., $3:$1 and $2:$1) relative to a smaller match ratio ($1:$1) had no additional impact, however.”
- [Karlan, List and Shafir (2011), Small matches and charitable giving, Journal of Public Economics (author PDF)](http://s3.amazonaws.com/fieldexperiments-papers2/papers/00284.pdf): “larger match ratios are not necessarily superior to smaller match ratios.”

**Declaring victory at launch. Early results can drift as novelty wears off or as people adapt. Keep the holdout running.**

Online-experiment research documents both novelty effects (early lifts that fade) and primacy effects (gains that grow as people adapt), which is why a long-running holdout matters.

- [Sadeghi et al. (2021), Novelty and Primacy: A Long-Term Estimator for Online Experiments, arXiv](https://arxiv.org/abs/2102.12893): “observed treatment effects are not always permanently stable, sometimes revealing increasing or decreasing patterns over time.”

### Testing the Redesign Without Fooling Yourself

**Karlan and List found their state split only after the fact, which is a reason to name segments before the results arrive: new versus returning donors, mobile versus desktop.**

The red/blue split in Karlan and List was an after-the-fact analysis. Naming subgroups in advance is standard in clinical trials and guards against chasing chance differences.

- [Karlan and List (2006), NBER Working Paper 12338](https://www.nber.org/system/files/working_papers/w12338/w12338.pdf): “Including these variables does not change the core result that the matching grant only worked in red states.”
- [Karlan, List and Shafir (2011), Small matches and charitable giving, Journal of Public Economics (author PDF)](http://s3.amazonaws.com/fieldexperiments-papers2/papers/00284.pdf): “lapsed givers are either not affected or adversely affected.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### The Experiment That Shapes Every Decision Here: supported with caveats

**Claim reviewed:** The match worked only among donors in states that voted Republican in 2004, a split the authors tested several explanations for and left to future research.

**Now reads:** And the match worked only among donors in states that voted Republican in 2004. The charity was a liberal advocacy group, and the authors tested several explanations for the split and left it to future research.

**Why:** The paper does report that the match worked only in red states, tested several explanations, and left the question to future research. What the article leaves out is that the charity was a liberal civil-liberties group, which is the most likely reason the split appeared and the main reason it may not carry over to other causes.

### The Experiment That Shapes Every Decision Here: contested

**Claim reviewed:** Lesson drawn from the experiment: a reason to act now matters more than its size.

**Now reads:** Three lessons follow, and each turns up below. Having a reason to give matters more than how big that reason is. The details you assume are doing the work often aren't. And an average effect can hide a group that doesn't respond at all.

**Why:** Karlan and List tested whether a match was offered and how big it was, not whether people were told to act now, so 'act now' is the article's addition. Field experiments with donors find deadlines and urgency lines do not raise giving: the same team's follow-up found an urgency line without a reason reduced giving, and 53,000 Danish donors gave at the same rate whatever deadline they were sent. Marketing research still finds scarcity and urgency cues raise purchase intentions, so the evidence points both ways while the article states the lesson as settled. Now cites [Karlan, List and Shafir (2011), Small matches and charitable giving, Journal of Public Economics (author PDF)](http://s3.amazonaws.com/fieldexperiments-papers2/papers/00284.pdf).

### The amount screen and the match: supported with caveats

**Claim reviewed:** Too many options and an easy-to-miss frequency choice are a psychological-capability barrier in COM-B terms.

**Now reads:** The toggling pointed to psychological capability, the effort of understanding the choice: a frequency option that was easy to miss and amounts with nothing to compare them by. The fix is in the screen, which is physical opportunity, so the change targets both.

**Why:** COM-B defines psychological capability as the capacity for comprehension and reasoning, and an overloaded, easy-to-miss choice does strain that. But the cause in this case sits in the screen design, which COM-B would usually code as physical opportunity. Either reading is defensible; the article gives only one.

### The amount screen and the match: contested

**Claim reviewed:** Six amount options were too many and drove back-and-forth toggling; cutting to three amounts reduces this barrier.

**Now reads:** The toggling pointed to psychological capability: a frequency choice that was easy to miss, and six amounts with nothing to tell them apart. Three amounts, each tied to what it pays for, give people a basis for comparing them. Whether fewer amounts helps on its own is an open question in the research, so the test plan checks it.

**Why:** The article treats six amounts as too many, which leans on choice overload. The general research is split: one meta-analysis of 50 experiments found an average effect near zero, a later one found the effect is real when options are hard to compare, and 401(k) and volunteering studies found more options meant less participation or more deferral. The most direct evidence cuts the other way: in seven studies a short list of amounts beat an open ask because it signaled a normal gift size, and in six experiments plus a natural experiment adding more amount options raised donations without cutting the share who gave. Now cites [Moon and VanEpps (2022), Giving Suggestions: Using Quantity Requests to Increase Donations, Journal of Consumer Research](https://doi.org/10.1093/jcr/ucac047).

### The amount screen and the match / Testing the Redesign: supported with caveats

**Claim reviewed:** Karlan and List's result suggests asking the funder for a longer $1:$1 match rather than a bigger ratio.

**Now reads:** On the match, Karlan and List's result suggests not paying for a bigger ratio. Whether a longer $1:$1 match beats a short one is our own question, not theirs. Donor experiments that varied deadline length found it made little difference, so the test plan checks it rather than assuming it.

**Why:** The half about not paying for a bigger ratio follows from Karlan and List. The half about a longer match is the article's own idea, labeled as such and put to a test, which is right. Readers should know the idea has already been tried: the same team randomized a short against a long match deadline and found no significant difference during the drive, and field experiments with donors found the length of a giving window did not change the share who gave, with the longest window doing worst in one study. Now cites [Damgaard and Gravert (2017), Now or never! The effect of deadlines on charitable giving: Evidence from two natural field experiments, Journal of Behavioral and Experimental Economics](https://doi.org/10.1016/j.socec.2016.04.013).

### Do's and Don'ts: supported with caveats

**Claim reviewed:** Escalating an incentive by default is a mistake: a bigger match, discount or bonus may cost more and change nothing.

**Now reads:** Escalating an incentive by default. A bigger match may cost more and change nothing. Test the size before you pay for it.

**Why:** For charity matches, the evidence backs the warning: bigger ratios did not raise giving in two field experiments. The sentence also extends it to discounts and bonuses, where size often does matter, and Karlan and List's data says nothing about those. The hedge 'may' keeps it from being wrong, but the example list reaches beyond the evidence.

### The first month: contested

**Claim reviewed:** A monthly gift is decided again every month, so a thank-you page that says when the first charge lands and a short update before the second charge support continued giving.

**Now reads:** The old thank-you page said "Thank you." The new one says when the first charge lands and what it will fund, and a short update arrives before the second charge. A monthly gift can be stopped any month, which is the argument of "Long-Term Persuasion" and "Funnel Psychology and Retention." Thank-you contact on its own has a poor record in field tests, so this change goes into the test plan with the others.

**Why:** A monthly gift can be stopped any month, so the instinct is sound, but the specific fix has a weak record. In field experiments with 500,000 new donors, a thank-you call had a precisely estimated null effect on retention when fundraisers had predicted an 80 percent lift. Telling donors what a gift achieves cut both ways in a mailing test, and subscription data show that making people re-decide a recurring charge raises cancellations, while small studies find thanks and acknowledgements lift goodwill. The article presents the new page and update as part of the fix rather than something to test. Now cites [Samek and Longfield (2023), Do Thank-You Calls Increase Charitable Giving? Expert Forecasts and Field Experimental Evidence, American Economic Journal: Applied Economics](https://doi.org/10.1257/app.20210068).

### Do's and Don'ts: supported with caveats

**Claim reviewed:** Early lifts can come from novelty, so keep the holdout running after launch.

**Now reads:** Declaring victory at launch. Early results can drift as novelty wears off or as people adapt. Keep the holdout running.

**Why:** Microsoft's experimentation researchers document that treatment effects in online tests drift over time, with novelty as one named cause, so keeping a holdout is sound advice. The same work notes the opposite drift too: effects can grow as people adapt, so early results can understate as well as overstate. Now cites [Sadeghi et al. (2021), Novelty and Primacy: A Long-Term Estimator for Online Experiments, arXiv](https://arxiv.org/abs/2102.12893).

### Testing the Redesign Without Fooling Yourself: supported with caveats

**Claim reviewed:** Karlan and List's state split argues for naming segments (new versus returning, mobile versus desktop) before the results arrive.

**Now reads:** Karlan and List found their state split only after the fact, which is a reason to name segments before the results arrive: new versus returning donors, mobile versus desktop.

**Why:** Naming segments before results arrive is sound practice, and the state split shows why effects can sit in one group. But Karlan and List found that split after the fact; their paper is an example of the problem, not a source for the remedy. The sentence reads as if the paper argues for pre-registration, which it does not.
