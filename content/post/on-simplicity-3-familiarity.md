---
title: "On simplicity #3 • Familiarity"
date: 2023-12-08T18:01:14Z
series: on-simplicity
---

We are incredibly good at [implicit learning](/2023/03/03/20-flow-and-intuition/#intuition-and-bias). Without consciously trying to spot patterns, subconsciously we constantly keep looking for them, continuously constructing and testing mental models, until we develop an intuition that feels like we know what’s going on, without being able to explain it.

[That intuition is not always correct.](/2023/06/23/fighting-insight-with-inference/#jumping-to-conclusions) But the more experience we collect doing something, the more accurate this intuition gets. Take, for instance, our intuition for how objects behave in the real world.

### Powerful intuition

Without studying for a degree in physics, we quickly learn just from everyday interactions at young age that larger and heavier objects move slower than smaller and lighter ones, and that it takes some time for objects to accelerate — they don’t just jump from being stationary to moving at a high speed. There is always a transition period where an object that starts to move steadily accelerates and then decelerates before it stops again. Also things don’t just appear out of thin air, they usually come from somewhere else. Whether we are able to explain the physics behind all this or not, we have a strong intuition for how objects in physical space behave, and if something doesn’t behave like this, we immediately know something is off.

In software, the rules of physics don’t apply. We can make things move, appear, and disappear on our screens without respecting any particular rules. And when we do that, it *feels* weird, foreign, broken. However, if we design animations and transitions and interactions that mimic the behavior of objects in the physical world, it feels much more natural. We are wired to expect everything to behave in the same way we implicitly learned most things around us do. And if we know what to expect from our environment, it becomes much easier for us to navigate and interact with that environment. That’s why it’s valuable to bring these behaviors to our user interfaces, even if that is technically more challenging and a lot more work.

Another good example for this is [scrolling on devices with touch input](/2023/06/09/design-as-higher-order-problem-solving/#making-meaning). Scrolling with inertia, where the view keeps scrolling when you lift your finger, but slowly decelerates until it comes to a halt, or until you put your finger back on the screen. Done well, it feels incredibly real, like a lightweight surface you can flick around in space easily, but that still seems to respect some laws of physics. And when you hit the edge of scrollable content, it doesn’t just stop, but instead makes you feel like you stretch a rubber band that becomes harder and harder to stretch the further you go.

What seems playful and unnecessary, turned out to potentially be the most important “feature” that made the iPhone a huge success and redefined every mobile user interface since then. Now every touch screen that doesn’t scroll like that feels broken.

There are many different approaches to technically simulate physics to make interfaces behave that way. Many of which aren’t that complicated, but they are still a lot more effort than not trying to simulate physics. So, arguably, not simulating physics in your user interface is “simpler”, but the result is unsatisfying and feels defective. Making that effort, however, and tuning it to feel really good makes a user interface much more intuitive and something people like to play with. Just because we are so familiar with objects respecting laws of physics, an interface that behaves like everything else we are used to becomes much simpler for us to navigate and explore. It just makes sense to us, regardless of the structural complexity that software designers and engineers needed to pull off to make it happen.

![](/images/e8daa9d6-aecf-459f-8132-5c8a282c0932.png)

Which brings us to another point I made in the [initial post of this series](/2023/10/27/on-simplicity/):

> 4. **Something incredibly complex can be amazingly simple.** 
> Simple things appear simple to us, when we are **familiar with their structure** and it makes sense to us. Once we familiarize ourselves with something, such that we deeply understand it, it becomes simpler to us. 
> **Its structure didn’t change. We did.** And that confuses the hell out of people who didn’t change with us. 
> This means simplicity and complexity are not opposite ends on a spectrum but less correlated and potentially independent dimensions.

This is different from what we usually mean when we talk about simplicity.

### Mechanical simplicity

Thanks to [a prevalent objective and scientific worldview](/2022/10/14/03-mind-vs.-matter/), we usually refer to the **mechanical complexity** of a thing: how easy it is to understand — how it is composed and how it works.

But this mechanical simplicity does not take into account that an observer can have intuitive understanding of incredibly complex patterns. This can make things that are extremely difficult to conceptually understand surprisingly simple to deal with intuitively.

Something might have a complex structure and behaviors that are difficult to explain, but as long as we are not looking for a mechanical explanation, but just interaction with it, and it behaves in ways that just make sense to us, we can have a much easier time to feel connected to it — [it feels more real to us](/2023/05/05/finding-meaning-in-the-nature-of-order/#4-ways-of-knowing).

And that realness translates into another kind of simplicity. It feels effortless to interact with something we intuitively understand, something we are intimately familiar with.

> Our modern conception of simplicity has gone wrong. **Simplicity as** ***depth*** **has been replaced by a mechanical idea of simplicity as the geometrically banal.** And most recently, in reaction to the banal simplicity of cubes and spheres, postmodernism has reintroduced complexity and ornament in a way that is too often merely dross, icing, fruitcake, and trinkets, overlaid on the fabric, shape and substance of our buildings.
>
> — Christopher Alexander, NoO.II.2.17[^1], *The drive to simplicity*

Alexander argues, architecture thinks of simplicity as the *geometrically banal*. 
I argue, software engineering thinks of simplicity as the *technically trivial*.

![](/images/636bfd12-58fe-40a0-9cbd-92eff389b37a.png)

### *Real* simplicity

Alexander proposes a different definition of simplicity, which has little to do with abstract, conceptual, propositional “understanding”. His version relies heavily on the relationships between things and ties directly into our [connectedness and sense of realness](/2022/12/23/13-agent-and-arena/) with our environment:

> The things we call simple in design — cubes, spheres — appear simple conceptually because they can be represented by simple mathematical schemes. But they are not, in any *real* sense, the simplest things which can be created at a given place and time.
>
> The simplest thing which can be created, in real terms, is **that thing which goes furthest to resolve, complete, hence to elaborate and underpin the structure of the world, its wholeness, which exists at that place**.
>
> In this sense a volcano, a cobweb, an oak tree are truly more simple… because as nearly as we can judge, they **perfectly resolve the forces, processes and conditions at that place, with the greatest economy of means and the greatest economy of form**.
>
> It is for this reason that **the simplest forms (“simplest” in this organic and complex sense) must be our targets in any conscious, human-inspired, human-engineered process** which aspires to the production of living structure. A process which purports to be a living one, but fails to create beautiful and living simplicity in the physical form it generates, must have something wrong with it.
>
> — Christopher Alexander, NoO.II.2.17, *What is simple?*

*Real* simplicity perfectly resolves the forces, processes, and conditions of the environment with the greatest economy of means and form.

We are part of the environment. 
We are part of and participate in these forces, processes, and conditions. 
When we design, we find ways to resolve them. And when we do it well, we may end up with something elegant and beautiful — something truly *simple.*

![](/images/a81dab68-d917-4c65-af3a-55e610dbd656.png)

### Context-dependence

The forces, processes, and conditions are dependent on the environment — on the context. This is the reason why every serious answer to a question like, “What would be the best way to resolve this?” has to start with, “It depends, …”

The mechanical approach looks for generic, universal, context-independent solutions. And while there is value in that to make scientific sense of the universe, something that does not respect its particular environment can never be properly adapted to that environment. **But it is deep adaptation and integration with the environment that yields us the specific, local, context-dependent connectedness that feels real and simple to us.**

The more familiar we are with a particular environment, the easier it will be for us to identify, influence, and resolve these forces, processes, and conditions. Our familiarity becomes an asset. And because of the nature of familiarity, we might not be consciously aware of our implicitly learned intuition that [subconsciously guides us in making good choices](/2023/03/03/20-flow-and-intuition/#intuition-and-bias).

It is easy to fall into the trap of looking for and assuming the existence of universally applicable generic solutions. Or that the objectively best design exists, we just need to find it. These kinds of solutions allure us with their promise of scalability, which is such a prominent force in our [current cultural climate](/2022/10/28/05-the-meaning-crisis/#headed-towards-collapse).

So much time is wasted in trying to convince others that we found the best design, the best architecture, the best programming language, the best platform, etc., ignoring that what works for us might work because we (and our team) are most familiar with it in our environment. Vim or Emacs? Forth or Lisp? Mac or PC? If it’s easy for you to pick a side, how much of that choice is based on your familiarity with one and your lack of familiarity with the other?

Instead of having fruitless conversations about which solution is objectively and universally better, we could learn so much from each other if we spend our time investigating how our environments differ. Then we could focus on the context-dependent forces, processes, and conditions, including our own familiarity and intuition, to find truly simple ways to resolve them.

> Economy, simplicity, drive the formation of ice on a pond. They drive the formation of flames in the fire. And they drive the formation and simplicity of what is most valuable in the sparseness of a simple room that contains hundreds of complex relationships boiled away almost to nothing, leaving only a quiet which approximates the void. […]
>
> Living structure may be understood, remembered, as that which remains behind from a continuous striving for the simple, and from the removal of dross. But this “simple” will be both simple and complex. It will be a deep structure capable of holding the most intricate content, yet boiled away, until nothing is left in it, except the few lines which awaken the heart.
>
> — Christopher Alexander, NoO.II.2.17, *All there is*

![](/images/9c56aa99-36e1-444f-a2a4-6ddab079bfdd.png)

---

Mirror of the Self *is a fortnightly newsletter series investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

*If you are new to this series, start here: [01 • A secular definition of sacredness](/2022/09/30/01-a-secular-definition-of-sacredness/). 
Overview and synopsis of articles 01-13: [Previously… — A Recap](/2023/01/06/previously-a-recap/). 
Overview and synopsis of articles 14-26: [Previously… — recap #2](/2023/04/28/previously-recap-%232/).*

*Another great way to start is my recent presentation [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/).*

[^1]: I’m trying something new here to have proper pointers to source material, but not waste so many words on repetitive information; at this point you should know that I’m citing a lot from Alexander’s *The Nature of Order*. The code means: book (in roman numerals) . chapter . section, section title; so in this case book 2, chapter 2, section 17. As usual, highlights in bold are mine, italics are Alexander’s.
