---
title: "Evidence review: Why Users Leave"
---

# Evidence review: Why Users Leave

Article: [Why Users Leave](https://attck.com/blog/why-users-leave/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**A visitor's decision to leave a page takes only seconds and is made on the first screen.**

The vignette is illustrative and fair as framing; the stronger general version in the conclusion (C20) is where the wording needs to change.

- [Liu, White & Dumais, SIGIR 2010](https://microsoft.com/en-us/research/wp-content/uploads/2010/10/dwelltime.pdf): “is less than 1 on 98.5% pages”
- [Nielsen, How Long Do Users Stay on Web Pages?, NN/g 2011](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/): “It's clear from the chart that the first 10 seconds of the page visit are critical for users' decision to stay or leave.”

### Two Billion Visits, One Shape

**In 2010, Liu, White and Dumais of Microsoft Research took two weeks of logs from a popular browser plug-in used by opted-in US English-language users and measured how long each visit lasted before the next page loaded.**

Confirmed in the authors' PDF on the Microsoft Research site. The last page of each session, often the true exit, is not measured.

- [Liu, White & Dumais, SIGIR 2010](https://microsoft.com/en-us/research/wp-content/uploads/2010/10/dwelltime.pdf): “We collected two-weeks of log data from a popular Web browser plug-in operating in the English (US) market, which records the searches and browsed pages for opted-in users.”

**They kept only pages with at least 10,000 visits, 205,873 pages in all, which is more than two billion visits.**

205,873 x 10,000 = 2.06 billion, a lower bound.

**They fitted a Weibull distribution, the model reliability engineers use for failure times, to each page's dwell times.**

Later work on Wikipedia logs (TeBlunthuis et al. 2019) found log-normal and Lomax fit reading times better than the Weibull. The claim here is only an attribution and stands.

**On 98.5% of the pages, it showed the falling pattern, which engineers call negative aging. Visits were most likely to end early; the longer a visit had lasted, the less likely it was to end in the next moment. In this data a visit ends when the next page loads, so a click deeper into the same site counts the same as leaving it.**

TeBlunthuis et al. (2019), on Wikipedia logs, found that the hazard rises in the first seconds of a page view and only then falls, a shape a two-parameter Weibull cannot show.

**The authors suggested a reason and named it "screen-and-glean": people skim a page to judge whether reading further is worth it, and the risk of leaving drops once a page passes that screening. The logs cannot show this directly, since a crowd that mixes quick leavers with committed readers would produce the same curve, but it fits how people describe their own browsing.**

The mixture explanation (Proschan 1963; Vaupel, Manton & Stallard 1979 in demography) is a mathematical alternative, not evidence against screening. The two can both be true.

- [Pirolli, Rational analyses of information foraging on the web, Cognitive Science 2005](https://europepmc.org/article/MED/21702778): “Web-site leaving is modeled as an ongoing assessment by the Web user of the expected benefits of continuing at a Web site as opposed to going elsewhere.”

**And screening was harsher for some kinds of page. Pages about education and computers showed it most strongly. Entertainment and travel pages showed it too, but they made up a larger share of the few pages that did not, which the authors took as a sign that less-entertaining pages may be screened more harshly.**

Categories came from a proprietary classifier and only the top 10 categories were analyzed; median shape was below 1 in all of them.

**Jakob Nielsen's summary for practitioners put the critical window at roughly the first 10 seconds of a visit.**

The same article says the curve flattens only after about 30 seconds and that users often leave in 10–20 seconds.

- [Nielsen, How Long Do Users Stay on Web Pages?, NN/g 2011](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/): “It's clear from the chart that the first 10 seconds of the page visit are critical for users' decision to stay or leave.”

**For design teams this moves the target. When a landing page has many short visits and few clicks onward, the first screen is the likeliest place it is failing, so look there before reworking the fifth section. First check that those short visits are not people who found their answer fast or clicked deeper into the site.**

Short visits after a click from a search ad track dissatisfaction well enough that Google researchers use bounce rate as a quality measure (Sculley et al. 2009), and eye-tracking shows about 57% of viewing time in the first screen and 74% in the first two (Pernice 2018), which is why the first screen is the place to look. The boundaries: Liu et al.'s dwell time ends at the next page load, so it does not separate exits from onward clicks; Google's analytics guidance says a high bounce rate is normal for pages whose job is done in one view; and the dwell time that marks a satisfied visit varies with a page's topic, length and readability (Kim et al. 2014).

- [Sculley, Malkin, Basu & Bayardo, Predicting bounce rates in sponsored search advertisements, KDD 2009](https://doi.org/10.1145/1557019.1557161): “we first provide quantitative analysis showing that bounce rate is an effective measure of user satisfaction.”
- [Pernice, Scrolling and Attention, Nielsen Norman Group 2018 (eye-tracking)](https://www.nngroup.com/articles/scrolling-and-attention/): “In our most recent study, users spent about 57% of their page-viewing time above the fold. 74% of the viewing time was spent in the first two screenfuls”
- [Improving Bounce Rate Prediction for Rare Queries by Leveraging Landing Page Signals, WWW Companion 2021, Bing logs; cites)](https://doi.org/10.1145/3442442.3453540): “users spend less than a specified time signifying that the user did not find a possible match of their query intent with the landing page content”
- [Wajnberg, Fauvergue & Pons, Patch leaving decision rules and the Marginal Value Theorem, Behavioral Ecology 11(6), 2000](https://doi.org/10.1093/beheco/11.6.577): “On average, T. brassicae females spent more time on patches of higher quality, and all patches were reduced to the same level of profitability before being left.”
- [Beauty matters: reducing bounce rate by aesthetics of experience product portal page, Industrial Management & Data Systems 2021, Taobao shop data; authors not captured)](https://doi.org/10.1108/imds-08-2020-0484): “text aesthetics has a U-shaped relationship with bounce rate, whereas the relationship between image aesthetics and bounce rate is insignificant.”
- [Lindgaard, Fernandes, Dudek & Brown, Attention web designers: You have 50 milliseconds to make a good first impression!, Behaviour & Information Technology 25(2), 2006](https://doi.org/10.1080/01449290500330448): “Thus, visual appeal can be assessed within 50 ms, suggesting that web designers have about 50 ms to make a good first impression.”

### Information Foraging Theory (book box)

**His models of information scent and patches explain leaving as a running comparison of what a page offers against what might be found elsewhere, and the first screen is where that comparison starts.**

Book record confirmed via OpenAlex; text paywalled.

- [Pirolli, Rational analyses of information foraging on the web, Cognitive Science 2005](https://europepmc.org/article/MED/21702778): “Web-site leaving is modeled as an ongoing assessment by the Web user of the expected benefits of continuing at a Web site as opposed to going elsewhere.”

### The wait before the screen

**In an experiment on web waiting times, Fiona Nah found that people's tolerable wait for a page during information retrieval was about two seconds, and that feedback during the wait made them willing to wait longer. Other studies put the limit higher, but they agree that every second of blank screen costs visitors.**

Galletta et al. (2004) found effects level off around 4 seconds (performance, intentions) and 8 seconds (attitudes). Krishnan & Sitaraman (2012) found video viewers start abandoning after about 2 seconds of startup delay.

- [Nah, Behaviour & Information Technology 2004](https://doi.org/10.1080/01449290410001669914): “the presence of feedback prolongs Web users' tolerable waiting time and the tolerable waiting time for information retrieval is approximately 2 s.”

### The interstitial at the door

**In 2016 Google announced that from January 2017 mobile pages with intrusive interstitials might rank lower because they 'provide a poorer experience to users'; popups covering content and standalone screens were examples, while reasonable, easily dismissed banners and legally required notices such as cookie consent were exempt.**

Google called the signal one of hundreds, and in 2023 said page-experience aspects may not all be used directly in ranking. Editors may also want to note that the opening scene's obstacle, a large cookie banner, is the kind of notice Google exempted; the user-experience point still holds even if the ranking one does not.

- [Phan, Helping users easily access content on mobile, Google Search Central Blog 2016](https://developers.google.com/search/blog/2016/08/helping-users-easily-access-content-on): “provide a poorer experience to users”

### Tool: lifelines

**Its WeibullFitter takes a list of visit durations and returns the shape parameter (rho_); a value below 1 means the risk of leaving falls over time, the same pattern Liu and colleagues found.**

WeibullFitter.fit() accepts an event_observed list, which matters for visits that were still open when tracking stopped.

- [lifelines WeibullFitter documentation](https://lifelines.readthedocs.io/en/latest/fitters/univariate/WeibullFitter.html): “controls if the cumulative hazard (see below) is convex or concave, representing accelerating or decelerating hazards.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Two Billion Visits, One Shape: supported with caveats

**Claim reviewed:** On 98.5% of the pages the Weibull shape parameter showed a falling risk of leaving (negative aging): visitors were most likely to leave early, and the longer they stayed the less likely they were to leave.

**Now reads:** On 98.5% of the pages, it showed the falling pattern, which engineers call negative aging. Visits were most likely to end early; the longer a visit had lasted, the less likely it was to end in the next moment. In this data a visit ends when the next page loads, so a click deeper into the same site counts the same as leaving it.

**Why:** The 98.5% figure is exactly what the paper reports. Two things the article leaves out: a 'visit' ends whenever the next page loads, so clicking deeper into the same site counts as leaving, and a later study with a more flexible model found the risk of leaving actually rises for the first few seconds before it falls.

### Two Billion Visits, One Shape: supported with caveats

**Claim reviewed:** The authors named the behavior 'screen-and-glean': people skim a page to judge whether reading further is worth it, and the risk of leaving drops once a page passes that screening.

**Now reads:** The authors suggested a reason and named it "screen-and-glean": people skim a page to judge whether reading further is worth it, and the risk of leaving drops once a page passes that screening. The logs cannot show this directly, since a crowd that mixes quick leavers with committed readers would produce the same curve, but it fits how people describe their own browsing.

**Why:** The authors did coin 'screen-and-glean', but they offered it as something they 'suspect' from the overall shape of the data, not something they observed people doing. A falling risk across a crowd can also come from mixing quick leavers with committed readers, with no one screening at all, a well-known effect in reliability engineering. The article states the skimming behavior as fact.

### Two Billion Visits, One Shape: supported with caveats

**Claim reviewed:** Education and computer pages were more likely to show screening, while entertainment and travel pages more often showed the opposite pattern, which the authors took as a sign that less-entertaining pages are screened more harshly.

**Now reads:** And screening was harsher for some kinds of page. Pages about education and computers showed it most strongly. Entertainment and travel pages showed it too, but they made up a larger share of the few pages that did not, which the authors took as a sign that less-entertaining pages may be screened more harshly.

**Why:** The paper does find screening stronger on less-entertaining pages and says so in its own summary. But every category it examined, entertainment and travel included, still showed the screening pattern on most pages; those categories were only over-represented among the small minority of pages that did not. The authors also call the harsher-screening idea a hypothesis.

### Two Billion Visits, One Shape: supported with caveats

**Claim reviewed:** A page with many short visits is usually failing a quick test at the top, so the fix sits in the first screen.

**Now reads:** For design teams this moves the target. When a landing page has many short visits and few clicks onward, the first screen is the likeliest place it is failing, so look there before reworking the fifth section. First check that those short visits are not people who found their answer fast or clicked deeper into the site.

**Why:** The sentence is a reasonable rule of thumb with boundaries the article should state. Short visits after a click from an ad or a search result do track dissatisfaction, and eye-tracking shows that most viewing time sits in the first screen or two, so looking there first is sound. But short visits in Liu et al.'s data include clicks deeper into the site, Google's own analytics guidance says a high bounce rate is normal for pages whose job is done in one view, and search research shows that how long a satisfied visit lasts depends on the page's topic, length and readability, so 'usually failing' is not something any source measures. Now cites [Kara Pernice, Scrolling and Attention, Nielsen Norman Group (2018)](https://www.nngroup.com/articles/scrolling-and-attention/).

### Information Foraging Theory (book box): supported with caveats

**Claim reviewed:** Pirolli's models of information scent and patches explain why the decision to leave is often made on the first screen.

**Now reads:** His models of information scent and patches explain leaving as a running comparison of what a page offers against what might be found elsewhere, and the first screen is where that comparison starts.

**Why:** Pirolli's foraging models do explain leaving as a cost-benefit judgment guided by information scent. They treat it as an ongoing assessment, though, not a decision made on the first screen; that part is the article's extension. The book itself was not opened, and this rests on Pirolli's 2005 paper summarizing the same models.

### The page that hides its answer: supported with caveats

**Claim reviewed:** Pages that pass the screening state what they offer in plain text on the first screen, using the words of the search or link that brought people there.

**Now reads:** Pages that pass tend to state what they offer in plain text on the first screen, using the words of the search or link that brought people there. Information-scent research predicts exactly this: people keep going when what they see matches what they were looking for.

**Why:** Matching the visitor's own words and stating the offer plainly is standard information-scent advice, and it fits the screening idea. But the article states it as an observed fact about pages that pass, which no source measured, and it does not credit the information-scent research it draws on. Now cites [Budiu, Information Scent: How Users Decide Where to Go Next, Nielsen Norman Group](https://www.nngroup.com/articles/information-scent/).

### The wait before the screen: supported with caveats

**Claim reviewed:** In an experiment on web waiting times, Fiona Nah found that people's tolerable wait for a page during information retrieval was about two seconds, and that feedback such as a progress indicator made them willing to wait longer.

**Now reads:** In an experiment on web waiting times, Fiona Nah found that people's tolerable wait for a page during information retrieval was about two seconds, and that feedback during the wait made them willing to wait longer. Other studies put the limit higher, but they agree that every second of blank screen costs visitors.

**Why:** Nah's abstract confirms both findings: feedback lengthened tolerable waits, and the tolerable wait for information retrieval was about 2 seconds. That figure comes from one lab experiment; other studies put the threshold between 2 and roughly 10 seconds, and mobile users in one study tolerated about four times the desktop delay. The 'progress indicator' detail could not be checked because the full paper is paywalled.

### Tool: lifelines: supported with caveats

**Claim reviewed:** lifelines' WeibullFitter takes visit durations and returns the shape parameter rho_; a value below 1 means the page shows the same early screening.

**Now reads:** Its WeibullFitter takes a list of visit durations and returns the shape parameter (rho_); a value below 1 means the risk of leaving falls over time, the same pattern Liu and colleagues found.

**Why:** lifelines' WeibullFitter does return the shape parameter rho_, and a value below 1 means the risk of leaving falls over time. Calling that 'the same early screening' borrows the paper's interpretation, which the data alone cannot prove. Now cites [lifelines WeibullFitter documentation](https://lifelines.readthedocs.io/en/latest/fitters/univariate/WeibullFitter.html).

### After the First Screen: not supported

**Claim reviewed:** Most departures are verdicts on a few seconds of evidence.

**Now reads:** Attention is spent where the return looks highest, and the first screen is where people estimate that return. The risk of leaving is highest in the first ten seconds or so, while people are judging that screen, which is good news: the evidence they judge is yours to design.

**Why:** No source measures the share of departures that happen within a few seconds, and the data on how long visits last point the other way. Nielsen, summarizing the same Microsoft study, says people often leave in 10 to 20 seconds, that the leaving curve only flattens after about 30 seconds, and that the average visit lasts a little under a minute; on Wikipedia the median page view is 25 seconds and the risk of leaving rises over the first seconds before it falls. The closest support, Chartbeat's finding that 55% of two billion page views had under 15 seconds of active time, puts the line at 15 seconds rather than a few, and drops to one in three on article pages. Now cites [Jakob Nielsen, How Long Do Users Stay on Web Pages?, Nielsen Norman Group (2011)](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/).
