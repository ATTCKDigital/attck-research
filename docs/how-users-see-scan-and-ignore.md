---
title: "Evidence review: How Users See, Scan, and Ignore"
---

# Evidence review: How Users See, Scan, and Ignore

Article: [How Users See, Scan, and Ignore](https://attck.com/blog/how-users-see-scan-and-ignore/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### The Myth of the "Reading" User

Information foraging theory models people as maximizing the rate of valuable information gained (Pirolli and Card 1999). Lab work on skimming shows the trade-off: skimmers keep the main ideas and lose detail (Duggan and Payne 2009).

- [Pernice, The Layer-Cake Pattern of Scanning Content on the Web, NN/g 2019](https://www.nngroup.com/articles/layer-cake-pattern-scanning/): “Recall that people are naturally efficient and attempt to put in the least possible work for achieving their goal”
- [Duggan & Payne, Text skimming, J Exp Psychol Appl 15(3), 2009](https://pubmed.ncbi.nlm.nih.gov/19751073/): “skimming improved memory for important ideas from a text but did not improve memory of less important details or of inferences made from information within the text.”

The percentages come from a 1997 think-aloud study with 19 participants (Morkes and Nielsen 1997). NN/g's later eyetracking work over 13 years confirmed that scanning dominates (Moran 2020), as do an eye-tracking study of skimming (Strukelj and Niehorster 2018) and a survey of screen-based reading (Liu 2005); motivated users sometimes read nearly everything (Pernice 2017).

- [Nielsen, How Users Read on the Web, NN/g 1997](https://www.nngroup.com/articles/how-users-read-on-the-web/): “In research on how people read websites we found that 79 percent of our test users always scanned any new page they came across; only 16 percent read word-by-word.”
- [Moran, How People Read Online: New and Old Findings, NN/g 2020](https://www.nngroup.com/articles/how-people-read-online/): “People rarely read online — they’re far more likely to scan than read word for word.”
- [Strukelj & Niehorster, One page of text: Eye movements during regular and thorough reading, skimming, and spell checking, Journal of Eye Movement Research 11(1), 2018](https://pubmed.ncbi.nlm.nih.gov/33828678/): “Skimming involved longer saccades, shorter average fixation durations, more word skipping, shorter total reading times evenly distributed across the page, and resulted in lower comprehension scores.”
- [Liu, Reading behavior in the digital environment, Journal of Documentation 61(6), 2005 (Crossref record; publisher page not fetched)](https://api.crossref.org/works/10.1108/00220410510632040): “The screen‐based reading behavior is characterized by more time spent on browsing and scanning, keyword spotting, one‐time reading, non‐linear reading, and reading more selectively, while less time is spent on in‐depth reading, and concentrated reading.”

### The Physiology of Digital Vision

Rayner notes that new visual information is not taken in during saccades, though cognitive processing continues.

- [Rayner, Eye movements and attention in reading, scene perception, and visual search (Bartlett Lecture), QJEP 2009](https://pages.ucsd.edu/~bkbergen/cogs200/Rayner-Bartlett.pdf): “Since vision is suppressed during a saccade (Matin, 1974), new information is only acquired during fixations.”

### 1. The F-Pattern

NN/g notes that good formatting can prevent F-shaped scanning (Pernice 2017).

- [Nielsen 2006](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/): “This dominant reading pattern looks somewhat like an F and has the following three components”

### Utilize Directional Cues

A meta-analysis of 423 gaze-cueing effects found the effect across tasks and cue types (McKay et al. 2021), and banner-ad experiments show averted gaze shifts attention to text and product (Sajjacholapunt and Ball 2014).

- [McKay et al., Psychological Bulletin 147, 2021](https://pubmed.ncbi.nlm.nih.gov/35404635/): “A gaze-cueing effect emerged across all levels of the assessed task and cue features, indicating that others' eye gaze reliably directs observers' attention.”
- [Sajjacholapunt & Ball, Frontiers in Psychology 5, 2014](https://pubmed.ncbi.nlm.nih.gov/24624104/): “in the condition involving faces with mutual gaze, the focus of attention was localized more on the face region rather than on the text or product”

### The "Squint Test" Audit Framework

Blur keeps the low spatial frequencies that drive the first, coarse pass of recognition (Bar et al. 2006), so the squint test approximates a first glance and visual weight; peripheral vision mainly loses the ability to sort out cluttered detail rather than going blurry (Rosenholtz 2016). Perceptual-model tools can help designers compare designs (Rosenholtz, Dorai and Freeman 2011) and research models predict attention on web pages and other designs (Fosco et al. 2020), but no independent validation of Attention Insight's accuracy figures was found.

- [Bar et al., Top-down facilitation of visual recognition, PNAS 103(2), 2006](https://pubmed.ncbi.nlm.nih.gov/16407167/): “We tested a specific model, proposing that low spatial frequencies facilitate visual object recognition by initiating top-down processes projected from orbitofrontal to visual cortex.”
- [Rosenholtz, Dorai & Freeman, Do predictions of visual perception aid design?, ACM Transactions on Applied Perception 8(2), 2011 (Crossref record; ACM page blocked)](https://api.crossref.org/works/10.1145/1870076.1870080): “DesignEye was capable of facilitating A/B comparisons between designs, and judgments about the quality of a design.”
- [Fosco, Casser, Bedi, O'Donovan, Hertzmann & Bylinskii, Predicting Visual Importance Across Graphic Design Types, UIST 2020 (arXiv)](https://arxiv.org/abs/2008.02912): “This paper introduces a Unified Model of Saliency and Importance (UMSI), which learns to predict visual importance in input graphic designs, and saliency in natural images, along with a new dataset and applications.”
- [Rosenholtz 2016 (PDF)](https://cshl-comp-neuro-vision.github.io/website/_static/pdfs/rosenholtz/rosenholtz-2016-annurev-vision.pdf): “Anstis (1998) applied Photoshop’s radial blur with parameters of spin = 1 and zoom = 4, producing an eccentricity-dependent blur”

### Case Study

Peer-reviewed eye-tracking studies of banner ads reproduced the effect: faces with direct gaze hold attention on the face (Sajjacholapunt and Ball 2014).

- [Sajjacholapunt & Ball 2014](https://pubmed.ncbi.nlm.nih.gov/24624104/): “in the condition involving faces with mutual gaze, the focus of attention was localized more on the face region rather than on the text or product”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### The Myth of the "Reading" User: supported with caveats

**Claim reviewed:** According to information foraging theory, users are on a high-speed mission to extract value with as little cognitive effort as possible.

**Now reads:** According to information foraging theory, users try to get the most useful information for the least time and effort. They weigh what a page seems to offer against the cost of digging for it.

**Why:** Pirolli and Card's theory says people try to maximize the rate at which they gain valuable information, which is a trade-off between value and effort, not a drive to spend as little effort as possible. NN/g's own writing uses the least-effort framing, so the idea is common in practice, but the citation is stretched. 'Ruthless' is the article's rhetoric.

### The Myth of the "Reading" User: supported with caveats

**Claim reviewed:** Eye-tracking research backs this up: a foundational NN/g study found that 79 percent of test users always scanned any new page; only 16 percent read word-by-word.

**Now reads:** Usability research backs this up. In a small 1997 Nielsen Norman Group study, 15 of 19 participants (79 percent) always scanned any new page they came across, and only 3 read word by word. NN/g's later eye-tracking studies found the same habit: people scan far more often than they read.

**Why:** The 79 and 16 percent figures are quoted correctly, but they come from a 1997 think-aloud study of 19 people (15 and 3 participants), not from eye tracking. The broader point now has backing from outside NN/g as well: an eye-tracking study of single pages shows skimming is a distinct, faster mode with a comprehension cost, and a survey of screen reading found more browsing, scanning and keyword spotting. Describe the study accurately and the claim stands. Now cites [Moran, How People Read Online: New and Old Findings, NN/g 2020](https://www.nngroup.com/articles/how-people-read-online/).

### The Physiology of Digital Vision: supported with caveats

**Claim reviewed:** High-resolution focus is limited to the fovea, which covers only the central two degrees of vision, roughly the size of a thumbnail held at arm's length.

**Now reads:** This covers only the central two degrees of vision, roughly the width of your thumb held at arm's length.

**Why:** The fovea does cover about 2 degrees, but the cited O'Shea paper says that is the width of a thumb at arm's length. A thumbnail is about 1.5 degrees. A one-word fix.

### The Physiology of Digital Vision: contested

**Claim reviewed:** Peripheral vision is low-resolution and primarily used to detect motion or heavy contrast.

**Now reads:** Everything outside this narrow cone falls into peripheral vision. It sees far less detail, but it does most of the work of taking in a page: it picks up motion and strong contrast, gives users the gist of the layout, and tells the eyes where to jump next.

**Why:** Peripheral vision does have lower resolution, and Rosenholtz notes that motion detection holds up well away from the fovea, so the sentence is not wrong about what the periphery is good at. But 'primarily used to detect motion or heavy contrast' is contradicted by a major review that calls this view a myth, by a systematic review of real-world tasks, by scene-gist experiments and their replication, and by driving research: the periphery gives the gist of a scene, guides where the eyes go next, and can steer a car on its own. Now cites [Rosenholtz, Capabilities and Limitations of Peripheral Vision, Annual Review of Vision Science 2, 2016](https://doi.org/10.1146/annurev-vision-082114-035733).

### The Physiology of Digital Vision: contested

**Claim reviewed:** Banner blindness is driven by this physiological limitation and is a learned cognitive filter: the brain subconsciously identifies ad-like elements (right rail, flashing colors, banner dimensions) and blocks them from conscious awareness before the eye even fixates on them.

**Now reads:** Limited attention drives banner blindness. This is not just a habit. It is a learned filter: once users learn that an area usually holds advertising, such as the right rail, flashing colors, or standard banner sizes, they stop looking there, or glance once and move on without taking it in. Eye-tracking studies disagree on how complete the avoidance is, and it is strongest when users are focused on a task.

**Why:** The 'learned filter' part holds: NN/g says users have learned not to look at the right rail, and lab work shows people learn to suppress locations that usually hold distractors, with fewer eye movements landing there. NN/g's own eye tracking and two older experiments also found users rarely fixate ads, which fits 'before the eye even fixates'. But peer-reviewed eye-tracking studies from 2011 to 2024 find most users glance at ads at least once and ignore them mainly during focused tasks, and nothing links the habit to the fovea. The mechanism is partly right and partly overstated. Now cites [Pernice, Banner Blindness Revisited, NN/g 2018](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/).

### The Physiology of Digital Vision: supported with caveats

**Claim reviewed:** In studies revisiting banner blindness, NN/g confirmed that users ignore these areas even when they contain helpful, non-advertising content.

**Now reads:** When NN/g revisited this phenomenon, it found that users often ignore these areas even when they contain helpful, non-advertising content.

**Why:** NN/g's 2018 study does show users skipping a right rail that held useful craft videos along with ads. The evidence is gaze plots and one heatmap, and other eye-tracking work shows avoidance is partial, so 'found' fits better than 'confirmed'.

### 1. The F-Pattern: supported with caveats

**Claim reviewed:** On dense pages like articles, search results or blog posts, users typically follow an F-shaped pattern: top line, a second shorter line, then the left margin for the rest of the page.

**Now reads:** On dense pages with little formatting, such as long articles or blog posts, users often follow an F-shaped pattern.

**Why:** The three-part F description matches NN/g's 2006 study. NN/g's 2017 follow-up says the F appears mainly when text has little or no web formatting and is not the only pattern, so 'typically' on all dense pages is too broad. Now cites [Pernice, F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant, NN/g 2017](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/).

### 1. The F-Pattern: supported with caveats

**Claim reviewed:** Content placed on the right side of the screen is frequently invisible, and the first two words of a sentence carry the most weight.

**Now reads:** Content on the right side of the screen gets far less attention. It also means the first two words of a line carry the most weight.

**Why:** NN/g data show strong left bias (80 percent of viewing time on the left half) and that users see about the first two words of list items. But 20 percent of viewing time is not 'invisible', and the right-side claim is not in the cited F-pattern article. Now cites [Fessenden, Horizontal Attention Leans Left, NN/g](https://www.nngroup.com/articles/horizontal-attention-leans-left/).

### 2. The Z-Pattern: contested

**Claim reviewed:** On low-density pages with clear hierarchy (landing pages, login screens) the eye moves in a Z-pattern: top-left logo, across to top-right, diagonally through the hero, ending bottom-right on the primary button.

**Now reads:** On low-density pages with a clear visual hierarchy, such as landing pages, designers often arrange content along a Z: logo at top left, navigation or CTA at top right, the hero across the middle, and the primary button at bottom right. One eye-tracking report on landing pages found this diagonal path works when the layout supports it, but eyes still go first to whatever stands out, so treat the Z as a layout convention rather than a fixed gaze path.

**Why:** The cited vendor blog offers no data and concedes that scanning is subjective, and NN/g's eye-tracking catalog has no Z-pattern. But one peer-reviewed eye-tracking report (Hernandez and Resnick 2013, over a hundred sites) found that landing pages built to support the diagonal Gutenberg path, which runs from top left to bottom right like the Z, produced simpler scan paths. That backs the Z as a layout that can work when the page is built for it, not as a path the eye follows on its own: eyes go first to whatever stands out, and 80 percent of fixations land on the left half of pages. Now cites [Hernandez & Resnick, Placement of Call to Action Buttons for Higher Website Conversion and Acquisition, HFES Annual Meeting 2013](https://doi.org/10.1177/1541931213571232).

### 2. The Z-Pattern: contested

**Claim reviewed:** The Z layout is effective because it guides users toward a conversion action at the end of the visual path.

**Now reads:** The logic of this layout is to put the conversion action where the eye is likely to land at the end of its path. One eye-tracking report on landing pages found more fixations and clicks on the main button when the layout supported this diagonal path, but the effect has not been measured in controlled tests, so check it on your own pages.

**Why:** One peer-reviewed eye-tracking report found more fixations and clicks on the Add to Cart button when landing pages supported the diagonal Gutenberg path, which is the best evidence for the Z's conversion logic. But it reports no numbers, mixed eye tracking with qualitative page ratings, and compared existing pages rather than running controlled A/B tests. NN/g's finding that 80 percent of fixations fall on the left half of pages is a reminder that a bottom-right button is not seen by default. Now cites [Hernandez & Resnick, Placement of Call to Action Buttons for Higher Website Conversion and Acquisition, HFES Annual Meeting 2013](https://doi.org/10.1177/1541931213571232).

### 3. The Layer-Cake Pattern: supported with caveats

**Claim reviewed:** The layer-cake pattern is the most efficient scanning method: users fixate only on headings and subheadings and skip body copy entirely until they find a relevant keyword.

**Now reads:** The most effective scanning method is the layer-cake pattern. Here, users fixate mostly on headings and subheadings and dip into the body copy only when a heading looks relevant.

**Why:** NN/g describes the layer-cake pattern as fixations 'mostly' on headings with occasional fixations on body text, not 'only' headings while skipping body copy 'entirely'. NN/g calls it the most effective scanning pattern, but ranks reading nearly everything (the commitment pattern) above it.

### Create Visual Speed Bumps: supported with caveats

**Claim reviewed:** Bullet points, bold text and pull quotes act as speed bumps that force a saccade to stop and become a fixation point.

**Now reads:** Bullet points, bold text, and pull quotes act as speed bumps. They give the scanning eye a reason to stop. Do not overdo them, though: styling that looks too promotional can be mistaken for an ad and skipped.

**Why:** Users in NN/g's 1997 study named bullets, bold text and headings as aids to scanning, so formatting does help. But no source shows formatting 'forces' the eye to stop, and NN/g warns that over-styled elements can look like ads and get skipped. Now cites [Morkes & Nielsen, Concise, SCANNABLE, and Objective, NN/g 1997](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/).

### Utilize Directional Cues: supported with caveats

**Claim reviewed:** Humans are biologically hardwired to follow others' gaze; if a subject in a photo looks at a button, the user's attention naturally follows, and if the subject looks at the user, attention halts at the face.

**Now reads:** People reliably follow the gaze of others. You can use this gaze cueing to direct attention. If a subject in a photo looks at a button, the user's attention tends to follow. If the subject looks at the user, attention tends to stay on the face.

**Why:** Gaze cueing is well established: a 2021 meta-analysis of 423 effects found that others' gaze reliably directs attention, and ad studies show direct gaze holds attention on the face. 'Biologically hardwired' goes further than the evidence, since effects depend on social context, and the cited source is a blog about a single study. Now cites [McKay et al., Psychological Bulletin 147, 2021](https://pubmed.ncbi.nlm.nih.gov/35404635/).

### The "Squint Test" Audit Framework: supported with caveats

**Claim reviewed:** Applying a heavy Gaussian blur simulates peripheral vision processing, and predictive eye-tracking tools offer a data-driven alternative; if the primary action is not identifiable while squinting, users will likely miss it while scanning.

**Now reads:** For a data-driven alternative, teams can try predictive attention tools such as Attention Insight, keeping in mind that their accuracy figures come from the vendors. You can also apply a heavy blur in your design software as a rough stand-in for a first glance. If the primary action is hard to find in the blurred version, it probably does not stand out enough.

**Why:** A heavy blur keeps the low spatial frequencies that the visual system processes first, so a blurred design is a fair stand-in for a first glance and for visual weight. It is not a simulation of peripheral vision, whose main loss is confusion from clutter rather than blur. Research-grade attention models for designs exist and perceptual tools help designers compare options, but the accuracy figures for commercial tools such as Attention Insight come from the vendors, and no study tests whether failing a squint test predicts a missed button. Now cites [Bar et al., Top-down facilitation of visual recognition, PNAS 103(2), 2006](https://doi.org/10.1073/pnas.0507062103).

### Eyetracking Web Usability (book box): supported with caveats

**Claim reviewed:** Nielsen & Pernice's Eyetracking Web Usability (New Riders, 2009, 437 pages) reports NN/g's large eyetracking studies, the research behind the F-pattern and banner blindness.

**Now reads:** The book-length report of Nielsen Norman Group's large eyetracking studies, the research behind the F-pattern and much of what we know about how users look at ads.

**Why:** The book exists as described and reports NN/g's large eyetracking studies, which include the F-pattern work. But banner blindness was described by Benway and Lane in 1998, a decade before the book, so it is not 'the research behind' it. The 437-page count was not verified.

### Case Study: supported with caveats

**Claim reviewed:** In James Breeze's eye-tracking study, a diaper brand tested two landing-page variants: with the baby facing the camera, heatmaps showed hotspots on the face and the headline and copy were largely ignored.

**Now reads:** Usability specialist James Breeze tracked the eyes of 106 people looking at two versions of an ad with a headline and a photo of a baby. When the baby faced the camera, heatmaps showed strong hotspots on the baby's face, and the headline and copy got much less attention.

**Why:** James Breeze did run an eye-tracking study of baby ads with 106 people, and a peer-reviewed study later found the same effect. But the cited write-up describes an ad, not a diaper brand's landing page, names no brand, and says the copy got 'quite a bit less attention', not that it was largely ignored. 'Face Priority' is not the source's term. Now cites [Sajjacholapunt & Ball, Frontiers in Psychology 5, 2014](https://pubmed.ncbi.nlm.nih.gov/24624104/).

### Case Study: supported with caveats

**Claim reviewed:** With the baby in profile looking at the headline, attention followed the baby's line of sight, causing a massive increase in fixations on the headline and copy; this confirms that visual cues can physically direct attention toward conversion elements.

**Now reads:** When the baby was turned in profile and looked at the headline, viewers' attention followed its line of sight, and the headline and copy got far more attention, though the face was still a hotspot. Peer-reviewed studies have since found the same effect: a face looking toward text or a product draws the eye there.

**Why:** The direction is right: when the baby looked at the headline, the copy got more attention, and two peer-reviewed studies found the same. But the write-up reports no statistics, the face stayed a major hotspot, and nobody measured conversions, so 'massive' and 'confirms' about conversion elements go too far. Now cites [Palcu, Sudkamp & Florack, Frontiers in Psychology 8, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5454066/).

### Conclusion: not supported

**Claim reviewed:** Users' vision is biologically prone to ignoring anything that resembles an advertisement.

**Now reads:** Their attention is highly selective, and they quickly learn to ignore anything that looks like an advertisement or takes too much effort to decipher.

**Why:** Every source checked treats ad avoidance as learned, not biological: NN/g says users have learned not to look at the right rail and calls ignoring ads a learned behavior, lab work shows people learn to suppress locations that usually hold distractors, and a 2023 eye-tracking study found avoidance depends on whether users are focused on a task. Eye tracking also shows most users do look at ads at least once. The second half of the sentence, about avoiding high cognitive load, does have support. Now cites [Pernice, Banner Blindness Revisited, NN/g 2018](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/).
