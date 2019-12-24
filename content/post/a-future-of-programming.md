---
title: A Future of Programming
date: 2019-12-24
categories:
- Beyond Code
---

Part 2 of my blog chain _Beyond Code_. Start [here]({{< ref "democratize-programming" >}}).

---

# ~~The~~ A Future of Programming
There are so many directions to explore to [democratize programming]({{< ref "democratize-programming" >}}). It's useful to be opinionated, make some choices upfront, and shrink the solution space a bit. You might disagree with my choices here, and that's ok. I write them down so we can find out quickly. That doesn't mean other directions are wrong or less promising, this is just the direction I am headed.

Read these principles as "one is more valuable than the other" — both sides have value, I just value one more than the other.


## Audience

### Augment human intellect > replace human intellect
[*Augment* human intellect](#augmenting-human-intellect). Don’t try [to replace it](#two-philosophies).

### Tools for everyone > better tools for experts
Everyone can create. Enable everyone, especially people from other domains outside programming, to take advantage of computation. Empower people to build their own systems and tools, giving them more of the powers that have only been available to programmers through writing code, so they can augment their own workflows in their own areas of expertise.

### Less, but better > complete
A small tool that works well for a single domain is more valuable than a generic tool that tries to be everything to everyone. A working solution that delivers value to a small group of people is valuable, even if it is not as expressive as a general programming language.

### Workflows > apps
Blur the line between developers and users. Enable people to modify the systems and tools they use and adapt them to their needs. Crack open the monolithic app model and expose finer-grained components and workflows to be combined in new ways. Apps can still coexist as a delivery mechanism for pre-packaged workflows that can be re-designed and potentially even integrated across different apps.

### Learn the craft > write code
Help people discover the craft of modeling by letting them build, explore, manipulate, and understand complex interactive systems in an approachable and entertaining way. Perhaps, writing code as translating a mental model of a complex system into a representation a computer can understand is part of that. Perhaps it's not.


## Experience

### Explore & experiment > plan & implement
Encourage exploration and experiments. Don’t expect people to already know what they want or need, let them discover through playful exploration. _Creation is discovery.[^BV1]_  

### Empathy > Proficiency
Make mistakes impossible (e.g. no syntax or type errors) or easy to revert (e.g. undo and redo, history graphs, time travel debugging). Move technicalities and implementation details (e.g. memory management) out of the way, but keep them accessible. Treat failure states as teaching opportunities.

### People-centric > System-centric
People should not have to adapt to the tool; the tool needs to adapt to people. If using the tool effectively is only possible if you understand how the tool works, it needs more work until it works more like you think.

### Direct (visual) manipulation > Think like a computer
Leave the limits of text-based editing behind. Design and build complex systems by exploring and manipulating visual, interactive representations of structure and behavior in real-time with immediate feedback. Instead of simulating algorithmic computation in our heads, leverage our unique abilities of embodied cognition.

### Immediate feedback > Distinct modes
Blur the lines between designing, building, and running the system; ideally there is no distinction between these modes. Minimize perceptible waiting times (like there are today for building or compiling). The system runs continuously and is modified directly — like shaping a digital material in real-time.

### Declarative > Imperative
Describe *what* instead of *how*; prefer declarative over imperative ways to describe aspects of a system. Turn the how into an implementation detail. Leave extension points for different implementations.

### Value people's privacy
Use as little data as necessary. Leave people in full control over their data. If you need to store user data, prefer local storage over servers, only store it encrypted, with only the user being able to decrypt it. Use end-to-end encryption. Avoid logging and analytics, and use [differential privacy](#differential-privacy) if you do.


## Technology

### Mobile > Desktop
Design for mobile first: small screens and touch interfaces on phones and tablets. Leverage mobile device capabilities. It should be possible to design complex systems on a smart phone. It’s ok if it’s more comfortable on a big screen, but there's not reason why it shouldn't be possible on a small screen.

### Distributed > Centralized
Prefer local over remote resources. Don’t push computation out to the network if it can be done locally. Enable as much functionality as possible offline, without access to a network. Consider performance and respect device limitations like connectivity and battery usage.

### Native > Web
Prefer fewer abstraction layers and develop as close to the hardware as feasible. Typical web applications are built on a complex stack of OS, web browser, language runtime, and libraries that introduce complexity, and with it a broader attack surface for security and performance issues. Keep the stack small. Remove dependencies when you can and it is economic to do so.

### Platform-specific > Cross-platform
Respect people's choice for a platform and deliver an optimized experience deeply integrated into that platform. Leverage platform-specific capabilities to provide a better experience.

---

*To be continued…*

## Further reading

* <a name="augmenting-human-intellect"></a>Douglas Engelbart: **Augmenting Human Intellect: A Conceptual Framework** \
	Douglas Engelbart outlines his vision to use computers not just for automation, but to augment human intelligence.
	<http://dougengelbart.org/content/view/138/000/>
* <a name="two-philosophies"></a>Ben Thompson: **Tech's Two Philosophies** \
	Ben Thompson contrasts two philosophies in Big Tech: Google and Facebook vs. Microsoft and Apple.
	<https://stratechery.com/2018/techs-two-philosophies/>
* <a name="inventing-on-principle"></a>Bret Victor: **Inventing on Principle**\
	<http://worrydream.com/#!/InventingOnPrinciple>
* <a name="differential-privacy"></a>Wikipedia: **Differential Privacy**\
	<https://en.m.wikipedia.org/wiki/Differential_privacy>

[^BV1]: Many breakthroughs were accidents, discovered along a path that was supposed to lead somewhere else. That's why creators need immediate connection with what they are creating and a tight feedback loop that enables them to see changes without delay.\
 –> [Inventing on Principle, Bret Victor](#inventing-on-principle)