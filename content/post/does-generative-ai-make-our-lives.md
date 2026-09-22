---
title: "Does generative AI make our lives simpler?"
date: 2024-06-28T17:00:33Z
---

A few newsletters ago [I was talking a little bit about Artificial Intelligence (Al)](/2023/05/26/mind-or-machine-who-cares/). If you read that, you know that I'm not particularly concerned about a looming Al apocalypse or singularity event, because I don't think we are anywhere close to achieving artificial *general* intelligence (AGI).

However, I am concerned enough about the *non*-general Al that we have unleashed already, which is transforming how we work, how we create, and ultimately how we think — right now. Well, I’m not really concerned about AI. To me this just seems to be the continuation of a pattern that has been going on in tech for a long time.

### Increasing productivity

LLMs are so good at generating code that people who didn't consider themselves programmers have started exploring creating little tools and apps with the help of generative AI. Experienced software developers have been using tools like GitHub Copilot for a while now to become more productive. If you ever did some serious programming yourself, you know that a lot of time is going into figuring out how libraries and frameworks work and which API calls to use for what effect, what the idiomatic way of doing something is in your chosen programming language and environment, and so on. In other words, programmers spend an awful lot of time in a web browser searching for answers on the internet.

Not anymore! Now we can chat with an LLM, and ideally we no longer have to figure out how to do a specific thing in code, we just tell it what we want done, and it writes the code for us. Of course, if you have actually tried this yourself, you know that it's not quite that straightforward. Yet. But overall, today's LLMs can significantly improve our productivity in getting stuff done just by putting us on the right path faster than search engines and Stack Overflow ever could.

Does that mean programming has become *simpler*?

The way I look at it is this: It has certainly become *[easier](/2024/06/14/voices-on-software-design-rich-hickey/)*.

### A growing stack of complexity

The computers and servers our software runs on are technically so complex that few people in the world fully understand how they work in all detail. Think of just the complexity of the central processor with billions of transistors. These have been designed by huge teams of engineers, many of them specialized on tiny parts of the design. I'm not even sure that there is any person in the world that can fully understand how a modern processor works in all detail. It's just too complicated for a single mind to grasp.

The operating systems (OS) these computers and servers run for basic operation have been developed over decades and consist of hundreds of millions of lines of code written by tens of thousands of engineers. Same here, there is just not a single individual on the planet that can possibly understand the whole OS in all detail. Of course, we have many excellent engineers that understand subsystems of the OS deeply, but we can't expect anyone to have a detailed holistic view of the whole system.

The apps and services that run on these operating systems may be less complicated, because they make use of many of the capabilities built into the chips and into the OS. We can use a simple API call to make a text field appear on our phone that essentially comes with more advanced text editing capabilities than desktop computers in the 1980s running a dedicated word processor. Just that text field you type a comment into, where you can highlight a word in bold text and paste in a clickable link is probably more sophisticated than early text processing engines.

The magic that makes all these leaps of productivity possible is the contract to exchange functionality, which reliably works in a specified way, for knowledge of how it does that. As a programmer you get to take advantage of all the shiny features without the burden of having to understand how a single one of them actually works. You get to drive the car, even if you have no idea how the engine works; you don't even have to know what an engine is, or that there is one of these in your car to make it work.

### Selective ignorance makes us productive

We got here through a massive amount of [cultivated ignorance](/2024/01/19/on-simplicity-%235-hiding-complexity/#cultivated-ignorance). We can ignore the complexity of certain parts of a system as long as there is somebody who makes it work more or less reliably to spec. Then we get to just tell it *what* we want, without having to know *how* to do it ourselves. And we get to use our time and mental capacity to deal with other — presumably more important — matters.

However, let us not forget that this doesn’t come for free. It also introduces a power imbalance. If you take advantage of something that is provided to you and that you don’t understand, you are now relying on it to continue to work as intended, and therefore you are dependent on somebody else to maintain and take care of it. You count on it to keep working in that exact way for the foreseeable future.

This, of course, is encouraged and exploited by one of the most important cultural systems we put in place worldwide: capitalism. This cultural framework makes it look like this is how the world works, this is how it’s supposed to be, and this is how it always has been. It wasn’t really like that until a few centuries ago, but that’s long enough for us to have completely forgotten.

If you have no idea how to do something, now there is always a person, a company, or a machine that knows how to do it and will happily do it for you, in exchange for money. You get *what* you want (or something close to it) without having to learn *how* to do it yourself. Yay! This is progress. At least that is what the people running these companies and collecting the money we give them keep telling us. Don’t mind the dependency, and the power dynamics that come from that. You can trust us! And surely you wouldn’t want to do all that boring and cumbersome stuff yourself, would you? Just sign here and subscribe! Oh, and don’t forget to have a credit card on file.

### A new layer on top

With Al and LLMs we built another layer on top of the already towering stack. Now you don't even have to figure out how to make computers do anything, because now there is a system that has that covered. You just need to know what you want it to do and tell it in natural language, and it will (hopefully) do that for you then (or something close to it).

A peculiar feature of LLMs is that they are themselves systems that we don’t fully understand — not even the scientists who invented their foundational technology. We don't know exactly how LLMs do what they do. A lot of research in Al is not about creating and improving these new AI systems, but essentially about figuring out how the ones we already have actually work.

Now, there is nothing wrong with taking advantage of all that utility and convenience available to us. Just like there is nothing wrong with driving a car that you wouldn’t know how to repair if it ever broke down. But perhaps it’s time to reflect: Are we really getting what we need or want out of this? And is this deal really as good as it sounds?

Needless to say, neither hardware nor software works perfectly reliably. There are bugs and security issues, and it takes us a long time to find and get rid of them. LLMs add to that list with novel side effects like hallucinations, where they come up with perfectly reasonable sounding fantasies, or prompt injection, where a malicious third party might sneak in some information into our prompt that changes what exactly the LLM is doing on our behalf without us noticing.

### More productive than ever, more dependent than ever

We are growing more and more dependent on the technologies we create. And we are too far in at this point (probably since the Industrial Revolution) to try to reverse that. We don’t have to. But I think we should remember how we got to where we are today, and what price we paid for it, and keep paying for it.

We pay for our ignorance with dependence. Dependence isn't inherently bad, sometimes it’s useful, even necessary. But at some point dependence interferes with our freedom and limits our agency. As we rely more and more on products and services that are provided to us through commercial entities, our lives become more and more intertwined with the values these entities represent. Last time I checked they weren’t as aligned as I’d like them to be.

If we keep piling up layer upon layer of things effectively nobody fully understands anymore, all developed and maintained by specialists peeking through the keyhole of their own expertise looking only at that tiny part of a complex system, how can we expect these systems to be holistically designed for what we want them to do?

To create something beautiful and well designed, you need to understand how it works and have the means to access the resources you need to build it. The former is under threat because we keep culturally unlearning how to do things in the name of productivity thanks to convenient tools and services doing them for us. The latter is under threat because we keep giving control over these resources away to corporations.

This is convenience masquerading as simplicity. This is [easy, but not simple](/2024/06/14/voices-on-software-design-rich-hickey/).

We have been focusing so much on productivity and progress that we have neglected cleaning up the messes we have created along the way. We have been so busy with increasing the output we produce that we no longer see the value in making things more beautiful and easier to understand.

There are so many opportunities to rebuild the tools and services and infrastructure we rely on to become easier to understand and use, less wasteful and more efficient, and more elegant — and with that also more reliable and more maintainable. It's just that these things have not been prioritized in the cultural framework we live in, which tends to value rapid innovation, rate of progress, and unbounded growth much more than creating beautiful and simple things that really matter to us.

We are stuck in a gigantic self-reinforcing feedback loop that keeps accelerating our pace of progress and our thirst for productivity and growth, and at the same time makes it look more and more ridiculous to think there is another way.

Maybe that’s naive, but I believe there is. 
Perhaps we have to be naive to even consider doing anything about it?

---

[Share](/2024/06/28/does-generative-ai-make-our-lives-simpler/)

Mirror of the Self *is a series of essays investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

***Series**: [Mirror of the Self](/series/mirror-of-the-self/) • [On simplicity…](/series/on-simplicity/) • [Voices on software design](/series/voices-on-software-design/) 
**Presentations**: [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/)*
