---
title: "On Apple's Love Affair With Swift"
date: 2018-06-20
---

I wanted to write a thoughtful article in response to [Dominik Wagner's "On my misalignment with Apple's love affair with Swift"](http://rant.monkeydom.de/posts/2018/06/10/on-my-misalignment-with-apple_s-love-affair-with-swift). During my research I realized, that Chris Lattner had already done this. Sort of. 17 months *before* Dominik published his piece.

Thanks to [Marco Arment](https://marco.org/), [Casey Liss](https://www.caseyliss.com/), and [John Siracusa](http://hypercritical.co) for recording a fabulous "not an interview show" with [Chris "extraordinary circumstance" Lattner](http://nondot.org/sabre/) back in January 2017, asking the right questions, and even [publishing a transcript](http://atp.fm/205-chris-lattner-interview-transcript).

I give you *Accidental Tech Podcast #205 - People Don't Use the Weird Parts*, the *Apple Love Affair Remix*:

Dominik Wagner:

> First of all: Which question did it desire to answer? Think about it. There is no one clean answer. It just wanted to be better, more modern, the future – the one language to rule them all. A first red flag for anyone who ever tried to do a 2.0 rewrite of anything.

Chris Lattner:

> The fundamental problem was Objective-C was built on top of C. C inherently has pointers. It has uninitialized variables. It has array overflows. It has all these problems that even if you have full control of your compiler and tool stack, you just can't fix. To fix dangling pointers, you would have to fix lifetime issues, and C doesn't have a framework to reason about that, and retrofitting that into a compatible way into the system just wouldn't really work.

> If you took away C from Objective-C, you couldn't use C arrays on the stack, for example. And if you couldn't do that, there's entire classes of applications where the performance just wouldn't be acceptable. We went around, around, around. We said the only way that this can make sense in terms of the cost of the disruption to the community is if we make it a safe programming language: not “safe” as in “you can have no bugs,” but “safe” in terms of memory safety while also providing high performance and moving the programming model forward.

[Swift.org](http://swift.org/about/):

> **Safe.** The most obvious way to write code should also behave in a safe manner. Undefined behavior is the enemy of safety, and developer mistakes should be caught before software is in production. Opting for safety sometimes means Swift will feel strict, but we believe that clarity saves time in the long run.

Chris Lattner:

> One of the best and most annoying things about Objective-C is that it has C in it. This has been hugely important for Objective-C in practice, because if you run into a performance problem with objc_msgSend, you can always rewrite that algorithm in C. That's really, really, really important for Objective-C being successful in both in the days of NeXT on 16 MHz processors and also today for the low-level code that people are writing. That’s also one of the problems that makes it so that Objective-C and C are so intertwined that you can't actually take the C part out of Objective-C without producing a different language.

[Swift.org](http://swift.org/about/):

> **Fast.** Swift is intended as a replacement for C-based languages (C, C++, and Objective-C). As such, Swift must be comparable to those languages in performance for most tasks. Performance must also be predictable and consistent, not just fast in short bursts that require clean-up later. There are lots of languages with novel features — being fast is rare.

Chris Lattner:

> I think that the people in the core team, the other people working on Swift, have looked at many, many other languages. If you're a Haskell nerd, there is tons of Haskell concepts built in. Protocols really are just like a very similar Haskell construct, for example. It's really about taking the best ideas from where we can get them and assembling them together. One of the major goals of Swift is for it to be familiar-feeling, because that makes it easier for people to pick up and they're not fighting unnecessary barriers that just get in the way of adoption.

> It being familiar is actually a success in that way, and it's not a result of Swift trying to be Go or C# or whatever, it's about taking the best ideas from them and assembling them together. I think that you can probably pick a language and there's some good idea that came from them including D or Dart or Go or whatever. Swift does really draw from many, many different sources and it's really hard to tease them all out.

[Swift.org](http://swift.org/about/):

> **Expressive.** Swift benefits from decades of advancement in computer science to offer syntax that is a joy to use, with modern features developers expect. But Swift is never done. We will monitor language advancements and embrace what works, continually evolving to make Swift even better.

----

Dominik Wagner:

> * It should scale from App/UI language down to system language.

Chris Lattner:

> Systems programming is, I think, the big next frontier, and I think that's where Swift can really distinguish itself from Java or other competitive languages, because among the widely used languages out there, there's really nothing that can unseat C or C++. Rust, for example, is an interesting language, but it hasn't gotten a lot of adoption yet and I think that Swift is more interesting than Rust in some of the higher-level application demands, but we'll see. Rust is a great language as well.

> I'm really interested to see the Swift-for-systems-programming work get going. I think that'll be a couple of years out before it really comes together, but once it does, I think that Swift can really be the next big thing and I'm excited about that. \[…\]

> I don't think it's reasonable for me as a crazy man going around saying, "Swift will someday do systems programming really well. You should remember that." I don't think that's a good way to spend time at the moment.

> When it does that, then the question becomes how do you make people aware of that and how do you get people to change their prior misconception? But at that point in time, you can have a very practical, “Look, you can do this, and this is so great, and now you get all the advantages of C but it's safe.” You can point to specific reasons why it's better.

----

Dominik Wagner:

* It is functional, object-oriented and protocol oriented all at the same time.

Chris Lattner:

> Swift also has a lot of things that just make common things easier. You can switch on a string, for example, and match the different cases. You can use enums — enums are just from the language geekery world of just algebraic data types. They're in tons of different functional languages. They're not novel by any means, but they're so useful and they solve so many problems just out of the box. Just having them at your fingertips is great. There's a lot of things about Swift and it probably depends on who you are, what you're experiences are. \[…\]

> If you look at Swift over time, Swift 1 and Swift 2 are as similar to Objective-C as we could make them. If you look at the way that selectors are named, for example, there's a very direct correlation. If you look at the way Swift 1 was explained to people, it was explained to people as, it's just like Objective-C. You can use all your same patterns. You can use all the same frameworks. You can continue doing objecting-oriented programming. You can do all these things, but it also has some cool new things like enums and pattern-matching and these other things. It's great because it's just cleaned up syntax for what you already know plus it has some cool new stuff that you can play with.

> Then you fast forward a year or two and the Swift community was really taking off. People were understanding what Swift was about. Swift open-source also enabled this. And Swift 3 is really about Swift becoming its own language that was really true to itself and stands by itself. That's where you see the method call syntax, for example, being radically changed and a lot of things coming together and really focusing and polishing the language.

----

Dominik Wagner:

* It is compiled and static, but emphasized the REPL and playground face that makes it want to look like a great scripting solution. Which it isn't.

Chris Lattner:

> I think the scripting side of it is maybe more straight-forward when the Swift community and the core team have time to deal with it, because they're talking about integrating regular expressions, multi-line string literals, and other features like that that people love from scripting languages. Those are big projects, but those are kind of well-known, I guess, and they will fit and drop right into the existing system that Swift provides.

----

Dominik Wagner:

* It seems to have been driven by the needs of the compiler and the gaps that needed to be filled for the static analyzer. Those seem to have been super-charged instead of catering to app developer's actual needs: efficient, hassle free, productive (iOS) App development.

Chris Lattner:

> What we realized in the Swift 3 timeframe is that the thing app developers would benefit from the most was actually source stability. Who actually wants their application to be broken when they get a new version of Xcode? Really nobody, right?

> Halfway through the release, we pivoted and source stability became the goal, so I'm really excited that when Swift 3.1 or Swift 4 comes out that it's still going to be able to build Swift 3 code, and even if there are minor changes that need to be made for one reason or another, that you can upgrade and you have great compatibility with your old code and you don't have to start the migrator before you can do anything. So it's going to be a great improvement for people's lives. \[…\]

> I think it's also an interesting question of whether ABI stability will be done for Swift 4 because it's huge amount of work. The work is well underway of course, but it's also not clear to me that's really the most important thing for the Swift community. One of the things that Ted [Kremenek] has been a huge champion for, and I think he's right about, is that the most important thing right now for the Swift community is making the compiler more reliable, making the error messages better, making compile times faster, and making it scale better to large projects. We'll see how the rest of the Swift 4 schedule goes, but I wouldn't be surprised if, at some point, they decide that focusing on that is more important than nailing ABI stability in Swift 4.

----

Dominik Wagner:

> * It is meant to offer progressive disclosure and be simple, to be used in playgrounds and learning. At the same time learning and reading through the Swift book and standard library is more akin to mastering C++. It is quite unforgiving, harsh, and complex.

Chris Lattner:

> Here's the way I look at it. You’re unlikely to run into anybody that says that Swift is a simple language. Swift is a complicated language. It's not simple in the sense that Scheme is simple, for example. It's also not simple in terms of when you talk to an Objective-C developer, they'll often claim that Objective-C is simple, ignoring all the C parts.

> C itself is a very complicated, weird language. It's just that people don't typically use the weird parts, and so they perceive C as being very simple. The way I project this onto Swift is that the secret to Swift and being easy to learn, easy to use as a teaching vehicle, but also powerful enough to solve the problems that need to be solved, is that the complexity inherent in the language needs to be progressively disclosed.

> Imagine if someday Swift had inline assembly support, for example. Only really low-level systems people or really bit-twiddling assembly programmers would use this feature, everybody else would ignore it, and it would not increase the apparent complexity of the language to people who didn't know what it was. For a feature like that, the most important thing is to make the syntax clear so that when you run up into it, you discover it in somebody else's code, you know that you don't know what it does. So you say, "That's interesting. I don't know what that is," and then you can do a search and find out, find the Stack Overflow article or whatever it is, to explain what this is to me. And then you can say, "Oh, I get it," and I either care or I don’t, but at that point in time you can dive in and learn more information.

> Assembly is never something that a Swift Playgrounds person working through Learn to Code 3 would ever want to know about. I think that one of the secrets to Swift's success in terms of getting people on board and being really approachable for people at all levels is that, just like in Python, you can start with just print(“Hello world”). You can do the exact same thing in Swift, and with Swift you don't need the “\n” on your string. It's really just print(“Hello world”). From there you can then introduce new concepts, you can grow it out over time, and this really allows people to understand either the syntax of the language or the conceptual programming things that they're learning as they go. The design of Swift is really geared around that.

> What that means if you project onto the systems programming features, comparing Swift to Rust, for example, I think it's very likely that Swift will get features for memory-ownership control, which will allow really, really high performance: it will allow solving performance problems with ARC, for example. Unlike Rust, we can't make that be a core part of the type system that everybody has to use. It has to be something that sufficiently smart programmers, when they're solving a specific performance problem, end up using, or an embedded-kernel programmer might want to use, but an application developer can completely ignore. That’s really the challenge: it’s deploying similar type-system mechanics and other low-level language geekery to the problem, but do so in a way that is tasteful and allows most normal people to just ignore it.

----

Dominik Wagner:

> It keeps defering the big wins to the future while it only offered a very labour intensive upgrade path. Without a steady revenue stream, many apps that would have just compiled fine if done in Objective‑C, either can't take advantage of new features of the devices easily, or had to be taken out of the App Store alltogether, because upgrading would be to costly. If you are working in the indie dev-scene, you probably know one of those stories as well. And while this is supposed to be over now, this damage has been done and is real.

Chris Lattner:

> I think it's definitely fair to say that in the Swift 1 and 2 timeframes, Swift as a language was changing really rapidly, and I could see why you'd feel like you're on uneven footing and not really sure what the language is, much less what the idioms are. Swift 3 really is quite well baked out, and I expect that going forward the new things are going to be additive, not changing the existing patterns. I think the Swift community in general has gone through the same kind of thing that you're feeling there, where it's not really clear the one right way to solve the problem, and maybe there are different good ways to do it with different trade-offs that weren't clear to people. I think people are starting to understand that now.

----

Dominik Wagner:

> On top of all of this, there is that great tension with the existing Apple framework ecosystem. While Apple did a great job on exposing Cocoa/Foundation as graspable into Swift as they could, there is still great tension in the way Swift wants to see the world, and the design paradigms that created the existing frameworks. That tension is not resolved yet, and since it is a design conflict, essentially can't be resolved. Just mitigated. From old foundational design patterns of Cocoa, like delegation, data sources, flat class hierarchies, over to the way the collection classes work, and how forgiving the API in general should be.

> If you work in that world you are constantly torn between doing things the Swift/standard-library way, or the Cocoa way and bridging in-between. To make matters worse there are a lot of concepts that don't even have a good equivalent.

Chris Lattner:

> Swift does support all the features for dynamic dispatch and method lookup and everything else that Objective-C does, it just requires you to use the Objective-C subset of the language because it exposes it through the run time. \[…\]

> I look at that as an area where the language is not fully baked out, it’s not fully serving their needs, and I think that's really unfortunate.

> That's not a good thing. I want there to be an awesome reflection model. I want there to be awesome features for sending messages like they're used to. I just want it to be developed and designed in the right way, and at the same time they're being annoyed that they can't do those things, there are a lot of other people being annoyed about compile times.

> What we have to do is balance between — just picking two random things — where does the engineering effort go? That's never a black and white thing. There's never a right answer. It's all based on gut and judgment and guesses, listening to the community, and talking to people. \[…\]

> That insight is what guides the priority decisions and the trade-offs that have to be made all the time, because nothing really is as clear as you'd like it to be.

----

Dominik Wagner:

> This, for me at least, generates an almost unbearable mental load. It leads to writers block and/or running around in cognitive circles trying to answer questions on how to best express the problem, or make Swift be happy with my code.

> To add insult to injury, all this attention is taken away from solving and focussing on the actual problem: writing a great app or framework that is a joy to use. Whereas Objective‑C/Cocoa always strived for maximum developer productivity and purpose.

> Yes, Swift code might end up being more correct in the end. It also might alert you to edge cases early on. However, the flip side is it inhibits your creativity while writing. When starting out to program, the way I enjoy working, I don't yet know how the API is best expressed. So I try out different ways to express it until I find a sweet spot. Then I go back and unify accordingly.

> Swift actively distracts me in that endeavor by making me answer questions I really don't want to answer right now. Yes, stuff might be less correct in the meantime, but heck that is what I want during the design phase. Find my concept, sweet spot, iterate, pivot quickly.

Chris Lattner:

> Swift, in its name, kind of connotes a whole bunch of different things including performance. But really, to me, the most important aspect is programmer productivity.

> The idea that Swift is really optimizing for is not letting you pound out the code as fast as possible — it really is designed and optimized for, as a programmer, you can spend the least amount of time to get to a working program as fast as possible.

> Getting to a working program includes the time it takes to debug something, to iterate and develop and fight the type system, and all the other things you have to do. But that time you spend having to fight the type system or figure out optionals or things like that pays itself back because your program works more often. You're actually not spending time chasing own dangling-pointer bugs or, in the case of Objective-C, you get an unrecognized-selector error, whatever those kinds of bugs are, and Swift tries to help you by the language guiding you and helping design things. \[…\]

> I think the challenge that Swift faces is because its focus is on building programs that work and that can be maintained and all the other things that we care about for large scale software, it’s maybe not the best solution for, “I want to pound out a quick script, use it once, and then throw it away.” In that case, you don't care about maintenance. You can fit all the code in your head. You don't care about good documentation or the other things that Swift encourages. That's a case where having a dynamic type system can be really liberating, so maybe that'll be a challenge for some people. But I think that as Swift gains ecosystems and libraries, its other advantages will be so great that hopefully it will be a good solution for those kinds of scripts as well.

----

Dominik Wagner:

> So my opposition to Swift is very deep – on a fundamental design level. I see it as the devil on your shoulder, always fighting for your attention away from your problem domain, back to how everything is completely correct, or more swifty. And at the same time it is very unforgiving towards bigger change - ever tried to switch code from objects back to structs, or vice versa?

Chris Lattner:

> I think that Swift really does encourage you down the right lines in some ways. But on the other hand, in other places where you're saying, "Should something be a class or a struct?”, the trade-offs are more nuanced and it's a harder thing, and the Swift compiler can't just know what problem it is that you want to solve, so it can't help you with that.

----

Dominik Wagner:

>  Just imagine a world where Objective‑C would have gotten the same amount of drive and attention Swift got from Apple? It is not a big leap to see that everyone would be better off right now. Swift just ended up being a jack of all trades, master of none.

Chris Lattner:

> Eventually, \[Swift\] got to the point where it was far enough along that it was posing strategic questions. The strategic questions were of the form: We have Objective-C. Objective-C is a great language. It is probably directly responsible for the iPhone being successful because it's really high-performance. It allows you to get your job done. It supports high-level frameworks in a beautiful way. There's a ton of stuff to love about Objective-C, and while there are a few things that are ugly about it, some “@“ signs and semicolons and other stuff like that, we can make Objective-C better. The question was always: Why not just make Objective-C better? Why don't we just keep evolving Objective-C? Why do we want to face potential disruption in terms of moving the entire development community to something new?

> We kicked that around for a long time. We talked about both sides and we came to realize that, yes, we can and should make Objective-C better, and we continued to invest in Objective-C. \[…\]

> We were talking about, okay, can we just make Objective-C better and can we feature-creep it to the language we want for the fullness of time? Because if we can, that would be much less disruptive to the community. We decided that, yeah, we can move Objective-C a lot closer to what we want so we can get automatic memory management with ARC, for example, but we can't ever take away the problems that lead to Objective-C being unsafe.

> One great example of that is ARC. It was really clear to me that if we were to get to memory safety, we had to have automatic memory management. I don't know if you want to go down the GC-versus-ARC rabbit hole or not, but ARC seemed like obviously the right model to me and to some other people. So we said, "Okay, we need to get to an automatic memory management model.” Objective-C isn’t, because at the time it had the Obj-C garbage collector which had numerous problems, so we have to get Objective-C to be memory-managed. That's why ARC became a thing. It became a really high priority, and I think that it's a great example of something that, by itself, had a huge amount of value to the Objective-C community. Then, after that, we had similar other efforts like modules, for example, that was a huge thing that both improved build time but was also absolutely essential to enabling Swift code to eventually just say "import UIKit" and get everything.

> There's a number of things that rolled out over the years, and it was really funny at the time because the Objective-C developers externally and even internally to Apple always accused the compiler and language team of taking Objective-C on this random walk, and they didn't know how it all fit together, and where's the strategy, and why are you guys working on this and why aren't you working on some other syntactic sugar that I want? Of course, we could never tell them, but there was a good reason. \[…\]

> It's really hard for people that haven’t been involved in the overall design of anything as complicated as Swift to be able to discern the difference between something that is the way it is out of an intentional decision, or the way it is as an accident of history. Now that the design process is public, I think that it becomes a lot easier for people to understand that difference.

----

Chris Lattner:

> And I have to say this is the most effort I've ever done to win over one Swift programmer.

> I'm not sure if this is a scalable approach.

*\*sigh\**

Sources:

- Dominik Wagner: [On my misalignment with Apple's love affair with Swift](http://rant.monkeydom.de/posts/2018/06/10/on-my-misalignment-with-apple_s-love-affair-with-swift)
- Chris Lattner: [Transcript of ATP Episode #205](http://atp.fm/205-chris-lattner-interview-transcript)
  ([Listen to the full episode](http://atp.fm/205))
