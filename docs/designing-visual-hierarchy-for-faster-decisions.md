---
title: "Evidence review: Designing Visual Hierarchy for Faster Decisions"
---

# Evidence review: Designing Visual Hierarchy for Faster Decisions

Article: [Designing Visual Hierarchy for Faster Decisions](https://attck.com/blog/designing-visual-hierarchy-for-faster-decisions/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**A shopper reaches the shipping step of checkout. Under the address form sits a small "Save" button, and further down is the button that matters: Continue to Payment.**

Baymard's finding concerns Apply and Save buttons on ordinary checkout fields such as address and payment. It names promo codes and gift cards as the exception, where users are less likely to miss the Apply button.

- [Baymard Institute, Söderlund, Checkout UX: Avoid "Apply" Buttons for Most Fields (2012, updated 2025)](https://baymard.com/blog/checkout-usability-apply-buttons): “In checkout testing, participants often forgot to select the “Apply” button, or confused it with the primary button required to move the checkout process forward.”

**Making the Apply button and the primary button visually distinct did not prevent the confusion.**

Baymard's observation is qualitative; it does not report how many participants were affected.

**Baymard's recommendation for most checkout fields is to drop the Apply button and update the field automatically. Promo codes are the exception: an Apply button can work there, as long as the page confirms the code was accepted.**

Baymard adds that promo and gift card fields can also auto-update, as long as users see a confirmation that the entry worked.

### What Hierarchy Decides

**Someone scanning a product page is not weighing forty elements. They are weighing the few that announced themselves, and choosing among those.**

Salience works in both directions: when people decide quickly, visually prominent options can win over options they actually prefer (Milosavljevic et al. 2012).

- [Influence of Visual Salience on Webpage Product Searches, ACM Transactions on Applied Perception (2019);](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3301413?fields=abstract): “In both cases, participants completed their search more quickly in the high-salience condition.”
- [Wolfe, Guided Search 6.0, Psychonomic Bulletin & Review (2021)](https://europepmc.org/article/MED/33547630): “When we encounter a scene, we can see something everywhere. However, we cannot recognize more than a few items at a time.”

**In 1933 Hedwig von Restorff showed that when one item in a list differs from the others, people remember it better than the rest.**

Von Restorff's result is about memory rather than first glances. Later reviews note she showed the effect does not depend on the odd item being visually striking (Hunt 1995).

- [Hunt, The subtlety of distinctiveness: What von Restorff really did, Psychonomic Bulletin & Review (1995)](https://link.springer.com/article/10.3758/BF03214414): “If all but one item of a list are similar on some dimension, memory for the different item will be enhanced.”

**Distinctiveness is relative: every additional element styled to stand out lowers the standing of the others.**

Visual search experiments show the same thing for attention: an irrelevant item in a unique color slows the search for a different target (Theeuwes 1992).

- [Duncan & Humphreys, Visual search and stimulus similarity, Psychological Review (1989)](https://doi.org/10.1037/0033-295X.96.3.433): “difficulty increases with increased similarity of targets to nontargets and decreasedsimilarity between nontargets, producing a continuum of search efficiency.”
- [Theeuwes, Perceptual selectivity for color and form, Perception & Psychophysics (1992)](https://link.springer.com/article/10.3758/BF03211656): “the presence of an irrelevant item with a unique color interferes with parallel search for a unique form, and vice versa.”

### Size Was Supposed to Win

**In Still's study the properties that best predicted entry points were position, color and text style; size and imagery did not predict them.**

Still's result is about where the eye lands first on web pages and about the properties in Faraday's model. In most other eye-tracking studies, larger elements are looked at sooner and more often (Peschel & Orquin 2013), size is a standard attribute that guides visual search (Wolfe & Horowitz 2017), and a later study of 36 real web pages found size and font size did help predict attention order (Vidyapu et al. 2020). Read Still's finding as size being a weaker and less reliable cue than position and contrast, not as a cue that never works.

- [Still, Web Page Visual Hierarchy: Examining Faraday's Guidelines for Entry Points, Computers in Human Behavior 84 (2018), author Highlights; Wayback Machine copy (2022-02-06) of the ScienceDirect abstract page, which returns 403 live](https://web.archive.org/web/20220206234642/https://www.sciencedirect.com/science/article/abs/pii/S0747563218301195): “Entry points are best predicted by Position, Color, or Text Style.”
- [Still 2018](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.chb.2018.03.014?fields=abstract): “It was found that both spatial position and distinctiveness can predict earlier attention engagement.”
- [Still & Still, Employing a Computational Model to Reveal Stimulus-Driven Influences in Interfaces, HFES Annual Meeting (2024); author PDF on the Psychology of Design lab site](http://www.psychofdesign.com/jeremiah/Still_Still_2024_HFES.pdf): “J. D. Still (2018) showed Faraday's heuristics do a poor job of predicting initial fixations.”
- [Still & Still, Beyond heuristics: predicting user attention with computational salience, Interacting with Computers (2026);](https://api.crossref.org/works/10.1093/iwc/iwag015): “Traditional heuristic approaches, such as visual hierarchy, have demonstrated limited empirical validity.”

**The second is that a large image is not a pointer. In Still's web pages, neither size nor imagery predicted where people looked first. A full-width hero photo can dominate a layout in a screenshot and still do little to lead anyone toward the decision the page exists to support. Size makes an element present. In Still's data, position, color and type style made it a starting point.**

Two web studies of banner blindness found that people often overlook large, distinctive banners while searching a page (Benway 1998; Burke et al. 2005), which fits Still's result that image and size did not predict entry points. In print ads, by contrast, pictures capture attention regardless of their size (Pieters & Wedel 2004), so the point is specific to task-driven use of web pages and says nothing about whether a hero photo helps or hurts the decision itself.

- [Benway, Banner Blindness: The Irony of Attention Grabbing on the World Wide Web, HFES Annual Meeting (1998);](https://api.crossref.org/works/10.1177/154193129804200504): “Web designers attempt to draw attention to important links by making them distinctive. However, when users are asked to find specific items, they often overlook these distinctive banners.”
- [Burke, Hornof, Nilsen & Gorman, High-cost banner blindness, ACM Transactions on Computer-Human Interaction (2005); eye tracking;](https://api.crossref.org/works/10.1145/1121112.1121116): “Eye tracking data reveal people rarely look directly at banners.”
- [Chandon, Hutchinson, Bradlow & Young, Does In-Store Marketing Work?, Journal of Marketing 73(6) (2009); supports the distinction between getting attention and getting action](https://api.crossref.org/works/10.1509/jmkg.73.6.1): “gaining in-store attention is not always sufficient to drive sales”
- [Still, Hicks & Cain, Mobile Interface Attentional Priority Model, SN Computer Science (2020); author PDF on the Psychology of Design lab site](http://www.psychofdesign.com/jeremiah/Still_Hicks_Cain_2020.pdf): “Faraday's visual hierarchy model could not predict fixations in webpages.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: supported with caveats

**Claim reviewed:** Baymard Institute has documented this pattern in checkout testing since 2012: participants often forget to press inline Apply buttons, or confuse them with the primary button.

**Now reads:** A shopper reaches the shipping step of checkout. Under the address form sits a small "Save" button, and further down is the button that matters: Continue to Payment.

**Why:** Baymard does report that test participants forgot to press inline Apply buttons or mistook them for the main button, and has written about it since 2012. But the article's opening scene uses a promo-code Apply button, which is the one case Baymard names as an exception: there, users are less likely to overlook Apply. The finding is real; the example chosen to illustrate it is the case it covers least.

### Introduction: supported with caveats

**Claim reviewed:** Baymard's recommendation is to drop the Apply button and update the field automatically.

**Now reads:** Baymard's recommendation for most checkout fields is to drop the Apply button and update the field automatically. Promo codes are the exception: an Apply button can work there, as long as the page confirms the code was accepted.

**Why:** For ordinary checkout fields, Baymard does recommend removing Apply buttons and updating the field automatically. For promo codes, the field in the article's opening scene, Baymard says an Apply button can make sense and treats auto-updating as an option that needs a visible confirmation. Placed right after the promo-code story, the sentence overstates what Baymard recommends for that case. Now cites [Baymard Institute, Söderlund, Checkout UX: Avoid "Apply" Buttons for Most Fields (2012, updated 2025)](https://baymard.com/blog/checkout-usability-apply-buttons).

### What Hierarchy Decides: supported with caveats

**Claim reviewed:** Hierarchy speeds decisions by narrowing the field: someone scanning a product page weighs only the two or three elements that announced themselves, and choosing from the wrong shortlist or inspecting everything slows people down.

**Now reads:** Someone scanning a product page is not weighing forty elements. They are weighing the few that announced themselves, and choosing among those.

**Why:** The broad idea holds: people can only take in a few items at once, salient items get looked at and found faster, and what people look at shapes what they choose. The specific 'two or three' number has no source, and salience can also steer quick choices toward options people do not actually prefer, so hierarchy speeds decisions only when it points at the right things, which the article does say. Now cites [Influence of Visual Salience on Webpage Product Searches, ACM Transactions on Applied Perception (2019)](https://doi.org/10.1145/3301413).

### Size Was Supposed to Win: supported with caveats

**Claim reviewed:** Still reported that the model had a strong, inappropriate bias toward size.

**Now reads:** Still found that the model leaned mainly on element size to pick entry points.

**Why:** The substance is right: Still's abstract says the model picked entry points mainly on element size alone. The exact phrase 'strong, inappropriate bias toward size' appears to come from the paper's highlights, which are behind a blocked publisher page and could not be checked word for word.

### Size Was Supposed to Win: contested

**Claim reviewed:** Moving an element up, giving it the only accent color on the screen, or changing its type weight will usually do more than making it larger.

**Now reads:** The first is that the tools teams treat as minor often do the most work. In Still's data, where an element sat and whether it stood out through color or type style predicted first fixations, and size did not. Other eye-tracking research finds that size does draw the eye, so treat position, a single accent color and type weight as the first tools to reach for, and size as one to add rather than one to count on alone.

**Why:** Still's Highlights give this rule more backing than pass 4 assumed: on his web pages, position, color and text style predicted where people looked first and size did not. But the article states the rule for all screens, and the wider evidence points the other way. A review of eye-tracking studies finds larger objects are looked at sooner and more often, size is a standard attribute that guides visual search, a large item captures attention in lab tasks, and a study of 36 real web pages found size and font size did predict attention order. NN/g, which the article cites, tells designers to make the most important element biggest. The defensible version is that position and contrast are the more reliable first tools, not that they usually beat size. Now cites [Peschel & Orquin, A review of the findings and theories on surface size effects on visual attention, Frontiers in Psychology (2013)](https://doi.org/10.3389/fpsyg.2013.00902).

### Size Was Supposed to Win: supported with caveats

**Claim reviewed:** A large image is not a pointer: a full-width hero photo can dominate a layout and still fail to lead anyone toward the decision; size makes an element present, while position, color and type make it a starting point.

**Now reads:** The second is that a large image is not a pointer. In Still's web pages, neither size nor imagery predicted where people looked first. A full-width hero photo can dominate a layout in a screenshot and still do little to lead anyone toward the decision the page exists to support. Size makes an element present. In Still's data, position, color and type style made it a starting point.

**Why:** The archived Highlights say entry points were not predicted by size or image, which is the finding the article draws on, and two web studies of banner blindness found that people often overlook large, distinctive graphics while using a page. So 'a large image is not a pointer' has real support for web pages. The caveats: no study tests full-width hero photos and whether visitors reach the decision, and in print ads pictures capture attention regardless of size while larger objects are fixated sooner in most eye-tracking studies. 'Size makes an element present' is the article's framing and reads best tied to Still's web-page data rather than stated as a general rule. Now cites [Benway, Banner Blindness: The Irony of Attention Grabbing on the World Wide Web, Proceedings of the Human Factors and Ergonomics Society Annual Meeting 42(5) (1998)](https://doi.org/10.1177/154193129804200504).

### A Product Page With Too Many Firsts: unverified

**Claim reviewed:** Delivery estimate, returns policy and rating with review count should sit physically close to the buy button, because these answer the questions that stall a purchase.

**Now reads:** Set smaller and quieter, but physically close to the button, since these are the details shoppers commonly check before they commit.

**Why:** The advice to keep delivery, returns and rating details next to the buy button is plausible and common in practice, but the article gives no source and the review found no direct test of it. Eye-tracking shows people look longer at the options they end up choosing, which is related but does not test placement.

### A Product Page With Too Many Firsts: supported with caveats

**Claim reviewed:** Styling express-pay as loudly as Add to Cart recreates the conditions of the Apply problem: two buttons that both look like the next step, forcing the shopper to stop and work out the difference.

**Now reads:** Styled as loudly as Add to Cart, it recreates part of the Apply problem: two buttons that both look like the next step, and a shopper who has to stop and work out the difference.

**Why:** Baymard documents a shopper hesitating between two competing primary buttons, and sites with one primary action per step had fewer problems, so the hesitation part of the analogy holds. The stakes differ, though: express pay and Add to Cart both lead to a purchase, so picking the 'wrong' one does not lose data the way skipping Apply does.

### Putting It to Work / Conclusion: supported with caveats

**Claim reviewed:** Emphasis behaves like a fixed budget: every element promoted to the top level takes attention from the elements already there, so more than two level-1 elements means a screen is over budget.

**Now reads:** As a working rule, more than two elements at level 1 means you are over budget.

**Why:** The idea that emphasis is a shared, limited budget is well supported: extra eye-catching items compete with the intended one, and animated items draw attention away from static ones on the same page. The 'more than two at level 1' cutoff has no source; it is a reasonable house rule, close to NN/g's advice to keep big elements to two at most, but should be presented as one. Now cites [Nielsen Norman Group, Gordon, Visual Hierarchy in UX: Definition (2021)](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/).

### Conclusion: supported with caveats

**Claim reviewed:** Within moments of landing on a screen, users have formed a feeling about it, and that feeling colors every decision that follows.

**Now reads:** Within moments of landing on a screen, users have formed a feeling about it, and that feeling can shape the decisions that follow.

**Why:** People do judge a web page's visual appeal within about 50 milliseconds, which supports 'within moments'. That this first feeling 'colors every decision that follows' goes beyond that study, and the review found no direct evidence for so broad a carry-over. Now cites [Lindgaard et al., Behaviour & Information Technology (2006)](https://doi.org/10.1080/01449290500330448).
