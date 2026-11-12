---
title: "Evidence review: Personalization Ethics and Failure Cases"
---

# Evidence review: Personalization Ethics and Failure Cases

Article: [Personalization Ethics and Failure Cases](https://attck.com/blog/personalization-ethics-and-failure-cases/)  
Reviewed: November 2026 · Method version 2 · [How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)

## How this review works

Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite the original work, and research from other fields that study the same mechanism. A separate reviewer weighed both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the article was corrected. The research below supports the article as it now reads.

## Background research

### Introduction

**On Christmas Eve 2014, Eric Meyer saw friends' Year in Review posts, most carrying the default caption "It's been a great year! Thanks for being a part of it." Then one addressed to him appeared, "Eric, here's what your year looked like!", showing a photo of his daughter, who had died that year.**

- [Meyer 2014, meyerweb.com](https://meyerweb.com/eric/thoughts/2014/12/24/inadvertent-algorithmic-cruelty/): “A picture of my daughter, who is dead. Who died this year.”

**Meyer called it "inadvertent algorithmic cruelty," the result of code that works for the overwhelming majority of people, designed for the ideal user having a good year.**

Quote and paraphrase confirmed.

**The ad kept returning with new festive backgrounds, and the way to hide it was, in Meyer's words, "practically insider knowledge."**

Quote confirmed.

### Two Ways a Personal Guess Goes Wrong

**Software can't easily tell whether a picture has a lot of likes because it is "hilarious, astounding, or heartbreaking."**

Quote confirmed; cross-field work on emotional content and sharing supports the point.

- [Meyer 2014, meyerweb.com](https://meyerweb.com/eric/thoughts/2014/12/24/inadvertent-algorithmic-cruelty/): “figure out if a picture has a ton of Likes because it's hilarious, astounding, or heartbreaking”
- [Brady et al. 2017, PNAS](https://doi.org/10.1073/pnas.1618923114): “the presence of moral-emotional words in messages increased their diffusion by a factor of 20% for each additional word”

### When Explaining Your Data Helps, and When It Backfires

**Aguirre and colleagues (2015) ran ads for a financial services brand on Facebook in the Netherlands for five days at three levels of personalization; click-through rose from 0.017% (none) to 0.077% (matched to stated interests), then fell to 0.032% when the ad also reflected age, gender and location.**

Pass 5 read the full paper. Prestudy 1 ran three versions of a financial services ad and a dog food ad on Facebook in the Netherlands for five days; for the financial brand, click-through rose from .017% with no personalization to .077% when the ad targeted people by their stated likes, then fell to .032% when it also reflected age, gender and location. The authors describe the study as exploratory and report aggregated click-through rates. Independent work points the same way: Goldfarb and Tucker's 2011 field experiment found that combining targeting with obtrusive formats lowered purchase intent, and a 2013 MIS Quarterly field experiment found people saved personalized offers more often only when their data stayed on their own phone. A 2025 meta-analysis of 53 experiments found personalized ads generally more persuasive than generic ones, with perceived relevance rather than intrusiveness explaining the effect, so the drop at high personalization is a real but context-dependent result rather than a rule.

- [Aguirre, Mahr, Grewal, de Ruyter & Wetzels, Journal of Retailing 91(1) 2015 [source 2], Prestudy 1 (accepted manuscript, City Research Online)](https://openaccess.city.ac.uk/id/eprint/15747/1/AGUIRRE%20et%20al%20%202015%20%282%29.pdf): “we selected a brand in each category: a well-known financial services brand and a familiar dog food brand sold in the Netherlands.”
- [Aguirre et al. 2015 [source 2], publisher's PDF from the Maastricht University repository (Internet Archive copy; the repository itself serves a bot check)](https://web.archive.org/web/20231102034248id_/https://cris.maastrichtuniversity.nl/ws/portalfiles/portal/65443620/mahr_2015_unraveling_the_personalization_paradox.pdf): “The advertisements ran for five days on Facebook, during which we collected the aggregated click-through rates (CTR).”
- [Goldfarb & Tucker, Online Display Advertising: Targeting and Obtrusiveness, Marketing Science 30(3) 2011 (large field experiment; OpenAlex abstract)](https://doi.org/10.1287/mksc.1100.0583): “Ads that match both website content and are obtrusive do worse at increasing purchase intent than ads that do only one or the other.”
- [Sutanto, Palme, Tan & Phang, Addressing the Personalization-Privacy Paradox, MIS Quarterly 37(4) 2013 (smartphone field experiment; OpenAlex abstract)](https://doi.org/10.25300/MISQ/2013/37.4.07): “it was only when it was privacy-safe that users saved product messages (reflecting content gratification) more frequently.”
- [Triggering the Personalization Backfire Effect, Behavioral Sciences 15(10) 2025 (lab experiments; Europe PMC abstract)](https://doi.org/10.3390/bs15101323): “highly intrusive, PII-based personalization was no more effective than a generic message and was significantly less effective than moderate, contextual personalization”
- [Noar, Benac & Harris, Does tailoring matter?, Psychological Bulletin 133(4) 2007 (meta-analysis of 57 health studies; supports the rise half only)](https://doi.org/10.1037/0033-2909.133.4.673): “The sample size-weighted mean effect size of the effects of tailoring on health behavior change was found to be r = .074.”

**The dog food ads followed the same shape, from 0.047% to 0.064% and back to 0.033%, though that first rise was small and the authors reported it as significant only on a one-tailed test.**

Pass 5 confirmed the dog food figures from the full text of Aguirre et al. (2015). The rise from .047% to .064% reached significance only on a one-tailed test (z = -1.38, p = .084); the fall from .064% to .033% was significant two-tailed (z = 2.60, p = .009). The pattern matches the financial brand in direction, with a much weaker first step.

- [Bleier & Eisenbeiss, Marketing Science 34(5) 2015 (field experiments; independent evidence of 'overpersonalization')](https://doi.org/10.1287/mksc.2015.0930): “Medium DCP banners, on the other hand, are initially less effective, but more persistent, so that they outperform high DCP banners over time.”

**Their experiments then pointed to a cause. Participants said they were more likely to click on more personalized ads when the firm had collected the information openly. When collection was covert, the same personalization made people feel vulnerable and less inclined to click.**

Corrected to say the experiments measured click intentions, not clicks.

- [Aguirre et al. 2015, Journal of Retailing (Maastricht University repository abstract)](https://cris.maastrichtuniversity.nl/en/publications/9f38a858-8e6f-4638-9bdd-0c96332297c7): “When firms engage in overt information collection, participants exhibit greater click-through intentions in response to more personalized advertisements”

**Trust cues, such as borrowing credibility from a trusted website, offset the drop caused by covert collection.**

- [Tucker 2014, Journal of Marketing Research](https://doi.org/10.1509/jmr.10.0355): “after this enhancement of perceived control over privacy, users were nearly twice as likely to click on personalized ads”

**Kim, Barasz and John found people judge whether an information flow is acceptable on two dimensions: gathered on the site showing the ad or elsewhere, and stated by the person or inferred by the firm; gathered elsewhere and inferred were the less acceptable halves.**

- [Kim, Barasz & John 2019, Journal of Consumer Research](https://doi.org/10.1093/jcr/ucy039): “obtained within versus outside of the website on which the ad appears, and 2) stated by the consumer versus inferred by the firm (the latter of each pair being less acceptable)”

**Revealing an unacceptable information flow made ads less effective, because it raised people's concern for privacy relative to their wish for personalization.**

Confirmed; later null results on generic targeting warnings noted as a boundary.

**Read together, the two papers suggest that disclosure tends to amplify whatever sits underneath it. If the data came from the person, on your own product, and people trust your platform, saying so can help. If it was inferred, or gathered elsewhere, saying so exposes it.**

Softened the synthesis and restored Kim et al.'s platform-trust condition; noted that some later studies find disclosures have little effect.

**A survey of more than 400 online shoppers found the people who most valued transparency features were the least willing to be profiled; the authors advised serving customers who want personalization and accepting that a privacy-sensitive minority will opt out.**

Confirmed in the abstract; direction consistent with later meta-analytic work.

- [Awad & Krishnan 2006, MIS Quarterly](https://doi.org/10.2307/25148715): “the consumers that value information transparency features most are also the consumers who are less willing to be profiled online”
- [Baruh, Secinti & Cemalcilar 2017, Journal of Communication](https://doi.org/10.1111/jcom.12276): “users concerned about privacy were less likely to use online services and share information and were more likely to utilize privacy protective measures”

### The trigger / The selection

**The trigger: "Meyer's fix was to ask instead: offer a preview with a simple yes or no, then ask whether to raise it again later or never, and honor the answer." The selection: "Meyer's other fix: don't pre-fill a picture until you know the person wants to see pictures from their year."**

Removed 'first' and 'second', which reversed the order of Meyer's suggestions.

- [Meyer 2014, meyerweb.com](https://meyerweb.com/eric/thoughts/2014/12/24/inadvertent-algorithmic-cruelty/): “don't pre-fill a picture until you're sure the user actually wants to see pictures from their year”

### The selection

**Content is chosen by engagement, which measures attention, not happiness. A photo can draw likes because it is funny or because it is heartbreaking.**

Added a citation for the engagement point.

- [Meyer 2014, meyerweb.com](https://meyerweb.com/eric/thoughts/2014/12/24/inadvertent-algorithmic-cruelty/): “figure out if a picture has a ton of Likes because it's hilarious, astounding, or heartbreaking”
- [Kleinberg, Mullainathan & Raghavan 2023, Management Science](https://doi.org/10.1287/mnsc.2022.03683): “we often make choices in the moment that are inconsistent with what we actually want”

### The delivery

**In a 2019 study, Ali and colleagues ran job ads on Facebook with identical targeting, optimized for clicks; in the most extreme cases, lumber-industry ads reached an audience 72% white and 90% male, supermarket cashier ads one 85% female, and taxi company ads one 75% Black.**

Figures confirmed in the full text (72% white and 90% male; 85% female; 75% Black).

- [Ali et al. 2019, CSCW (arXiv preprint)](https://arxiv.org/abs/1904.02095): “ads with the same targeting options can deliver to vastly different racial and gender audiences depending on the ad creative alone”
- [Imana, Korolova & Heidemann 2021, WWW](https://doi.org/10.1145/3442381.3450077): “multiple studies have shown that ad delivery on such platforms can be skewed by gender or race due to hidden algorithmic optimization by the platforms”

**The ad creative alone was enough to skew delivery, so an ethics review that checks only the audience a team selects misses what the optimizer does next (neutral targeting does not guarantee neutral delivery).**

Confirmed; market costs (Lambrecht & Tucker 2019) and budget also skew delivery.

- [Lambrecht & Tucker 2019, Management Science](https://doi.org/10.1287/mnsc.2018.3093): “because of crowding out”

### Design for Real Life

**Design for Real Life (Meyer & Wachter-Boettcher, A Book Apart, 2016, 132 pages): its publisher describes the method as identifying "stress cases" and designing with compassion.**

Confirmed; source link points to a publisher that no longer sells the book.

- [A Book Apart product page](https://abookapart.com/products/design-for-real-life): “by identifying stress cases and designing with compassion”

### Conclusion

**Meyer closed his post by asking the industry for more awareness of failure modes, edge cases and worst-case scenarios.**

- [Meyer 2014, meyerweb.com](https://meyerweb.com/eric/thoughts/2014/12/24/inadvertent-algorithmic-cruelty/): “to increase awareness of and consideration for the failure modes, the edge cases, the worst-case scenarios”

### The information-flow test (checklist)

**Disclosure: could the element say "because you…" with the real reason, without making the person uneasy?**

Dropped the citation from the Disclosure item; the Exit item's 'whole category' and 'one obvious step' are the article's extension of Meyer's opt-out point.

- [Kim, Barasz & John 2019, Journal of Consumer Research](https://doi.org/10.1093/jcr/ucy039): “obtained within versus outside of the website on which the ad appears, and 2) stated by the consumer versus inferred by the firm (the latter of each pair being less acceptable)”
- [Meyer 2014, meyerweb.com](https://meyerweb.com/eric/thoughts/2014/12/24/inadvertent-algorithmic-cruelty/): “Where the human aspect fell short, at least with Facebook, was in not providing a way to opt out.”
- [Tucker 2014, Journal of Marketing Research](https://doi.org/10.1509/jmr.10.0355): “after this enhancement of perceived control over privacy, users were nearly twice as likely to click on personalized ads”

## What changed in the article

These edits were made on November 12, 2026 after the review.

### When Explaining Your Data Helps, and When It Backfires: supported with caveats

**Claim reviewed:** The dog food ads rose and fell the same way, from 0.047% to 0.064% and back to 0.033%.

**Now reads:** The dog food ads followed the same shape, from 0.047% to 0.064% and back to 0.033%, though that first rise was small and the authors reported it as significant only on a one-tailed test.

**Why:** The full text confirms the dog food figures exactly: .047% with no personalization, .064% with targeting by stated likes, and .033% when the ad also used age, gender and location. The shape matches the financial brand, but the first step was weak: the authors report the rise as significant only on a one-tailed test (z = -1.38, p = .084), while the fall from .064% to .033% was clear (z = 2.60, p = .009, two-tailed). 'Rose and fell the same way' is right about direction and glosses over how small and uncertain the rise was.

### When Explaining Your Data Helps, and When It Backfires: supported with caveats

**Claim reviewed:** Aguirre et al.'s experiments pointed to a cause: participants clicked more on more personalized ads when the firm collected the information openly; when collection was covert, the same personalization made people feel vulnerable and less inclined to click.

**Now reads:** Their experiments then pointed to a cause. Participants said they were more likely to click on more personalized ads when the firm had collected the information openly. When collection was covert, the same personalization made people feel vulnerable and less inclined to click.

**Why:** The finding and the vulnerability explanation are in the paper, but its experiments measured how likely people said they were to click, not actual clicks. The article's 'participants clicked more' overstates what was measured.

### When Explaining Your Data Helps, and When It Backfires: supported with caveats

**Claim reviewed:** Read together, the two papers say disclosure amplifies whatever sits underneath it: if the data came from the person on your own product, saying so helps; if it was inferred or gathered elsewhere, saying so exposes it.

**Now reads:** Read together, the two papers suggest that disclosure tends to amplify whatever sits underneath it. If the data came from the person, on your own product, and people trust your platform, saying so can help. If it was inferred, or gathered elsewhere, saying so exposes it.

**Why:** The synthesis fits the direction of both papers, but it is stated more firmly than the evidence allows. Kim et al. found disclosure helped only when people trusted the platform, Aguirre et al. tested open versus hidden collection rather than stated versus inferred data, and several newer studies find that disclosures often change little either way.

### The trigger / The selection: supported with caveats

**Claim reviewed:** Meyer's proposed fixes were to ask instead of push (offer a preview with a simple yes or no, then ask whether to raise it again later or never, and honor the answer) and not to pre-fill a picture until you know the person wants to see pictures from their year.

**Now reads:** The trigger: "Meyer's fix was to ask instead: offer a preview with a simple yes or no, then ask whether to raise it again later or never, and honor the answer." The selection: "Meyer's other fix: don't pre-fill a picture until you know the person wants to see pictures from their year."

**Why:** Both fixes are Meyer's, quoted accurately. But Meyer listed the pre-fill fix first and the ask-first fix second, so calling them his 'first' and 'second' fix reverses his order.

### The selection: supported with caveats

**Claim reviewed:** Content chosen by engagement measures attention, not happiness.

**Now reads:** Content is chosen by engagement, which measures attention, not happiness. A photo can draw likes because it is funny or because it is heartbreaking.

**Why:** The point is well grounded: engagement tracks what grabs attention, and research shows in-the-moment behavior often differs from what people actually want. The sentence has no citation, though its clearest source is Meyer's post, already cited nearby. Now cites [Kleinberg, Mullainathan & Raghavan, The Challenge of Understanding What Users Want, Management Science (2023)](https://doi.org/10.1287/mnsc.2022.03683).

### The copy: unverified

**Claim reviewed:** Copy that describes ("Your 2014 in photos") rather than evaluates works for the people having a good year and doesn't wound the rest.

**Now reads:** Copy that describes ("Your 2014 in photos") rather than evaluates still works for the people having a good year and is less likely to wound the rest.

**Why:** No study was found that compares descriptive and evaluative captions for personal recaps, so the claim that descriptive copy 'works' and 'doesn't wound' is untested. It is sensible advice, but neutral wording cannot help if the photo itself is the painful part, as in Meyer's case.

### The information-flow test (checklist): supported with caveats

**Claim reviewed:** Checklist items are attributed to the sources: Source and Place to; Disclosure ('could the element say "because you…" with the real reason without making the person uneasy') to; Worst day and Exit ('hide it, and switch off the whole category, in one obvious step') to.

**Now reads:** Disclosure: could the element say "because you…" with the real reason, without making the person uneasy?

**Why:** The checklist is sound advice, and the Source and Place items rest squarely on Kim et al. But Aguirre et al. tested open versus hidden collection, not 'because you' explanations, and Meyer asked only for a way to opt out, not a one-step switch for a whole category, so those citations imply more backing than they give.
