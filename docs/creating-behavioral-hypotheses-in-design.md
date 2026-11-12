---
title: "Evidence review: Creating Behavioral Hypotheses in Design"
---

# Evidence review: Creating Behavioral Hypotheses in Design

Article: [Creating Behavioral Hypotheses in Design](https://attck.com/blog/creating-behavioral-hypotheses-in-design/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

The term HiPPO comes from Avinash Kaushik (2006) and was later popularized in Kohavi's experimentation papers.

- [Kaushik, Seven Steps to Creating a Data Driven Decision Making Culture (2006)](https://www.kaushik.net/avinash/seven-steps-to-creating-a-data-driven-decision-making-culture/): “HiPPO’s rule the world, they over rule your data, they impose their opinions on you and your company customers”

Multivariable (factorial) experiments can estimate the effect of several simultaneous changes. A single bundled A/B test cannot.

- [Wingify (VWO), Lyyti success story](https://wingify.com/success-stories/lyyti/): “The variation beat the original, because it included at least 3 elements that were missing in the original”

### Building a Hypothesis Library

Cognitive load theory (Sweller 1988) comes from instructional design, where a 2019 meta-analysis confirms that segmenting helps. Survey experiments (Peytchev et al. 2006; Toepoel et al. 2009; Mavletova and Couper 2014) find tradeoffs between paged and single-page forms, and Baymard reports no inherent advantage for either checkout format.

- [Rey et al., A Meta-analysis of the Segmenting Effect, Educational Psychology Review 31 (2019)](https://eric.ed.gov/?id=EJ1217373): “This meta-analysis contains 56 investigations including 88 pairwise comparisons and reveals a significant segmenting effect with small to medium effects for retention and transfer performance.”
- [Toepoel, Das & van Soest, Design of Web Questionnaires: The Effects of the Number of Items per Screen, Field Methods 21(2) 2009](https://doi.org/10.1177/1525822x08330261): “nonresponse increases with the number of items appearing on a single screen.”

Social proof effects vary by setting; a two-hotel replication of the towel-reuse study found descriptive-norm messages no better than a standard appeal (Bohner & Schluter 2014).

- [Influence at Work, The 7 Principles of Persuasion](https://www.influenceatwork.com/7-principles-of-persuasion/): “Especially when they are uncertain, people will look to the actions and behaviors of others to determine their own.”

### Clearer Choices on the Pricing Page

The VWO case reports page visits rather than completed trials and gives no sample size.

- [Wingify (VWO), Lyyti success story](https://wingify.com/success-stories/lyyti/): “increasing visits to the lead generation page by 93.71%, with a statistical significance of 96%.”

The Lyyti test bundled three changes, so the reasons given for the lift are the team's interpretation, not separate findings.


### Prioritizing Hypotheses with Evidence

ICE was popularized by Sean Ellis (Hacking Growth, 2017). Scores are subjective, which is part of why the article's added evidence column is useful.

- [ProductPlan, ICE Scoring Model glossary](https://www.productplan.com/glossary/ice-scoring-model/): “is in no small part due to the person who created it, Sean Ellis.”

### Case Study: The Endowed Progress Effect

Nunes and Drèze (2006) handed out 300 loyalty cards and tracked redemptions for nine months; 34% versus 19% is a 1.8-fold difference, significant at p < .01. The authors report moderators (the reason given for the bonus stamps and the currency of progress), Koo and Fishbach (2010) find endowed progress matters most early in goal pursuit, and a 2020 study finds the related goal-gradient effect weakens under high power.

- [Kivetz, Urminsky & Zheng, The Goal-Gradient Hypothesis Resurrected, JMR 2006](https://doi.org/10.1509/jmkr.43.1.39): “the illusion of progress toward the goal induces purchase acceleration (e.g., customers who receive a 12-stamp coffee card with 2 preexisting “bonus” stamps complete the 10 required purchases faster”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: contested

**Claim reviewed:** Most design failures stem from untested assumptions, not bad ideas.

**Now reads:** Many design changes fail because no one tested the assumption behind them. When companies run controlled experiments on their own ideas, only a minority win: about a third at Microsoft, and 10 to 20 percent at Google and Bing.

**Why:** No source is cited, and no study measures why design changes fail. The nearest evidence is experiment win rates: about a third of ideas tested at Microsoft improve their target metric, and only 10 to 20 percent do at Google and Bing. That supports testing assumptions, because experts cannot tell winners in advance, but it also shows that most ideas really are not good, so the 'not bad ideas' half runs against the evidence. Now cites [Kohavi & Thomke, The Surprising Power of Online Experiments, Harvard Business Review (2017)](https://hbr.org/2017/09/the-surprising-power-of-online-experiments).

### Introduction: supported with caveats

**Claim reviewed:** In digital product teams, decisions often hinge on a gut instinct or the Highest Paid Person's Opinion (HiPPO).

**Now reads:** In digital product teams, decisions often hinge on a gut instinct or what analytics writer Avinash Kaushik calls the HiPPO, the Highest Paid Person's Opinion.

**Why:** The HiPPO idea is real and widely used, but the term was coined by Avinash Kaushik and the article does not credit him. 'Often' rests on practitioner opinion, not a measurement of how product teams decide. Now cites [Kaushik, Seven Steps to Creating a Data Driven Decision Making Culture (Occam's Razor, 2006)](https://www.kaushik.net/avinash/seven-steps-to-creating-a-data-driven-decision-making-culture/).

### Introduction: supported with caveats

**Claim reviewed:** Launching a complete redesign all at once muddies the water; you never know which tweak actually moved the needle.

**Now reads:** Launching a complete redesign all at once muddies the water. Unless the test is designed to separate the changes, you can't tell which tweak moved the needle.

**Why:** A redesign that changes many things at once does make it hard to say which change mattered. 'You never know' goes too far, because multivariable tests are built to separate several changes at once. The article's own Lyyti example bundled three changes and still drew a lesson from them. Now cites [Kohavi, Crook & Longbotham, Online Experimentation at Microsoft (2009)](https://exp-platform.com/Documents/ExPThinkWeek2009Public.pdf).

### From Guess to Hypothesis: misattributed

**Claim reviewed:** Increasing the size and contrast of a button reduces targeting effort in line with Fitts's Law, a theory from motor control research.

**Now reads:** Making the free trial button larger will reduce targeting effort in line with Fitts's Law, and stronger contrast will make it easier to spot. Together they should raise the click-through rate by at least 10 percent within two weeks of rollout.

**Why:** Fitts's Law predicts how long a rapid aimed movement takes from the target's distance and width, so the size half is right and the motor-control attribution is fair. Contrast is not a term in the law. Harder-to-see targets do take longer to hit, but the one recent study that measured this needed a model that extends Fitts's Law to fit the data. The law also predicts movement time, not click-through rate. Now cites [MacKenzie, Fitts' law as a research and design tool in human-computer interaction, Human-Computer Interaction 7(1) 1992](https://www.yorku.ca/mack/hci1992.html).

### Building a Hypothesis Library: supported with caveats

**Claim reviewed:** Where cognitive load is high, splitting forms into steps helps, drawing on cognitive load theory.

**Now reads:** High cognitive load? Test splitting long forms into steps. Cognitive load theory, and a meta-analysis of segmented instruction, suggest smaller chunks are easier to process, though experiments on paged versus single-page forms show tradeoffs rather than a clear winner.

**Why:** In cognitive load theory's home field, a meta-analysis of 56 studies finds that breaking instruction into segments improves learning and lowers reported load, so the theory does back chunking. Form and survey experiments are less clear-cut: fewer items per screen cuts skipped questions but lengthens completion, one large student survey found tradeoffs either way, and on phones a single scrolling page was faster and better liked. Multi-step forms are a reasonable thing to test, not a settled fix. Now cites [Rey et al., A Meta-analysis of the Segmenting Effect, Educational Psychology Review (2019)](https://eric.ed.gov/?id=EJ1217373).

### Building a Hypothesis Library: supported with caveats

**Claim reviewed:** Adding quotes from recent buyers taps into Cialdini's work on social proof.

**Now reads:** Low social proof? Add quotes from recent buyers or show how many people use the product, drawing on Cialdini's work on social proof.

**Why:** Cialdini's social proof principle says people copy what others do when they are unsure, so the attribution is fair. Individual buyer quotes are testimonials, a looser fit than showing what many people do. A field replication of a famous social-proof message also found it worked no better than a standard message, so results vary. Now cites [Influence at Work, The 7 Principles of Persuasion](https://www.influenceatwork.com/7-principles-of-persuasion/).

### Clearer Choices on the Pricing Page: supported with caveats

**Claim reviewed:** After a test that ran for more than five months, the variation produced a 93.7% increase in visits to the free trial page.

**Now reads:** After a test that ran for more than five months, the variation produced a 93.7% increase in visits to the free trial page, at 96% statistical significance. VWO did not report how many of those visits became sign-ups.

**Why:** The numbers match the source. But the metric is visits to the sign-up page, not sign-ups, the reported significance is only 96%, and no sample size is given. Vendor success stories are also a selected sample, since most tested ideas do not win.

### Clearer Choices on the Pricing Page: supported with caveats

**Claim reviewed:** The lift came from clarity: features beside prices let prospects compare plans without leaving the page, and a single repeated call to action removed a competing decision.

**Now reads:** The likely lesson is about clarity. With features listed beside the prices, prospects could compare plans without leaving the page, and every button now asked for the same thing. Because the changes shipped together, the test can't say which one mattered most.

**Why:** The case study itself gives this explanation, so the article is not inventing it. But all the changes shipped together, so the test cannot show which one caused the lift. The variation also had five more buttons than the original, which sits awkwardly with a lesson about 'not quantity'.

### Clearer Choices on the Pricing Page: not supported

**Claim reviewed:** In Sheena Iyengar's 2000 'Jam Study', reducing jam flavors in a grocery display from 24 to 6 increased sales by 900%.

**Now reads:** In a well-known 2000 field study by Sheena Iyengar and Mark Lepper, about 30% of shoppers who stopped at a display of 6 jams bought one, compared with 3% at a display of 24, even though the larger display drew more people. Later research suggests the effect depends heavily on context, and a meta-analysis found no effect on average.

**Why:** The study is real (Iyengar and Lepper, 2000), but the article misdescribes it. Nothing was reduced: the 6-jam and 24-jam displays alternated every hour over two Saturdays. The large display drew more people (145 of 242 passers-by stopped, versus 104 of 260), but only 4 of those buyers purchased jam, against 31 at the small display. The 900% figure is the tenfold purchase rate among shoppers who stopped (3% versus 30%), not a rise in sales. Later meta-analyses find the average choice-overload effect near zero or dependent on conditions. Now cites [Iyengar & Lepper, When Choice Is Demotivating, Journal of Personality and Social Psychology (2000)](https://pubmed.ncbi.nlm.nih.gov/11138768/).

### Clearer Choices on the Pricing Page: not supported

**Claim reviewed:** The same pressure (choice overload) behind the Lyyti result shows up in the jam study.

**Now reads:** Removing a competing call to action is a different lever from cutting the number of products on offer, but both aim to make the next step easier to see.

**Why:** Lyyti did not cut the number of plans; it went from two button messages to one while adding five buttons. The jam study compares 6 products with 24, and Iyengar and Lepper themselves note that earlier research found choice among a few options better than no choice, so trimming two messages to one is not the pressure they studied. Practitioner tests on adding or removing a second call to action go both ways, and neither source links the two cases. Now cites [Chernev, Bockenholt & Goodman, Choice Overload: A Conceptual Review and Meta-Analysis, JCP 2015](https://www.kellogg.northwestern.edu/academics-research/research/detail/2015/when-product-assortment-leads-to-choice-overload-a-conceptual/).

### Case Study: The Endowed Progress Effect: supported with caveats

**Claim reviewed:** The pre-stamped group had a 34% completion rate versus 19% for the control group.

**Now reads:** Over the following nine months, 34% of the head-start group completed their cards, compared with 19% of the control group.

**Why:** The 19% and 34% figures are widely reported and match a secondary summary of the paper. The article leaves out that these are completion rates over about nine months, and the numbers were not checked against the paper's own table.

### Case Study: The Endowed Progress Effect: supported with caveats

**Claim reviewed:** The illusion of progress doubled the motivation to finish, which proves that behavior is driven by how effort is framed, not only by effort required.

**Now reads:** The head start, worth nothing in real terms, raised completion from 19 percent to 34 percent, nearly double. The study suggests behavior depends not just on the effort required, but on how that effort is framed.

**Why:** The primary source now confirms the result: 300 cards, nine months, and 34% versus 19% redemption, with an independent coffee-card experiment finding the same pattern. But 34 against 19 is 1.8 times, so 'nearly doubled' is right and 'doubled' is not; the study measured card redemption, not motivation; and 'proves' overstates one field study whose authors report that the effect depends on the reason given for the head start, with later work finding further limits.
