---
title: "Evidence review: Mental Models and Misalignment: Why Users Reject Unfamiliar Designs"
---

# Evidence review: Mental Models and Misalignment: Why Users Reject Unfamiliar Designs

Article: [Mental Models and Misalignment: Why Users Reject Unfamiliar Designs](https://attck.com/blog/mental-models-and-misalignment-why-users-reject-unfamiliar-designs/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

A survey of 516 web users found shared, stable expectations about where many common web objects belong (Roth et al. 2010), though not for every object.

- [Chan, Mental Models and User Experience Design (NN/g, 2024)](https://www.nngroup.com/articles/mental-models/): “Thus, a big part of customers' mental models of your site will be influenced by information gleaned from other sites.”
- [Roth, Schmutz, Pauwels, Bargas-Avila & Opwis, Mental models for web objects, Interacting with Computers 22(2) (2010)](https://doi.org/10.1016/j.intcom.2009.10.004): “Users generally agree about the locations of many, but not all, web objects. These mental models are robust to demographic factors like gender and web expertise.”

Familiar designs do better on two measured fronts: inconsistent command syntax across applications cost users extra actions in a controlled study (Satzinger & Olfman 1998), and in a study of first impressions, websites that broke the usual layout were judged less attractive (Tuch et al. 2012). Whether broken expectations make people leave has not been measured directly, and consumer research shows that a moderate surprise can also make a product more appealing.

- [Satzinger & Olfman, User Interface Consistency across End-User Applications: The Effects on Mental Models, JMIS 14(4) (1998); publisher page returns 403, quote matched against the OpenAlex record of the DOI](https://doi.org/10.1080/07421222.1998.11518190): “As hypothesized, inconsistent action language syntax across applications resulted in more user actions to complete tasks.”
- [Google Research blog summarizing Tuch, Presslaber, Stoecklin, Opwis & Bargas-Avila (2012), Users love simple and familiar designs](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/): “Designs that contradict what users typically expect of a website may hurt users’ first impression and damage their expectations.”
- [Do users hate redesign? A literature review on user resistance to interface changes, Revista Economica (2021); Crossref record](https://doi.org/10.56043/reveco-2021-0005): “Redesigning interfaces that individuals are used to implies unlearning the navigation routine and learning a new one, leading to cognitive load.”
- [Baymard Institute, Cart abandonment rate statistics (reasons for abandonment survey)](https://baymard.com/lists/cart-abandonment-rate): “17% of US online shoppers have abandoned an order due to a “too long / complicated checkout process””

### The Psychology of Expectation (Jakob's Law)

Product-design research adds a nuance: people prefer new designs as long as the novelty does not cost typicality (Hekkert et al. 2003, the 'most advanced, yet acceptable' principle).

- [Nielsen, End of Web Design (NN/g, 2000)](https://www.nngroup.com/articles/end-of-web-design/): “This means that users prefer your site to work the same way as all the other sites they already know.”

### Information Architecture (IA) Mismatches

The relaunch also moved M&S off an Amazon-run platform and forced every customer to re-register (Guardian; City A.M.).

- [Wood, Shareholders attack Marks & Spencer as website revamp loses customers (The Guardian, 2014)](https://www.theguardian.com/business/2014/jul/08/marks-and-spencer-shareholders-attack-website-online-sales-fall): “M&S said online sales had fallen 8% in the past three months as customers were unable to navigate through the glossy-magazine-style articles and videos to make purchases.”

The re-registration requirement (half of six million shoppers had not signed up again) is a second likely cause of the drop.


### Case Study: Snapchat's 2018 Redesign

By Q2 2019 daily users had recovered to 203 million with the friends/publishers split still in place (Snap Q2 2019 earnings release).

- [Clover, MacRumors (2018)](https://www.macrumors.com/2018/08/07/snapchat-redesign-millions-of-lost-users/): “Snap said it had 188 million daily active Snapchat users during the second quarter of 2018, down from 191 million during the first quarter of the year.”

A year later Snapchat had 203 million daily users, above its pre-redesign level, with friends and publishers still separated (Snap Q2 2019 earnings release).


## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: supported with caveats

**Claim reviewed:** No user arrives with an empty mind; users bring an 'invisible manual' written by thousands of hours on other websites, apps and software, and these internal templates are called mental models.

**Now reads:** In reality, no user arrives with an empty mind. They bring expectations learned on other websites, apps, and software.

**Why:** The cited NN/g article says much of a user's mental model of a site comes from other sites, and a large online study found users share stable expectations about where common web objects sit. The 'thousands of hours' figure is rhetorical, and the same study found agreement covers many objects but not all.

### Introduction: supported with caveats

**Claim reviewed:** When a design breaks users' mental models it forces them to switch from automatic processing to conscious problem-solving, which creates cognitive friction that often leads to abandonment.

**Now reads:** However, when a design breaks these models, even for the sake of "innovation," it forces the user to stop and work out what to do. That extra effort slows people down, sours first impressions, and can lead some of them to give up.

**Why:** Breaking what users expect does measurably cost them: inconsistent ways of operating software add extra steps in the lab, designs that look unfamiliar hurt first impressions in Google's large-sample study, and a 2021 review describes relearning a changed interface as a cognitive load. But 'often leading to abandonment' is still an inference. Nobody has measured how often broken expectations end a session, consumer research finds that moderate novelty can make people like a product more, and the only abandonment numbers available are self-reported checkout surveys, not mental-model studies. Now cites [Google Research, Users love simple and familiar designs (summary of Tuch et al. 2012)](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/).

### The Psychology of Expectation (Jakob's Law): supported with caveats

**Claim reviewed:** Jakob's Law, coined by Jakob Nielsen, states 'a simple mathematical truth': users spend most of their time on other sites, so they prefer your site to work the same way as all the other sites they already know.

**Now reads:** The governing principle of this behavior is Jakob's Law, coined by usability expert Jakob Nielsen. It starts from a plain observation: users spend most of their time on other sites.

**Why:** Jakob's Law is correctly attributed to Nielsen and the cited 2000 article states it in these words. Calling it 'a simple mathematical truth' overstates it: Nielsen offers an observation about how people spend their time, not a proof.

### The Psychology of Expectation (Jakob's Law): supported with caveats

**Claim reviewed:** This preference is rooted in Schema Theory, which explains how the brain organizes knowledge into scripts to save energy.

**Now reads:** This is rooted in schema theory, which describes how people organize knowledge into familiar patterns and scripts so they can handle routine situations with less mental effort.

**Why:** Schema theory is real and well established, and experiments show that leaning on stored category knowledge frees up mental resources. But the article cites nothing, and 'save energy' is a metaphor for saving limited attention, not literal energy. Now cites [Macrae, Milne & Bodenhausen, Stereotypes as energy-saving devices, JPSP (1994)](https://doi.org/10.1037/0022-3514.66.1.37).

### The Psychology of Expectation (Jakob's Law): supported with caveats

**Claim reviewed:** Users expect a top-left logo to be a home button; moving the logo to the center and making it non-clickable breaks this schema and causes a micro-moment of frustration that degrades trust.

**Now reads:** If a designer moves that logo to the center, the schema breaks. In one usability study, people were six times as likely to fail to reach the homepage in a single click when the logo was centered.

**Why:** An NN/g usability study found people were about six times as likely to fail to reach the homepage in one click when the logo was centered, so the navigation half is well supported. The 'degrades trust' half has no evidence; nobody measured trust. Now cites [Whitenton, Centered Logos Hurt Website Navigation (NN/g, 2016)](https://www.nngroup.com/articles/centered-logos/).

### How Misalignment Shows Up: misattributed

**Claim reviewed:** Misalignment occurs when the 'System Model' (how the database or org chart is structured) clashes with the 'User Model' (how people perceive the task).

**Now reads:** Misalignment occurs when the way a system is built, which often mirrors the database or the org chart, clashes with the way people think about the task. Don Norman describes this as the gap between the designer's model and the user's model; Alan Cooper calls the first the "implementation model."

**Why:** The gap between how designers and users understand a product is Norman's idea, and the cited book is where he explains it. But his terms are the designer's (or design) model, the user's model and the system image, and his point is that the designer can only reach the user through the system image. A 'System Model' defined as how the database or org chart is structured is Alan Cooper's 'implementation model', which Cooper coined in his own books. The article cites Norman for Cooper's framing. Now cites [Cooper, The Inmates Are Running the Asylum (Sams, 1999)](https://www.oreilly.com/library/view/inmates-are-running/0672326140/).

### Information Architecture (IA) Mismatches: supported with caveats

**Claim reviewed:** In its 2014 website redesign, Marks & Spencer shifted from standard catalog navigation (Mens, Womens, Home) to a 'lifestyle' editorial magazine structure focused on trends.

**Now reads:** A widely reported example came in 2014, when Marks & Spencer replaced its Amazon-run website with its own platform, which mixed shopping with magazine-style articles and videos.

**Why:** The Guardian confirms the 2014 M&S site featured glossy, magazine-style articles and videos. It says nothing about the old site using a 'Mens, Womens, Home' catalog or about a switch to a trend-based structure, and it reports a bigger change the article leaves out: M&S moved off a site that had been run by Amazon.

### Information Architecture (IA) Mismatches: not supported

**Claim reviewed:** The M&S redesign violated the mental model of a department-store shopper who wanted to filter by size and price.

**Now reads:** Shoppers complained that the new site was hard to navigate and that the editorial content got in the way of buying. Many had come to shop, not to read.

**Why:** The cited Guardian piece says nothing about size or price filters. The complaints it records are that the site was tricky to use and that customers had to re-register. Reviews published at the launch show the new site did have faceted filtering, and one usability consultancy said it tested well. M&S's own chief executive blamed the editorial content for getting in the way of buying. So the article's filtering diagnosis is not just unsourced; it points the wrong way. Now cites [Diginomica, When will Marks and Spencer's approach to digital retail get some magic and sparkle? (2014)](https://diginomica.com/marks-spencers-approach-digital-retail-magic-sparkle).

### Information Architecture (IA) Mismatches: supported with caveats

**Claim reviewed:** M&S online sales fell 8 percent in the three months that followed, as customers struggled to find their way through the magazine-style pages to make a purchase.

**Now reads:** Online sales fell 8 percent in the following quarter. M&S blamed customers' difficulty navigating the magazine-style pages, though only about half of its online shoppers had re-registered on the new site.

**Why:** The 8 percent drop and the company's own explanation, that customers could not navigate the magazine-style pages, are in the cited Guardian article. The same article reports a large confound: about half of six million customers had not re-registered after the move off Amazon's platform, and M&S called it an expected settling-in period. The site launched in February, so the three months reported were not quite 'the three months that followed.'

### Icon Ambiguity: not supported

**Claim reviewed:** A 'Heart' icon is universally understood as 'Like' or 'Favorite'.

**Now reads:** Only a handful of icons, such as home, print, and the magnifying glass for search, are recognized almost everywhere. Even a heart is ambiguous: one site uses it for "Like," another for "Save."

**Why:** The best-known icon research names the heart as one of the icons users frequently misunderstand, because sites use it for favorites, bookmarks, featured items or ratings. Only home, print and the search magnifier come close to universal recognition. Research on icon identification does show that familiarity makes a heavily used icon easy to recognize, which is why people know a heart means something positive, but that does not settle what it does on a given site. Now cites [Harley, Icon Usability (NN/g, 2014)](https://www.nngroup.com/articles/icon-usability/).

### Icon Ambiguity: supported with caveats

**Claim reviewed:** Across Android and iOS the Share icon has shifted shapes (an arrow popping out of a box vs three connected dots), causing measurable confusion.

**Now reads:** Android and iOS use different "Share" icons (three connected dots vs. an arrow rising out of a box), and in one informal survey fewer than 40 percent of respondents knew what the Android icon meant.

**Why:** Android and iOS do use different share icons, and an informal survey found that well under half of respondents recognized either one, so 'confusion' has some data behind it. 'Measurable' oversells an uncited blog survey, and no one measured confusion caused by the shapes changing over time. Now cites [Bursztein, Choose the right sharing icon to boost user engagement](https://elie.net/blog/web/choose-the-right-sharing-icon-to-boost-user-engagement).

### Use External Consistency: supported with caveats

**Claim reviewed:** Deviating from the learned checkout script, for example by asking for billing information before shipping details, will likely trigger validation errors and drop-offs.

**Now reads:** Users have already learned this script. Deviating from it adds friction: checkout research finds that making shoppers fill in both a billing and a shipping address form by default creates extra work and errors, both of which lead to abandonment.

**Why:** The general point now has support: Baymard's checkout research finds that showing both a billing and a shipping address form by default creates extra work and errors that lead to abandonment, its guidance ties re-typing after validation errors to abandonment, and a literature-based form-design guideline says to keep questions in a sequence users expect. What remains unsupported is the specific example: no study was found showing that asking for billing before shipping triggers validation errors. Now cites [Baymard Institute, Guideline 566: Shipping Address and Billing Address](https://baymard.com/guidelines/566-shipping-address-and-billing-address).

### Card Sorting for Navigation: not supported

**Claim reviewed:** If navigation labels match users' card-sort grouping (e.g., 80 percent grouping 'Mortgages' under 'Buying a Home'), the cognitive load required to find the content drops to near zero.

**Now reads:** For example, if you are a bank, you might think "Mortgages" belongs under "Products." A card sort might show that most of your users put it under "Buying a Home." Labels that match the user's grouping make content easier to find, though a card sort alone predicts only part of what users will struggle with, so confirm the structure with a tree test.

**Why:** Matching labels to users' vocabulary does help: menu research shows browsing improves with information scent, and NN/g recommends card sorting to discover groupings. But 'near zero' cognitive load is not what the evidence shows. In a combined study, how hard items were to sort predicted only about 16 percent of how hard they were to find, and information architecture research notes that different users and different goals produce different groupings. The 80 percent figure is an invented example and should read as one. Now cites [Sauro, Card Sorting + Tree Testing: The Science of Great Site Navigation (MeasuringU)](https://measuringu.com/cardsort-tree-test/).

### Case Study: Snapchat's 2018 Redesign: supported with caveats

**Claim reviewed:** In an effort to drive ad revenue, Snap rolled out a major update that separated 'Social' content (chats with friends) from 'Media' content (stories from publishers and celebrities) into two different screens.

**Now reads:** The Scenario: Partly to drive ad revenue and attract new users, Snap Inc. rolled out a major update that changed the app's architecture.

**Why:** The BBC confirms Snap made the change partly to sell more ads and that it separated friends' content from publishers'. The BBC also says it was meant to attract new users, and Snap's own announcement framed it around separating the social from the media, so ad revenue was one motive among several.

### Case Study: Snapchat's 2018 Redesign: not supported

**Claim reviewed:** Before the redesign, Snapchat users had a single chronological feed for all communications.

**Now reads:** Previously, chats sat on one side of the camera and Stories on the other, where friends' Stories appeared in reverse chronological order mixed in with publisher content. The redesign moved friends' chats and Stories to one screen, sorted by an algorithm, and publishers and celebrities to another.

**Why:** Before the redesign Snapchat already had two screens either side of the camera: chats on the left, sorted by how recently you talked, and Stories on the right, where friends' Stories ran in reverse chronological order mixed with publishers' Discover content. Four reports from launch day and Snap's own announcement describe it this way. The article is right that the old app was chronological and mixed friends with media, but wrong that there was a single feed for all communications. Now cites [Constine, TechCrunch, Snapchat's redesign (2017)](https://techcrunch.com/2017/11/29/snapchat-redesign/).

### Case Study: Snapchat's 2018 Redesign: supported with caveats

**Claim reviewed:** The next quarter daily active users fell 2 percent, from 191 million to 188 million, a drop Snap's CEO attributed to 'the disruption caused by our redesign.'

**Now reads:** The next quarter, daily active users fell 2 percent, from 191 million to 188 million, even as monthly users grew. Snap's CEO said the drop was primarily driven by "the disruption caused by our redesign."

**Why:** The numbers and the quoted phrase are accurate. The article drops two details from the CEO's statement: the decline was 'primarily' driven by people using the app slightly less often, and monthly users kept growing.

### Case Study: Snapchat's 2018 Redesign: supported with caveats

**Claim reviewed:** Snap was eventually forced to roll back key aspects of the design to realign with user expectations.

**Now reads:** Snap later rolled back some of the changes, restoring time order for chats and moving friends' Stories back, while keeping friends and publishers on separate screens.

**Why:** Snap did reverse some changes, restoring time order for chats and moving friends' Stories back, as the article's own source reports. But it kept the core separation of friends from publishers, so 'forced to roll back key aspects' overstates a partial rollback, and daily users later recovered with the new structure intact. Now cites [Clover, MacRumors (2018)](https://www.macrumors.com/2018/08/07/snapchat-redesign-millions-of-lost-users/).
