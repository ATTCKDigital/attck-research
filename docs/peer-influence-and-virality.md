---
title: "Evidence review: Peer Influence and Virality"
---

# Evidence review: Peer Influence and Virality

Article: [Peer Influence and Virality](https://attck.com/blog/peer-influence-and-virality/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Influence Travels Along the Product

**Peer influence is hard to measure because friends tend to be alike: when two friends both adopt something, it may be influence or shared tastes.**

The friends-are-alike problem is documented directly by Aral, Muchnik and Sundararajan (2009), which Aral and Walker cite for it.

- [Aral & Walker, Management Science 57(9), 2011](https://www.sinanaral.io/s/creating-social-contagion-through-viral-product-design.pdf): “Unfortunately, evaluating the effects of viral product design features is difficult because peer effects and WOM are typically endogenous”
- [Aral, Muchnik & Sundararajan, PNAS 106(51), 2009](https://doi.org/10.1073/pnas.0908800106): “homophily explains >50% of the perceived behavioral contagion”

**One of the most reliable ways to separate the two is to randomize what the product lets people share.**

Randomizing product features is one of several experimental designs for peer effects; peer encouragement designs (Eckles, Kizilcec and Bakshy, 2016) are another.

### The Facebook Movie App Trial

**In this trial, the bigger lever was whether everyday use was visible to the people around the user at all. Whether that holds for your product depends on how often people would bother to invite, and on what the product gives them a reason to send.**

A panel study of iOS apps (Information Systems Research, 2022) found that adding social sharing features raised demand only for niche apps; a 2026 field experiment found reward design changes how many referrals people send.

- [Aral & Walker, Management Science 57(9), 2011](https://www.sinanaral.io/s/creating-social-contagion-through-viral-product-design.pdf): “passive-broadcast messaging is used more often, generating more total peer adoption in the network”

**The other limit is scale. A study of a billion diffusion events on Twitter found that most spread is shallow: about 99 percent of adoptions came from the original poster or that account's direct followers, and popularity was largely driven by the size of the largest single broadcast. Long chains of person-to-person sharing did happen, but they were the exception.**

A 2024 study of about a billion reshared Facebook posts found ordinary content spread mainly one-to-many, while misinformation sometimes reached millions through long peer-to-peer chains.

- [Goel, Anderson, Hofman & Watts, Management Science 62(1), 2016](https://5harad.com/papers/twiral.pdf): “we find that structural virality is typically low, and remains so independent of size, suggesting that popularity is largely driven by the size of the largest broadcast”
- [The Diffusion and Reach of (Mis)Information on Facebook during the U.S. 2020 Election, Sociological Science 11, 2024](https://doi.org/10.15195/v11.a41): “non-misinformation spread primarily through one-to-many affordances (mainly, Pages)”

### Three Share Moments, Before and After

**In an analysis of three months of New York Times articles, Jonah Berger and Katherine Milkman found that positive content was more likely to make the paper's most e-mailed list than negative content, that content evoking high-arousal emotions such as awe, anger or anxiety did better, and that low-arousal sadness did worse. Later studies on other platforms agree that emotion matters but differ on which emotions help.**

A 2025 study of 387,000 WeChat articles found anxiety, love and surprise spread farther while anger and sadness dampened spread, so the role of anger varies by platform.

- [Berger & Milkman, Journal of Marketing Research 49(2), 2012](https://jonahberger.com/wp-content/uploads/2013/02/ViralityB.pdf): “Content that evokes high-arousal positive (awe) or negative (anger or anxiety) emotions is more viral.”
- [Brady, Wills, Jost, Tucker & Van Bavel, PNAS 114(28), 2017](https://doi.org/10.1073/pnas.1618923114): “the presence of moral-emotional words in messages increased their diffusion by a factor of 20% for each additional word”
- [Akpinar & Berger, Journal of Marketing Research 54(2), 2017](https://doi.org/10.1509/jmr.13.0350): “emotional appeals (which use drama, mood, music, and other emotion-eliciting strategies) are more likely to be shared”

**Useful, interesting or surprising articles were more likely to be e-mailed too, though what people pass on depends on the channel.**

For video ads on general social platforms, information-focused content was shared less (Tellis and colleagues, 2019).

- [Kim, Journal of Communication 65(3), 2015](https://doi.org/10.1111/jcom.12160): “Informational utility and novelty had stronger positive associations with e-mail-specific virality, whereas emotional evocativeness, content familiarity, and exemplification played a larger role in triggering social media-based retransmissions.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Influence Travels Along the Product: supported with caveats

**Claim reviewed:** The cleanest way to separate influence from similarity is to randomize what the product lets people share.

**Now reads:** One of the most reliable ways to separate the two is to randomize what the product lets people share.

**Why:** The source calls randomized trials 'one of the most effective ways' to measure peer effects, not the cleanest. Other randomized designs exist, such as randomly nudging a person's friends instead of switching product features. The point stands, but the superlative goes past the source.

### The Facebook Movie App Trial: supported with caveats

**Claim reviewed:** Per message, invitations were roughly three times more effective at bringing in a new user.

**Now reads:** Invitations converted at about 10 percent, notifications at about 1 percent. Once the authors accounted for who sent and received each message, invitations were still roughly three times more effective per message at bringing in a new user.

**Why:** The paper does say invitations were about three times more effective per message. But the article puts this right after the 10 percent versus 1 percent conversion rates, which imply a tenfold gap. The threefold figure is after the authors' statistical controls, and readers need that to see why the numbers differ.

### The Facebook Movie App Trial: supported with caveats

**Claim reviewed:** The trial suggests the bigger lever is whether everyday use is visible to the people around the user at all, rather than the invite screen.

**Now reads:** In this trial, the bigger lever was whether everyday use was visible to the people around the user at all. Whether that holds for your product depends on how often people would bother to invite, and on what the product gives them a reason to send.

**Why:** In this trial, automatic notices did more total work than invitations, and the article hedges with 'the trial suggests'. But it was one Facebook app around 2009, the authors say rewards could raise invitation use, and a later study of iOS apps found social sharing features raised demand only for niche apps. Calling visibility the bigger lever for products in general goes past the evidence. Now cites [Design for Social Sharing: The Case of Mobile Apps, Information Systems Research (2022)](https://doi.org/10.1287/isre.2022.1151).

### The Facebook Movie App Trial: supported with caveats

**Claim reviewed:** A study of a billion diffusion events on Twitter found that most spread is shallow: popularity was largely driven by the size of the largest single broadcast, not by long chains of person-to-person sharing.

**Now reads:** The other limit is scale. A study of a billion diffusion events on Twitter found that most spread is shallow: about 99 percent of adoptions came from the original poster or that account's direct followers, and popularity was largely driven by the size of the largest single broadcast. Long chains of person-to-person sharing did happen, but they were the exception.

**Why:** The study did analyze about a billion diffusion events on Twitter and found most spread is shallow and driven by the largest broadcast. But its headline finding is that popular items grow in very different ways, sometimes through long chains of sharing. 'Broadcast' there means one account with many followers, not a product's automatic notices.

### The Facebook Movie App Trial: supported with caveats

**Claim reviewed:** Peer features raise adoption among the people near your users but rarely turn a product into an epidemic on their own.

**Now reads:** Peer features raise adoption among the people near your users. On their own, they rarely turn a product into an epidemic, and the trial's authors note that viral features still depend on advertising to build a first base of users.

**Why:** This is the article's own conclusion from and, not something either paper tested. The evidence leans its way: Goel and colleagues find almost all spread is one step from the source, and Aral and Walker say viral features still need advertising to build a starting user base. A 2025 country-scale experiment adds that adoption often needs signals from several friends, which fits 'rarely' but is not a direct test.

### Three Share Moments, Before and After: supported with caveats

**Claim reviewed:** In an analysis of three months of New York Times articles, Berger and Milkman found that content evoking high-arousal emotions such as awe, anger or anxiety was shared more, and low-arousal sadness less.

**Now reads:** In an analysis of three months of New York Times articles, Jonah Berger and Katherine Milkman found that positive content was more likely to make the paper's most e-mailed list than negative content, that content evoking high-arousal emotions such as awe, anger or anxiety did better, and that low-arousal sadness did worse. Later studies on other platforms agree that emotion matters but differ on which emotions help.

**Why:** The paper says exactly this, based on the New York Times most e-mailed list in 2008. Later studies on other platforms agree that emotion drives sharing, but disagree on specific emotions: a 2025 study of 387,000 WeChat articles found anger and sadness both dampened spread. The article also leaves out the paper's first finding, that positive content was more viral than negative. Now cites [Emotions in Online Content Diffusion, Information Systems Research (2025)](https://doi.org/10.1287/isre.2022.0611).

### Three Share Moments, Before and After: supported with caveats

**Claim reviewed:** Useful, interesting or surprising content was shared more too.

**Now reads:** Useful, interesting or surprising articles were more likely to be e-mailed too, though what people pass on depends on the channel.

**Why:** The paper found useful, interesting and surprising content more likely to be e-mailed, though these were control variables rather than its main test. Other research shows the channel matters: useful news drives e-mail sharing, while for video ads on social platforms information-focused content was shared less.

### Building Products People Pass On: supported with caveats

**Claim reviewed:** Personal invites convert best, so ask for invitations where someone has something worth recommending, after value.

**Now reads:** Ask for invitations after value. Personal invites convert best per message, so place them where someone has something worth recommending, and test whether a small reward raises how often people send them.

**Why:** The per-message advantage of invitations is in the source. The advice to ask 'after value' is reasonable and fits referral research showing sender effort signals quality, but the trial did not test timing; its authors suggested rewards as the fix for low invitation use.

### Building Products People Pass On: unverified

**Claim reviewed:** Automatic posts the user never agreed to spend their reputation and your trust; invite walls produce messages nobody meant to send.

**Now reads:** Invite walls. Gating signup behind invitations can raise invitation counts while leaving users less engaged.

**Why:** This advice has no citation. A randomized experiment on a dating platform found that requiring more referrals produced more invitations but less engaged users, which partly backs the invite-wall point. No study was found that directly tests whether silent automatic posts cost the sender's reputation or trust. Now cites [Belo & Li, Social Referral Programs for Freemium Platforms, Management Science (2022)](https://doi.org/10.1287/mnsc.2022.4301).
