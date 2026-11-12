---
title: "Evidence review: Building Behavioral Design Systems"
---

# Evidence review: Building Behavioral Design Systems

Article: [Building Behavioral Design Systems](https://attck.com/blog/building-behavioral-design-systems/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Components Have Specs. Decisions Rarely Do.

**The GOV.UK Design System tells teams not to pre-select radio options, because a preselected answer makes it more likely that users will miss a question or submit the wrong answer.**

GOV.UK's guidance against preselected radio options matches a large body of default-effect research: a 2019 meta-analysis of 58 studies found that people are more likely to pick whatever option is preselected.

- [Radios, GOV.UK Design System](https://design-system.service.gov.uk/components/radios/): “Do not pre-select radio options as this makes it more likely that users will: not realise they’ve missed a question submit the wrong answer”
- [Jachimowicz et al. (2019), Behavioural Public Policy (Crossref record)](https://api.crossref.org/works/10.1017/bpp.2018.43): “When people make decisions with a pre-selected choice option – a ‘default’ – they are more likely to select that option.”

**Each GOV.UK component page also has a section for research on the component, even when it is mostly a call for findings, and a dated log of changes.**

On the Radios page, the research section mainly invites teams to share what they have learned about conditionally revealed questions; other component pages carry more detail.

### Opening scene

**She doesn't see three teams. She sees one company that says different things depending on where she asks, and she trusts the rest of the product a little less. Research on omnichannel shoppers points the same way: how consistent a company's content and process are across its channels predicts how much customers trust it.**

The opening scene is a composite, not a study. Research outside UX supports its direction: surveys of omnichannel shoppers (868 respondents in one study, 318 in another, 1,547 in a banking study) find that consistent content and process across channels predicts trust in the company, and a 2003 experiment found that customers who experienced dynamic pricing trusted the retailer's good intentions less. Two boundaries are worth knowing: a 2021 experiment with representative US samples found that mild dark patterns, such as a preselected option, did not provoke the backlash that aggressive ones did, and none of the studies tested a three-channel scenario like this one.

- [Lin, Huang & Cheng (2022), 'A binding tie: why do customers stick to omnichannel retailers?', Information Technology & People (Crossref record; survey, n = 868)](https://api.crossref.org/works/10.1108/itp-01-2021-0063): “content consistency, process consistency and perceived fluency all have significant effects on trust.”
- [Garbarino & Lee (2003), 'Dynamic pricing in internet retail: Effects on consumer trust', Psychology & Marketing (Crossref record; experiment)](https://api.crossref.org/works/10.1002/mar.10084): “Results show that mean benevolence trust is significantly lower (which leads to a marginal decrease in overall trust) and the weight given to benevolence trust in the formation of overall trust substantially increases.”
- [Güney & Uslu (2026), 'A Study on the Mediating Role of Brand Trust in the Impact of Omnichannel Integration Quality on Brand Loyalty', Sosyal Mucit Academic Review (Crossref record; survey, n = 318)](https://api.crossref.org/works/10.54733/smar.1808797): “The results show that content consistency, process consistency, and assurance quality have significant positive effects on brand trust, while channel-service configuration does not.”
- [Tran Xuan, Truong & Vo Quang (2023), 'Omnichannel retailing with brand engagement, trust and loyalty in banking', International Journal of Bank Marketing (Crossref record; survey, n = 1,547)](https://api.crossref.org/works/10.1108/ijbm-07-2022-0292): “The findings denote that integration quality, perceived fluency and assurance quality significantly influence brand trust.”

### Finding 1: COM-B gives the diagnosis a vocabulary

**For a design system, the value is the order of operations: name the behavior, diagnose which condition is missing, then choose the pattern. The authors note this still needs testing as a route to more effective interventions, but it guards against an obvious mistake. A team that skips the diagnosis can add persuasive copy to a screen where the real gap was opportunity, because the button sat below the fold all along.**

Michie and colleagues say research is still needed to show the Behaviour Change Wheel produces more effective interventions, and meta-analyses of health interventions have found that theory-based designs are, on average, no more effective than those without a stated theory. Diagnosis-first is a sound working habit, not a proven performance gain.

- [Michie, van Stralen & West (2011), Implementation Science (Europe PMC full text)](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3096582/fullTextXML): “In order to choose the interventions likely to be most effective, it makes sense to start with a model of behaviour.”

**Michie's group later built a taxonomy of 93 behavior change techniques in 16 groups, agreed through expert consensus so that interventions could be reported precisely.**

The 2013 taxonomy has since been extended into the Behaviour Change Technique Ontology, which lists 247 techniques in 20 groups (Marques et al., 2024).

- [Michie et al. (2013), Annals of Behavioral Medicine (Europe PMC record)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23512568%20AND%20SRC:MED&resultType=core&format=json): “This resulted in 93 BCTs clustered into 16 groups.”

### Finding 2: EAST gives patterns a shared language, and a revision history

**A team can learn the four words in an afternoon, which makes them handy top-level categories for a pattern library. BIT itself says EAST is not meant to be comprehensive, so expect a few patterns that fit none of the four.**

BIT describes EAST's simplicity as a strength but says it is not meant to be comprehensive.

- [BIT, EAST revised edition, Preface](https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf): “EAST is a simple, pragmatic framework for practitioners, and that simplicity seems to have been a strength.”

**The 2014 report featured a field experiment suggesting a signature box at the top of an insurance form increased honest reporting; that study failed to replicate and was retracted after evidence of data manipulation emerged.**

The original study (Shu et al., 2012, PNAS) was retracted in 2021. A 2020 PNAS paper with the original authors found no effect of signing first on honest reporting.

- [Kristal et al. (2020), PNAS (Crossref record)](https://api.crossref.org/works/10.1073/pnas.1911695117): “we observed no effect of signing first on honest reporting.”

**BIT's own trials in similar settings had not found the effect either. The team now considers signature placement an unreliable way to increase honesty, while noting that this does not mean honesty prompts never work.**

BIT notes that honesty prompts can still work; a 2023 set of preregistered studies with more than 7,500 people found honesty oaths reduced dishonesty, though by less than earlier studies reported.

### Finding 2 / Do's and Don'ts

**A library that had codified "sign at the top" in 2015 could easily still be shipping it; several government agencies had adopted the practice before the replication failed.**

Kristal and colleagues note that government agencies adopted the sign-first practice after the original paper, and research on retractions shows discredited findings keep being used long after they are withdrawn.

- [Kristal et al. (2020), PNAS (Crossref record)](https://api.crossref.org/works/10.1073/pnas.1911695117): “Since this finding was published, various government agencies have adopted this practice.”
- ['Why retracted articles can have an influential afterlife' (2026), Stem Cells Translational Medicine (Europe PMC record)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1093/stcltm/szag080%22&resultType=core&format=json): “retracted articles can maintain an influential afterlife in the academic literature, online materials from non-profit organizations and private businesses, and responses from generative artificial intelligence.”
- [BIT, EAST revised edition](https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf): “this incident highlights how important replication studies are to ensure that recommendations remain robust.”

### One Pattern Entry, Before and After

**Default: No preselection; both options carry equal weight. The user arrived with a decision, and people tend to stick with whatever is preselected, so a default set against her choice works against her rather than helping.**

A 2019 meta-analysis of 58 studies found that preselected options are chosen more often, though the size of the effect varies widely.

- [Jachimowicz et al. (2019), Behavioural Public Policy (Crossref record)](https://api.crossref.org/works/10.1017/bpp.2018.43): “When people make decisions with a pre-selected choice option – a ‘default’ – they are more likely to select that option.”
- [Radios, GOV.UK Design System](https://design-system.service.gov.uk/components/radios/): “Do not pre-select radio options as this makes it more likely that users will: not realise they’ve missed a question submit the wrong answer”
- [BIT, EAST revised edition](https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf): “Harness the power of defaults. People tend to stick with pre-set options, so choose defaults carefully.”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Components Have Specs. Decisions Rarely Do.: supported with caveats

**Claim reviewed:** Each GOV.UK component page also has a section for research on the component and a dated log of changes.

**Now reads:** Each GOV.UK component page also has a section for research on the component, even when it is mostly a call for findings, and a dated log of changes.

**Why:** The Radios page has both a research section and a dated change log, and a spot-check of seven other GOV.UK component pages found both on every one. The caveat is that the Radios research section is mostly a request for research rather than a summary of findings.

### Opening scene: supported with caveats

**Claim reviewed:** When the same decision is presented inconsistently across channels (preselected in the app, neutral on the web, a surprise deadline by email), the customer trusts the rest of the product less.

**Now reads:** She doesn't see three teams. She sees one company that says different things depending on where she asks, and she trusts the rest of the product a little less. Research on omnichannel shoppers points the same way: how consistent a company's content and process are across its channels predicts how much customers trust it.

**Why:** The scene is uncited, but the direction it implies is backed by research outside UX. Surveys of omnichannel shoppers repeatedly find that consistent content and process across a company's channels predicts how much customers trust it, and a pricing experiment found that treating customers differently lowers trust in the company's good intentions. The caveats: that evidence is mostly survey-based, none of it tests this exact three-channel scenario, and a large experiment found that mild manipulations such as a preselected option do not by themselves provoke a backlash, so the loss of trust depends on the customer noticing the mismatch. Now cites [Lin, Huang & Cheng (2022), A binding tie: why do customers stick to omnichannel retailers?, Information Technology & People, vol. 36, no. 3 (2023)](https://doi.org/10.1108/ITP-01-2021-0063).

### Finding 1: COM-B gives the diagnosis a vocabulary: supported with caveats

**Claim reviewed:** The value of the framework is the order of operations: name the behavior, diagnose which condition is missing, then choose the pattern; a team that skips the diagnosis applies the wrong fix (e.g. persuasive copy where the gap was opportunity).

**Now reads:** For a design system, the value is the order of operations: name the behavior, diagnose which condition is missing, then choose the pattern. The authors note this still needs testing as a route to more effective interventions, but it guards against an obvious mistake. A team that skips the diagnosis can add persuasive copy to a screen where the real gap was opportunity, because the button sat below the fold all along.

**Why:** The paper does argue that choosing interventions should start from a model of behavior, so naming the behavior and diagnosing the gap first is a fair reading. But the authors also say it is untested whether the wheel leads to more effective interventions, and reviews in health psychology find theory-based interventions are, on average, no more effective than others. The article presents the payoff as given.

### Finding 2: EAST gives patterns a shared language, and a revision history: supported with caveats

**Claim reviewed:** The four EAST words can be learned in an afternoon, which is why they work well as the top-level categories of a pattern library.

**Now reads:** A team can learn the four words in an afternoon, which makes them handy top-level categories for a pattern library. BIT itself says EAST is not meant to be comprehensive, so expect a few patterns that fit none of the four.

**Why:** BIT credits EAST's simplicity for its uptake, which supports the 'learn it in an afternoon' point. But BIT also says EAST is not meant to be comprehensive, so using it as the complete set of top-level categories will leave some patterns, such as ones that address a skills or knowledge gap, without an obvious home. Now cites [BIT, EAST: Four Simple Ways to Apply Behavioural Insights (revised edition)](https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf).

### Finding 2: EAST gives patterns a shared language, and a revision history: supported with caveats

**Claim reviewed:** BIT's own trials in similar settings had not found the signature-placement effect, and the team now considers signature placement an unreliable way to increase honesty.

**Now reads:** BIT's own trials in similar settings had not found the effect either. The team now considers signature placement an unreliable way to increase honesty, while noting that this does not mean honesty prompts never work.

**Why:** BIT says its own trials in similar settings did not find the effect and that it now considers signature placement unreliable, which the article reports accurately. BIT adds that this does not mean honesty prompts never work, and a large preregistered study found honesty oaths do reduce cheating somewhat. Readers could take the article to mean honesty prompts in general fail.

### Finding 2 / Do's and Don'ts: supported with caveats

**Claim reviewed:** A pattern codified from a finding can outlive its evidence: a library that had codified 'sign at the top' in 2015 would still be shipping it.

**Now reads:** A library that had codified "sign at the top" in 2015 could easily still be shipping it; several government agencies had adopted the practice before the replication failed.

**Why:** The general point holds: retracted findings keep circulating in research, company materials and AI answers, and government agencies had adopted the sign-first practice before it failed to replicate. 'Would still be shipping it' states a guess as a certainty, though, and the article cites nothing for it. Now cites [Kristal et al. (2020), Signing at the beginning versus at the end does not decrease dishonesty, PNAS](https://doi.org/10.1073/pnas.1911695117).

### Watch: The Science of Behaviour Change: supported with caveats

**Claim reviewed:** In the 2019 Royal Institution panel, Susan Michie introduces the idea that behavior depends on capability, opportunity and motivation, alongside Toby Park of the Behavioural Insights Team and Nick Chater.

**Now reads:** A Royal Institution event in which Susan Michie introduces the idea that behavior depends on capability, opportunity and motivation, with talks from Toby Park of the Behavioural Insights Team and behavioral scientist Nick Chater.

**Why:** The video description confirms a 2019 Royal Institution event with Susan Michie, Toby Park of BIT and Nick Chater. It is a set of talks with a Q&A rather than a single panel, and that Michie introduces COM-B in it was not checked against a transcript, though it is likely given her role.

### One Pattern Entry, Before and After: supported with caveats

**Claim reviewed:** When the user arrived with a decision, a default set against it (e.g. preselecting 'Keep plan') adds friction rather than help.

**Now reads:** Default: No preselection; both options carry equal weight. The user arrived with a decision, and people tend to stick with whatever is preselected, so a default set against her choice works against her rather than helping.

**Why:** The direction is well supported: people tend to stick with whatever is preselected, so a default set against what the customer came to do works against her, and GOV.UK advises against preselection for related reasons. 'Friction' is a loose word for it, since a preselected option steers the choice more than it adds steps, and default effects vary in size. The article cites nothing for the rule. Now cites [Jachimowicz, Duncan, Weber & Johnson (2019), When and why defaults influence decisions: a meta-analysis of default effects, Behavioural Public Policy](https://doi.org/10.1017/bpp.2018.43).
