---
title: "Evidence review: Behavioral Signals in Adaptive Interfaces"
---

# Evidence review: Behavioral Signals in Adaptive Interfaces

Article: [Behavioral Signals in Adaptive Interfaces](https://attck.com/blog/behavioral-signals-in-adaptive-interfaces/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**In Office 2000, menus promoted commands you used to a short menu; the rest waited behind a chevron at the bottom or appeared after a few seconds. The idea, as Jensen Harris described it, was that you would eventually have a fully tuned interface that showed only what you needed.**

Harris's own account of Office 2000's adaptive menus was confirmed in the archived post.

- [Harris, Combating the Perception of Bloat (2005)](https://learn.microsoft.com/en-us/archive/blogs/jensenh/combating-the-perception-of-bloat-why-the-ui-part-3-2): “the idea was that eventually you'd have a fully-tuned, auto-customized UI that would show you only what you need and use.”
- [McGrenere, Baecker & Booth 2002, CHI (OpenAlex abstract)](https://doi.org/10.1145/503376.503406): “Results showed that participants were better able to navigate through the menus and toolbars and were better able to learn with our prototype.”

**Writing in 2005, as his team built the Ribbon, Harris said Adaptive Menus 'were not successful': people use a wide range of features so no default short menu suited everyone, a wrong short menu forced two scans, and the full menu reset your place when it opened. The menus also felt random: a command was in one spot, and two days later it was gone.**

Independent lab and field studies (Mitchell and Shneiderman 1989; McGrenere, Baecker and Booth 2002) found users slower with or less fond of menus that reorder themselves, matching Harris's account.

- [Mitchell & Shneiderman 1989, SIGCHI Bulletin (OpenAlex abstract)](https://doi.org/10.1145/67243.67247): “Eighty-one percent of the subjects preferred working with static menus to working with dynamic menus.”

**Harris: 'Auto-customization, unless it does a perfect job, is usually worse than no customization at all.'**

As a general rule Harris's line is too strong: spatially stable adaptation such as ephemeral menus (Findlater et al., 2009) was faster than static menus at high accuracy and not significantly slower at low accuracy. The article's 'half right' framing already allows for this.

### A Signal Is a Proxy, Not a Preference

**An adaptation changes the place people come back to, so when it moves things, people have to relearn where they are.**

Mitchell and Shneiderman (1989) found that people who started with self-reordering menus were significantly slower, and 81% preferred static menus.

- [Mitchell & Shneiderman 1989, SIGCHI Bulletin (OpenAlex abstract)](https://doi.org/10.1145/67243.67247): “The subjects that used adaptive dynamic menus for the first set of tasks were significantly slower than those who used static menus on the first set of tasks.”

**Implicit signals (clicks, dwell time, purchases, skips) are plentiful and cheap, which is why most adaptive systems lean on them.**

Kelly and Teevan (2003) describe implicit feedback as attractive because large quantities can be gathered at no extra cost to the user.

- [Kelly & Teevan 2003, SIGIR Forum (OpenAlex abstract)](https://doi.org/10.1145/959258.959260): “as large quantities of implicit data can be gathered at no extra cost to the user, they are attractive alternatives.”
- [Joachims et al. 2005, SIGIR (OpenAlex abstract)](https://doi.org/10.1145/1076034.1076063): “we conclude that clicks are informative but biased.”

**Explicit signals are scarce and biased in their own way, since the people who bother to rate are not everyone.**

Ratings in a real recommender system were found to be missing not at random (Marlin and Zemel, 2009).

- [Marlin & Zemel 2009, RecSys (OpenAlex abstract)](https://doi.org/10.1145/1639714.1639717): “we demonstrated strong evidence for violations of the missing at random condition in a real recommender system.”
- [Hu, Pavlou & Zhang 2009, CACM (OpenAlex abstract)](https://doi.org/10.1145/1562764.1562800): “J-shaped distribution”

### Accuracy Does the Work, Predictability Keeps the Trust

**At 70% accuracy people used the adaptive toolbar 86% of the times it held the right button, against 71% at 50%, and finished faster; predictability had no significant effect on speed.**

The no-effect-on-speed result for predictability comes from one lab study; no replication was found among the citing papers checked.

- [Gajos et al., CHI 2008 (author-hosted PDF)](https://www.eecs.harvard.edu/~kgajos/papers/2008/kgajos-chi08-predictability.pdf): “At the 50% accuracy level the adaptive toolbar was used 70.6% of the time when it contained the correct button, compared with 86.4% at the 70% accuracy level.”
- [Findlater & McGrenere, CHI 2008 (OpenAlex abstract)](https://doi.org/10.1145/1357054.1357249): “Results show that high accuracy adaptive menus have an even larger positive impact on performance and satisfaction when screen real estate is constrained.”

**Findlater and McGrenere compared static, adaptive and user-adaptable menus with 27 people: the static menu was significantly faster than the adaptive one, and most participants preferred the version they could arrange themselves.**

Findlater and McGrenere's own 2008 follow-up found high-accuracy adaptive menus improved speed and satisfaction, especially on small screens.

- [Findlater & McGrenere, CHI 2004 (OpenAlex abstract)](https://doi.org/10.1145/985692.985704): “The static menu was found to be significantly faster than the adaptive menu”

**Harris's line fits adaptation that moves things. Later studies found that adaptation which leaves items in place, adding a shortcut or briefly highlighting likely choices, cost little even when its guesses were often wrong, though it can make people less aware of the features it doesn't surface.**

Ephemeral adaptation (Findlater et al., 2009) kept menu items in place and was not significantly slower than a static menu even at low accuracy; Findlater and McGrenere (2008) note that accurate adaptation can reduce awareness of other features.

- [Findlater, Moffatt, McGrenere & Dawson, CHI 2009 (OpenAlex abstract)](https://doi.org/10.1145/1518701.1518956): “ephemeral adaptive menus are faster than static menus when accuracy is high, and are not significantly slower when it is low”

### The minutes you stayed

**YouTube added watch time in 2012 and saw an immediate 20% drop in views, a cost it chose to accept; Goodrow describes staying up late watching random videos he would rather not have spent the evening on.**

Kelly and Belkin (2004) found no general relationship between reading time and usefulness, supporting the article's point that time spent is not value.

- [Goodrow, On YouTube's Recommendation System (2021)](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/): “When we first incorporated watchtime into recommendations, we saw an immediate 20% drop in views.”
- [Kelly & Belkin 2004, SIGIR (OpenAlex abstract)](https://doi.org/10.1145/1008992.1009057): “no general, direct relationship between display time and usefulness”
- [Kleinberg, Mullainathan & Raghavan 2023, Management Science (OpenAlex abstract)](https://doi.org/10.1287/mnsc.2022.03683): “many users seem to regret the time they spend on these platforms.”

### Pull quote

**'When a measure becomes a target, it ceases to be a good measure.' (Marilyn Strathern, 'Improving Ratings': Audit in the British University System)**

Strathern's 1997 wording is the popular form of what she and Keith Hoskin call Goodhart's law.

- [Strathern 1997](https://gwern.net/doc/statistics/decision/1997-strathern.pdf): “When a measure becomes a target, it ceases to be a good measure.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: supported with caveats

**Claim reviewed:** Research published two years later suggests Harris was half right.

**Now reads:** Research published in 2008 suggests he was half right.

**Why:** Harris's post is dated October 10, 2005 and the Gajos study appeared at CHI in April 2008, so the gap is closer to two and a half years than two. The 'half right' reading is fair: in that study accuracy drove speed and use, while predictability still mattered for satisfaction.

### A Signal Is a Proxy, Not a Preference: supported with caveats

**Claim reviewed:** Because adaptation persists, its errors accumulate, and every time the layout shifts, people have to relearn where things are.

**Now reads:** An adaptation changes the place people come back to, so when it moves things, people have to relearn where they are.

**Why:** Lab studies show that menus which move items slow people down while they relearn positions, so the core point holds. The claim that errors accumulate is plausible but was not tested directly, and adaptation that leaves items where they are avoids the relearning cost. The sentence is uncited. Now cites [Mitchell & Shneiderman, Dynamic versus static menus: an exploratory comparison, SIGCHI Bulletin (1989)](https://doi.org/10.1145/67243.67247).

### Accuracy Does the Work, Predictability Keeps the Trust: supported with caveats

**Claim reviewed:** Gajos et al. (2008) had 23 experienced Office users work in a modified Word interface with an extra toolbar of eight buttons that held the needed button 50% or 70% of the time and updated either predictably (most recently used) or at random.

**Now reads:** Twenty-three intermediate to expert users of Office-style software worked in a modified Word interface with an extra toolbar of eight buttons that changed as they went.

**Why:** The design details are right: 23 participants, a modified Word interface, eight adaptive buttons, 50% or 70% accuracy, and most-recently-used versus random updates. The paper describes participants as intermediate to expert users of Office-style applications, which is a little looser than 'experienced Office users'.

### Accuracy Does the Work, Predictability Keeps the Trust: supported with caveats

**Claim reviewed:** Harris's line holds for adaptation that moves things; adaptation that adds a shortcut and stays legible has more room for error.

**Now reads:** Harris's line fits adaptation that moves things. Later studies found that adaptation which leaves items in place, adding a shortcut or briefly highlighting likely choices, cost little even when its guesses were often wrong, though it can make people less aware of the features it doesn't surface.

**Why:** The idea is sound, but neither cited study compared copying with moving, so the article leans on them for something they did not test. Later work on menus that keep items in place and only highlight likely choices supports it directly. That work also found a cost: accurate shortcuts make people less aware of the rest of the features. Now cites [Findlater, Moffatt, McGrenere & Dawson, Ephemeral adaptation: the use of gradual onset to improve menu selection performance, CHI (2009)](https://doi.org/10.1145/1518701.1518956).

### The stars you gave, and the history you can see: unverified

**Claim reviewed:** Most product teams skip re-checking signals; a signal is usually chosen once, when a feature is built, and then quietly becomes the definition of success.

**Now reads:** Teams often skip that step. A signal is usually chosen once, when a feature is built, and can quietly become the definition of success.

**Why:** No study was found measuring how many product teams re-check their signals after launch, so 'most product teams' is an unsupported generalization. The risk it describes is well documented, but its prevalence is not.
