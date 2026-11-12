---
title: "Evidence review: Designing for Trust Between Users"
---

# Evidence review: Designing for Trust Between Users

Article: [Designing for Trust Between Users](https://attck.com/blog/designing-for-trust-between-users/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Opening

**On a large online labor marketplace, over six years the share of workers receiving a perfect five-star score grew from 33 percent to 85 percent.**

The paper's body text counts the same figure as a share of contracts; its introduction counts workers, as the article does.

- [Filippas, Horton, Golden, Reputation Inflation (authors' 2020 version)](https://john-joseph-horton.com/papers/longrun.pdf): “the fraction of workers receiving a perfect 5-star rating grew from 33% to 85% in just 6 years.”

**The platform tried a sensible fix. Alongside the public rating, it asked clients a private question the worker never saw. At first it asked, "Would you hire this freelancer again, if you had a similar project?" Later it asked clients to rate, from 0 to 10, how likely they were to recommend the freelancer.**

The hire-again question was replaced in June 2014 by a 0 to 10 recommend question; the trend and publication results in the paper use the recommend score.

**The private answers were candid. In the ten months the platform collected them, public scores for the same jobs edged up while private scores fell.**

The private-versus-public comparison covers about ten months, during which public scores rose only slightly.

- [Jawahar and Williams, Where all the children are above average: the performance appraisal purpose effect (Personnel Psychology, 1997)](https://doi.org/10.1111/j.1744-6570.1997.tb01487.x): “performance evaluations obtained for administrative purposes were, on average, one‐third of a standard deviation larger than those obtained for research or employee development purposes.”

**After ten months, the platform began showing future clients batched averages of the private scores; they started rising immediately, while the tone of the written feedback barely changed.**

Evidence comes from one platform's policy change, compared before and after.

### Why Ratings Drift Upward

**In the same marketplace, 28.4 percent of clients who privately said they would definitely not hire a worker again still gave that worker four or more stars in public.**

Only 6.6 percent of clients chose 'definitely not', so the 28.4 percent is a share of a small group.

- [Filippas, Horton, Golden, Reputation Inflation (authors' 2020 version)](https://john-joseph-horton.com/papers/longrun.pdf): “28.4% of those employers that privately report that they would definitely not hire the same worker in the future, publicly assign them 4 or more stars out of 5.”
- [Home and away (Psychology & Marketing, 2019)](https://doi.org/10.1002/mar.21264): “Our findings indicate that there is a consistent review gap between institutional actors and peer‐to‐peer actors.”

**Reporting a bad experience is costly to the rater: the other party may complain or retaliate, and a low score can harm someone's income.**

In this marketplace both sides' reviews were revealed together, so retaliation meant complaints or lost cooperation rather than a revenge rating.

- [Bolton, Greiner, Ockenfels, Engineering Trust: Reciprocity in the Production of Reputation Information (Management Science, 2013)](https://doi.org/10.1287/mnsc.1120.1609): “Reciprocity in feedback giving distorts the production and content of reputation information in a market, hampering trust and trade efficiency.”
- [van Rooyen et al. (BMJ, 1999)](https://pubmed.ncbi.nlm.nih.gov/9872878/): “Reviewers randomised to be asked to be identified were 12% (95% confidence interval 0.2% to 24%) more likely to decline to review than reviewers randomised to remain anonymous”

### The case for ratings

**In a smaller second test, one or two negative ratings on a new seller did not measurably change what buyers paid.**

The negative-feedback result came from a small subsidiary test and measured price paid; large eBay panel data link a first negative to falling sales.

- [Resnick, Zeckhauser, Swanson, Lockwood, The Value of Reputation on eBay (Experimental Economics, 2006), author pre-publication version](https://presnick.people.si.umich.edu/papers/postcards/PostcardsFinalPrePub.pdf): “Surprisingly, one or two negative feedbacks for our new sellers did not affect buyers’ willingness-to-pay.”

### The case against trusting them forever

**Filippas, Horton and Golden's estimates put more than half of the rise in scores over six years down to inflation rather than better work.**

An earlier draft of the paper estimated that at least 35 to 45 percent of the rise was inflation; the 2020 version says more than half.

- [Filippas, Horton, Golden, Reputation Inflation (authors' 2020 version)](https://john-joseph-horton.com/papers/longrun.pdf): “Our estimates suggest that more than 50% of the increase in scores over a 6 year period was due to inflation”

### Book callout

**Kraut and Resnick turn social science research into numbered design claims about getting people to contribute and keeping behavior in line. Resnick also led the eBay reputation experiment cited here, and the book's chapters on regulating behavior and on newcomers give useful background for the checklist.**

The book predates the Airbnb and inflation studies, so it is background reading rather than the source for the reveal and privacy questions.

- [Kraut and Resnick, Building Successful Online Communities (MIT Press, 2012), Crossref record](https://doi.org/10.7551/mitpress/8472.001.0001): “translating general findings into useful design claims”

### Reveal both reviews at once

**In a large experiment on Airbnb, Andrey Fradkin, Elena Grewal and David Holtz hid each review until both host and guest had submitted one. Somewhat more people reviewed, partly from curiosity about what the other side wrote.**

Review rates rose 1.7 percent for guests and 9.8 percent for hosts; a lab study found the opposite direction.

- [Fradkin, Grewal, Holtz, Reciprocity and Unveiling in Two-Sided Reputation Systems (Marketing Science, 2021)](https://andreyfradkin.com/assets/reviews_paper.pdf): “The treatment stimulated more reviewing in total. This is due to users’ curiosity about what their counterparty wrote and/or the desire to have feedback visible to other users.”

**Retaliation and reciprocation fell, and ratings came out slightly lower. (Do's list: Hide reviews until both are in. It reduces the fear of a revenge review and the temptation to trade compliments.)**

The rating drop under simultaneous reveal was small (average guest rating 0.25 percent lower), and a marketplace that already used simultaneous reveal still saw inflation.

- [Bolton, Greiner, Ockenfels (Management Science, 2013)](https://doi.org/10.1287/mnsc.1120.1609): “we run laboratory experiments to investigate how reciprocity can be managed by changes in the way feedback information flows through the system, leading to more accurate reputation information”

### Decide what identity shows first

**In a field experiment on Airbnb, requests from guests with distinctively African American names were 16 percent less likely to be accepted than identical requests from guests with distinctively white names.**

A later Airbnb field experiment (Cui, Li and Zhang, 2020) found a similar gap.

- [Edelman, Luca, Svirsky, Racial Discrimination in the Sharing Economy (AEJ: Applied, 2017), abstract](https://www.aeaweb.org/articles?id=10.1257/app.20160213): “applications from guests with distinctively African American names are 16 percent less likely to be accepted relative to identical guests with distinctively white names.”
- [Cui, Li, Zhang, Discrimination with Incomplete Information in the Sharing Economy (Management Science, 2020)](https://doi.org/10.1287/mnsc.2018.3273): “requests from guests with African American–sounding names are 19.2 percentage points less likely to be accepted than those with white-sounding names.”
- [Bertrand and Mullainathan (American Economic Review, 2004)](https://doi.org/10.1257/0002828042002561): “White names receive 50 percent more callbacks for interviews.”

### Decide what identity shows first / Do's and Don'ts

**Where the transaction allows it, lead with evidence of behavior, such as reviews, verification and response history, and show names and photos once the decision has been made. In a later Airbnb experiment, a single positive review closed the gap between guests with white and African American names. Reviews can carry bias too, so check outcomes by group after the change.**

The Edelman, Luca and Svirsky experiment used names only. Evidence that reputation information narrows the gap comes from Cui, Li and Zhang (2020); evidence on photos comes from Doleac and Stein (2013).

- [Cui, Li, Zhang (Management Science, 2020)](https://doi.org/10.1287/mnsc.2018.3273): “when guest accounts receive a positive review, the acceptance rates of guest accounts with white- and African American–sounding names are statistically indistinguishable.”
- [Doleac and Stein, The Visible Hand: Race and Online Market Outcomes (Economic Journal, 2013)](https://doi.org/10.1111/ecoj.12082): “Black sellers do worse than white sellers on a variety of market outcome measures: They receive 13% fewer responses and 17% fewer offers.”
- [Edelman, Luca, Svirsky (2017), author's accepted manuscript](https://www.benedelman.org/publications/airbnb-guest-discrimination-2016-09-16.pdf): “Airbnb has several options to reduce discrimination. For example, it could conceal guest names, just as it already prevents transmission of email addresses and phone numbers”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Opening: supported with caveats

**Claim reviewed:** Alongside the public rating, the platform asked clients a private question the worker never saw: "Would you hire this freelancer again, if you had a similar project?"

**Now reads:** The platform tried a sensible fix. Alongside the public rating, it asked clients a private question the worker never saw. At first it asked, "Would you hire this freelancer again, if you had a similar project?" Later it asked clients to rate, from 0 to 10, how likely they were to recommend the freelancer.

**Why:** The quoted question is accurate, but the platform replaced it in June 2014 with a 0 to 10 question about how likely the client was to recommend the freelancer. The falling private scores and the later publication described next are about that recommend score, so the story joins two different private questions into one.

### Opening: supported with caveats

**Claim reviewed:** The private answers were candid: over the same period that public scores kept climbing, private scores for the same jobs went down.

**Now reads:** The private answers were candid. In the ten months the platform collected them, public scores for the same jobs edged up while private scores fell.

**Why:** The paper does find private scores falling while public scores for the same jobs rose. But that comparison covers only the roughly ten months private scores were collected, not the six years in the opening line, and the public rise in that window was small. Research on workplace appraisals agrees that ratings with no consequences come out lower.

### Why Ratings Drift Upward (pull quote): not supported

**Claim reviewed:** Resnick, Zeckhauser, Friedman and Kuwabara wrote: "Reputation systems seek to establish the shadow of the future to each transaction by creating an expectation that other people will look back on it."

**Now reads:** Reputation systems seek to restore the shadow of the future to each transaction by creating an expectation that other people will look back upon it.

**Why:** The idea is sound and the source is the right one, but the pull quote changes the authors' words. Their text, re-read for this pass, says reputation systems seek to 'restore' the shadow of the future and that others will 'look back upon it'; 'restore' carries their argument that strangers have lost an incentive long-term relationships provide. The publisher's page is blocked, so the wording rests on the authors' own pre-publication version, which the review script confirmed; no copy with 'establish' was found anywhere.

### The case for ratings: supported with caveats

**Claim reviewed:** In a second test, one or two negative ratings on a new seller made no difference to what buyers paid.

**Now reads:** In a smaller second test, one or two negative ratings on a new seller did not measurably change what buyers paid.

**Why:** The paper does report that one or two negatives did not affect what buyers paid. But this was a small side experiment, and 'made no difference' turns a result too weak to detect into a finding of no effect. Larger eBay panel data found that a seller's first negative was followed by a sharp drop in sales.

### Book callout: supported with caveats

**Claim reviewed:** Kraut and Resnick's Building Successful Online Communities (MIT Press, 2012, 328 pages) turns social science research into numbered design claims, and its chapters on contribution and regulating behavior back the checklist's questions on reveals, privacy and newcomers.

**Now reads:** Kraut and Resnick turn social science research into numbered design claims about getting people to contribute and keeping behavior in line. Resnick also led the eBay reputation experiment cited here, and the book's chapters on regulating behavior and on newcomers give useful background for the checklist.

**Why:** The book exists, translates social science into design claims, and has chapters on contribution, regulating behavior and newcomers. It was published years before the Airbnb reveal experiment and the inflation paper, so it cannot back the checklist's specific questions on reveal timing and private signals. The 328-page count could not be confirmed.

### Reveal both reviews at once: supported with caveats

**Claim reviewed:** In a large Airbnb experiment that hid each review until both host and guest had submitted one, more people reviewed, partly from curiosity about what the other side wrote.

**Now reads:** In a large experiment on Airbnb, Andrey Fradkin, Elena Grewal and David Holtz hid each review until both host and guest had submitted one. Somewhat more people reviewed, partly from curiosity about what the other side wrote.

**Why:** The paper says hiding reviews until both were in increased reviewing, from curiosity about the other side's review or wanting feedback to show. The increases were modest, 1.7 percent for guests and 9.8 percent for hosts, and an earlier lab study found simultaneous reveal lowered review rates, so the size of the effect matters.

### Reveal both reviews at once: supported with caveats

**Claim reviewed:** Under simultaneous reveal, retaliation and reciprocation fell, and ratings came out lower.

**Now reads:** Retaliation and reciprocation fell, and ratings came out slightly lower. (Do's list: Hide reviews until both are in. It reduces the fear of a revenge review and the temptation to trade compliments.)

**Why:** The paper reports less retaliation and reciprocation and lower ratings, but the drop in ratings was tiny, about a quarter of one percent. The Do's list goes further and says hiding reviews 'removes' the fear of a revenge review. The labor marketplace in the inflation paper already revealed reviews together and still saw scores inflate, so simultaneous reveal reduces one cost of honesty but not the others.

### Decide what identity shows first: supported with caveats

**Claim reviewed:** Edelman, Luca and Svirsky concluded that the platform's design choices facilitated discrimination.

**Now reads:** The authors wrote that their results suggest the platform's design choices facilitate discrimination.

**Why:** The authors do link the bias to Airbnb's design choices, but they say their results 'suggest' it rather than that they concluded it. The difference is small and easy to fix.

### Decide what identity shows first / Do's and Don'ts: supported with caveats

**Claim reviewed:** Leading with evidence of behavior (reviews, verification, response history) and showing names and photos only after the decision reduces the discrimination the Airbnb experiment measured.

**Now reads:** Where the transaction allows it, lead with evidence of behavior, such as reviews, verification and response history, and show names and photos once the decision has been made. In a later Airbnb experiment, a single positive review closed the gap between guests with white and African American names. Reviews can carry bias too, so check outcomes by group after the change.

**Why:** The cited experiment used names only, with no photos, and did not test hiding identity, so it does not show that reordering a profile reduces bias. Other work points mostly the same way: on Airbnb a single positive review erased the name gap, and a field experiment found photos showing race cut buyer responses. But reviews can themselves carry racial bias, and anonymous resumes in France backfired, so 'lead with behavior' helps without guaranteeing a fair outcome. Now cites [Cui, Li, Zhang, Discrimination with Incomplete Information in the Sharing Economy (Management Science, 2020)](https://doi.org/10.1287/mnsc.2018.3273).

### Do's and Don'ts: unverified

**Claim reviewed:** A behavioral question such as "Would you work with them again?" is easier to answer honestly than a star rating, as long as it stays private.

**Now reads:** Keep a behavioral question private. On one large marketplace, clients answered "Would you hire them again?" more candidly in private than they rated in public, until the answers were published.

**Why:** No source is cited, and none found tests whether 'would you work with them again?' is answered more honestly than a star rating when both are equally private. In the cited marketplace the candor came from privacy: once the private score was published, it inflated too. Studies do show question wording and scale format change how ratings come out, so the idea is plausible but untested as written. Now cites [Filippas, Horton, Golden, Reputation Inflation (Marketing Science, 2022)](https://doi.org/10.1287/mksc.2022.1350).

### Keep private questions private / Do's and Don'ts: supported with caveats

**Claim reviewed:** Once a private score starts appearing on profiles it will inflate like the public one; each signal a platform publishes inflates once it carries consequences.

**Now reads:** Publishing every signal you collect. Most signals inflate once they carry consequences.

**Why:** On the cited platform the private score did inflate once published, and appraisal and grading research shows ratings with consequences drift up. That supports 'expect it to inflate'. 'Each one inflates' turns one platform's result into a rule, and a peer-review trial found that exposing evaluators did not change their verdicts.

### Checklist (Newcomers): contested

**Claim reviewed:** For newcomers, one or two early negative ratings may matter less than teams fear.

**Now reads:** Newcomers: how does someone with no reviews earn a first chance? Do not count on early negatives being harmless: one small eBay experiment found no price effect from one or two, but larger studies find a first negative hits hard, so give new users other ways to show they can be trusted.

**Why:** The cited experiment is real but small: three new sellers were given one or two negatives and 35 matched pairs of lots were sold over three weeks, and the authors call the null result puzzling and say it could be a small-sample failure to detect an effect. Larger studies point the other way: on eBay a seller's first negative was followed by weekly sales growth turning from plus 5 percent to minus 8 percent, and across economics, management, marketing, sociology and psychology, negative marks weigh more than positive ones. The 'may' hedge keeps the sentence from being false, but a checklist item should not lean on one null result against that record. Now cites [Cabral and Hortaçsu, The Dynamics of Seller Reputation: Evidence from eBay (Journal of Industrial Economics, 2010)](https://doi.org/10.1111/j.1467-6451.2010.00405.x).
