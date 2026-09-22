---
title: "On Simplicity #5 • Hiding complexity"
date: 2024-01-19T18:01:06Z
series: on-simplicity
---

Let’s talk about the best way we know how to do software development at scale — hiding complexity.

> 9. We mostly hide complexity in such a way that we **accept to ignore** certain complex and unintelligible parts of a thing as long as it provides utility or convenience. **We are culturally accustomed to consider a thing simple, if its utility is convenient to access, even though we have no idea how it works.** I think this is a misguided interpretation of simplicity and a fundamental problem that prevents us from designing things holistically, because **how could we design a better whole if we don’t understand the whole thing?**

### Utility first

First of all, things have to work. They have to be functional. [Our highest priority is](/2022/10/28/05-the-meaning-crisis/#headed-towards-collapse) *[utility](/2022/10/28/05-the-meaning-crisis/#headed-towards-collapse)*[.](/2022/10/28/05-the-meaning-crisis/#headed-towards-collapse) Our second highest perhaps *convenience* — how easy it is for us to make use of that utility.

Everything beyond a feature’s utility — its usability, its comprehensibility, its simplicity, its beauty, is of lesser value to us, and often difficult and costly to achieve. At the same time there are many other features waiting to be implemented promising more utility. There’s not enough time to make things simple or beautiful. [And there is no real](/2023/06/09/design-as-higher-order-problem-solving/#solving-problems) *[need](/2023/06/09/design-as-higher-order-problem-solving/#solving-problems)* [either.](/2023/06/09/design-as-higher-order-problem-solving/#solving-problems) A desire may be there, yes, but in our current economic framework desire is an externality to be ignored. At least until technical debt turns it back into a need, because now it interferes with the creation of more utility.

### Cultivated ignorance

[Our economic framework does not put enough value on preserving coherence, intelligibility, deep understanding and intuitive familiarity.](/2023/05/26/mind-or-machine-who-cares/#infected-by-banality) In fact, we proceed towards the opposite: It doesn’t really matter *how* it works, as long as it reliably works “to spec” — as long as it does *what* we expect it to do. All it needs is to pass the tests. It doesn’t necessarily have to pass them beautifully.

This cultivated ignorance has turned into a powerful strategy for scaling the creation of utility. We can simply ignore what we cannot comprehend behind so called abstractions. We can hide complexity behind interfaces. We can replace deep understanding of *how* with a shallow understanding of *what*. That’s enough to keep building.

As long as an interface keeps doing what it is supposed to be doing, everything is fine. This is how libraries, frameworks, and platforms enable us to scale. We no longer need to be bothered with the details, as long as there is a contract in place that lets us assume that however it does it, it will keep doing it, reliably, in the exact same way in the future.

In return for a dependency on such library, framework, or platform, we can save days, weeks, months, and years of work of figuring out those parts ourselves. And we can spend all that time on creating more utility instead. What’s not to like about this?

Economic incentives push us towards maximizing utility at the cost of intelligibility. Utility is what sells the product. More utility means more power. More is more. An intelligible and beautiful implementation of a feature is certainly useful, and nobody argues with that, but it’s nice to have. Utility, however, is a must have.

There is just enough imbalance between the two that over time we accumulate features but also understand less of how everything works together — which is when we like to say that “complexity has emerged”.

### Generative AI

I see this reflected in the welcoming stance that many software engineers have towards artificial intelligence: We no longer have to figure out APIs ourselves. We no longer have to understand how they have been designed and how they are supposed to be used. A large language model (LLM) can do it for us! That makes us so much more productive.

This is all true, and I find myself integrating LLMs into my own process more and more. Because there are just too many different APIs to know, too many different capabilities to use, too many different platforms to support. If an AI model can take care of all these details, we can focus on the important stuff — creating more utility. And further contribute to the proliferation of features, APIs, capabilities, libraries, frameworks, platforms — more complexity.

Generative AI enables us to create more utility without having to understand the details of how this utility is created. For instance, code generation: If it compiles and runs and passes the tests, if it does what we want, what incentives do we really have to read and try to understand the code?

At the moment some of us are still skeptical, and companies that provide generative AI are still unsure about legal ramifications, so the “official” stance is, “of course you check the code before you push it into production”. But the way this is going, it will soon be covered by just another clause in a license agreement nobody reads anyway and readily accepts with a click. Responsibility transferred. Now let’s go and build more stuff!

It becomes a self-fulfilling prophecy: Understanding of a system is not necessary to extend it. Generative AI will accelerate our utility creation and amplify our cultivated ignorance. Ironically, generative AI itself is a system we do not fully understand. We don’t know how it does what it does. Some scientists are trying to work that out, but who cares? Look at all the additional productivity to create more utility, faster!

When in the past some engineers were required to understand enough of a system to implement new functionality, we can now implement new functionality without a requirement to understand at all. We can now leave that to a generative, stochastic, potentially non-deterministic AI and grow our dependence on it.

Could there possibly be a problem with that?

### Additive design

If there is a problem with that, it is not an obvious one. Chances are, you are reading this using software that has been built with thousands of dependencies. Clearly, this approach works. This is just how software is built these days. And look how far we have come!

If there is a problem with cultivated ignorance, it must be subtle.

What is the easiest way to make sure that the implementation behind an interface keeps doing what it is doing? The easiest way is to not change anything. We establish invariants, static fixed points in an ever changing environment. A good portion of the work a software engineer does is to figure out good invariants. We rely on these invariants to be stable.

As a consequence, we practice additive design. Additive design leaves the existing untouched to not break anything and creates more utility by adding components that are only integrated as much as they have to be to make them work. This also helps with division of labor among different people and teams and enables software development at scale.

Not only does our economic framework discourage us from spending time on beautiful software architecture, on top of that we are strongly encouraged to leave things that work alone and “never touch a running system”.

Instead we turn to a design approach accumulating distinct, isolated features that can be developed in parallel independent of each other and require only minimal integration into the existing codebase, to reduce the risk of breaking existing functionality. We can leave existing parts alone, and keep adding new parts on top or on the side. You can see how important this is to us in the way we look to create “reusable” components that are as versatile and universal as possible. Cue discussions about “composition” and “Lego blocks”.

It works. One could argue, it proves that a deep understanding of the whole system is not necessary to extend it. That’s how most software is built today and has been for decades. This is what enables new engineers to jump in and build “real stuff” in no time. This surely must be a good thing!?

### Manufactured unintelligibility

Additive design causes a system to grow quicker than with a more integrative approach that keeps changing core parts but has much higher risks of breaking things.

When a system grows in distinct, decoupled, independent parts, duplication occurs where we don’t look, for instance by adding various separate libraries that all have their own implementations of more basic algorithms. Cruft accumulates in the parts that could and should be replaced or at least modified but aren’t, because we can’t risk to break something.

As a result, the whole system becomes more complicated and difficult to understand. And over time, our intuitive familiarity with the existing parts fades, as we forget how exactly they work and why we designed them that way. Or the people who do leave. Or the components we used came from libraries we did not bother to understand beyond their interfaces anyway.

This turns into a vicious cycle of increasing complexity — manufactured unintelligibility is built into the process.

But still the question remains: Is this really a problem?

Experienced software engineers often sense problems and suggest refactoring, but we all know how this usually works out. Individual engineers may be able to sneak in some smaller clean-up as long as they also keep shipping features, but overall there is not enough willingness to support large-scale refactoring until technical debt has become an obvious barrier to shipping new features. If utility is not in danger, beauty is always welcome, but optional.

But not just the technical implementation becomes more incoherent and unintelligible over time. The same happens to customers using the product. As features are added even while existing functionality is preserved, customers notice the product growing. Even if the parts they use still work the same way, they can see new functionality appearing. Often we want them to and aggressively point them to it. More utility. More power. Go and use it!

Perhaps for some it is what they were hoping for and they embrace it. But the more features we add, the more likely new functionality tries to reach a different set of customers, and individual customers who don’t belong to that set can become overwhelmed, may consider it bloat, or might even feel alienated — the product that once was exactly what they wanted and “made for them” has turned into a bloated behemoth of features they only use a fraction of. It is no longer for them. Maybe they are now locked in and for various reasons it is too difficult for them to switch to something else. However, eventually, some begin to look for a simpler, leaner alternative, that countless new VC-funded start-ups are happy to provide. The software life-cycle repeats.

### The software life-cycle

If a minimum viable product is successful, it hits the spot for a group of early adopters. Something about it fulfills their needs well enough — the product is adapted enough to their requirements to *obviously* fit a specific use case — they can easily comprehend that this product fits their need and how it does so. They may say that it does “exactly what they wanted”, even if they didn’t really know what they wanted until they saw it, and even if it has other obvious limitations because it is brand new.

Fueled by the early promise of potential product-market fit (and lots of venture capital, of course), now the next stage of the software life-cycle kicks in: more features. Give those early adopters the other things they want to do but currently can’t. The software grows. Complexity too. But that’s just how it works, right?

At some point it becomes clear that the hunger for additional features can never be satisfied, but now the complexity reaches a stage where only one thing can help: more customers. To reach new customers, other new features need to be added. Perhaps large groups of customers have a specific context that the current product can’t properly address, such as a corporate environment. Priorities change to adapt to these environments to “unlock” these groups of new customers.

Over time, if successful, more and more customers can be reached. The product supports many different use cases in many different contexts. And because most of these changes have been additive, most of what worked in the past still kind of works and almost in the same way. But something weird happens: There are more customers overall, but fewer customers love the product. Some early adopters disappeared, looking to early adopt something else.

The vibe shifts. In the beginning the product attracted early adopters with [a clear](/2022/11/18/08-existential-modes/#expressive-individuality) *[unique](/2022/11/18/08-existential-modes/#expressive-individuality)* [identity](/2022/11/18/08-existential-modes/#expressive-individuality). It was doing one thing right, and it was obvious what that thing was. But it was limited. Then it matured and took on a more [categorical identity](/2022/11/18/08-existential-modes/#existential-modes--having-and-being) that is less defined, less opinionated, less unique. The product now competes in a *category* of similar products. Customers may still have their favorite, but it has become somewhat replaceable.

Even if we try to keep what worked untouched or almost the same, as the product grows, as it becomes more capable, and more complicated, all these new features and capabilities need to be surfaced somehow. And that changes the perception of the product.

First new features for a limited product are overall perceived as positive because it is clearly becoming more powerful. But there is a tipping point where additional features are no longer experienced as an extension of capability, but as an accumulation of feature creep. The more features there are that are not relevant to an individual user, the greater the chance that they will perceive these new features as bloat. Of course, each customer is different and their individual tipping point is in a different spot which depends on their particular context.

To some extent customers are able and willing to grow with the product and absorb some of its added complexity in exchange for added utility. But this doesn’t work indefinitely. If new features and capabilities are added and not properly integrated, the product as a whole feels less coherent and becomes harder to understand. What can I do with it? How does this work? What does this button do?

One way out is proper integration. Finding the right places for new features and capabilities in the existing structure, so that they *make sense* and don’t just feel bolted on. But that kind of integration requires modification of what already exists. And, in some cases, it might be more valuable to do without certain features to keep a product’s identity sharp and defined.

Something that tries to do everything most likely doesn’t do anything well. It’s easier to have an identity, a brand, if you are opinionated, if you do things a certain way, and if you don’t do certain things at all. You want to keep a coherent identity, something your customers understand and like, [something they can fall in love with](/2023/05/05/finding-meaning-in-the-nature-of-order/#reciprocal-realization), [something they want to grow with](/2022/11/18/08-existential-modes/#living-process--reciprocal-realization).

**Unintuitively, coherence is something you lose quickly, if you just keep adding things.**

### Some integration required

Good user experience design can alleviate the effects of growth by properly integrating new capabilities into what already exists, preserving coherence, consistency, and identity of a product that makes sense to customers.

Good software architecture can alleviate the effects of growth by properly integrating new capabilities into what already exists, preserving coherence, consistency, and identity of a system that makes sense to developers.

Coherence has its place and is important. And I would argue [coherence is simplicity](/2023/11/10/on-simplicity-%232-meaning-ful-design/#meaning-ful-design). We tend to consider simplicity — if at all — very late in the process of designing something. Make it work, make it fast, make it convenient, then maybe make it simple. Because it is somewhat of an afterthought, we end up with more complicated things. However, this means we have an opportunity to care more about simplicity earlier in the process and change things for the better — by realizing the value of coherence and integration.

The real problem here is not that we are not aware of this. Ask the engineers of the product, most of them will complain about not having been able to fix some architectural issues they clearly know how to improve. Ask the customers, most of them will tell you if they feel like there has been a lot of functionality added lately they don’t really need or care about. But when we zoom out it really affects just a few engineers, and it really just affects a few customers.

The real problem is that neither of those are considered enough of an issue, when your company has more important problems because it has grown into an economic machine that is now expected to deliver a certain amount of revenue or engagement. It’s obvious that something is going wrong, but whatever it is *it doesn’t make sense* to stop growing.

The environment that enabled us to spend time and effort building a new thing in the first place is now pushing us to keep growing. In the beginning, we were “just” required to find anything worthwhile building (that attracts some customers). But the longer we keep playing this game, we will eventually lock ourselves into an optimization race up the local maximum hill we are going to die on and forfeit our chance to find one of the larger global maxima mountains. At some point another pivot just makes a lot less sense than burning everything down or letting it die slowly and then start over from scratch again — leaving all the complexity behind.

[Integration is what can preserve structure, coherence, intelligibility](/2023/02/10/17-the-essence-of-design/#differentiating--integrating--complexifying), the whole that is more than just a sum of parts — an identity worth engaging with, something you can make sense of, something you understand, something that is alive, something you want to fall in love with. Something that transcends categorical existence and becomes irreplaceably unique. Something that is not just a tool like any other, but [your environment you feel at home in](/2023/07/07/from-tools-to-environments/). Something that is not just useful, but significant.

The way we design software today — hiding complexity and cultivating our ignorance — is the best way we know how to build software at scale so far. It has proven to take us far beyond what the early computing pioneers imagined and enables us to create ever more utility and power, [soon supercharged with AI](/2023/05/12/modally-confused-ai/).

Unfortunately, it produces things that over time likely become more incoherent and unintelligible, are perceived as bloated and confusing and less fit for purpose, and ultimately lose their significance, if they ever were significant to us in the first place.

For most of us that is not really a problem.

But [some of us](/2023/03/31/23-the-mystery-of-wonder-and-awe/#the-deepest-experience-of-order) wonder what a world would look like where this was different.

---

Mirror of the Self *is a fortnightly newsletter series investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

*If you are new to this series, start here: [01 • A secular definition of sacredness](/2022/09/30/01-a-secular-definition-of-sacredness/). 
Overview and synopsis of articles 01-13: [Previously… — A Recap](/2023/01/06/previously-a-recap/). 
Overview and synopsis of articles 14-26: [Previously… — recap #2](/2023/04/28/previously-recap-%232/).*

*Another great way to start is my recent presentation [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/).*
