---
title: "Evidence review: Cognitive Load and How to Reduce It"
---

# Evidence review: Cognitive Load and How to Reduce It

Article: [Cognitive Load and How to Reduce It](https://attck.com/blog/cognitive-load-and-how-to-reduce-it/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### The Bandwidth Problem

**Working memory is a finite resource, similar to a computer's RAM.**

Cowan (2010) puts the limit at roughly three to five meaningful items; resource models (Ma, Husain & Bays 2014) describe it as a limited pool shared flexibly across items.

- [Cowan, The Magical Mystery Four, Current Directions in Psychological Science, 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/): “There are severe limits in how much can be kept in mind at once (~3–5 items).”
- [Baddeley, Working Memory, Science (1992), PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/1736359/): “The term working memory refers to a brain system that provides temporary storage and manipulation of the information necessary for such complex cognitive tasks as language comprehension, learning, and reasoning.”

**When a digital interface demands more processing power than the user has available, cognitive overload occurs. The result is slower, more error-prone work, and sometimes abandonment.**

In shopper surveys, 17% of US shoppers say they abandoned an order because checkout was too long or complicated (Baymard); cost and trust reasons are more common.

- [de Jong, Cognitive load theory, educational research, and instructional design: some food for thought, Instructional Science, 2010](https://eric.ed.gov/?id=EJ874567): “if a learning task requires too much capacity, learning will be hampered.”

### Cognitive Load Theory

**Cognitive load researchers usually describe three types of load. Intrinsic Load is the inherent difficulty of the task itself (e.g., calculating a mortgage rate). It cannot be eliminated, only managed. Extraneous Load is the unnecessary difficulty added by poor design (e.g., a confusing font, a hidden navigation menu, or visual clutter). This is waste and should be eliminated. Germane Load is the effort spent actually processing and learning the information (e.g., understanding a pricing tier). The theory's authors now treat it less as a separate load than as the useful share of a person's limited capacity, and some researchers argue the first two types are all you need. For interface design, the practical split is the first two: keep the task's real difficulty, and remove the difficulty you added.**

The three-type model comes from Sweller, van Merrienboer and Paas (1998), not the 1988 paper cited as. In their 2019 review the same authors describe germane load as redistributing working memory resources rather than adding to total load, and Kalyuga (2011) argues a two-type (intrinsic/extraneous) framework is sufficient. Questionnaire studies (Leppink et al. 2013; Klepsch et al. 2017) still recover three factors.

- [Young, Van Merrienboer, Durning & Ten Cate, Cognitive Load Theory: implications for medical education: AMEE Guide No. 86, Medical Teacher (2014)](https://pubmed.ncbi.nlm.nih.gov/24593808/): “CLT identifies three types of cognitive load that impact WM: intrinsic load (associated with performing essential aspects of the task), extraneous load (associated with non-essential aspects of the task) and germane load”
- [Leppink, Paas, Van der Vleuten, Van Gog & Van Merrienboer, Development of an instrument for measuring different types of cognitive load, Behavior Research Methods (2013)](https://pubmed.ncbi.nlm.nih.gov/23572251/): “revealed a three-component solution, consistent with the types of load that the different items were intended to measure.”
- [Klepsch, Schmitz & Seufert, Development and Validation of Two Instruments Measuring Intrinsic, Extraneous, and Germane Cognitive Load, Frontiers in Psychology (2017)](https://doi.org/10.3389/fpsyg.2017.01997): “The improved version of the naïve rating turned out to be a useful, feasible, and reliable instrument.”

### How This Behavior Shows Up

**The split-attention effect occurs when users must hold information in mind while moving their eyes between physically separated sources (e.g., a map legend separated from the map), which burns working memory; integrating related information spatially and temporally makes the task easier.**

Meta-analyses (Ginns 2006; Schroeder & Cenkci 2018, g = 0.63) support the effect, mainly for complex material and novices.

- [Ginns, Integrating information: meta-analysis of spatial and temporal contiguity, Learning and Instruction, 2006](https://eric.ed.gov/?id=EJ747512): “for complex learning materials in particular, increasing either the spatial or temporal contiguity of related elements of information can lead to substantial learning gains.”
- [Schroeder & Cenkci, Spatial contiguity and spatial split-attention effects, EPR, 2018](https://eric.ed.gov/?id=EJ1186641): “A random effects meta-analysis of 58 independent comparisons (n = 2426) produced an overall effect size of g = 0.63”
- [Cited source (pass 2)](https://www.davidlewisphd.com/courses/EDD8121/readings/1992-ChandlerSweller-SplitAttention.pdf): “In a normal training environment, the integrated instructions group outperformed the conventional group.”

**"Decision fatigue" is often used loosely, but the core idea has a research trail: in field studies, people who have already made many decisions tend to default, defer, or take the easier option more often. The effect varies by setting, lab tests of the underlying "depleted resource" idea have mostly failed to replicate, and some well-known findings have other explanations, so treat it as a tendency, not a law. The design lesson holds either way: do not ask users to make decisions they do not need to make.**

For: Levav et al. (2010) randomized field experiments on car and suit configurators (more default acceptance after many choices); Persson et al. (2019), Allan et al. (2019), Hirshleifer et al. (2019) and a 2025 preregistered systematic review (Maier et al.: effects in 45% of tests). Against: ego-depletion multi-lab replications found d = 0.04 (Hagger et al. 2016) and d = 0.06 (Vohs et al. 2021), Dang et al. (2021) d = 0.10; Andersson et al. (2025) found no decision fatigue in triage nurses; Glockner (2016) and Weinshall-Margel and Shapard (2011) give non-fatigue explanations for the parole-judge result.

- [Pignatiello, Martin & Hickman, Decision fatigue: A conceptual analysis, Journal of Health Psychology (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6119549/): “making decisions may possess negative ramifications for controlling ones’ behavior and the quality of subsequent decisions.”
- [Levav, Heitmann, Herrmann & Iyengar, Order in Product Customization Decisions: Evidence from Field Experiments, Journal of Political Economy 118 (2010)](https://doi.org/10.1086/652463): “We find that order affects the design of a suit that people configure and the design and price of a car that people purchase by influencing the likelihood that they will accept the default option suggested by the firm.”
- [Persson, Barrafrem, Meunier & Tinghog, The effect of decision fatigue on surgeons' clinical decision making, Health Economics 28 (2019)](https://pubmed.ncbi.nlm.nih.gov/31344303/): “patients who met a surgeon toward the end of his or her work shift were 33 percentage points less likely to be scheduled for an operation compared with those who were seen first.”
- [Allan et al., Clinical decisions and time since rest break: An analysis of decision fatigue in nurses, Health Psychology 38 (2019)](https://pubmed.ncbi.nlm.nih.gov/30896218/): “For every consecutive call taken since last rest break, the odds of nurses making a conservative management decision (i.e., arranging for callers to see another health professional the same day) increased by 5.5%”
- [Hirshleifer, Levi, Lourie & Teoh, Decision fatigue and heuristic analyst forecasts, Journal of Financial Economics 133 (2019)](https://doi.org/10.1016/j.jfineco.2019.01.005): “We find that forecast accuracy declines over the course of a day as the number of forecasts the analyst has already issued increases.”
- [Maier, Powell, Murchie & Allan, Systematic review of the effects of decision fatigue in healthcare professionals on medical decision-making, Health Psychology Review 19 (2025)](https://pubmed.ncbi.nlm.nih.gov/40591577/): “45% of cases that quantitatively assessed the decision fatigue hypothesis provided evidence of significant decision fatigue effects across diagnostic, test ordering, prescribing, and therapeutic decisions.”

**Edward Tufte's critique of "chartjunk" makes a related point in visual form. He called it decoration that "does not tell the viewer anything new": busy grid lines, excess tick marks, the debris of computer plotting. Tufte framed this as a matter of data and ink rather than cognitive load, and later studies found that some embellishment does not hurt comprehension and can even help recall. The rule, then, is to cut decoration that gets in the way, not all decoration.**

The reading of chartjunk as a cost to the viewer is common in visualization research (Hullman et al. 2011 describe the rule as avoiding elements that 'slow comprehension'), and the seductive details meta-analysis (Rey 2012) supports the mechanism in learning materials. Experiments on charts are mixed: Gillan and Richman (1994) and Skau et al. (2015) found decoration costs, Bateman et al. (2010) and Haroz et al. (2015) found no cost and some recall benefit.

- [Tufte, The Visual Display of Quantitative Information (1983), p. 107, as quoted in Few, The Chartjunk Debate (2011, PDF)](https://webspace.science.uu.nl/~telea001/uploads/VACourse/Few11.pdf): “The interior decoration of graphics generates a lot of ink that does not tell the viewer anything new”
- [Hullman, Adar & Shah, Benefitting InfoVis with Visual Difficulties, IEEE TVCG 17 (2011)](https://doi.org/10.1109/TVCG.2011.175): “Distracting elements like decorative "chartjunk" or extraneous information are avoided so as not to slow comprehension.”
- [Rey, A review of research and a meta-analysis of the seductive detail effect, Educational Research Review 7 (2012), ERIC record](https://eric.ed.gov/?id=EJ986386): “This effect is mainly explained by assuming an overloading of the working memory, attention distraction, schema interference or coherence disruption.”
- [Gillan & Richman, Minimalism and the Syntax of Graphs, Human Factors 36 (1994)](https://doi.org/10.1177/001872089403600405): “the higher the data-ink ratio, the faster the response time and the greater the accuracy.”
- [Skau, Harrison & Kosara, An Evaluation of the Impact of Visual Embellishments in Bar Charts, Computer Graphics Forum 34 (2015, PDF)](https://kosara.net/papers/2015/Skau-EuroVis-2015.pdf): “The results of this experiment confirm that common embellishments can significantly impact the perceptual performance of bar charts, and that these impacts differ substantially based on the task”

### Case Study: GOV.UK

**The reasoning lines up with cognitive load.**

A mobile survey experiment (Mavletova & Couper 2014) found scrolling faster than paging, with no rise in quitting.

- [Cited source (pass 2)](https://www.gov.uk/service-manual/design/form-structure): “Starting with one thing on a page helps people to: understand what you’re asking them to do focus on the specific question and its answer find their way through an unfamiliar process”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### The Bandwidth Problem: supported with caveats

**Claim reviewed:** When an interface demands more processing than the user has available, cognitive overload occurs, and the result is not just frustration but abandonment.

**Now reads:** When a digital interface demands more processing power than the user has available, cognitive overload occurs. The result is slower, more error-prone work, and sometimes abandonment.

**Why:** The first half, that overload happens when demands exceed capacity, is standard cognitive load theory, though the research measures learning, not interface use. The second half, that overload leads to abandonment, has no source. Shopper surveys attribute only a minority of abandonments to complex checkouts, and a controlled survey experiment found that splitting content across screens did not reduce quitting. Now cites [de Jong, Cognitive load theory, educational research, and instructional design, Instructional Science (2010)](https://eric.ed.gov/?id=EJ874567).

### Cognitive Load Theory: supported with caveats

**Claim reviewed:** Cognitive Load Theory, developed by educational psychologist John Sweller in 1988, posits that human learning and task execution are severely hampered when working memory is overwhelmed.

**Now reads:** Cognitive Load Theory (CLT), developed by educational psychologist John Sweller in 1988, holds that learning suffers when a task uses up working memory that could otherwise go to understanding.

**Why:** Sweller's 1988 paper is the accepted origin of cognitive load theory, and it argues that heavy problem-solving load leaves less capacity for learning. But the paper is about learning, specifically schema acquisition, not general 'task execution', and 'severely hampered' is stronger than its wording. Critics also note that load is hard to measure.

### Cognitive Load Theory: supported with caveats

**Claim reviewed:** There are three types of cognitive load that compete for mental bandwidth: intrinsic, extraneous and germane; germane load is 'good' load because it leads to value.

**Now reads:** Cognitive load researchers usually describe three types of load. Intrinsic Load is the inherent difficulty of the task itself (e.g., calculating a mortgage rate). It cannot be eliminated, only managed. Extraneous Load is the unnecessary difficulty added by poor design (e.g., a confusing font, a hidden navigation menu, or visual clutter). This is waste and should be eliminated. Germane Load is the effort spent actually processing and learning the information (e.g., understanding a pricing tier). The theory's authors now treat it less as a separate load than as the useful share of a person's limited capacity, and some researchers argue the first two types are all you need. For interface design, the practical split is the first two: keep the task's real difficulty, and remove the difficulty you added.

**Why:** The three-type scheme is the standard account of cognitive load theory: it is how medical education guides teach it, and two validated questionnaires recover three separate factors. But the article presents the 1998 version as settled. The theory's own authors have since redefined germane load as a redistribution of working memory resources rather than a third load that competes for bandwidth, and Kalyuga argues the third type is redundant. The taxonomy is fair to cite; the 'competing' framing and the certainty are not. Now cites [Sweller, van Merrienboer & Paas, Cognitive Architecture and Instructional Design: 20 Years Later, Educational Psychology Review 31 (2019), open access](https://doi.org/10.1007/s10648-019-09465-5).

### Cognitive Load Theory: supported with caveats

**Claim reviewed:** Intrinsic load (the inherent difficulty of the task) cannot be eliminated, only managed.

**Now reads:** Intrinsic Load: The inherent difficulty of the task itself (e.g., calculating a mortgage rate). You cannot remove it, but you can lower it by breaking the task into steps and building on what users already know.

**Why:** For a given task and a given person, intrinsic difficulty can't be designed away, so the gist holds. But cognitive load theory itself says intrinsic load depends on what the person already knows, and it can be lowered by sequencing, for example presenting pieces one at a time before combining them. 'Cannot be eliminated' is fair; 'only managed' should acknowledge that sequencing and experience reduce it. Now cites [Sweller, Element Interactivity and Intrinsic, Extraneous, and Germane Cognitive Load, Educational Psychology Review (2010)](https://eric.ed.gov/?id=EJ883815).

### Cognitive Load Theory: unverified

**Claim reviewed:** One reason one-click checkout works is that it relies on a learned schema (saved addresses, saved payment methods, familiar confirmation patterns), reducing the new thinking required in the moment.

**Now reads:** One plausible reason one-click checkout works is that it relies on what users already know: saved addresses, saved payment methods, familiar confirmation patterns. It also simply removes steps. Either way, the interface reduces the amount of new thinking required in the moment.

**Why:** It is plausible that saved details and familiar patterns let people check out without new thinking, and cognitive load theory supports the general idea that stored knowledge frees up working memory. But no study found isolates schemas as the reason one-click checkout works, and simply having fewer steps and fields would explain the effect just as well.

### Cognitive Load Theory: misattributed

**Claim reviewed:** Modern research suggests working memory capacity is frequently closer to 3-5 meaningful items than the older '7 plus or minus 2', depending on conditions and chunking.

**Now reads:** A useful nuance: the older "7 plus or minus 2" idea is often quoted in UX, but more recent research suggests working memory capacity is frequently closer to 3 to 5 meaningful items, depending on conditions and chunking. Treat capacity as smaller than you want it to be, and your designs get better.

**Why:** The 3 to 5 item estimate is well supported and newer work keeps finding an item limit of about three or four, with the exact number still argued over. But it comes from Nelson Cowan, not from the source cited: is Miller's 1956 paper, the origin of the 'seven plus or minus two' figure the sentence is correcting. Cowan's 2010 paper, which states the 3 to 5 figure directly, is already source. Now cites [Cowan, The Magical Mystery Four, Current Directions in Psychological Science 19 (2010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/).

### How This Behavior Shows Up: contested

**Claim reviewed:** Interfaces that present too many equal-weight options simultaneously (e.g., a mega-menu with 50 links) paralyze the user; 'kitchen sink' dashboards result in a user who looks at everything but sees nothing.

**Now reads:** Hick's Law predicts a slowdown, not a stall. The stall comes from a different effect, choice overload: when options are many, similar, and hard to compare, people are more likely to put off the decision or fall back on a default. The effect is real in some settings (retirement plan menus with dozens of funds, complex product sets) but far from universal, and well-structured mega menus test fine because people can see rather than remember. Cluttered "Kitchen Sink" dashboards have a related problem: crowded displays make it harder to find the one thing that matters. The lesson is not fewer options at any cost. It is options that are easy to compare, with the important ones given more weight.

**Why:** The cited Hyman study shows reaction time rising predictably with the number of options; it says nothing about paralysis, menus or dashboards. Whether many similar options 'paralyze' people is genuinely disputed: one meta-analysis of 50 experiments found an average effect of about zero, while a second, larger one found a reliable effect once conditions such as hard-to-compare options and difficult decisions are taken into account, and field data on 401(k) menus and brain imaging point the same way. The specific mega-menu example cuts the other way, because user testing and menu-breadth experiments find broad, well-structured menus work well. The dashboard half is supported by visual clutter research. Now cites [Chernev, Bockenholt & Goodman, Choice overload: A conceptual review and meta-analysis, Journal of Consumer Psychology 25 (2015)](https://doi.org/10.1016/j.jcps.2014.08.002).

### How This Behavior Shows Up: supported with caveats

**Claim reviewed:** Decision fatigue has a research trail: making repeated decisions can degrade the quality of subsequent decisions and increase avoidance.

**Now reads:** "Decision fatigue" is often used loosely, but the core idea has a research trail: in field studies, people who have already made many decisions tend to default, defer, or take the easier option more often. The effect varies by setting, lab tests of the underlying "depleted resource" idea have mostly failed to replicate, and some well-known findings have other explanations, so treat it as a tendency, not a law. The design lesson holds either way: do not ask users to make decisions they do not need to make.

**Why:** The sentence is carefully hedged ('can'), and the research trail it points to is real: randomized field experiments on product configurators found that people who had already made many choices accepted more defaults, large observational studies of surgeons, helpline nurses, GPs and financial analysts show later decisions drifting toward the easier option, and a 2025 preregistered systematic review found significant effects in 45% of tests. The caveats are serious: the lab mechanism usually offered (ego depletion) failed two large multi-lab replications, the famous parole-judge result has non-fatigue explanations, a 2025 preregistered field study found nothing, and the review itself says the concept is inconsistently defined. Now cites [Levav, Heitmann, Herrmann & Iyengar, Order in Product Customization Decisions: Evidence from Field Experiments, Journal of Political Economy 118 (2010)](https://doi.org/10.1086/652463).

### How This Behavior Shows Up: supported with caveats

**Claim reviewed:** Every visual element on a screen, no matter how small, requires a micro-amount of processing power to ignore; decorative icons, heavy grid lines and unnecessary gradients are 'cognitive taxes'.

**Now reads:** Visual elements on a screen compete for attention. Decorative icons, heavy grid lines, and unnecessary gradients can act as "cognitive taxes," especially when they crowd the things users are looking for. If they do not convey information or help users orient, they are probably noise.

**Why:** Clutter research supports the general point that extra, disorganized items make search and recognition harder. But 'every element, no matter how small' goes too far: when the main task is demanding, irrelevant items often go unprocessed, and one study found decorated charts no harder to read and better remembered. Decoration is a cost to justify, not an automatic tax. Now cites [Rosenholtz, Li & Nakano, Measuring visual clutter, Journal of Vision (2007)](https://pubmed.ncbi.nlm.nih.gov/18217832/).

### How This Behavior Shows Up: supported with caveats

**Claim reviewed:** Edward Tufte's critique of 'chartjunk' is essentially an argument about extraneous cognitive load in visual form.

**Now reads:** Edward Tufte's critique of "chartjunk" makes a related point in visual form. He called it decoration that "does not tell the viewer anything new": busy grid lines, excess tick marks, the debris of computer plotting. Tufte framed this as a matter of data and ink rather than cognitive load, and later studies found that some embellishment does not hurt comprehension and can even help recall. The rule, then, is to cut decoration that gets in the way, not all decoration.

**Why:** Tufte never uses the language of cognitive load; he frames chartjunk as non-data ink, 'graphic paraphernalia' such as over-busy grids, and a matter of content gracefully displayed. But his definition turns on decoration that 'does not tell the viewer anything new', and the visualization research community reads the chartjunk rule exactly as the article does, as a rule against elements that slow comprehension. So the gloss is a reasonable and common reading, not Tufte's own words. The caveat is that experiments on whether decoration costs the viewer are mixed: some find embellishment hurts accuracy, others find no loss and better recall. The cited page contains only page references. Now cites [Tufte, The Visual Display of Quantitative Information, 2nd ed. (Graphics Press, 2001), chapter 5, pp. 107-121](https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/).

### Practical Application: supported with caveats

**Claim reviewed:** Progressive disclosure means not showing everything at once and showing only the information necessary for the current step.

**Now reads:** Do not show everything at once. Show the most important options first and keep advanced ones a click away. For multi-step tasks, show only what the current step needs.

**Why:** Nielsen's guidance supports showing the most important options first and the rest on request. The article blends this with 'one step at a time', which Nielsen treats as a separate pattern, staged disclosure. The advice is sound, but a survey-design experiment found that splitting content across screens on mobile was slower, so it is not free.

### Practical Application: not supported

**Claim reviewed:** Domino's mastered progressive disclosure with its Pizza Tracker: instead of a complex logistics table it shows a simple progress bar with one status at a time ('Prep', 'Bake', 'Delivery'), keeping customers informed without overwhelming them.

**Now reads:** Domino's "Pizza Tracker" shows the same instinct at work. Instead of a logistics table, it shows a short bar of stages, from order placed to out for delivery, that lights up as each one is completed, with the details of the order a tap away. Customers stay informed without being overwhelmed.

**Why:** Domino's own descriptions of the tracker, from its 2008 launch and its March 2026 redesign, show every stage on one bar that lights up as the order moves along, not one status at a time, and the stages have never been 'Prep, Bake, Delivery' (2008: received, prep, oven, boxed, out for delivery; 2026: placed, make, deliver or pick up, mmm!). It is a good example of keeping people informed with a simple progress view, and the 2026 version does tuck details behind a tap, but it does not show progressive disclosure as the article and Nielsen define it, and 'mastered' has no source. Now cites [Domino's press release, Domino's Updates Its Iconic, Industry-First Tracker for an Even Better Customer Experience (24 Mar 2026), via Nasdaq](https://www.nasdaq.com/press-release/dominosr-updates-its-iconic-industry-first-tracker-even-better-customer-experience).

### Practical Application: supported with caveats

**Claim reviewed:** A 16-digit card number is printed and typed in four groups of four, and a phone number is easier to read back when split by convention, because of chunking.

**Now reads:** That is why a 16-digit card number is usually printed and typed in four groups of four, and why a phone number is easier to read back when it is split by convention.

**Why:** NN/g gives both examples and recommends conventional chunked formats and auto-formatting. The 'that is why' is looser: card numbers are grouped by convention, and some cards such as 15-digit Amex use other groupings. The design advice stands.

### Case Study: GOV.UK: supported with caveats

**Claim reviewed:** GDS gives GOV.UK teams a starting rule of one thing per page (one question, piece of information or decision), which the Service Manual says helps people understand what is asked, focus on one question, find their way through an unfamiliar process and recover from errors; the reasoning is about cognitive load.

**Now reads:** The reasoning lines up with cognitive load.

**Why:** The Service Manual's rule and its list of benefits are reported accurately, and the article already calls the rule a starting point. Neither GDS source uses the words 'cognitive load', so that framing is the article's (reasonable) reading. One controlled mobile survey experiment found a single scrolling page faster and better rated than paging, so one thing per page is not always better.
