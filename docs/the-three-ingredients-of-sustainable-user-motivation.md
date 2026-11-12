---
title: "Evidence review: The Three Ingredients of Sustainable User Motivation"
---

# Evidence review: The Three Ingredients of Sustainable User Motivation

Article: [The Three Ingredients of Sustainable User Motivation](https://attck.com/blog/the-three-ingredients-of-sustainable-user-motivation/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**Sustainable engagement, the kind that builds habit and loyalty, depends less on external pressure and more on motivation the user owns. That includes intrinsic motivation, when people find the activity itself rewarding, and values they have taken on as their own, when they find it meaningful.**

Self-determination theory does not split motivation into good intrinsic and bad extrinsic. Its founders note that well-internalized extrinsic motivation also predicts positive outcomes (Ryan & Deci 2020).

- [Ryan & Deci, Contemporary Educational Psychology 61 (2020), author preprint](https://selfdeterminationtheory.org/wp-content/uploads/2020/04/2020_RyanDeci_CEP_PrePrint.pdf): “Technically intrinsic motivation pertains to activities done “for their own sake,” or for their inherent interest and enjoyment (Deci & Ryan, 2000).”

**When a digital experience satisfies these three needs, people are more likely to enjoy it and come back to it; studies of video game players find each need predicts continued play.**

The evidence that need satisfaction predicts return use comes mainly from video game studies (Ryan, Rigby & Przybylski 2006), which are correlational; reviews note that HCI work rarely tests SDT directly (Tyack & Mekler 2020).

- [Ryan, Rigby & Przybylski, The Motivational Pull of Video Games, Motivation and Emotion 30 (2006), author-hosted PDF](https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf): “Results show that SDT’s theorized needs for autonomy, competence, and relatedness independently predict enjoyment and future game play.”

### Ingredient 1: Autonomy

**The result can be what psychologists call psychological reactance: a defensive mix of irritation and pushback against the system. Online, it shows up as avoidance, and sometimes as users leaving altogether.**

Reactance theory comes from Jack Brehm (1966). In an online experiment, forced pop-up ads produced irritation and ad avoidance (Edwards, Li & Lee 2002).

- [Edwards, Li & Lee, Forced Exposure and Psychological Reactance, Journal of Advertising 31(3), 2002](https://gwern.net/doc/economics/advertising/2002-edwards.pdf): “The consequences of intrusiveness were shown to be caused by feelings of irritation and ad avoidance.”
- [Rains, The Nature of Psychological Reactance Revisited: A Meta-Analytic Review, Human Communication Research 39(1), 2013](https://doi.org/10.1111/j.1468-2958.2012.01443.x): “the intertwined model—in which reactance is modeled as a latent factor with anger and counterarguments serving as indicators—best fit the data.”

### Ingredient 2: Competence

**Vague error messages are among the quickest ways to undercut a user's sense of competence. When a user sees "Something went wrong" with no explanation, the interface tells them something failed without offering a way forward.**

Evidence on error messages comes mostly from programming education, where plainer messages reduced frustration in one study (2023) and had no measurable effect in another (Denny et al. 2014).

- [The Effect of Automated Error Message Feedback on Undergraduate Physics Students Learning Python, Journal for STEM Education Research (2023)](https://doi.org/10.1007/s41979-022-00084-4): “Our results show a statistically significant reduction in negative student emotions, such as frustration and anxiety”

### Feedback Loops and Progressive Disclosure

**Similarly, LinkedIn uses a profile completion meter to make progress visible. Rather than presenting a daunting empty form, it breaks the profile into small, manageable tasks, and as the meter fills, the user gets a small sense of achievement.**

Visible progress toward a goal can increase persistence (Nunes & Drèze 2006), but a meta-analysis of web-survey experiments found progress bars do not reliably reduce drop-off (Villar et al. 2013).

- [Interaction Design Foundation, What is Gamification?](https://ixdf.org/literature/topics/gamification): “LinkedIn's profile completion progress bar encourages users to fully complete their profiles.”
- [Nunes & Drèze, The Endowed Progress Effect, Journal of Consumer Research 32(4), 2006](https://doi.org/10.1086/500480): “people provided with artificial advancement toward a goal exhibit greater persistence toward reaching the goal.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: misattributed

**Claim reviewed:** Early gamification gave users badges and points to make them act and stay; this behaviorist approach relies entirely on extrinsic motivation.

**Now reads:** In the early days of gamification, many product teams worked from a simple premise: if you want users to do something, give them a badge; if you want them to stay, give them points. Critics called this approach behaviorist, closer to training with treats, because it leaned on external rewards rather than on the activity itself.

**Why:** The cited IxDF page still says the opposite of the sentence it supports: it presents badges and leaderboards as tapping intrinsic motivation and gives no history of a behaviorist early phase. The behaviorist, reward-based reading of early gamification is a real position, but it lives in other sources: a behavior-analysis chapter that explains points and badges as positive reinforcement, and Nicholson's critique of 'BLAP' (badges, levels, achievements, points) gamification as external reward. 'Relies entirely' still overstates it, because the feedback that points carry tends to raise intrinsic motivation rather than lower it. Now cites [Nicholson, Strategies for Meaningful Gamification: Concepts behind Transformative Play and Participatory Museums, Meaningful Play (2012)](https://scottnicholson.com/pubs/meaningfulstrategies.pdf).

### Introduction: contested

**Claim reviewed:** Extrinsic gamification tactics can generate a short-term spike in metrics but rarely sustain long-term engagement.

**Now reads:** These tactics can produce a short-term lift in metrics, but the results are uneven. In some studies the gains fade once the novelty wears off; in others they hold or recover, depending on the product and the people using it.

**Why:** The evidence splits cleanly rather than favoring the article. The newest long study of a gamified course (756 students over 14 weeks) found the effect of points and competition faded after four weeks and then partly recovered, and a review of financial incentives found behavior gains fade within three months of removing the reward. But two meta-analyses of randomized physical-activity trials found gamification effects that persist after the program ends, a long-term loyalty-program study found light buyers became more loyal over time, and gamification reviews describe effects as context-dependent rather than short-lived. 'Rarely sustain' is stronger than any of this supports; 'uneven' is accurate. Now cites [Rodrigues et al., Gamification suffers from the novelty effect but benefits from the familiarization effect: Findings from a longitudinal study, International Journal of Educational Technology in Higher Education (2022)](https://doi.org/10.1186/s41239-021-00314-6).

### Introduction: unverified

**Claim reviewed:** Users eventually develop 'gamification blindness' or feel manipulated by push notifications and arbitrary rewards.

**Now reads:** Over time, many users seem to tune these rewards out, much as they learned to ignore banner ads, and some come to feel manipulated by the steady stream of push notifications and arbitrary rewards.

**Why:** 'Gamification blindness' reads like an established finding, but no study or academic source uses the term; the nearest is a vendor blog phrase. The idea, that people stop noticing repeated reward cues the way they stop noticing banner ads, is plausible, but nobody appears to have tested it. Feeling manipulated by notifications is also asserted without a source.

### Introduction: supported with caveats

**Claim reviewed:** Sustainable engagement comes from intrinsic motivation, when a user interacts with a product because they find the activity itself rewarding or meaningful.

**Now reads:** Sustainable engagement, the kind that builds habit and loyalty, depends less on external pressure and more on motivation the user owns. That includes intrinsic motivation, when people find the activity itself rewarding, and values they have taken on as their own, when they find it meaningful.

**Why:** The definition matches the cited paper: intrinsic motivation means doing something for its own sake. But the same paper warns that the contrast with extrinsic motivation 'is not a simple one', and that well-internalized extrinsic motivation, such as doing something because you value it, also predicts lasting positive outcomes. Folding 'meaningful' into intrinsic motivation and treating extrinsic motivation as the opposite of sustainable misstates the source.

### Introduction: supported with caveats

**Claim reviewed:** When a digital interface satisfies autonomy, competence and relatedness, users return largely of their own volition.

**Now reads:** When a digital experience satisfies these three needs, people are more likely to enjoy it and come back to it; studies of video game players find each need predicts continued play.

**Why:** Games research supports the core idea: across four studies, players' sense of autonomy, competence and relatedness each predicted whether they kept playing. But those studies are correlational, reviews of HCI work find SDT is usually invoked rather than tested, and the sentence sits on a source that does not discuss digital products. Duolingo's own research shows reminders and streaks also drive return visits, so 'of their own volition' should be softened. Now cites [Ryan, Rigby & Przybylski, The Motivational Pull of Video Games, Motivation and Emotion (2006)](https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf).

### Ingredient 1: Autonomy: supported with caveats

**Claim reviewed:** When users feel trapped (unskippable video, hard-to-cancel subscription, forced account creation), their need for autonomy is violated, producing psychological reactance that often leads them to abandon the product.

**Now reads:** The result can be what psychologists call psychological reactance: a defensive mix of irritation and pushback against the system. Online, it shows up as avoidance, and sometimes as users leaving altogether.

**Why:** Psychological reactance is a well-established theory (Brehm), and experiments on forced exposure online show intrusive ads cause irritation and avoidance; one retailer famously gained buyers by removing forced registration. The theory is not credited, though, and how often reactance leads people to abandon a product 'entirely' has not been measured. Now cites [Edwards, Li & Lee, Forced Exposure and Psychological Reactance, Journal of Advertising (2002)](https://gwern.net/doc/economics/advertising/2002-edwards.pdf).

### Designing for Agency: contested

**Claim reviewed:** Dark patterns such as pre-checked consent boxes or hidden unsubscribe buttons may improve conversion short term but destroy brand trust.

**Now reads:** Conversely, dark patterns, like pre-checked consent boxes or hidden unsubscribe buttons, are the antithesis of autonomy. They often raise conversion numbers, and the subtle ones can pass unnoticed. But users who notice them read them as a lack of goodwill, and the heavy-handed ones provoke a backlash that costs the brand trust.

**Why:** The conversion half is well supported: the largest experiments find dark patterns work on all consumer groups and that mild ones more than double sign-ups. The trust half is mixed. Two small lab experiments found dark patterns and scarcity cues lower brand trust and perceived vendor goodwill, but the biggest study found mild patterns of the kind the article names (pre-checked boxes) produced no measurable backlash; only aggressive ones did. 'Destroy brand trust' holds mainly for heavy-handed tactics and for users who notice. Now cites [Luguri & Strahilevitz, Shining a Light on Dark Patterns, Journal of Legal Analysis (2021)](https://doi.org/10.1093/jla/laaa006).

### Ingredient 2: Competence: supported with caveats

**Claim reviewed:** Nothing destroys the feeling of competence faster than a vague error message; it tells users they have failed without a path forward.

**Now reads:** Vague error messages are among the quickest ways to undercut a user's sense of competence. When a user sees "Something went wrong" with no explanation, the interface tells them something failed without offering a way forward.

**Why:** The general point holds: novices given plain-language error messages reported less frustration and anxiety. But results are mixed (one controlled study of improved error messages found no effect), 'nothing destroys competence faster' is a superlative no study could test, and a 404 page usually signals a broken link rather than a user mistake. Now cites [The Effect of Automated Error Message Feedback on Undergraduate Physics Students Learning Python, Journal for STEM Education Research (2023)](https://doi.org/10.1007/s41979-022-00084-4).

### Feedback Loops and Progressive Disclosure: not supported

**Claim reviewed:** TurboTax is successful despite the complexity of taxes because its 'Refund Monitor' provides a continuous visual feedback loop.

**Now reads:** TurboTax shows how this works and what it can cost. For years its running refund total let users see the effect of each entry, a steady form of feedback that supports a sense of competence, and its step-by-step wizard breaks a stressful task into small questions. But, as Nielsen Norman Group points out, the wizard also asks users to give up much of their autonomy, and TurboTax Online now shows the running total only at the review stage.

**Why:** No source links TurboTax's commercial success to its running refund display, and the article cites none. Intuit's own help page, updated November 2026, says TurboTax Online no longer shows a running refund tracker at each step and instead shows the total in the review section, so the 'continuous' feedback loop the article describes is not what current users see. The article's own source, Nielsen Norman Group, uses TurboTax as a trade-off: its wizard builds competence but takes away much of the user's autonomy. Now cites [Kohler, Autonomy, Relatedness, and Competence in UX Design, NN/g (2022)](https://www.nngroup.com/articles/autonomy-relatedness-competence/).

### Feedback Loops and Progressive Disclosure: supported with caveats

**Claim reviewed:** LinkedIn's 'Profile Strength' meter uses progressive disclosure, guiding users through small tasks so that as the meter fills they experience achievement.

**Now reads:** Similarly, LinkedIn uses a profile completion meter to make progress visible. Rather than presenting a daunting empty form, it breaks the profile into small, manageable tasks, and as the meter fills, the user gets a small sense of achievement.

**Why:** The LinkedIn example comes from the article's own source without credit, and that source calls it a gamified progress bar, not progressive disclosure, which is a different pattern (hiding advanced options until needed). The mechanism has support: an artificial head start toward a goal makes people more persistent. But a meta-analysis of 32 web-survey experiments found progress bars do not generally reduce drop-off, so the effect is not automatic. Now cites [Interaction Design Foundation, What is Gamification?](https://ixdf.org/literature/topics/gamification).

### Social Proof and Multiplayer Experiences: supported with caveats

**Claim reviewed:** Relatedness can be engineered through 'multiplayer' presence; Figma made design social by showing other users' cursors, satisfying the need for connection.

**Now reads:** Relatedness can be designed through shared presence. Figma lets colleagues work on the same file at once and see each other's cursors moving across the canvas, a small cue that reminds users they are part of a team rather than working alone.

**Why:** NN/g does use Figma as an example of relatedness through collaboration, but it does not mention cursors or say Figma transformed design into a social activity, and nothing supports 'instantly'. Research on collaborative writing tools also finds that seeing others at work makes people worry about how they are perceived, so presence cues are not purely warm.

### Social Proof and Multiplayer Experiences: contested

**Claim reviewed:** Conversational, empathetic microcopy in support chat signals the user is heard by a human and satisfies the need for connection.

**Now reads:** Even in solitary B2B SaaS tools, tone of voice can help. Microcopy that is plain, conversational and specific makes the product feel less mechanical, and a warm reply after something goes wrong can soften the blow. Be careful with scripted empathy, though. When users know they are talking to a bot, a line like "We know this is frustrating" can read as intrusive rather than caring, and a fast, clear fix or a route to a real person usually serves them better.

**Why:** Several experiments support the first half: chatbots that express sympathy or use a warm, social style are rated higher than flat ones, and AI-written replies can make people feel heard. But the article's example is a frustrated user in a support chat, and the newest and most rigorous study of that exact moment (three experiments in MIS Quarterly, 2026) found that empathetic bot messages after a service failure triggered reactance and lowered satisfaction, matching the earlier finding that human-like bots backfire with angry customers. People also feel less heard once they learn a reply came from AI, which undercuts 'heard by another human.' Now cites [Han, Yin & Zhang, Bots with Empathy: Reactance Against Emotion-Aware AI Agents in Customer Service, MIS Quarterly (2026)](https://doi.org/10.25300/MISQ/2026/18683).

### Glued to Games: supported with caveats

**Claim reviewed:** Glued to Games (Rigby & Ryan, 2011), co-written by SDT co-founder Richard Ryan, explains why autonomy, competence and relatedness keep players coming back and why points and badges on their own do not.

**Now reads:** Co-written by Richard Ryan, one of self-determination theory's two founders, this book applies the theory to the products people return to by choice. It explains how autonomy, competence and relatedness keep players coming back.

**Why:** The cited page confirms the authors, the 2011 date and that the book explains game engagement through the three needs, and Ryan is one of SDT's two founders. The cited page does not mention points or badges, so the claim that the book explains why they fail on their own could not be checked from that source; the 186-page count was also not verified.

### Case Study: Duolingo: not supported

**Claim reviewed:** Duolingo achieved massive scale by systematically satisfying autonomy (self-set daily goals from 'Casual' to 'Insane'), competence (bite-sized lessons, immediate feedback) and relatedness (Friend Quests, leaderboards).

**Now reads:** Duolingo is a useful example of features that map onto all three needs, although the company itself credits its growth to gamification mechanics such as streaks, leaderboards and reminders, tuned by thousands of A/B tests. Autonomy: users pick a daily goal, from "Casual" to "Intense". Competence: lessons are short, feedback is immediate, and a fanfare marks each finished lesson. Relatedness: Friend Quests and leaderboards turn a solitary activity into a shared one.

**Why:** No source shows that Duolingo grew by satisfying the three needs, and Duolingo's own account says something different. Its IPO filing credits gamification features such as Streaks and Leaderboards, tuned by thousands of A/B tests, for bringing learners back, and its former chief product officer credits leaderboards, streaks and push notifications for the growth turnaround without mentioning motivation theory. The one survey that tested Duolingo through the lens of self-determination theory found competence and relatedness mattered but autonomy was not a significant mediator, and the top goal tier is 'Intense', not 'Insane'. Now cites [Duolingo, Inc., Form S-1 registration statement, SEC (2021), section 'Motivating game mechanics'](https://www.sec.gov/Archives/edgar/data/1562088/000162828021013065/duolingos-1.htm).
