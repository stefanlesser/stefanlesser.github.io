---
title: "To build or not to build?"
date: 2023-08-04T17:00:06Z
---

In [my presentation at Building Beauty](/2023/05/05/finding-meaning-in-the-nature-of-order/) I discussed the [distinction between describing and making](/2023/05/05/finding-meaning-in-the-nature-of-order/#iii-making), and tangentially asked the question: Are we software people actually *making* things, or merely *describing* them?

There is, of course, a certain depth to that question, especially if you consider [Aristotle’s conformity theory](/2022/12/23/13-agent-and-arena/#in-touch-with-reality), and Alexander’s thoughts on [a feeling-based process to apply structure-preserving transformations](/2023/02/10/17-the-essence-of-design/#the-fundamental-process) during a building process.

### Writing code is describing

As software people our immediate output is code. That which we design and arguably build, we manifest through a codified description of the thing, or at least its behavior.

Code *describes* the thing we want built, how it behaves, and how to build it. There is a step in the development cycle which is called the “build phase”. That should be a clue as to where the actual building happens — and who actually does it.

*Building* a piece of software is at this point almost fully automated and completely done by the machine. We are crafting a formal description so the computer can then build from that description. We are at least one step removed from touching and shaping the raw bits of the result and instead try to describe as precisely as possible what the computer should build for us, how to build it, and how the built thing should behave. But ultimately it is the machine that does the actual building.

*(Technically, what I’m describing is most accurate for compiled languages, where the compilation step is equivalent to building, and the built product is an application binary that can then be executed. But even though interpreted languages seem to blend building and running, and the distinction between them seems less important, they still have the separation described in the following paragraph.)*

### The environment is ~~missing~~ abstracted away

Another clue that we are not the builder is that in our world of describing things formally, a huge part of the system is not present — all the data and the environment that will be there eventually at runtime is just an abstract assumption, a preconceived notion, a simulated reality in our minds. Which we deliberately keep distant, because that’s where all the nasty variability is, but as we design the system we want to focus on its invariants.

But the variability of the system is where all the interesting stuff happens. We need state, we need the specific environment [with all its overwhelming complexity](/2023/04/07/24-opening-the-eye-to-the-storm/) to determine — [mostly with our S1](/2023/06/23/fighting-insight-with-inference/#dual-processing) — what’s really going on. How it feels. And then we can go back to the simplified abstract model of what’s supposed to be going on that S2 can continue theorizing about.

We even remove ourselves further from the building process and the environment as we attempt to improve the programming languages we use to formally describe what we would like the computer to build for us. Sometimes we get lost in the specifics of literal *formal*ities.

### Build, wipe, repeat

Another indication that we removed ourselves from building is that there is a development *cycle*. We make a change to the formal description, then our development environment rebuilds the whole thing from scratch. Every. Single. Time.

*(Yes, technically we have invented all kinds of tricks to not do exactly that, but most of these optimizations still have the same effect — we start over from a well-defined initial state, even if we only compiled what has actually changed.)*

Let’s face it: We are not building. We don’t shape material. We throw away the material the computer shaped for us in the last iteration, wipe the virtual work surface clean, and then have the computer build an entirely new version from scratch, according to our slightly modified specification. We are more like architects (in the colloquial sense, not in the sense of what Alexander wants architects to be).

No wonder we cannot feel deeply involved and connected to the building process. What we do is different from what a painter does and feels when they apply a brush stroke to a canvas, or what a carpenter does and feels when they carve a piece of wood. We are not touching material. We are not immediately sensing the consequences of our actions instantly reflected in the environment. We are standing back, reflecting, analyzing, theorizing.

We are standing in the corner of the workshop, overseeing, and telling others what we would like to have built. Our “material” is a language of specification. There is no wood to carve or clay to mold, or if there is, others do that for us according to our specs. And the skill we need to do this well is primarily analytical and abstract — [deeply rooted in S2](/2023/06/23/fighting-insight-with-inference/#dual-processing).

The bad news: We are describing, not building. We cannot directly connect to the experience of shaping material in a tight feedback loop of manipulating the environment and immediately sensing how those changes impact us.

The good news: We are still in charge of a generative process. And with the power and speed of modern computation, we may be able to at least get to a generative process so quick that the feedback loop feels so tight that it almost qualifies as instant.

### Generating, not building

Usually, these days, the build process happens relatively quickly. Sometimes, in small projects, it can be so fast that we almost don’t notice it happening. Fast computation is one of the few things computers are really good at. So there is still an opportunity for a tight enough feedback loop that enables some sort of connection to an almost immediate sensory experience, [which is so essential for flow](/2023/03/03/20-flow-and-intuition/).[^1]

But the issue is not just raw speed. We also need to find a way to make a fundamentally analytic activity accessible to holistic sensory experience. We need to [give S1 a chance to do its magic, and not leave everything up to S2](/2023/06/23/fighting-insight-with-inference/#cognitive-leaping).

Early programming environments like Smalltalk, which were designed before today’s sharp divide between users and programmers existed, feel different. You *[live](/2023/07/07/from-tools-to-environments/)* [in the system](/2023/07/07/from-tools-to-environments/) and modify it as it is running. The changes you make stick around. There is no need to rebuild everything from scratch all the time (although there is the possibility), as you modify both state and behavior of the system itself. You have the option to start over from a clean s[l|t]ate, but by default you keep around what you have and modify it.

This seems a little bit closer to shaping material. It is still not like molding clay with your hands or a piece of wood with an appropriate tool guided by your hands. But it is a lot closer to that than shouting at someone from across the room, telling them to start over and build it slightly different this time.

Another example for a generative process that feels closer to what we are after are modern note-taking approaches. When you curate your Zettelkasten or tend to your digital garden, you are continuously shaping a knowledge graph that grows and changes with you over time. That still doesn’t feel quite like sculpting clay, because you are still manipulating bits not atoms in a stereotypically analytical process. But at least you are living in your garden, not just formally describing one.

If we inhabit the environment we intend to change, we have the opportunity to engage in [reciprocal realization](/2022/11/18/08-existential-modes/#living-process--reciprocal-realization) with it — as we change the environment, it has the capability to change us. Hopefully, we grow together, each of us becoming better in (and through) the process.

---

Mirror of the Self *is a fortnightly newsletter series investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

*If you are new to this series, start here: [01 • A secular definition of sacredness](/2022/09/30/01-a-secular-definition-of-sacredness/). 
Overview and synopsis of articles 01-13: [Previously… — A Recap](/2023/01/06/previously-a-recap/). 
Overview and synopsis of articles 14-26: [Previously… — recap #2](/2023/04/28/previously-recap-%232/).*

*Another great way to start is my recent presentation [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/).*

[^1]: If you are familiar with Bret Victor’s work, this is close to one of his main points he makes in his excellent presentation [“Inventing on Principle”](http://worrydream.com/#!/InventingOnPrinciple), which sadly seems to have vanished from the Interwebs…?
