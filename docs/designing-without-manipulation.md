---
title: "Evidence review: Designing Without Manipulation"
---

# Evidence review: Designing Without Manipulation

Article: [Designing Without Manipulation](https://attck.com/blog/designing-without-manipulation/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**In 2020 a team of software engineering researchers examined 240 popular mobile apps and found at least one interface built to trick people in 95% of them; on average each app used at least seven different types.**

A 2024 sweep by 27 consumer-protection authorities found dark patterns on about three quarters of 642 subscription sites and apps, a lower rate than 95% but the same picture.

- [Di Geronimo et al., CHI 2020](https://doi.org/10.1145/3313831.3376600): “95% of the analyzed apps contain one or more forms of Dark Patterns”
- [ICPEN, Sweep finds majority of websites and mobile apps use dark patterns, 2024](https://icpen.org/news/1360): “has found that 75,7% of them employed at least one dark pattern, and 66,8% of them employed two or more dark patterns”

**When shown app screens, most of 589 people did not recognize the tricks, though they did better once the issue had been explained.**

A 2026 experiment found that labeling dark patterns improved people's ability to recognize them in a task, consistent with the 'did better once explained' finding.

**When another team surveyed 406 people a year later, respondents were generally aware that manipulative designs influence them, but by their own account that general awareness did not make them less likely to be swayed.**

The survey separates general awareness, which made no difference to self-reported influence, from the ability to recognize specific patterns, which was linked to lower self-reported influence.

- [Bongard-Blanchy et al., DIS 2021 (arXiv preprint)](https://arxiv.org/abs/2104.12653): “we found that they are generally aware of the influence that manipulative designs can exert on their online behaviour. However, being aware does not equip users with the ability to oppose such influence.”

**The paper takes its title from one participant's comment: "I am definitely manipulated, even when I am aware of it. It's ridiculous!"**

The paper's title quotes a single survey respondent.

### Intro / Conclusion

**Intro: "If most people miss manipulation, and knowing about it is a weak defense, the line between persuasion and manipulation has to be drawn where the screen is made." Conclusion: "Users can't be the only safeguard here. They miss most of these patterns, knowing about them helps less than you would hope, and the mildest versions caused no measurable upset in testing."**

Research from several fields finds that knowing about a manipulative design is a weak defense: seven experiments found that disclosing a default's purpose does not weaken it, a review of nudge studies reached the same conclusion, large workplace trials found security awareness training did not change who fell for phishing, and a 2026 review of dark-pattern experiments found that interventions mostly failed. Specific recognition and short training can reduce susceptibility somewhat, which is why the wording was softened from 'doesn't help' to 'a weak defense'. The article's point that designers, not users, must carry the responsibility still stands.

- [Bongard-Blanchy et al., DIS 2021 (arXiv preprint;)](https://arxiv.org/abs/2104.12653): “being aware does not equip users with the ability to oppose such influence”
- [Di Geronimo et al., CHI 2020 (;](https://doi.org/10.1145/3313831.3376600): “The online experiment shows that most users do not recognize Dark Patterns, but can perform better in recognizing malicious designs if informed on the issue.”
- [Steffel, Williams & Pogacar, Journal of Marketing Research 2016 (seven experiments;, publisher page blocked)](https://doi.org/10.1509/jmr.14.0421): “This research shows that consumers appreciate transparency, but disclosure does not make defaults less influential.”
- [de Ridder, Kroese & van Gestel, Perspectives on Psychological Science 2022 (evidence review;](https://doi.org/10.1177/1745691621995183): “We find that nudge effects do not hinge on transparency or modes of thinking but that personal preferences moderate effects”
- [Loewenstein, Bryce, Hagmann & Rajpal, Behavioral Science & Policy 2015](https://doi.org/10.1353/bsp.2015.0000): “The effect of the defaults persisted, despite the disclosure, suggesting that their effectiveness may not depend on deceit.”
- [A Systematic Review of User Experiments on the Effects of Dark Patterns, CHI 2026](https://doi.org/10.1145/3772318.3790383): “external interventions have been mostly unsuccessful in mitigating their effects”
- [Ho et al., Understanding the Efficacy of Phishing Training in Practice, IEEE S&P 2025 (RCT, 19,500 employees;](https://doi.org/10.1109/sp61157.2025.00076): “we find no significant relationship between whether users have recently completed cybersecurity awareness training and their likelihood of failing a phishing simulation”
- [Eisend & Tarrahi, Persuasion Knowledge in the Marketplace: A Meta-Analysis, Journal of Consumer Psychology 2022](https://doi.org/10.1002/jcpy.1258): “persuasion knowledge cannot suppress or eliminate persuasion effects in the marketplace, as it only reaches around 50% of the explanatory power of persuasion”

### Where Influence Becomes Manipulation

**Susser, Roessler and Nissenbaum define manipulating someone as intentionally and covertly influencing their decision-making by targeting and exploiting their decision-making vulnerabilities; 'manipulation is hidden influence.'**

Susser, Roessler and Nissenbaum's definition is quoted accurately.

- [Susser, Roessler & Nissenbaum, Internet Policy Review 2019](https://doi.org/10.14763/2019.2.1410): “In our view, manipulation is hidden influence. Or more fully, manipulating someone means intentionally and covertly influencing their decision-making, by targeting and exploiting their decision-making vulnerabilities.”

**The authors set manipulation against persuasion (offering reasons a person can think about and evaluate) and coercion (constraining options), both of which people usually know are happening.**

The persuasion and coercion contrasts match the paper.

**Manipulation is discovered only afterwards: 'when we learn we have been manipulated we feel played.'**

Direct quote, accurate.

**The authors locate the problem in the attempted covertness rather than in any particular tactic. Other philosophers, such as Michael Klenk, argue that manipulation can also happen in the open, but covertness is a practical test for designers to start with.**

The hidden-influence account is one leading definition; others define manipulation as careless influence that can be overt.

**For naming what you find, Colin Gray and colleagues analyzed 118 examples, most of them shared online by practitioners, and grouped them into five strategies.**

Gray's five strategies remain high-level categories in a 2024 ontology that harmonizes ten taxonomies into 64 pattern types.

- [Gray et al., CHI 2018 (NSF PAR manuscript)](https://par.nsf.gov/servlets/purl/10057203): “In total, we collected a corpus of 118 artifacts. Of these, 45 were collected from social media outlets, 40 from practitioner blogs, 19 from news outlets”

**Gray et al.'s definitions: nagging is a repeated intrusion that redirects the task; obstruction makes an interaction harder than needed to dissuade an action; sneaking hides, disguises or delays relevant information; interface interference privileges some actions over others, including preselection and hidden information; forced action requires a specific action to get functionality.**

Definitions match Gray et al. (2018).

### How Far a Mild Trick Goes

**Luguri and Strahilevitz recruited a nationally representative sample of 1,963 American participants for an apparent privacy survey, then told them they would be signed up for a data and identity-theft protection plan: six months free, then $2.99 or $8.99 a month.**

Study design accurately described.

**Control saw Accept and Decline; the mild group saw a preselected 'Accept and continue (recommended)' beside 'Other options', and declining meant choosing 'I do not want to protect my data or credit history' and giving a reason; the aggressive group also had to wait through screens of alarming identity-theft information.**

Condition descriptions match the paper.

**Mild patterns more than doubled acceptance, and aggressive ones nearly quadrupled it.**

Participants were debriefed that no one would be charged, so acceptance was a stated choice; default-effect research shows the direction holds widely.

- [Luguri & Strahilevitz, Journal of Legal Analysis 2021](https://doi.org/10.1093/jla/laaa006): “users exposed to mild dark patterns were more than twice as likely to sign up for a dubious service as those assigned to the control group”
- [Jachimowicz et al., Behavioural Public Policy 2019](https://doi.org/10.1017/bpp.2018.43): “While our analysis reveals a considerable influence of defaults ( d = 0.68, 95% confidence interval = 0.53–0.83), we also discover substantial variation”

**In this experiment, price made no difference: tripling the monthly fee had no effect on uptake.**

The price result held in both studies but comes from hypothetical sign-ups with a free introductory period.

**Afterwards, people in the aggressive condition reported being significantly more upset, while the mild group's mood showed no measurable difference from the control group's.**

A cookie-consent experiment found that obstruction even raised people's sense of control, consistent with mild patterns going unnoticed.

**Less educated participants were significantly more likely to accept when they met the mild patterns.**

Consistent with Bongard-Blanchy et al.'s detection gap by education.

- [Bongard-Blanchy et al., DIS 2021 (arXiv preprint)](https://arxiv.org/abs/2104.12653): “participants with a high school degree or lower detected less dark patterns”

**A second study separated the tactics. Hidden information, trick questions and obstruction were the most effective; in that study, "must act now" messages did not make people more likely to buy.**

The tactic ranking comes from a single study of one service offer.

**A preselected "recommended" button and a guilt-laden decline option produced a large effect and no measurable upset. The usual safety net, waiting for complaints, would probably have missed it.**

Services research finds most dissatisfied customers never complain, which supports treating a quiet complaints inbox as weak evidence.

- [Chebat, Davidow & Codjovi, Silent Voices, Journal of Service Research 2005](https://doi.org/10.1177/1094670504273965): “noncomplaining dissatisfied consumers represent a vast majority of the dissatisfied consumers”

### Interface interference

**The "before" uses the button wording from Luguri and Strahilevitz's mild condition. The rewrite states the price that starts after the free months, which the original left for later.**

The example adapts the study's mild-condition wording.

## What changed in the article

These edits were made on November 12, 2026 after the review.

### Introduction: supported with caveats

**Claim reviewed:** A year later another team surveyed 406 people; respondents were generally aware that manipulative designs influence them, but that awareness did not give them the ability to resist.

**Now reads:** When another team surveyed 406 people a year later, respondents were generally aware that manipulative designs influence them, but by their own account that general awareness did not make them less likely to be swayed.

**Why:** The words match the paper's abstract, but resistance was measured by asking people how likely they were to be influenced, not by watching what they did. The same paper found that people who recognized patterns more easily reported being less influenced, which the article leaves out.

### Introduction: supported with caveats

**Claim reviewed:** The paper's title, "I am definitely manipulated, even when I am aware of it. It's ridiculous!", puts the finding in one line.

**Now reads:** The paper takes its title from one participant's comment: "I am definitely manipulated, even when I am aware of it. It's ridiculous!"

**Why:** The quote is exact, but it is one participant's comment that the authors chose as a title, not their summary of the results. Their own conclusion is more nuanced.

### Intro / Conclusion: supported with caveats

**Claim reviewed:** People can't reliably spot manipulation, and spotting it doesn't protect them; knowing about these patterns doesn't help.

**Now reads:** Intro: "If most people miss manipulation, and knowing about it is a weak defense, the line between persuasion and manipulation has to be drawn where the screen is made." Conclusion: "Users can't be the only safeguard here. They miss most of these patterns, knowing about them helps less than you would hope, and the mildest versions caused no measurable upset in testing."

**Why:** The article's own survey source says general awareness does not equip people to resist, and strong evidence from other fields agrees that knowing is a weak defense: seven experiments found that telling people a default is meant to steer them does not weaken it, a review of nudge research reached the same conclusion, two large workplace trials found security awareness training made no measurable difference to who fell for phishing, and a 2026 review of dark-pattern experiments found interventions mostly failed to blunt their effects. The wording still overstates: the same survey found people who recognized specific patterns more easily reported being less influenced, a 2025 study found users who knew about dark patterns rejected the promoted option far more often, and short training or inoculation can reduce susceptibility for a while. The broad point, that users cannot be the safeguard, stands; 'spotting it doesn't protect them' and 'doesn't help' should be softened to 'knowing about it is a weak defense'. Now cites [Mary Steffel, Elanor F. Williams and Ruth Pogacar, "Ethically Deployed Defaults: Transparency and Consumer Protection through Disclosure and Preference Articulation," Journal of Marketing Research 53(5), 2016 (seven experiments showing that disclosing a default's purpose does not weaken it)](https://doi.org/10.1509/jmr.14.0421).

### Where Influence Becomes Manipulation: supported with caveats

**Claim reviewed:** The authors locate the problem in the attempted covertness rather than in any particular tactic; an emotional appeal made openly is visible influence, while the same appeal designed to work below notice is manipulative.

**Now reads:** The authors locate the problem in the attempted covertness rather than in any particular tactic. Other philosophers, such as Michael Klenk, argue that manipulation can also happen in the open, but covertness is a practical test for designers to start with.

**Why:** The authors do say covertness, not the tactic, is what makes influence manipulative, and the charity example is a fair illustration. But this is one position in a live debate: other philosophers argue manipulation can be open, and the article presents the test without noting that. Now cites [Michael Klenk, (Online) manipulation: sometimes hidden, always careless, Review of Social Economy (2021)](https://doi.org/10.1080/00346764.2021.1894350).

### Where Influence Becomes Manipulation: supported with caveats

**Claim reviewed:** Colin Gray and colleagues analyzed 118 practitioner-shared examples and grouped them into five strategies: nagging, obstruction, sneaking, interface interference and forced action.

**Now reads:** For naming what you find, Colin Gray and colleagues analyzed 118 examples, most of them shared online by practitioners, and grouped them into five strategies.

**Why:** The 118-item corpus and five strategies match the paper. Ten of the 118 came from the authors' own use of products, so 'practitioner-shared' describes most but not all of the corpus.

### How Far a Mild Trick Goes: supported with caveats

**Claim reviewed:** Price made no difference: tripling the monthly fee had no effect on uptake.

**Now reads:** In this experiment, price made no difference: tripling the monthly fee had no effect on uptake.

**Why:** The paper says tripling the price had no effect, but limits it to 'this domain', a hypothetical sign-up with a free first period. In real purchases price usually matters, and how visible it is changes how much.

### How Far a Mild Trick Goes: supported with caveats

**Claim reviewed:** People in the aggressive condition reported being significantly more upset, while the mild group's mood was indistinguishable from the control group's.

**Now reads:** Afterwards, people in the aggressive condition reported being significantly more upset, while the mild group's mood showed no measurable difference from the control group's.

**Why:** The paper reports a strong backlash to aggressive patterns and none to mild ones. 'Indistinguishable' is a little firmer than the paper's 'did not prompt discernable emotional backlash', which means no significant difference rather than proven sameness.

### How Far a Mild Trick Goes: supported with caveats

**Claim reviewed:** A second study found hidden information, trick questions and obstruction were the most effective tactics; 'must act now' messages did not make people more likely to buy; the price result held again ('Decision architecture, not price, drove consumer purchasing decisions').

**Now reads:** A second study separated the tactics. Hidden information, trick questions and obstruction were the most effective; in that study, "must act now" messages did not make people more likely to buy.

**Why:** The paper's second study reports exactly this ranking and the null result for 'must act now' messages. It is one study in one scenario; other shopping experiments find urgency and scarcity cues can raise impulsive buying, so the null result should be framed as this study's finding.

### How Far a Mild Trick Goes: supported with caveats

**Claim reviewed:** The mild condition produced a large effect and no measurable backlash, so waiting for complaints would never have caught it; that is why the authors argue the strongest case for intervention concerns subtle dark patterns.

**Now reads:** A preselected "recommended" button and a guilt-laden decline option produced a large effect and no measurable upset. The usual safety net, waiting for complaints, would probably have missed it.

**Why:** The authors do argue the strongest case for intervention concerns subtle patterns. But the study measured mood right after a hypothetical choice, not complaints, refunds or cancellations, so 'would never have caught it' is an inference. Research showing most dissatisfied customers never complain supports the direction of the inference.

### Interface interference: supported with caveats

**Claim reviewed:** The 'before' example ('Accept and continue (recommended),' preselected, beside a text link reading 'Other options') is Luguri and Strahilevitz's mild condition word for word.

**Now reads:** The "before" uses the button wording from Luguri and Strahilevitz's mild condition. The rewrite states the price that starts after the free months, which the original left for later.

**Why:** The button wording matches the study's mild condition. The paper does not say 'Other options' was a text link, and the mild condition also had a second decline screen, so 'word for word' overstates the match.
