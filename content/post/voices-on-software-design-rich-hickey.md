---
title: "Voices on software design: Rich Hickey"
date: 2024-06-14T17:00:49Z
series: voices-on-software-design
---

I’ve been reviewing several classic programming papers about simplicity, complexity, and adjacent topics. Here I’m sharing some highlights from the papers and my thoughts about them.

Today’s paper is not a paper but a video, and you can’t really have a series [On Simplicity…](/series/on-simplicity/) without being aware of: [Rich Hickey • Simple Made Easy](https://www.infoq.com/presentations/Simple-Made-Easy/)

## Simple Made Easy

*Rich Hickey • 2011*

{{< youtube id="SxdOUGdseq4" >}}

> *We need to build simple systems if we want to build good systems. I don’t think we focus enough on that.*

Agreed.

> *I love word origins. They’re tremendous fun. One of the reasons why they’re fun is because words eventually come to mean whatever we all accept them to mean. You know, whatever is commonly understood to be the meaning is what it means. And it’s often interesting to say, I wish we could go back to what it really means and use that. And I think there’s a couple of words that I’m going to use in this talk that I would love for you to come away knowing the origins of and try to use more precisely, especially when talking about software.*

Hickey is known for his love of words and many of his presentations include reflections on the etymology of words he considers important. I deeply respect people who are concerned about which words they use and where their meaning comes from. A good indicator that they apply such precision and attention to detail to other things as well.

### Defining “simple”

Hickey actually attempts a definition of simplicity. A surprisingly rare treat in many treatises on simplicity.

> *So the first word is simple. And the roots of this word are sim and plex, and that means “one fold” or “one braid” or “twist”. […]*
>
> *And the opposite of this word is complex, which means “braided together” or “folded together”. Being able to think about our software in terms of whether or not it’s folded together is sort of the central point of this talk. […]*
>
> *So if we want to try to apply “simple” to the kinds of work that we do, we’re going to start with this concept of having one braid. And look at it in a few different dimensions. […] **If we want to look for simple things, we want to look for things that have sort of one of something. They do, they have one role. They fulfill one task or job. They’re about accomplishing sort of one objective.**They might be about one concept like security.*
>
> *And sort of overlapping with that is they may be about a particular dimension of the problem that you’re trying to solve. The critical thing there, though, is that when you’re looking for something that’s simple, you want to see it have focus in these areas. You don’t want to see it combining things.*
>
> *On the other hand, we can’t get too fixated about one. In particular, simple doesn’t mean that there’s only one of them. Right? It also doesn’t mean an interface that only has one operation. So it’s important to distinguish cardinality, counting things, from actual interleaving. **What matters for simplicity is that there is no interleaving, not that there’s only one thing**, and that’s very important.*

One role, one job, one objective. Focus on one thing. One concept that makes sense to us. It’s not a composite, or at least we don’t (have to) care that it is. We have a sense for its [gestalt](/2023/05/05/finding-meaning-in-the-nature-of-order/#gestalt-perception). We don’t have to [analyze](/2023/06/23/fighting-insight-with-inference/#dual-processing) it. We understand it [intuitively](/2023/12/08/on-simplicity-%233-familiarity/#powerful-intuition).

It’s not about one thing as in just one thing. There can be many, but they’re kind of all the same in some regard. They are of the same type. They are in the same category. And that type or category is obvious to us.

What matters is that there is no interleaving of multiple things. There should not be anything that makes it less clear what type it is and what category it belongs in. There should not be anything that requires us to switch on our analytical thinking to make sense of it.

> *Okay, the other critical thing about simple, as we’ve just described it, right, is if something is interleaved or not, that’s sort of an objective thing. You can probably go and look and see. I don’t see any connections. I don’t see anywhere where this twist was something else, so simple is actually an objective notion. That’s also very important in deciding the difference between simple and easy.*

For Hickey simple therefore becomes an objective property. I don’t agree with this fully, but let’s have him share more of his perspective first.

A little later in the presentation, he adds another important aspect:

> *The meaning of simple means unentangled, not twisted together with something else. It doesn’t mean I already know what it means. **Simple does not mean I already know what it means.***

### Defining “easy”

> *The other word we frequently use interchangeably with simple is the word easy. And the derivation there is to a French word. And the last step of this derivation is actually speculative, but I bought it because it serves this talk really well. And that is from the Latin word that is the root of “adjacent”, which means to lie near and to be nearby. And the opposite is hard. Of course, the root of hard has nothing to do with lying near. It doesn’t mean lie far away. It actually means strong or tortuously so.*
>
> *So let’s look at easy. I think this notion of nearness is really, really cool. In particular, obviously there’s many ways in which something can be near. Right? There’s sort of the physical notion of being near. Is something, you know, right there. And I think that’s where the root of the word came from. This is **easy to obtain because it’s nearby**. It’s not in the next town. I don’t have to take a horse or whatever to go get to it. We don’t have the same notion of physicality necessarily in our software, but we do sort of have our own hard drive or our own toolset, or it’s sort of the ability to make things physically near by getting them through things like installers and stuff like that.*
>
> *The second notion of nearness is something **being near to our understanding, or in our current skill set**. And I don’t mean in this case near to our understanding meaning a capability. I mean literally near something that we already know. So the word in this case is about **being familiar**.*
>
> *I think that, collectively, we are infatuated with these two notions of easy. **We are just so self-involved in these two aspects; it’s hurting us tremendously. All we care about is, can I get this instantly and start running it in five seconds?** It could be this giant hairball that you got, but all you care is, you know, can you get it?*
>
> *In addition, we’re fixated on, oh… I can’t; I can’t read that. Now I can’t read German. Does that mean German is unreadable? No. I don’t know German. So this sort of approach is definitely not helpful. In particular, **if you want everything to be familiar, you will never learn anything new because it can’t be significantly different from what you already know and not drift away from the familiarity.***

The first aspect of “easy” is a form of convenience. Stuff that’s nearby is convenient to get to. We might call it something else, like “fast” or “efficient”, or, well, just “easy”. But it’s about convenience. And most often it’s about [convenient utility](/2024/01/19/on-simplicity-%235-hiding-complexity/#utility-first) — it does something for us we want to get done, or at least it gets us much closer to where we want to be without a lot of fuzz and hassle.

The second aspect of “easy” is about [familiarity](/2023/12/08/on-simplicity-%233-familiarity/). What’s “near to our understanding” or “in our current skill set”. And if we encounter something that is not, like when looking at code somebody else wrote, we rather claim that it’s not good and rewrite it in a familiar way instead of taking the time to understand it and potentially learn something.

> *There’s a third aspect of being easy that I don’t think we think enough about that’s going to become critical to this discussion, which now is being **near to our capabilities**. And we don’t like to talk about this because it makes us uncomfortable because what kind of capabilities are we talking about? If we’re talking about easy in the case of violin playing or piano playing or mountain climbing or something like that. Well, you know, I don’t personally feel bad if I don’t play the violin well because I don’t play the violin at all.*
>
> *But the work that we’re in is conceptual work, so **when we start talking about something being outside of our capability, it really starts trampling on our egos in a big way**. And so, due to a combination of hubris and insecurity, we never really talk about whether or not something is outside of our capabilities. It ends up that it’s not so embarrassing after all because we don’t have tremendously divergent abilities in that area.*

I’ve re-read this part many times, trying to figure out why Hickey considers “near to our capabilities” a distinct aspect from “near to our understanding”. The way I make sense of it is the difference between being familiar with a propositional concept and being capable of performing a procedural skill. Capabilities in this case add non-propositional knowledge to the mix.

The examples he chooses, playing piano and mountain climbing, are go to examples for activities that require non-propositional knowledge acquired through implicit learning, developed through deliberate practice in, ideally, a flow state. Programming, then, must also at least partially have such procedural skills that rely on tacit knowledge. And his criticism is that we don’t talk about that enough. This also aligns well with [Naur’s view](/2024/04/19/voices-on-software-design-peter-naur/#a-theory-that-cannot-be-expressed-fully).

> *The last thing I want to say about easy and the critical thing to distinguish it from simple is that easy is relative. Playing the violin and reading German are really hard for me. They’re easy for other people, certain other people. So unlike simple where we can go and look for interleavings, look for braiding, easy is always going to be, easy for whom, or hard for whom? It’s a relative term.*
>
> *The fact that we throw these things around sort of casually saying, “Oh, I like to use that technology because it’s simple”. And when I’m saying “simple”, I mean easy. And when I am saying “easy”, I mean because I already know something that looks very much alike that. It’s how this whole thing degrades and we can never have an objective discussion about the qualities that matter to us in our software.*

In summary, for Hickey *simple* is an objective property of the thing we are looking at, and *easy* is relative, depending on the convenience, familiarity, and capability of the person talking about it. We throw both of these terms around as if they are interchangeable, which makes productive conversations about simplicity really difficult.

### Reasoning about programs with limited analytical capacity

On top of our imprecise usage of the words “simple” and “easy”, we are faced with the limitations of our cognitive system.

> *How can we possibly make things that are reliable that we don’t understand? It’s very, very difficult. I think Professor Sussman made a great point saying there’s going to be this tradeoff. As we make things more flexible and extensible and dynamic, in some possible futures for some kinds of systems, we are going to make a tradeoff in our ability to understand their behavior and make sure that they’re correct. **But for the things that we want to understand and make sure are correct, we’re going to be limited. We’re going to be limited to our understanding.***
>
> *And our understanding is very limited, right? There’s the whole notion of how many balls can you keep in the air at a time, or how many things can you keep in mind at a time? It’s a limited number, and it’s a very small number. So we can only consider a few things and — when things are intertwined together — we lose the ability to take them in isolation.*
>
> *So if every time I think I pull out a new part of the software I need to comprehend, and it’s attached to another thing, I had to pull that other thing into my mind because I can’t think about the one without the other. That’s the nature of them being intertwined. So every intertwining is adding this burden, and the burden is kind of combinatorial as to the number of things that we can consider. So, **fundamentally, this complexity — and by complexity I mean this braiding together of things — is going to limit our ability to understand our systems.***

It’s extremely *easy* to run into [combinatorial explosion](/2022/12/02/10-problem-solving-and-combinatorial-explosion/), so we must cautiously decide how many concepts we want to deal with at a time. The main challenge is when “braided” complex concepts require us to pull in too many ideas that go beyond our [limited intellectual capacity](/2023/06/23/fighting-insight-with-inference/#dual-processing). It becomes much harder, and perhaps even impossible, to make sense of such concepts.

One way to deal with this is, of course, to stop trying to understand their inner workings altogether and reduce our understanding to just their utility in the form of a much simpler interface that [hides all the complexity of its inner workings](/2024/01/19/on-simplicity-%235-hiding-complexity/). We know this approach works and we have scaled our way to where we are today mostly using this technique.

But of course, this comes to bite us as soon as we have to make changes…

> ***If you’re going to change software, you’re going to need to analyze what it does and make decisions about what it ought to do. At least you’re going to have to go and say: What is the impact of this potential change? And what parts of the software do I need to go to to effect the change?***
>
> *I don’t care if you’re using XP or Agile or anything else. You’re not going to get around the fact that **if you can’t reason about your program, you can’t make these decisions**. But I do want to make clear here because a lot of people, as soon as they hear the words “reason about”, they’re like, “Oh, my God! Are you saying that you have to be able to prove programs?” I am not. I don’t believe in that. I don’t think that’s an objective. I’m just talking about informal reasoning, the same kind of reasoning we use every day to decide what we’re going to do.*

How effective we are at making changes is directly related to how well we understand how the system works.

> *One of the problems I think we have is this conundrum that **some things that are easy actually are complex**. So let’s look: There are a bunch of constructs that have complex artifacts that are very succinctly described. **Some of the things that are really dangerous to use are so simple to describe. They’re incredibly familiar.** If you’re coming from object-orientation, you’re familiar with a lot of complex things. They’re very much available.*
>
> *And they’re **easy to use**. In fact, by all measures, conventional measures, you would look at them and say this is easy. But we don’t care about that. Again, the user is not looking at our software, and they don’t actually care very much about how good a time we had when we were writing it. What they care about is what the program does, and if it works well, it will be related to whether or not the output of those constructs were simple. In other words, what complexity did they yield?*
>
> *When there is complexity there, we’re going to call that incidental complexity. It wasn’t part of what the user asked us to do. We chose a tool, it had some inherent complexity in it; it’s incidental to the problem. I didn’t put the definition in here, but “incidental” is Latin for “your fault”.*

I cannot help but see the excessive use of libraries and frameworks as one of the best examples illustrating this idea. With just a few lines of code, which are convenient and quick to write, we adopt a potentially massive dependency on hundreds, thousands, perhaps even millions of lines of code that we did not write, do not understand, and perhaps don’t even have any control over.

And this problem is recursive. What if the library developer applied the same strategy? Within seconds of typing a single function call that looks like any other, we potentially hook into a deep hierarchy of complex dependencies.

To be fair, more often than not this works so well, that most of us don’t have the slightest feeling of anxiety about this. This is just how modern software development works. Right?

Whether this being problematic or not, what it definitely means is that we no longer stand a chance in possibly understanding all this complexity, because this is just too much to even try to pick apart.

> *We actually can’t get much smarter. We’re not going to move; **we’re not going to move our brain closer to the complexity. We have to make things near by simplifying them.***
>
> *But the truth here is not that there are these super bright people who can do these amazing things and everybody else is stuck. The juggling analogy is pretty close. The average juggler can do three balls. The most amazing juggler in the world can do, like, nine balls, or twelve, or something like that. They can’t do 20 or 100. We’re all very limited. **Compared to the complexity we can create, we’re all statistically at the same point in our ability to understand it, which is not very good. So we’re going to have to bring things towards us.***
>
> *And because we can only juggle so many balls, you have to make a decision. How many of those balls do you want to be incidental complexity and how many do you want to be problem complexity? How many extra balls? Do you want to have somebody throwing you balls that you have to try to incorporate in here? Oh, use this tool! And you’re like, “Whoa! More stuff.” Who wants to do that?*

So if we know that we can’t possibly deal with that much complexity, we at least can make good decisions about how much of it we accept in our project.

And do we make good decisions about that?

> *As programmers, we are looking at all kinds of things, and I just see it. You know, read Hacker News or whatever. It’s like: “Oh, look! This thing has this benefit.” “Oh, great. I’m going to do that.” “Oh, but this has this benefit.” “Oh, that’s cool.” “Oh, that’s awesome. You know, that’s shorter.” **You never see in these discussions: Was there a trade-off? Is there any downside? Is there anything bad that comes along with this? Never. Nothing.***
>
> *It’s just like we look all for benefits. So as programmers now, I think **we’re looking all for benefits, and we’re not looking carefully enough at the byproducts.***

No, we don’t.

*Here I’m going to skip over some exceptionally good programming advice that is practically the meat of Hickey’s talk. It’s too technical and specific for the purposes of this more general overview, but if you are a programmer and you want to become better at detecting the sources for incidental complexity and learn about ways to avoid and mitigate them, you need to watch this talk. Several times. Perhaps you should [do it right now](https://www.youtube.com/watch?v=SxdOUGdseq4).*

Some important ideas from the conclusion of his presentation:

### Abstraction doesn’t mean “hiding stuff”

> *An abstract, again, here’s an actual definition, not a made up one: **It means to draw something away. And, in particular, it means to draw away from the physical nature of something.***
>
> *I do want to distinguish this from, that sometimes people use this term really grossly to just mean hiding stuff. That is not what abstraction is, and that’s not going to help you in this space.*

Hickey has made up his mind on whether our popular scaling technique of [hiding complexity](/2024/01/19/on-simplicity-%235-hiding-complexity/) behind interfaces is the way to go.

### Simplicity is a choice

> *The bottom line is: **Simplicity is a choice. It’s your fault if you don’t have a simple system. And I think we have a culture of complexity.** To the extent we all continue to use these tools that have complex outputs, we’re just in a rut. We’re just self-reinforcing. And we have to get out of that rut.*

[We have a culture of complexity](/2024/01/19/on-simplicity-%235-hiding-complexity/#cultivated-ignorance), because we misunderstand “simple” as “easy”.

> *It requires sensibilities and care. **Your sensibilities about simplicity being equal to ease of use are wrong.** They’re just simply wrong. We saw the definitions of simple and easy. They’re completely different things. **Easy is not simple.***

Sensibilities and care. [Amen](/2023/05/26/mind-or-machine-who-cares/#jony-ive-on-care-and-carelessness).

> *We’re going to try to create abstractions that have simplicity as a basis. We’re going to spend a little time upfront simplifying things before we get started. And recognize that **when you simplify things, you often end up with more things. Simplicity is not about counting. I’d rather have more things hanging nice, straight down, not twisted together, than just a couple of things tied in a knot.** And the beautiful thing about making them separate is you’ll have a lot more ability to change it, which is where I think the benefits lie. I think this is a big deal, and I hope everybody is able to bring it into practice or use this as a tool for convincing somebody else to do that.*

---

[Share](/2024/06/14/voices-on-software-design-rich-hickey/)

Mirror of the Self *is a series of essays investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

***Series**: [Mirror of the Self](/series/mirror-of-the-self/) • [On simplicity…](/series/on-simplicity/) • [Voices on software design](/series/voices-on-software-design/) 
**Presentations**: [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/)*
