---
title: Functional Programming Resources
date: 2017-11-18T21:42:33Z
---

## Start Here

These are my recommended resources to start with, if you are planning to go down the same path and learn functional programming.

- [★ Functional Programming Basics - What’s It All About?](https://pragprog.com/magazines/2013-01/functional-programming-basics)
  "Functional Programming is programming without assignment statements." This means data in memory is (mostly) immutable and that makes parallelism for multiple CPU cores much easier to reason about. This article is a very high-level introduction into one of the core concepts of FP and ties it to one of the main benefits. I do think there's more to it than that, but this should get you excited about it.
- [★ Professor Frisby's Mostly Adequate Guide to Functional Programming](https://drboolean.gitbooks.io/mostly-adequate-guide/content/)
  Thorough and practical introduction to functional programming concepts using JavaScript. Gets you up to speed quickly, and there's no weird syntax to get used to. A great resource to start with.
- [★ 📺 (30m) Functional programming patterns for the non-mathematician (cut)](https://www.youtube.com/watch?v=AvgwKjTPMmM)
  Good introduction on how you can practically use composition, lenses, (which are built on monoids, functors, applicatives, and monads) for nesting (composition), null checking (Maybe), error handling (Either), and accumulation (reduce) in JavaScript.
- [★ 📕 PureScript by Example](https://leanpub.com/purescript/read)
  PureScript's syntax and libraries are almost identical to Haskell's, and this book is much shorter and more practical. I'd recommend learning PureScript (and Haskell) by starting with this book.
- [★ Getting started with Haskell • Stack Overflow](https://stackoverflow.com/questions/1012573/getting-started-with-haskell/1016986#1016986)
  Gives you a high-level overview of what the journey of learning Haskell can look like. Several good pointers to articles and resources.
- [★ 📕 Haskell Programming from First Principles](http://haskellbook.com)
  Massive introduction into Haskell with lots of explanation and exercises. Some people find it too exhaustive, but I like this book much better than the free "Learn you a Haskell", although it's still very academic. It starts off with a very abstract introduction to lambda calculus, which I believe is an important basis to know about before diving into Haskell. It does make the first chapter a little strange — keep reading and don't judge the book until after chapter 2.
- [Mapping the Monado](https://blog.jfo.click/mapping-the-monado/)
  Pragmatic and honest introduction to monads. Also includes an excellent list of resources at the end.
- [★ Monoids, Functors, Applicatives, and Monads: 10 Main Ideas](https://monadmadness.wordpress.com/2015/01/02/monoids-functors-applicatives-and-monads-10-main-ideas/)
  Great summary of the key points on the four algebras that show up everywhere in Haskell (and are hiding in other languages as well).
- [Conal Elliott - Denotational Design: From Meanings To Programs](https://www.youtube.com/watch?v=bmKYiUOEo2A&t=3s)
  Conal shows how he designs a simple, functional API for a graphics manipulation framework from scratch and iterates on it to make use of already available algebraic structures that maximize reusability and minimize implementation effort.
- [★ Haskell Typeclassopedia](https://wiki.haskell.org/Typeclassopedia)
  Given how important it is to understand types in Haskell, this article explains the most abstract (read: used everywhere) type classes in great detail and helps form an intuitive understanding of functor, applicative, and monad.
- [★ Diehl: What I Wish I Knew While Learning Haskell](http://dev.stephendiehl.com/hask/)
  The first two sections *Basics* and *Monads* are packed with great practical tips and a solid foundation for understanding monads, an abstract concept that shows up everywhere in Haskell and functional programming.

## General

- [Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs](http://worrydream.com/refs/Backus-CanProgrammingBeLiberated.pdf)
  Influential article written in 1978 describing a functional system for computation which sounds a lot like what functional programming languages these days are built on.
- [📺 (60m) "I See What You Mean" by Peter Alvaro](https://www.youtube.com/watch?v=R2Aa4PivG0g)
  Entertaining presentation about modeling state with declarative languages. Many applicable concepts although it is understandably a little heavy on the relational language this talk is about.
- [From Higher-Order Functions to Libraries And Frameworks](http://raganwald.com/2016/12/15/what-higher-order-functions-can-teach-us-about-libraries-and-frameworks.html)
  How higher-order functions influence the expressiveness and complexity of programs. This is part 1 of a series of 3 articles.
- [Functional Programming is taking over UIs with Pure Views](https://medium.freecodecamp.com/the-revolution-of-pure-views-aed339db7da4)
  Why functional programming helps keeping the user interface layer simple and enables hot module replacement, time-travel debugging and similar features.
- [A Beginner-Friendly Tour through Functional Programming in Scala](http://degoes.net/articles/easy-monads)
  Introduces benefits of functional programming by transforming a simple console program from imperative to declarative step by step. Even though it's using Scala, it helps understanding the basic building blocks of FP and their benefits.
- [Destroy All Ifs — A Perspective from Functional Programming](http://degoes.net/articles/destroy-all-ifs)
  By replacing conditionals with lambdas, we can invert control and make our code both easier to reason about and more generic. Moving conditionals from places hidden in the deepest nested function up to the caller makes intent clear and prevents mistakes.
- [Sum Types](https://www.schoolofhaskell.com/school/to-infinity-and-beyond/pick-of-the-week/sum-types)
- [Evaluating cellular automata is comonadic](http://blog.sigfpe.com/2006/12/evaluating-cellular-automata-is.html)
- [Streaming Combinators and Extracting Flat Parallelism](http://futhark-lang.org/blog/2017-06-25-futhark-at-pldi.html)
- [Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire](http://eprints.eemcs.utwente.nl/7281/01/db-utwente-40501F46.pdf)
- ? 📕 Modeling Data with Functional Programming in R

## JavaScript

- [JavaScript without Loops](http://jrsinclair.com/articles/2017/javascript-without-loops/index.html)
  Looks at how map, reduce, filter, and find help separate iteration logic from what we actually want to achieve when working with arrays in JavaScript.
- [JavaScript. But less iffy.](http://jrsinclair.com/articles/2017/javascript-but-less-iffy/)
  Simplifying conditionals by returning early, using ternaries, and replacing control structure with data in JavaScript.
- [A Functional Programmer’s Introduction to JavaScript (Composing Software)](https://medium.com/javascript-scene/a-functional-programmers-introduction-to-javascript-composing-software-d670d14ede30)
- [Higher Order Functions (Composing Software)](https://medium.com/javascript-scene/higher-order-functions-composing-software-5365cf2cbe99)
- ? [📺 Functional Programming in JavaScript](https://www.youtube.com/watch?v=BMUiFMZr7vk&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84)

## Haskell

- [Learn Haskell the hard way](http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way)
  Just as promised in the title, an introduction to Haskell from zero to monads in a rather short article. I don't think this is a good tutorial to start with, but after reading about the concepts in other places, the additional examples and different ways of explaining monads in this article are very helpful.
- [Let vs. Where](https://wiki.haskell.org/Let_vs._Where)
  Very helpful article to understand where it is appropriate to use let or where.
- [💡 Scalable program architectures](http://www.haskellforall.com/2014/04/scalable-program-architectures.html)
  Explains the core concept of composition with monoids: combine several components together of type A to generate a new component of the same type A, indistinguishable in character from its substituent parts. These abstractions scale limitlessly because they always preserve combinability, therefore we never need to layer further abstractions on top.
- [💡 The category design pattern](http://www.haskellforall.com/2012/08/the-category-design-pattern.html)
- [💡 The functor design pattern](http://www.haskellforall.com/2012/09/the-functor-design-pattern.html)
  Functors are adapters that bridge between categories. Instead of rewriting functions for a different category, a functor allows you to re-use the existing function to work in another category.
- [Queer Types - Applicatives and Alternatives](https://queertypes.com/posts/59-applicatives-alternatives.html)
  Practical introduction into how applicatives (and alternatives, which build on it) can be used.
- [Foldable and Traversable](https://blog.jakuba.net/2014/07/30/foldable-and-traversable.html)
- [Haskell/Understanding monads/State](https://en.wikibooks.org/wiki/Haskell/Understanding_monads/State)
- [Scalable program architectures](http://www.haskellforall.com/2014/04/scalable-program-architectures.html)
- [Equational reasoning at scale](http://www.haskellforall.com/2014/07/equational-reasoning-at-scale.html)
- [📺 (20m) George Wilson - When Less is More and More is Less: Trade-Offs in Algebra](https://www.youtube.com/watch?v=VXl0EEd8IcU)
  Great overview of abstract algebra structures in Haskell, their laws, and which power we can derive from them.
- [📺 (1h:30m) C++Now 2017: Ryan Newton "Haskell taketh away: limiting side effects for parallel programming"](https://www.youtube.com/watch?v=lC5UWG5N8oY)
  Fascinating look into the direction and development of Haskell.
- [📺 Tangible Functional Programming](http://youtube.com/)
- [📺 (60m) Fastware - Andrei Alexandrescu](https://www.youtube.com/watch?v=o4-CwDo2zpg)
- ? [EdX course: Introduction to Functional Programming (via Haskell)](https://www.edx.org/course/introduction-functional-programming-delftx-fp101x-0)
- ? [Haskell Communities and Activities Report • 32nd Ed. May 2017](https://www.haskell.org/communities/05-2017/html/report.html)

### Practical Haskell

- [📕 Purely Functional Data Structures](https://www.cs.cmu.edu/~rwh/theses/okasaki.pdf)
  Proves that purely functional data structures can be as fast as imperative algorithms thanks to memoization and clever algorithm design.
- [📕 Real World Haskell • Bryan O'Sullivan, Don Stewart, and John Goerzen](http://book.realworldhaskell.org/read/)
  This book promises to teach more practical Haskell, which makes it a welcome alternative to all the academic books out there. *Haven't read it yet, so I don't know if that's true.*
- [📕 Parallel and Concurrent Programming in Haskell](http://chimera.labs.oreilly.com/books/1230000000929/index.html)
  This book gets mentioned and referred to a lot, surprisingly not just for topics around the book's title.
- [The Fun of Programming • Ch. 7 Functional Images](http://conal.net/papers/functional-images/fop-conal.pdf)
  Creating visual patterns with math based on transformation functions. Great example of how composing small components can yield complex effects.
- [📺 (45m) Manuel Chakravarty - Haskell SpriteKit: A Case Study in Turning a Stateful into a Functional API](https://www.youtube.com/watch?v=H_z4NKvxf1U&app=desktop)
- [Introduction to brick, a Haskell library for building terminal user interfaces](https://samtay.github.io/articles/brick.html)
- [Writing Video Games in a Functional Style](http://prog21.dadgum.com/228.html)
  A collection of articles exploring the implementation of arcade games and their game state and game loops in a functional style.
- [Code Us Some Roguelike in Haskell (Part 2)](http://jamiltron.com/2012/07/Code_Us_Some_Roguelike2.html)

### Haskell Resources

- [Haskell Wiki](https://wiki.haskell.org/)
- [Hoogle](https://www.haskell.org/hoogle/) — Enter a type signature and it will find you matching functions
- [Hayoo](http://hayoo.fh-wedel.de/) — Same but with support for third-party packages
- [Vim and Haskell in 2016](http://www.stephendiehl.com/posts/vim_2016.html) — How to set up your dev env with vim for Haskell

## PureScript

- [📺 Luka Jacobowitz - Reactive Programming in the Browser with Scala.js and PureScript](https://m.youtube.com/watch?v=pE-3bg31Jlo)
- [📺 Intro to PureScript - Utah Haskell Meetup](https://m.youtube.com/watch?v=9a57V3bvzaI)
- [📺 PureScript & Pux ~ Front End Authority (Oct 2016)](https://youtu.be/NmT5-j3-xzg)
- [Pux](http://purescript-pux.org)

## Swift

- [📺 (45m) Brandon Williams - Finding Happiness in Functional Programming](https://www.youtube.com/watch?v=A0VaIKK2ijM)
  Exploring the benefits and downsides of functional concepts in practical use, from isolation of side (and co-)effects to coding for an interface we wish we had instead of the one we're given. Great points about how to encapsulate state management with lenses using UIKit as an example.
- [📺 (10 Talks) Functional Swift Conference 2017](http://2017.funswiftconf.com)
- [💡 📺 (25m) Brandon Kase: Composable Caching in Swift](https://www.youtube.com/watch?v=8uqXuEZLyUU)
  Using a monoidal structure to simplify layered caching with composable caches.
- [💡 📺 (40m) Brandon Kase: Beyond Types in Swift](https://m.youtube.com/watch?v=6z9QjDUKkCs)
  Adding functionality without adding complexity through abstract algebra:
  - Magma: closed binary operators = composable operation
  - Semi-group: + associativity = parallelization
  - Monoid: + identity = dropping the optional
  - Commutative Monoid: + commutativity = reorder
  - Bounded Semilattice: + idempotence = no need for memory
- [💡 📺 (40m) Monoids, Predicates and Sorting Functions](https://www.youtube.com/watch?v=VFPhPOnPiTY)
  This demonstrates the practical application of the other Brandon's talk above with live coding in Swift Playgrounds. Impressive composability of the simplest components by building them up following the rules and laws.
- [Swift Enums Are "sum" Types. That Makes Them Very Interesting](https://mislavjavor.github.io/2017-04-19/Swift-enums-are-sum-types.-That-makes-them-very-interesting/)
  Explains product and sum types and shows how they can be used to minimize possible use cases and define away potential error states. With examples for use cases for sum types (enums) like router and theme patterns and tree data structures.
- [Algebraic Structure and Protocols](http://www.fewbutripe.com/swift/math/algebra/2015/02/17/algebraic-structure-and-protocols.html)
  This article takes a mathematical approach to introduce monads through semigroups.
- [The Algebra of Predicates and Sorting Functions](http://www.fewbutripe.com/swift/math/algebra/monoid/2017/04/18/algbera-of-predicates-and-sorting-functions.html)
  Extends the knowledge about semigroups and monoids to introduce predicate and sorting functions.
- [📺 (30m) Brandon Williams - Lenses in Swift](https://www.youtube.com/watch?v=ofjehH9f-CU)
  Using lenses and prisms to create getters and setters for immutable values.
- [An aside about flatMap and monads](https://www.cocoawithlove.com/blog/an-aside-about-flatmap-and-monads.html)
  Practical notes on Monads in Swift and Haskell, and how Swift's flatMap sometimes is a proper monad and sometimes isn't (and why that's totally fine).
- [Composable HTML Views in Swift](http://www.fewbutripe.com/swift/html/dsl/2017/06/29/composable-html-views-in-swift.html)
  Improving an eDSL for generating HTML in Swift with the powers of abstract algebra in form of Monoids.
- [Swift — memoize() walk through](https://medium.com/@mvxlr/swift-memoize-walk-through-c5224a558194)
- [Functional Swift and Memoization](http://blog.scottlogic.com/2014/09/22/swift-memoization.html)
- [📺 (20m) Optimizing Swift Collections • Károly Lőrentey at dotSwift 2017](https://www.dotconferences.com/2017/01/karoly-lorentey-optimizing-swift-collections)
  Deep dive into performance characteristics of Swift Collection types.
- [Apple Swift Ownership Manifesto](https://github.com/apple/swift/blob/master/docs/OwnershipManifesto.md)
- [The Elm Architecture in Swift](https://github.com/chriseidhof/tea-in-swift)

## Category Theory

- [Haskell/Category theory](https://en.wikibooks.org/wiki/Haskell/Category_theory)
  After being familiar with using functors, monoids, and monads in Haskell, this article introduces just enough category theory to understand the maths behind those concepts.
- [📺 (60m) Category Theory for the Working Hacker by Philip Wadler](https://www.youtube.com/watch?v=V10hzjgoklA)
  If you want to take it an abstraction level higher, this surprisingly entertaining talk explains the math behind lambda calculus called category theory.
- [Monads Made Difficult](http://www.stephendiehl.com/posts/monads.html)
  Explains monads coming from category theory. This is only helpful if you enjoy the math a lot.
- [Duality for Haskellers](http://blog.ezyang.com/2012/10/duality-for-haskellers/)
  Explains the concept of duality in category theory using sum/product, top/bottom, and fold/unfold on lists.
- [Flipping arrows in coBurger King](http://blog.ezyang.com/2010/07/flipping-arrows-in-coburger-king/)
  Explains co-monad and duality and the concept of "flipping arrows" in category theory.
- [Data and Codata](http://blog.sigfpe.com/2007/07/data-and-codata.html)

## Functional Patterns to Manage Complexity

- [💡 📺 (60m) Gabriel Gonzales: Applied category theory and abstract algebra - λC Winter Retreat 2017](https://www.youtube.com/watch?v=WsA7GtUQeB8)
  "[We can] tackle software complexity by reusing standard interfaces that originate in the fields of category theory and abstract algebra." Builds understanding for composition going from composable functions to composable values (monoids) to composable types (applicatives) and shows how powerful these concepts are to decompose programs into simple building blocks.
- [💡 A Modern Architecture for FP](http://degoes.net/articles/modern-fp)
  "We shouldn’t write programs — we should write descriptions of programs, which we can then introspect, transform, and interpret at will." How to architect a program that uses separate layers of DSLs to encode business logic in separate domains, and having an interpreter combining those DSLs to generate the actual program. It seems cumbersome to do this, but the composability of this approach looks promising.
- [💡 Modern Functional Programming: Part 2](http://degoes.net/articles/modern-fp-part-2)
  John edited his thoughts in part 1 into a more coherent and clear picture in this article and gives a glimpse into the future of programming by combining interpreters for different DSLs.
- [📺 (45m) Sandy Maguire: Don't Eff It Up: Free Monads in Action](https://www.youtube.com/watch?v=gUPuWHAt6SA)
  Shows a technique to combine different side effects with free monads using the Eff(ects) monad, which can be used as an alternative to monad transformers with less boilerplate.
- [📺 (40m) John A De Goes: MTL Versus Free Deathmatch - λC 2016](https://www.youtube.com/watch?v=JLevNswzYh8)
  Fun talk diving deeper into John's thoughts about the future of programming with abstract functional structures generating and manipulating the program before it's being executed.
- [📺 (1h:15m) John DeGoes: Beyond Free Monads - λC Winter Retreat 2017](https://www.youtube.com/watch?v=A-lmrvsUi2Y)
  More thoughts about John's vision of programming with abstract functional concepts and why we need a better programming language to actually make that future happen.
