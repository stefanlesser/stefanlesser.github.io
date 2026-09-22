---
title: "Voices on software design: Niklaus Wirth"
date: 2024-05-31T17:01:17Z
series: voices-on-software-design
---

I’ve been reviewing several classic programming papers about simplicity, complexity, and adjacent topics. Here I’m sharing some highlights from the papers and my thoughts about them.

Today’s paper is: [Niklaus Wirth • A Plea for Lean Software](https://montcs.bloomu.edu/Readings/Scientific-Technical/Niklaus%20Wirth%20-%20A%20Plea%20for%20Lean%20Software%20-%20OCR.pdf)

## A Plea for Lean Software

*Niklaus Wirth • 1995*

In this paper Wirth mainly criticizes how

> *Software’s girth has surpassed its functionality, largely because hardware advances make this possible.*

### Causes for „fat software“

Wirth fat-shames software that shows signs of a wide-spread obesity epidemic already in 1995. Consuming *mega*bytes of storage and memory and exhausting processing cycles still measured in *mega*hertz didn‘t sit well with him as he reminisces about text editors that fit into 8000 bytes of storage and ran with 32 KBytes of memory.

What happened? Complexity, of course. But Wirth criticizes a specific source of that complexity, which may sound familiar:

> *A primary cause of complexity is that **software vendors uncritically adopt almost any feature that users want**. Any incompatibility with the original system concept is either ignored or passes unrecognized, which renders the design more complicated and its use more cumbersome. When a system’s power is measured by the number of its features, quantity becomes more important than quality. Every new release must offer additional features, even if some don’t add functionality.*

Feature creep through uncritical adoption of features. I wrote about the same concept calling it [additive design](/2024/01/19/on-simplicity-%235-hiding-complexity/#additive-design).

### All the features, all the time

He sees an opportunity in designing systems to only offer essential facilities and extension points, because he identifies one of the main problems as shipping monolithic collections of features for a whole audience, thereby ignoring the specific needs of individuals.

> *Another important reason for software complexity lies in monolithic design, wherein all conceivable features are part of the system’s design. **Each customer pays for all features but actually uses very few.** Ideally, only a basic system with essential facilities would be offered, a system that would lend itself to various extensions. Every customer could then select the extensions genuinely required for a given task.*

While he doesn‘t discuss here how this extension mechanism should work exactly, later in the second half of the paper he reveals his Oberon project that is a whole working implementation of several of his ideas, including such an extension mechanism.

However, there isn’t really any substantial motivation to design systems like this, because… Moore’s Law, essentially.

> *Increased hardware power has undoubtedly been the primary incentive for vendors to tackle more complex problems, and more complex problems inevitably require more complex solutions. **But it is not the inherent complexity that should concern us; it is the self-inflicted complexity.** There are many problems that were solved long ago, but for the same problems we are now offered solutions wrapped in much bulkier software.*

Not unlike [Brooks‘ essential and accidental complexity](/2024/05/17/voices-on-software-design-frederick-p.-brooks/), Wirth distinguishes between two kinds of complexity here. However, he uses a much stronger and more opinionated adjective for the kind we need to worry about: it is not just „accidental“ as in Brooks, it is „self-inflicted“. We are reinventing wheels, and we‘re making them much chunkier than they need to be.

### Complexity equals power

One part that stands out to me is Wirth‘s characterization of a kind of confusion that we fall prey to. Instead of becoming suspicious about what is unintelligible to us and makes us dependent, we rather admire comforting stories of power, innovation, and progress we keep telling ourselves these technologies will enable.

> *A system’s ease of use always should be a primary goal, but that ease should be based on an underlying concept that makes the use almost intuitive. Increasingly, people seem to misinterpret complexity as sophistication, which is baffling — **the incomprehensible should cause suspicion rather than admiration**. Possibly this trend results from a mistaken belief that using a somewhat mysterious device confers an aura of power on the user. (What it does confer is a feeling of helplessness, if not impotence.) Therefore, the lure of complexity as a sales incentive is easily understood; complexity promotes customer dependence on the vendor.*

He has some thoughts on why we are pulled into this confusion:

> *Of course, a customer who pays — in advance — for service contracts is a more stable income source than a customer who has fully mastered a product’s use. Industry and academia are probably pursuing very different goals; hence, the emergence of another “law:”*
>
> - *Customer dependence is more profitable than customer education.*

I cannot help and see reflections of [modal confusion](/2022/11/18/08-existential-modes/#modal-confusion) in this, where business incentives push customers to *having* access to [convenient utility](/2024/01/19/on-simplicity-%235-hiding-complexity/#utility-first) over *becoming* proficient in using a powerful tool. And as we expand our power, available to us through the click of a button, our understanding and our skills atrophy, we become dependent on having those buttons.

### Software is all design

He describes an interesting difference between hard- and software:

> *Designing solutions for complicated problems, whether in software or hardware, is a difficult, expensive, and time-consuming process. Hardware’s improved price/performance ratio has been achieved more from better technology to duplicate (fabricate) designs than from better design technique mastery. **Software, however, is all design**, and its duplication costs the vendor mere pennies.*

Hardware can benefit (and has massively) from improvements in manufacturing. We can produce far better chips in far higher quantities for far less cost. In other words we have gotten much better at duplicating things over and over again more efficiently. Software, however, can‘t really benefit from that, because it can already be duplicated almost without any effort at all.

> *Initial designs for sophisticated software applications are invariably complicated, even when developed by competent engineers. **Truly good solutions emerge after iterative improvements or after redesigns that exploit new insights**, and the most rewarding iterations are those that result in program simplifications. Evolutions of this kind, however, are extremely rare in current software practice — **they require time-consuming thought processes that are rarely rewarded**. Instead, software inadequacies are typically corrected by quickly conceived additions that invariably result in the well-known bulk.*

To significantly improve software, we need an iterative process and creative insight. [Exactly what we don‘t have the patience for](/2023/06/23/fighting-insight-with-inference/) in most contexts.

### Never enough time

> *Time pressure is probably the foremost reason behind the emergence of bulky software. The time pressure that designers endure discourages careful planning. It also discourages improving acceptable solutions; instead, it encourages quickly conceived software additions and corrections. **Time pressure gradually corrupts an engineer’s standard of quality and perfection. It has a detrimental effect on people as well as products.** […]*

While we don‘t have enough time for care- and [meaning-ful design](/2023/11/10/on-simplicity-%232-meaning-ful-design/), we at least have better and faster hardware, which deals with the bulkiness of our obese software, so we can keep moving fast and learn… nothing.

> *Software’s resource limitations are blithely ignored, however: Rapid increases in processor speed and memory size are commonly believed to compensate for sloppy software design. **Meticulous engineering habits do not pay off in the short run, which is one reason why software plays a dubious role among established engineering disciplines.***

### Languages and design methodology

Wirth speaks of „planning“, „perfection“, and „meticulous engineering“ as desirable practices of a design process. Although I‘m worried that these words have taken on quite negative connotations today, his criticism seems more relevant than ever. While we cannot achieve perfection, some of the caring we would put into it if we tried is missing from the way we design and develop software today.

> *Methodical design, for example, is apparently undesirable because products so developed take too much “time to market.” Analytical verification and correctness-proof techniques fare even worse; in addition, these methods require a higher intellectual caliber than that required by the customary “try and fix it” approach. **To reduce software complexity by concentrating only on the essentials is a proposal swiftly dismissed as ridiculous in view of customers‘ love for bells and whistles.** When “everything goes” is the modus operandi, methodologies and disciplines are the first casualties.*

### Reinventing the wheel?

Getting slightly more technical, I enjoyed this provocation about type systems:

> ***Without type checking, the notion of abstraction in programming languages remains hollow and academic.** Abstraction can work only with languages that postulate strict, static typing of every variable and function. In this respect, C fails — it resembles assembler code, where “everything goes.”*

In many discussions I witnessed the apparently more popular opinion that type checking is what makes programming languages hollow and academic. Seeing him argue for the exact opposite is a stimulating prompt to rethink.

He later on comments on types and object-oriented programming:

> Remarkably enough, **the abstract data type has reappeared 25 years after its invention under the heading** ***object oriented*****.** This modern term’s essence, regarded by many as a panacea, concerns the construction of class (type) hierarchies. Although the older concept hasn’t caught on without the newer description “object oriented,” programmers recognize the intrinsic strength of the abstract data type and convert to it.

When he wrote this in 1995, object-oriented programming has just become the hot new thing. But his reframing of object-oriented as a reinvention of abstract data types hints at what he means when he criticizes that we keep reinventing the wheel, reimplementing good ideas from the past in a more complicated, bulkier way.

### Some lessons learned from Oberon

This post is already too long, so I won‘t go much into the second half of the paper that discusses Oberon[^1]. However, I have to mention just a few of the lessons learned he concludes his paper with.

> *The belief that complex systems require armies of designers and programmers is wrong. **A system that is not understood in its entirety, or at least to a significant degree of detail by a single individual, should probably not be built.** […]*
>
> *Programs should be written and polished until they acquire publication quality. **It is infinitely more demanding to design a publishable program than one that „runs“.** Programs should be written for human readers as well as for computers. If this notion contradicts certain vested interests in the commercial world, it should at least find no resistance in academia.*

I could not agree more with this plea for intelligibility and his (demonstrated) belief in the benefits of a holistic understanding of the whole system.

> ***Reducing complexity and size must be the goal in every step** — in system specification, design, and in detailed programming. A programmer’s competence should be judged by the ability to find simple solutions, certainly not by productivity measured in “number of lines ejected per day.” Prolific programmers contribute to certain disaster. […]*
>
> *With Project Oberon we have demonstrated that flexible and powerful systems can be built with substantially fewer resources in less time than usual. The plague of software explosion is not a “law of nature.” It is avoidable, and it is the software engineer’s task to curtail it.*

Wirth is part of a minority, but by far not the only one who believes that we can substantially move the needle on how we design and develop software. A lot more can be done than we (are led to) believe. There is a good chance that we don’t have to live with the complexity we have learned to accept around us today, and the dependence that comes with it.

The remedy he suggests in 1995 is a return to essentials and trust in discipline and methodology. We now have a quarter of a century more experience and know that essentials are extremely difficult to define and discipline and methodology alone will not pull us out of the mess we maneuvered ourselves into. But that doesn’t mean his premise is wrong.

We can, of course, trust AI to take care of such complexity for us. In return, [we grow even more dependent on systems we don’t understand](/2024/01/19/on-simplicity-%235-hiding-complexity/#generative-ai). But if Wirth is right and a lot of the complexity is self-inflicted and there are ways to design equally as powerful systems with a lot less complexity and a lot more intelligibility, maybe we have another attractive alternative future ahead of us.

---

[Share](/2024/05/31/voices-on-software-design-niklaus-wirth/)

Mirror of the Self *is a series of essays investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

***Series**: [Mirror of the Self](/series/mirror-of-the-self/) • [On simplicity…](/series/on-simplicity/) • [Voices on software design](/series/voices-on-software-design/) 
**Presentations**: [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/)*

[^1]: Today, at least. Perhaps some day in the future…
