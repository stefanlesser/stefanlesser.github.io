---
title: "Voices on software design: Peter Naur"
date: 2024-04-19T17:01:10Z
series: voices-on-software-design
---

I’ve been reviewing several classic programming papers about simplicity, complexity, and adjacent topics. Here I’m sharing some highlights from the papers and my thoughts about them.

Today’s paper is: [Peter Naur • Programming as Theory Building (1985)](https://pages.cs.wisc.edu/~remzi/Naur.pdf)

## Programming as Theory Building

*Peter Naur · 1985*

Peter Naur confronts us with a perspective on programming that was certainly unusual back in 1985, and is unusual still: The objective of programming is not to create a program, but to cause insight. (As usual, highlights mine.)

> ***[P]rogramming properly should be regarded as an activity by which the programmers form or achieve a certain kind of insight, a theory, of the matters at hand.** This suggestion is in contrast to what appears to be a more common notion, that programming should be regarded as a production of a program and certain other texts.*

Much like how a plan is useless, but planning is indispensable, documentation is auxiliary to the knowledge that has been built up in the programmer’s mind.

> *[P]rogramming in this sense primarily must be the programmers’ building up knowledge of a certain kind, knowledge taken to be basically the programmers’ immediate possession, any documentation being an auxiliary, secondary product.*

It’s almost like he says the quiet part out loud. In 1985. That’s still not how we understand programming today. We don’t want to understand it like this. This is terrifying!

### A theory that cannot be expressed fully

Naur directly addresses the nature of such knowledge as impossible to be fully externalized.

> *The dependence of a theory on a grasp of certain kinds of similarity between situations and events of the real world gives the reason why **the knowledge held by someone who has the theory could not, in principle, be expressed in terms of rules**. In fact, the similarities in question are not, and cannot be, expressed in terms of criteria, no more than the similarities of many other kinds of objects, such as human faces, tunes, or tastes of wine, can be thus expressed.*

Even though the language differs, I see the acknowledgement of [non-propositional ways of knowing](/2022/11/04/06-four-ways-of-knowing/), and a clear realization that not all knowing can be reduced to propositions. Designing a system and writing a program causes deeper understanding on the procedural, perspectival, and participatory levels of knowing. As such, the theory and the programmers who have developed it cannot be separated.

> *A main claim of the Theory Building View of programming is that **an essential part of any program, the theory of it, is something that could not conceivably be expressed, but is inextricably bound to human beings**. It follows that in describing the state of the program it is important to indicate the extent to which programmers having its theory remain in charge of it.*

We are uncomfortably dependent on the programmers’ experience, and realizing this flies in the face of all arguments towards engineers being flexible resources that can be deployed to projects at will.

Even methodology needs to be subordinate to the programmer’s individual experience. There cannot be a universal “best” way of doing it; what is best is always [context-dependent](/2023/12/08/on-simplicity-%233-familiarity/#context-dependence) — and the programmers, their individual experience, and their team structure are all parts of that context.

> *Indeed, on this view the quality of the theory built by the programmer will depend to a large extent on the programmer’s familiarity with model solutions of typical problems, with techniques of description and verification, and with principles of structuring systems consisting of many parts in complicated interactions. Thus many of the items of concern of methods are relevant to theory building. Where the Theory Building View departs from that of the methodologists is on the question of which techniques to use and in what order. On the Theory Building View **this must remain entirely a matter for the programmer to decide, taking into account the actual problem to be solved**.*

All the “best architecture practices” talks you have listened to probably skipped over the fact that they were context-dependent and tried to sell you something as universal when it was in fact situational.

The naive view of a program just being a codified but complete representation of behavior that can theoretically be understood by anyone capable of reading the code is not realistic.

### Beyond correctness

Interestingly, the Theory Building View introduces a way to further distinguish modifications to source code beyond being functionally correct: they can be more or less conforming to the theory of the program. This gives us another way to judge the quality of these modifications beyond just their correctness.

> *On the basis of the Theory Building View the decay of a program text as a result of modifications made by programmers without a proper grasp of the underlying theory becomes understandable. As a matter of fact, **if viewed merely as a change of the program text and of the external behaviour of the execution, a given desired modification may usually be realized in many different ways, all correct. At the same time, if viewed in relation to the theory of the program these ways may look very different, some of them perhaps conforming to that theory or extending it in a natural way, while others may be wholly inconsistent with that theory**, perhaps having the character of unintegrated patches on the main part of the program. This difference of character of various changes is one that can only make sense to the programmer who possesses the theory of the program. At the same time the character of changes made in a program text is vital to the longer term viability of the program. **For a program to retain its quality it is mandatory that each modification is firmly grounded in the theory of it. Indeed, the very notion of qualities such as simplicity and good structure can only be understood in terms of the theory of the program**, since they characterize the actual program text in relation to such program texts that might have been written to achieve the same execution behaviour, but which exist only as possibilities in the programmer’s understanding.*

Note how Naur explicitly comments on properties like quality, simplicity, and “good structure” as fundamentally grounded in the theory of the program and therefore the person holding that theory in their mind. These criteria are not just dependent on the design decisions that have been codified in the written source code, but they require a capability to compare them to other design possibilities to judge their quality against, most of those existing only in the minds of the people who understand the theory of the program.

Different implementations can all be functionally correct and demonstrate the same correct behavior perhaps even verified by tests, but each correct implementation can be more or less consistent with the theory. Correctness alone is not sufficient to assess quality. For that, we also need to judge its conformance to the theory. Sounds like having [a coherent, intelligible theory](/2023/11/10/on-simplicity-%232-meaning-ful-design/) could help.

### More than just code

Where [Conway’s previously discussed paper](/2024/04/12/voices-on-software-design-melvin-e.-conway/) describes challenges with knowledge about a program through an organizational lens of managing teams, Naur gets deep into the nature of that knowledge and how it impacts good design on the level of the individual.

We cannot “do good design” without a good theory of the program, without a proper understanding of how the system works. This understanding, what he calls “theory”, is deeper than propositional knowing and impossible to fully externalize.

Even though it seems that everything relevant must be captured in the structural-functional organization of the system alone, in the code that defines it, it still relies on our subjective experience how we make sense of it. How we interpret the code, how we understand what is does and why it does it that way, determines the theory in our minds.

Whether we like it or not, the source code of a program is not sufficient to describe it completely. As we make sense of a program by studying its code and documentation, we build our own theory of it. And our theory will likely differ from the theory of the people who wrote it in the first place.

Keep that in mind next time you look at a codebase you are not [familiar](/2023/12/08/on-simplicity-%233-familiarity/) with.

---

[Share](/2024/04/19/voices-on-software-design-peter-naur/)

Mirror of the Self *is a weekly newsletter series investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

*If you are new to this series, start here: [On simplicity…](/2023/10/27/on-simplicity/)*

*The previous series starts here: [01 • A secular definition of sacredness](/2022/09/30/01-a-secular-definition-of-sacredness/). 
Overview and synopsis of articles 01-13: [Previously… — A Recap](/2023/01/06/previously-a-recap/). 
Overview and synopsis of articles 14-26: [Previously… — recap #2](/2023/04/28/previously-recap-%232/).*

*Also check out my presentation [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/).*
