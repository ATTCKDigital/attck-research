---
title: "Evidence review: Loss Aversion and Checkout Design"
---

# Evidence review: Loss Aversion and Checkout Design

Article: [Loss Aversion and Checkout Design](https://attck.com/blog/loss-aversion-and-checkout-design/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**In Baymard Institute's survey of US online shoppers, excluding people who were only browsing, 40% had abandoned a cart because extra costs (shipping, tax, fees) were too high, the top reason.**

Baymard's figure comes from shoppers' own reports of why they left, which is useful for ranking reasons but does not measure how often each reason actually causes abandonment.

- [Baymard Institute, Cart Abandonment Rate](https://baymard.com/lists/cart-abandonment-rate): “Excluding those, the top reasons are extra costs being too high (40%), slow delivery (20%), and not trusting the site with card details (19%).”

### Why the Last Step Hurts More

**Prospect theory (1979) values outcomes as gains and losses from a reference point rather than final wealth, with a value function 'generally steeper for losses than for gains.'**

A 2020 multinational replication (Ruggeri et al., Nature Human Behaviour) reproduced most of the original 1979 choice patterns.

- [Kahneman & Tversky, Prospect Theory, Econometrica (1979), OpenAlex abstract](https://doi.org/10.2307/1914185): “The value function is normally concave for gains, commonly convex for losses, and is generally steeper for losses than for gains.”

**In Kahneman, Knetsch and Thaler's 1990 experiments, mugs sold for $6.00 at the campus bookstore; owners set a median selling price of $7.12 while choosers valued the mug at $3.12, although both groups were in financially identical positions.**

The size and even the existence of the mug endowment effect is disputed: Plott and Zeiler (2005, 2011) report that the gap can vanish when procedures control for subject misconceptions, while Isoni, Loomes and Sugden (2011) dispute their reading.

- [Kahneman, Knetsch & Thaler, JPE (1990), OpenAlex abstract](https://doi.org/10.1086/261737): “Contrary to theoretical expectations, measures of willingness to accept greatly exceed measures of willingness to pay.”

**Whether an online cart creates a true endowment effect is an open question, but saved carts and 'reserved for you' labels are designed to borrow the feeling.**

Perceived ownership without legal ownership is documented in consumer research (Peck & Shu 2009), which is the closest support for the idea that carts borrow an ownership feeling.

- [Peck & Shu, The Effect of Mere Touch on Perceived Ownership, Journal of Consumer Research (2009)](https://doi.org/10.1086/598614): “For nonowners, or buyers, perceived ownership can be increased with either mere touch or with imagery encouraging touch.”

### How Much Heavier Is a Loss?

**The popular version, used in this series' article on cognitive bias, says a loss hurts about twice as much as an equal gain pleases. A 2024 review of 607 published estimates did land near two on average, but individual estimates range widely, and some studies find little or no loss aversion at all.**

Meta-analytic estimates of the loss aversion coefficient range from about 1.3 (Walasek, Mullett & Stewart 2018, risky choice only) to about 2 (Brown et al. 2024); a 2025 re-meta-analysis in the Journal of Economic Psychology argues the effect is not robust.

- [Brown, Imai, Vieider & Camerer, Meta-analysis of Empirical Estimates of Loss Aversion, Journal of Economic Literature (2024)](https://doi.org/10.1257/jel.20221698): “the mean loss aversion coefficient is 1.955 with a 95 percent probability that the true value falls in the interval [1.820, 2.102]”

**Together with the endowment research, the two papers give a more useful rule than "twice as much." Losses tend to weigh more when people are unsure what something is worth, and the feeling of already having something and the reference they were given seem to matter too. Checkout often brings all three together.**

A 2022 meta-analysis of loss-framed incentives found sizable lab effects but near-zero effects in field experiments, a reminder that loss effects measured in the lab can shrink in real settings.

- [Mrkva et al. (2020), OpenAlex abstract](https://doi.org/10.1002/jcpy.1156): “more domain knowledge and experience were associated with lower loss aversion, though people of all knowledge and experience levels were loss averse”
- [Peck & Shu, The Effect of Mere Touch on Perceived Ownership, Journal of Consumer Research (2009)](https://doi.org/10.1086/598614): “For nonowners, or buyers, perceived ownership can be increased with either mere touch or with imagery encouraging touch.”

### Fees that arrive at the end

**Late fees win sales by hiding the full price until it is hard to compare, and the shopper pays for it. The study's authors note that loss aversion may be one reason buyers who meet the fee at checkout rarely go back and re-shop, but they did not test that. The trick is not guaranteed: a field experiment at a cinema found that a surcharge hidden until checkout won more clicks and then lost the same sales at the final step.**

Blake et al. explain the StubHub result through hidden prices that look lower and search frictions, and name loss aversion only as one untested possibility. A 34,000-customer cinema field experiment (European Economic Review, 2020) found a hidden surcharge won selections but lost them again at checkout, leaving demand unchanged, and a 2025 marketplace experiment found drip pricing raised prices paid for identical gift cards by about 10%.

- [Blake, Moshary, Sweeney & Tadelis, Price Salience and Product Choice, NBER w25186 (same paper as)](https://www.nber.org/papers/w25186): “making the full purchase price salient to consumers reduces both the quality and quantity of goods purchased”
- [Blake et al., NBER working paper PDF (same paper as), Table 4 discussion](https://www.nber.org/system/files/working_papers/w25186/w25186.pdf): “Consistent with misinformation, Back-end Fee users are almost 19% more likely to select tickets (transition from stage 1 to 2) than Upfront Fee users.”
- [Measuring and Mitigating Drip Pricing Overcharge, SSRN 5565238 (2025), Crossref record](https://doi.org/10.2139/ssrn.5565238): “Relative to transparent pricing, drip pricing increases the average price paid by up to a plateau of about 10% (maximum 13%) for the same gift cards.”
- [Regulating Drip Pricing in Platform Markets (California SB 478, Airbnb data), SSRN 7203424 (2026), Crossref record](https://doi.org/10.2139/ssrn.7203424): “pre-policy cleaning fee ratios positively predicted occupancy, confirming drip pricing bias in consumer decision-making”

### Free-shipping thresholds

**'Add $14 for free shipping' frames the shipping charge as money the shopper can still win back; a threshold that first appears at review acts as one more late cost.**

Free-shipping thresholds raise sales in retailer data (Lewis, Singh & Fay 2006) but can be unprofitable, and free shipping has a jump effect on demand beyond its dollar value.

- [Lewis, Singh & Fay, Marketing Science (2006)](https://doi.org/10.1287/mksc.1050.0150): “Promotions such as free shipping and free shipping for orders that exceed some size threshold are found to be very effective in generating additional sales.”
- [Partitioned Pricing and Consumer Welfare, SSRN (2020), Crossref record](https://doi.org/10.2139/ssrn.3676900): “I also document a discontinuous positive effect of free shipping on consumer demand, which is novel to the literature.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Why the Last Step Hurts More: supported with caveats

**Claim reviewed:** In 1991 Tversky and Kahneman carried prospect theory into riskless choice, showing that a shift in the reference point can reverse preferences.

**Now reads:** In 1991 they carried it into choices with no gamble involved, with a model of how a shift in the reference point can reverse what people prefer.

**Why:** The 1991 paper builds a model that explains preference reversals caused by reference shifts; the abstract credits those reversals to 'much experimental evidence' rather than showing them itself. 'Showing' slightly overstates the paper's own contribution.

### Why the Last Step Hurts More: contested

**Claim reviewed:** A fee revealed late registers as a loss stacked on an already-accepted price; the same total shown from the start would be experienced as one price.

**Now reads:** Our shopper's reference was $120, so the extra $18.47 can feel like a loss stacked on a purchase she had already accepted. Shown from the start, the same total would have been one price. Shown late, it reads as a price plus a penalty. Whether that sting is loss aversion, surprise or a sense of being misled has not been tested directly, but the reaction itself is well documented: in the StubHub experiment described below, shoppers who first saw fees at checkout were far more likely to quit at that step.

**Why:** The article states as fact that a late fee is felt as a loss on top of a price the shopper had already accepted. The behavior it describes is well documented: in the StubHub experiment, shoppers who first saw fees at checkout were 45% less likely to complete the purchase at that step. But no study tests whether that reaction is loss aversion rather than surprise, a sense of being misled, or simply a higher price; the StubHub authors name loss aversion as one possible explanation and say they remain agnostic, marketing experiments measure the reaction as perceived deception, and the economics of fees explains their effects through inattention. Now cites [Greenleaf, Johnson, Morwitz & Shalev, The price does not include additional taxes, fees, and surcharges: A review of research on partitioned pricing, Journal of Consumer Psychology (2015)](https://doi.org/10.1016/j.jcps.2015.04.006).

### How Much Heavier Is a Loss?: supported with caveats

**Claim reviewed:** The popular version says a loss hurts about twice as much as an equal gain pleases.

**Now reads:** The popular version, used in this series' article on cognitive bias, says a loss hurts about twice as much as an equal gain pleases. A 2024 review of 607 published estimates did land near two on average, but individual estimates range widely, and some studies find little or no loss aversion at all.

**Why:** The article presents 'about twice' as the popular version and then questions it, which is fair. A large 2024 meta-analysis puts the average near 2, but another meta-analysis of risky-choice studies found a much smaller value, and lab work shows the ratio can vanish or reverse with context. Now cites [Brown, Imai, Vieider & Camerer, Meta-analysis of Empirical Estimates of Loss Aversion, Journal of Economic Literature (2024)](https://doi.org/10.1257/jel.20221698).

### How Much Heavier Is a Loss?: supported with caveats

**Claim reviewed:** Mrkva, Johnson, Gachter and Herrmann (2020) replied with five samples totalling 17,720 people; everyone was loss averse, but the size of the effect moved.

**Now reads:** Kellen Mrkva, Eric Johnson, Simon Gächter and Andreas Herrmann replied in 2020 with five samples totalling 17,720 people. People at every level of knowledge and experience were loss averse on average, but the size of the effect moved.

**Why:** The five samples and 17,720 total are right. 'Everyone was loss averse' overstates the paper, which reports that people at all knowledge and experience levels were loss averse on average, not every individual.

### How Much Heavier Is a Loss?: supported with caveats

**Claim reviewed:** Losses weigh more when people are unsure what something is worth, when they feel they already have it, and when a change departs from the reference they were given; checkout often hits all three.

**Now reads:** Together with the endowment research, the two papers give a more useful rule than "twice as much." Losses tend to weigh more when people are unsure what something is worth, and the feeling of already having something and the reference they were given seem to matter too. Checkout often brings all three together.

**Why:** Only the uncertainty part comes from the two cited papers: Mrkva et al. found less loss aversion with more knowledge. The ownership part draws on endowment research the article cites elsewhere, and 'checkout often hits all three' is the author's own inference. Field studies also show loss framing effects can shrink sharply outside the lab.

### Fees that arrive at the end: supported with caveats

**Claim reviewed:** Drip pricing works: late fees win sales by moving the reference point, and the shopper pays for it.

**Now reads:** Late fees win sales by hiding the full price until it is hard to compare, and the shopper pays for it. The study's authors note that loss aversion may be one reason buyers who meet the fee at checkout rarely go back and re-shop, but they did not test that. The trick is not guaranteed: a field experiment at a cinema found that a surcharge hidden until checkout won more clicks and then lost the same sales at the final step.

**Why:** The cited study, read in full, confirms that late fees raised StubHub's sales and spending: users shown fees late were 19% more likely to select a ticket, bought pricier seats, and spent about 21% more. But the paper never uses the idea of a moved reference point; it models hidden fees as making prices look lower, tests surprise, limited learning and search frictions, and names loss aversion only as one possible reason buyers do not go back and re-shop. A cinema field experiment also found that a shrouded surcharge won clicks and then lost the same sales at checkout, so the gain is not guaranteed. Now cites [To buy or not to buy? Price salience in an online shopping field experiment, European Economic Review (2020)](https://doi.org/10.1016/j.euroecorev.2020.103593).

### Timers, stock warnings and reminders: supported with caveats

**Claim reviewed:** Pull quote attributed to Mathur et al.: 'By not stating the deadline, websites withhold information from users, and thus misrepresent the nature of the offer.'

**Now reads:** Replace the pull quote with one from the countdown-timer section: "it can mislead users into believing an offer is expiring when in reality it is not" (Arunesh Mathur et al., Dark Patterns at Scale). Or keep the current quote and move it beside the "ending soon" offers, labeled as about urgency messages with no stated deadline.

**Why:** The quote is verbatim, but the paper wrote it about 'limited-time messages' that give no deadline at all, not about countdown timers, and it credits the point to another source. Placed under the timer discussion, it reads as a verdict on timers, which do state a deadline.

### Thinking, Fast and Slow (book box): supported with caveats

**Claim reviewed:** Part IV of Thinking, Fast and Slow (2011, 499 pages) covers prospect theory, the endowment effect and bad events.

**Now reads:** Daniel Kahneman | Farrar, Straus and Giroux | 2011 | 499 pages (hardcover). If the box keeps the paperback link, change the page count to 512.

**Why:** Part IV ('Choices') does include chapters titled Prospect Theory, The Endowment Effect and Bad Events, per reviewer recall; the publisher page could not confirm the table of contents. The linked page is the paperback edition and lists 512 pages, not 499 (499 matches the 2011 hardcover).
