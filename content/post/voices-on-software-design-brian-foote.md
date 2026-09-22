---
title: "Voices on software design: Brian Foote and Joseph Yoder"
date: 2024-07-26T17:00:37Z
series: voices-on-software-design
---

I’ve been reviewing several classic programming papers about simplicity, complexity, and adjacent topics. Here I’m sharing some highlights from the papers and my thoughts about them.

Today’s paper is [Brian Foote, Joseph Yoder • Big Ball of Mud](http://www.laputan.org/mud/).

### Big Ball of Mud

*Brian Foote, Joseph Yoder • 2001*

At the height of object-oriented programming and the software design patterns movement, which was of course inspired by Christopher Alexander’s work *A Pattern Language*, several papers set out to discover patterns in the way we create software.

Foote and Yoder settle on documenting the dominant “architecture” at the time, which they charmingly named “Big Ball of Mud”.

> *The architecture that actually predominates in practice has yet to be discussed: the BIG BALL OF MUD.*
>
> *A BIG BALL OF MUD is haphazardly structured, sprawling, sloppy, duct-tape and bailing wire, spaghetti code jungle. We’ve all seen them. These systems show unmistakable signs of unregulated growth, and repeated, expedient repair. Information is shared promiscuously among distant elements of the system, often to the point where nearly all the important information becomes global or duplicated. The overall structure of the system may never have been well defined. If it was, it may have eroded beyond recognition. Programmers with a shred of architectural sensibility shun these quagmires. Only those who are unconcerned about architecture, and, perhaps, are comfortable with the inertia of the day-to-day chore of patching the holes in these failing dikes, are content to work on such systems. Still, this approach endures and thrives. **Why is this architecture so popular? Is it as bad as it seems, or might it serve as a way-station on the road to more enduring, elegant artifacts? What forces drive good programmers to build ugly systems? Can we avoid this? Should we? How can we make such systems better?***

At first you may be led to think, “Are they serious?” But then you get to the list of questions they ask — an excellent list of questions to look at. It almost seems like there are hidden forces at work pushing us to forego good architecture and build something ugly. In this paper they set out to answer these questions and explain why good design is so incredibly difficult to pull off.

Pretty quickly, they make a connection to understanding and experience: How well we understand the problem in its domain determines how elegant the solution we can find.

> *A certain amount of controlled chaos is natural during construction, and can be tolerated, as long as you clean up after yourself eventually. Even beyond this though, **a complex system may be an accurate reflection of our immature understanding of a complex problem**. **The class of systems that we can build at all may be larger than the class of systems we can build elegantly, at least at first.** A somewhat ramshackle rat’s nest might be a state-of-the-art architecture for a poorly understood domain. This should not be the end of the story, though. As we gain more experience in such domains, we should increasingly direct our energies to gleaning more enduring architectural abstractions from them.*

Good design requires deep understanding and experience. We cannot expect to figure out a great design on the first try for a domain we know nothing about. And what keeps us from gaining that understanding and collecting all that experience? The usual suspects: cost, time-to-market, and skill.

> ***One reason that software architectures are so often mediocre is that architecture frequently takes a back seat to more mundane concerns such as cost, time-to-market, and programmer skill.** Architecture is often seen as a luxury or a frill, or the indulgent pursuit of lily-gilding compulsives who have no concern for the bottom line. Architecture is often treated with neglect, and even disdain. While such attitudes are unfortunate, they are not hard to understand. Architecture is a long-term concern.*

Long-term concerns give way to short-term ones in the culture we have established that is driven by economic incentives.

However, there is something positive in starting with an ugly, underdeveloped architecture: If we don’t expect to have found the right place for everything, it still has the flexibility to go where it needs to go as we figure it out along the way.

> *Indeed, an immature architecture can be an advantage in a growing system because data and functionality can migrate to their natural places in the system unencumbered by artificial architectural constraints. **Premature architecture can be more dangerous than none at all, as unproved architectural hypotheses turn into straightjackets that discourage evolution and experimentation.***

In the first few pages they establish the tension between planning ahead to gain long-term benefits and preventing necessary experimentation to figure out what is best. We need to find a sweet spot that stabilizes what is already good and difficult to improve, but leaves the space to dramatically change what is not good enough yet and needs to be refined and occasionally reinvented.

> *Architecture is expensive, especially when a new domain is being explored. Getting the system right seems like a pointless luxury once the system is limping well enough to ship. **An investment in architecture usually does not pay off immediately.** Indeed, if architectural concerns delay a product’s market entry for too long, then long-term concerns may be moot.*

Good architecture is fundamentally opposed to the cultural economic environment we operate in.

> *Often, initial versions of a system are vehicles whereby programmers learn what pieces must be brought into play to solve a particular problem. Only after these are identified do the architectural boundaries among parts of the system start to emerge.*

It seems obvious: to become good at something, we need to do it multiple times. Just like physical exercise — to see results, we have to “get the reps in”. But building the same thing several times at great expenditure is not compatible with a profit-driven development process, and as soon as the system does what it is supposed to do, it is done, at least from the perspective of someone who intends to maximize profits.

Another recurring theme: Software is not really visible directly. We can only see it through various different representations that filter and highlight different aspects of it.

> *Programs are made of bits. The manner in which we present these bits greatly affects our sense of how they are put together. Some designers prefer to see systems depicted using modeling languages or PowerPoint pictures. Others prefer prose descriptions. Still others prefer to see code. **The fashion in which we present our architectures affects our perceptions of whether they are good or bad, clear or muddled, and elegant or muddy.***
>
> *Indeed, one of the reasons that architecture is neglected is that much of it is “under the hood”, where nobody can see it. If the system works, and it can be shipped, who cares what it looks like on the inside?*

Good architecture is hard because those who can make decisions to encourage it usually do not care, and those who care are usually not in a position to make such decisions.

The rest of the paper describes seven patterns the authors identified, which attempt to explain how and why we often end up with software that is not well designed. As this post is already more than long enough, I’m just going to quote some of my favorite parts.

### Big ball of mud

> *Sadly, architecture has been undervalued for so long that **many engineers regard life with a BIG BALL OF MUD as normal**. Indeed some engineers are particularly skilled at learning to navigate these quagmires, and guiding others through them. Over time, this symbiosis between architecture and skills can change the character of the organization itself, as **swamp guides become more valuable than architects**.*

> ***Just as it is easier to be verbose than concise, it is easier to build complex systems than it is to build simple ones.** Skilled programmers may be able to create complexity more quickly than their peers, and more quickly than they can document and explain it. Like an army outrunning its logistics train, complexity increases until it reaches the point where such programmers can no longer reliably cope with it.*

> *Status in the programmer’s primate pecking order is often earned through ritual displays of cleverness, rather than through workman-like displays of simplicity and clarity. **That which a culture glorifies will flourish.***

> ***One of mud’s most effective enemies is sunshine.** Subjecting convoluted code to scrutiny can set the stage for its refactoring, repair, and rehabilitation. Code reviews are one mechanism one can use to expose code to daylight.*

> *A BIG BALL OF MUD usually represents **a triumph of utility over aesthetics, because workmanship is sacrificed for functionality**. Structure and durability can be sacrificed as well, because an incomprehensible program defies attempts at maintenance. The frenzied, feature-driven “bloatware” phenomenon seen in many large consumer software products can be seen as evidence of designers having allowed purely utilitarian concerns to dominate software design.*

### Throwaway code

> *Time*, or a lack thereof, is frequently the decisive force that drives programmers to write THROWAWAY CODE. **Taking the time to write a proper, well thought out, well documented program might take more time that is available to solve a problem, or more time that the problem merits.** Often, the programmer will make a frantic dash to construct a minimally functional program, while all the while promising him or herself that a better factored, more elegant version will follow thereafter. They may know full well that building a reusable system will make it easier to solve similar problems in the future, and that a more polished architecture would result in a system that was easier to maintain and extend.

### Piecemeal growth

> ***When designers are faced with a choice between building something elegant from the ground up, or undermining the architecture of the existing system to quickly address a problem, architecture usually loses.** Indeed, this is a natural phase in a system’s evolution […]. This might be thought of as messy kitchen phase, during which pieces of the system are scattered across the counter, awaiting an eventual cleanup. The danger is that the clean up is never done. With real kitchens, the board of health will eventually intervene. With software, alas, there is seldom any corresponding agency to police such squalor.*

> *In the software world, we deploy our most skilled, experienced people early in the lifecycle. Later on, maintenance is relegated to junior staff, and resources can be scarce. **The so-called maintenance phase is the part of the lifecycle in which the price of the fiction of master planning is really paid.** It is maintenance programmers who are called upon to bear the burden of coping with the ever widening divergence between fixed designs and a continuously changing world. If the hypothesis that architectural insight emerges late in the lifecycle is correct, then this practice should be reconsidered.*

> ***We believe that a certain amount of up-front planning and design is not only important, but inevitable.** No one really goes into any project blindly. The groundwork must be laid, the infrastructure must be decided upon, tools must be selected, and a general direction must be set. A focus on a shared architectural vision and strategy should be established early.*

### Keep it working

> *“Probably the greatest factor that keeps us moving forward is that we use the system all the time, and we keep trying to do new things with it. **It is this “living-with” which drives us to root out failures, to clean up inconsistencies, and which inspires our occasional innovation.**” — Daniel H. H. Ingalls*

> *Architects who live in the house they are building have an obvious incentive to insure that things are done properly, since they will directly reap the consequences when they do not. The idea of the architect-builder is a central theme of Alexander’s work. Who better to resolve the forces impinging upon each design issue as it arises as the person who is going to have to live with these decisions? **The architect-builder will be the direct beneficiary of his or her own workmanship and care.** Mistakes and shortcuts will merely foul his or her own nest.*

> *When you are living in the system you’re building, you have an acute incentive not to break anything. A plumbing outage will be a direct inconvenience, and hence you have a powerful reason to keep it brief. You are, at times, working with live wires, and must exhibit particular care. **A major benefit of working with a live system is that feedback is direct, and nearly immediate.***

> *Design space might be thought of as a vast, dark, largely unexplored forest. Useful potential paths through it might be thought of as encompassing working programs. The space off to the sides of these paths is much larger realm of non-working programs. From any given point, a few small steps in most directions take you from a working to a non-working program. From time to time, there are forks in the path, indicating a choice among working alternatives. In unexplored territory, the prudent strategy is never to stray too far from the path. Now, if one has a map, a shortcut through the trekless thicket that might save miles may be evident. **Of course, pioneers, by definition, don’t have maps. By taking small steps in any direction, they know that it is never more than a few steps back to a working system.***

### Shearing layers

> *Adaptability and Stability are forces that are in constant tension. On one hand, systems must be able to confront novelty without blinking. On the other, they should not squander their patrimony on spur of the moment misadventures.**Therefore, factor your system so that artifacts that change at similar rates are together.** Most interactions in a system tend to be within layers, or between adjacent layers. Individual layers tend to be about things that change at similar rates. Things that change at different rates diverge. Differential rates of change encourage layers to emerge.*

> *Can we identify such layers in software? Well, at the bottom, there are data. Things that change most quickly migrate into the data, since this is the aspect of software that is most amenable to change. Data, in turn, interact with users themselves, who produce and consume them. Code changes more slowly than data, and is the realm of programmers, analysts and designers. In object-oriented languages, things that will change quickly are cast as black-box polymorphic components. Elements that will change less often may employ white-box inheritance. The abstract classes and components that constitute an object-oriented framework change more slowly than the applications that are built from them. Indeed, their role is to distill what is common, and enduring, from among the applications that seeded the framework. As frameworks evolve, certain abstractions make their ways from individual applications into the frameworks and libraries that constitute the system’s infrastructure [Foote 1988]. Not all elements will make this journey. Not all should. Those that do are among the most valuable legacies of the projects that spawn them. Objects help shearing layers to emerge, because they provide places where more fine-grained chunks of code and behavior that belong together can coalesce.*

> *Artifacts that evolve quickly provide a system with dynamism and flexibility. They allow a system to be fast on its feet in the face of change. Slowly evolving objects are bulwarks against change. They embody the wisdom that the system has accrued in its prior interactions with its environment. Like tenure, tradition, big corporations, and conservative politics, they maintain what has worked. They worked once, so they are kept around. They had a good idea once, so maybe they are a better than even bet to have another one.*

> *“Things that are good have a certain kind of structure. You can’t get that structure except dynamically. Period. In nature you’ve got continuous very-small-feedback-loop adaptation going on, which is why things get to be harmonious. That’s why they have the qualities we value. **If it wasn’t for the time dimension, it wouldn’t happen. Yet here we are playing the major role creating the world, and we haven’t figured this out.** That is a very serious matter.” — Christopher Alexander*

### Sweeping it under the rug

> *There is a limit to how much chaos an individual can tolerate before being overwhelmed. At first glance, a BIG BALL OF MUD can inspire terror and despair in the hearts of those who would try to tame it. The first step on the road to architectural integrity can be to identify the disordered parts of the system, and isolate them from the rest of it. Once the problem areas are identified and hemmed in, they can be gentrified using a divide and conquer strategy. **Overgrown, tangled, haphazard spaghetti code is hard to comprehend, repair, or extend, and tends to grow even worse if it is not somehow brought under control.***

> *It should go without saying that comprehensible, attractive, well-engineered code will be easier to maintain and extend than complicated, convoluted code. However, it takes time and money to overhaul sloppy code. Still, the cost of allowing it to fester and continue to decline should not be underestimated. **Therefore, if you can’t easily make a mess go away, at least cordon it off. This restricts the disorder to a fixed area, keeps it out of sight, and can set the stage for additional refactoring.***

### Reconstruction

> *Writing-off a system can be traumatic, both to those who have worked on it, and to those who have paid for it. Software is often treated as an asset by accountants, and can be an expensive asset at that. Rewriting a system, of course, does not discard its conceptual design, or its staff’s experience. **If it is truly the case that the value of these assets is in the design experience they embody, then accounting practices must recognize this.***

> *When a system becomes a BIG BALL OF MUD, its relative incomprehensibility may hasten its demise, by making it difficult for it to adapt. **It can persist, since it resists change, but cannot evolve, for the same reason.** Instead, its inscrutability, even when it is to its s hort-term benefit, sows the seeds of its ultimate demise.*

> ***In the end, software architecture is about how we distill experience into wisdom, and disseminate it.** We think the patterns herein stand alongside other work regarding software architecture and evolution that we cited as we went along. Still, we do not consider these patterns to be anti-patterns. There are good reasons that good programmers build BIG BALLS OF MUD. It may well be that the economics of the software world are such that the market moves so fast that long term architectural ambitions are foolhardy, and that expedient, slash-and-burn, disposable programming is, in fact, a state-of-the-art strategy. The success of these approaches, in any case, is undeniable, and seals their pattern-hood.*

> *Periods of moderate disorder are a part of the ebb and flow of software evolution. As a master chef tolerates a messy kitchen, developers must not be afraid to get a little mud on their shoes as they explore new territory for the first time. **Architectural insight is not the product of master plans, but of hard won experience.** The software architects of yesteryear had little choice other than to apply the lessons they learned in successive drafts of their systems, since RECONSTRUCTION was often the only practical means they had of supplanting a mediocre system with a better one.*

---

[Share](/2024/07/26/voices-on-software-design-brian-foote-and-joseph-yoder/)

Mirror of the Self *is a series of essays investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

***Series**: [Mirror of the Self](/series/mirror-of-the-self/) • [On simplicity…](/series/on-simplicity/) • [Voices on software design](/series/voices-on-software-design/) 
**Presentations**: [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/)*
