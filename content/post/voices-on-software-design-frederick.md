---
title: "Voices on software design: Frederick P. Brooks"
date: 2024-05-17T17:01:35Z
series: voices-on-software-design
---

I’ve been reviewing several classic programming papers about simplicity, complexity, and adjacent topics. Here I’m sharing some highlights from the papers and my thoughts about them.

Today’s paper is: [Frederick P. Brooks, Jr. • No Silver Bullet — Essence and Accident in Software Engineering (1986)](https://worrydream.com/refs/Brooks_1986_-_No_Silver_Bullet.pdf)

[Subscribe now](https://stefanlesser.substack.com/subscribe?)

## No Silver Bullet — Essence and Accident in Software Engineering

*Frederick P. Brooks, Jr. · 1986*

The famous distinction between *essential* and *accidental* complexity is from this paper. Brooks defines the essence of software — and therefore the source of *essential* complexity — as an abstract, conceptual construct that can be represented in many different ways (as usual, highlights mine):

> *The essence of a software entity is a construct of interlocking concepts: data sets, relationships among data items, algorithms, and invocations of functions. **This essence is abstract, in that the conceptual construct is the same under many different representations.** It is nonetheless highly precise and richly detailed.*
>
> *I believe the hard part of building software to be the specification, design, and testing of this conceptual construct, not the labor of representing it and testing the fidelity of the representation. We still make syntax errors, to be sure; but they are fuzz compared to the conceptual errors in most systems.*

[Like Naur](/2024/04/19/voices-on-software-design-peter-naur/), Brooks hints at the essence of software being [knowledge that cannot fully be represented in its various](/2022/11/04/06-four-ways-of-knowing/) *[propositional](/2022/11/04/06-four-ways-of-knowing/)* [representations](/2022/11/04/06-four-ways-of-knowing/). And our main job as software engineers is to figure out that abstract essence, which is compatible to Naur’s *theory* which programmers form about the problem they are trying to solve, and which goes beyond what is codified in the program text.

Notably, Brooks draws a clear boundary between the *inessential* representation and testing of the fidelity of the representation, and the *essential* specification, design, and testing of the conceptual construct. Again, the artifact or the code is secondary; what counts is building the theory in our minds.

### Software minimizes repetition

Brooks points out an interesting property of software that physical creations do not share: There is little to no repetition in software, because repetition is usually collapsed into a single construct — think of the DRY (Don’t Repeat Yourself) principle.

> *Software entities are more complex for their size than perhaps any other human construct, because **no two parts are alike** (at least above the statement level). **If they are, we make the two similar parts into one**, a subroutine, open or closed. In this respect software systems differ profoundly from computers, buildings, or automobiles, where repeated elements abound.*

There is lots to say about why this creates challenges with [our intuitive sense making](/2023/03/03/20-flow-and-intuition/#intuition-and-bias) — repetition is an incredibly important aspect for triggering our pattern recognition which fuels our implicit learning. We can only detect patterns if we can find similarities. In software we systematically try to get rid of them.

This partially explains why software also seems to grow more complex much faster:

> *Likewise, a scaling-up of a software entity is not merely a repetition of the same elements in larger size; **it is necessarily an increase in the number of different elements**. In most cases, the elements interact with each other in some nonlinear fashion, and the complexity of the whole increases much more than linearly.*

In a way, when we look at source code, we deal with a compressed representation of behavior that aspires to collapse all repetition. That hinders our intuitive pattern recognition and makes writing code by definition a more intricate analytic affair.

### Conforming to arbitrary interfaces

Brooks continues to define four inherent properties of the software essence:

- complexity
- conformity
- changeability
- invisibility

Conformity contributes to complexity in the form of conformance to arbitrary interfaces.

> *Software people are not alone in facing complexity. Physics deals with terribly complex objects even at the “fundamental” particle level. The physicist labors on, however, in **a firm faith that there are unifying principles to be found**, whether in quarks or in unified field theories. Einstein repeatedly argued that there must be simplified explanations of nature, because God is not capricious or arbitrary.*
>
> *No such faith comforts the software engineer. Much of the complexity he must master is **arbitrary complexity, forced without rhyme or reason by the many human institutions and systems to which his interfaces must confirm**. These differ from interface to interface, and from time to time, not because of necessity but only because they were designed by different people, rather than by God.*
>
> *[…] But in all cases, much complexity comes from conformation to other interfaces; this cannot be simplified out by any redesign of the software alone.*

Whether you think of it as God, nature, the universe, or evolution as an alternative designer that blessed us with wide-reaching and universal unifying principles, this is an interesting way to contrast [the arbitrariness of uncoordinated designs by many](/2023/05/26/mind-or-machine-who-cares/#infected-by-banality). God may not throw dice, but we certainly do when we design things.

### Constant pressure to change

Another source of complexity is a constant pressure to change.

> *All successful software gets changed. Two processes are at work. As a software product is found to be useful, people try it in new cases at the edge of, or beyond, the original domain. The pressures for extended function come chiefly from users who like the basic function and invent new uses for it.*
>
> *Second, successful software also survives beyond the normal life of the machine vehicle for which it is first written. If not new computers, then at least new disks, new displays, new printers come along; and the software must be conformed to its new vehicles of opportunity.*
>
> *In short, **the software product is embedded in a cultural matrix of applications, users, laws, and machine vehicles**. These all change continually, and **their changes inexorably force change upon the software product**.*

Software has to continually adapt to an ever-changing environment that includes user expectations and machine capabilities.

### The “invisible” conceptual nature of software

Brooks also emphasizes how the abstract, conceptual nature of software leads to cognitive problems of making sense of it — what he means by it being “invisible”:

> *The reality of software is not inherently embedded in space. Hence **it has no ready geometric representation in the way that land has maps, silicon chips have diagrams, computers have connectivity schematics**. As soon as we attempt to diagram software structure, we find it to constitute **not one, but several, general directed graphs, superimposed one upon another**. The several graphs may represent the flow of control, the flow of data, patterns of dependency, time sequence, name-space relationships. These are usually not even planar, much less hierarchical. Indeed, one of the ways of establishing conceptual control over such structure is to enforce link cutting until one or more of the graphs becomes hierarchical.*
>
> *In spite of progress in restricting and simplifying the structures of software, they remain inherently unvisualizable, thus depriving the mind of some of its most powerful conceptual tools. This lack not only impedes the process of design within one mind, it severely hinders communication among minds.*

As we try to make sense of software, we tend to reduce its real structure, which is difficult to grasp analytically, to simpler graph structures, preferably hierarchies, which we are much more accustomed to think with. We must not forget that by doing so we leave out certain connections that are no longer represented in our model, but still exist in reality. Every model we come up with is necessarily over-simplified, just to make it “thinkable” — to “fit it in our heads”.

### Great designs come from great designers

Brooks concludes with a key claim that rhymes with [Naur’s realization of how dependent we are on the people building the theory](/2024/04/19/voices-on-software-design-peter-naur/#a-theory-that-cannot-be-expressed-fully): Great designs come from great designers. As much as we may think certain techniques and processes may help, design is primarily a skill that needs to be performed by people who are good at it. Experience and tacit, deeper ways of knowing outperform whatever we achieve to capture in propositions.

> *Whereas the difference between poor conceptual designs and good ones may lie in the soundness of design method, the difference between good designs and great ones surely does not. **Great designs come from great designers. Software construction is a creative process. Sound methodology can empower and liberate the creative mind; it cannot enflame or inspire the drudge.***
>
> *The differences are not minor—it is rather like Salieri and Mozart. Study after study shows that **the very best designers produce structures that are faster, smaller, simpler, cleaner, and produced with less effort**. The differences between the great and the average approach an order of magnitude.*
>
> *A little retrospection shows that although many fine, useful software systems have been designed by committees and built by multipart projects, those software systems that have excited passionate fans are those that are the products of one or a few designing minds, great designers. Consider Unix, APL, Pascal, Modula, the Smalltalk interface, even Fortran; and contrast with Cobol, PL/I, Algol, MVS/370, and MS-DOS.*

### Software construction is a creative process

It seemed that we had reached a point in 1986 where it was obvious that the design and creation of software is impossible to mechanize and requires human experience and creativity to yield great results.

Almost half a century later, this view is challenged. Still. Instead of empowering and liberating creative minds [we attempt to enflame and inspire the ultimate drudge](/2023/05/12/modally-confused-ai/) — the computing machines themselves.

[Can machines become minds?](/2023/05/26/mind-or-machine-who-cares/) We will see how this plays out. Most of us will live and deal with the consequences in our lifetimes.

But what happened to those visions of empowering and liberating creative minds by augmenting their intellect and supporting their agency? 
Who’s still up for making progress with that? 
✋

---

[Share](/2024/05/17/voices-on-software-design-frederick-p.-brooks/)

Mirror of the Self *is a series of essays investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

***Series**: [Mirror of the Self](/series/mirror-of-the-self/) • [On simplicity…](/series/on-simplicity/) • [Voices on software design](/series/voices-on-software-design/) 
**Presentations**: [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/)*
