---
title: "Switching contexts"
date: 2023-07-21T17:01:04Z
---

Perhaps you noticed that I switched this newsletter to a fortnightly cadence. Does that mean I’m out of ideas? Far from it. I’ve been trying hard to put the things I write about into practice.

For the first time in a long time, over the last two weeks I spent most of my time programming, and not a single minute writing. So, yes, this is going to be another one of those quickly improvised posts, cobbled together at the last minute.

I was — and still am — hoping that eventually I’ll be able to write for this newsletter and program [~~tools~~ environments](/2023/07/07/from-tools-to-environments/) that help me with writing the newsletter within the same week, making progress on both simultaneously. As it turns out, that is really hard.

As I wrote a lot about in the [last](/2023/06/09/design-as-higher-order-problem-solving/) [few](/2023/06/23/fighting-insight-with-inference/) [posts](/2023/07/07/from-tools-to-environments/), I suspect one of the most important principles for developing something meaningful is to be able to [live in it](/2023/07/07/from-tools-to-environments/) as soon as possible. So I have been trying to get to such a point quickly. As it turns out, that also is really hard.

Well, nobody claimed it was quick or easy.

### Context (aka environment) switching

You’ve heard about context switching with multi-tasking, and how it negatively affects our productivity. I won’t go too deep into that here. Let me just point out that mental context switching goes along — at least in my particular situation that I’m describing here — with switching environments. Environments that exist mostly inside my computer.

My **writing environment** consists of:

- my *research* setup, which is a few tab groups open in a few Safari windows
- my *note taking* setup, which is currently a strange mix of Bear, iA Writer and Logseq
- my *writing* setup, which is pretty much just typing into the Substack editor directly at this point

This is all far from ideal, and a huge reason why I want to make changes to all of these. All involved apps are good at supporting parts of my process, and spectacularly bad at supporting others. That’s not really the apps’ fault, because they have been designed with different workflows in mind. On the plus side, this combination has resulted in successfully publishing everything on this Substack so far.

My **programming environment** consists of:

- my *note taking* setup, which is the same as above
- my *development IDE*, which is Xcode, as I am working on an app for iPad and iPhone primarily
- at least one open *Simulator* window to test what I’m working on
- a *terminal window*, because it wouldn’t be a programming environment without one, would it?
- various other open Safari windows with different tab groups, which I use to look up API documentation and best practices[^1]

My programming environment is mostly defined by the platform and technology choices I made for my project, which are of course debatable, but don’t really matter that much here. The important bit is:

Apart from my notes, these two environments are completely different from each other. The way I interact with each of them — the way I live within them — feels remarkably different.

The funny thing is, you wouldn’t be able to tell from looking at me. I just sit in the same spot, in front of the same computer, staring into the same screen, touching the same trackpad and typing on the same keyboard. But let me tell you, for me these worlds are so different that I even need an extra week between publishing posts to get anything done apparently.

### Designing environments

Well, this is only half the truth. Or maybe two thirds of it. There is a third environment I haven’t really mentioned yet. And that is the environment I am designing and trying to build.

Every once in a while, when I’m programming in my development environment, I click a “play” button (what an appropriate label), and then I context switch into a simulated (and terribly unfinished) version of the environment I’m building — the app I eventually hope to be able to “live in”.

And this is where it gets interesting.

There is a huge difference between considering the built, simulated, unfinished app environment as merely an extension of your development environment to verify that whatever particular detail you are writing code for right now works correctly, or alternatively consider it as traveling to a place you eventually plan to inhabit.

### “It works.” — “No, it doesn’t.”

Just last week, looking back, I made a lot of progress[^2]. Many things are possible now that weren’t possible last Monday. Yet, “living in it” doesn’t feel good at all.

For instance, there is some data persistence, but I’m not even trusting my own code enough yet to put actual data into it — something that’s absolutely required to be livable. I also know that the data model is still changing, and so it’s not just that I’m worried that I could lose data, it’s that I know that whatever data I put in there needs to evolve with the data model over time.

Another example is that editing my data isn’t as convenient as I’d like it to be. Often it’s still easier to add data into the database directly — the equivalent of opening up the hood and doing things only a car mechanic knows how to do. Great that I am that kind of software mechanic, and that I can do this, but that’s obviously not ideal and just forces me to do even more context switching.

And then there are smaller details that aren’t really critical, but just make it feel unpolished and wonky. There’s an input text field that awkwardly changes size with the amount of text you put into, but not in a way you would like it to. And when you input too much text so that it fills up multiple lines of text until the screen is full, the cursor goes off-screen and it doesn’t scroll automatically so that you no longer see what you’re typing.

These three examples could easily be classified as “must have”, “should have”, and “nice to have”, with a professional software developer attitude, who is under resource constraints and has to prioritize work. But in a way, if you really intend to live in that environment, these are all “must haves”.

Yes, technically it is way more important that your data is safe and doesn’t disappear than some missing automatic scrolling feature. There clearly is no debate about that. It would be ridiculous to suggest otherwise. However, you wouldn’t really want to use it until this annoying text field works properly, would you?[^3]

There is a difference in the definition of “works” depending on which camp you are in: From a software development standpoint “works” is often achieved when correct function is realized. From a user experience perspective, pure function is not at all sufficient. The developer says, “Ok, works as specified. Feel free to request a change to the spec, if you want it to work differently.” The user says, “This doesn’t work at all. This is broken. Isn’t that obvious?”

Sometimes it is obvious. But if you [can’t propositionally explain the problem](/2023/07/07/from-tools-to-environments/#justifying-intuition), it won’t make it on the task list.

### Products or artworks?

Professional software development has this notion of requirements being so clearly specified that meeting the spec is equivalent to the task being checked off the list, and another high priority task taking its place. That’s all happening in the [propositional](/2022/11/04/06-four-ways-of-knowing/) realm. By definition, every other intuition or “feeling” is not part of the spec (and how could it be) and is not considered. That’s the only way to keep that infinite task list at least somewhat in check.

However, if you allow yourself to judge your work as you experience it in your demo environment, and you [accept difficult to describe intuitions as valid feedback](/2023/06/23/fighting-insight-with-inference/#alexanders-feeling) that directs further development, you open yourself up to [new discoveries that can take you off track](/2023/06/23/fighting-insight-with-inference/#cognitive-leaping) and are detrimental to efficient progress on your task list, but may take you to exactly [those places you know you want to be in](/2023/06/09/design-as-higher-order-problem-solving/#making-meaning).

Whether you create technology or art, you need both. Products might get away with mostly efficient coordination of propositionally specified work items, with the occasional intuition worked in, to make it any good. Artworks might live mostly from the artists intuition and sometimes ridiculously long and inefficient periods of “waiting for inspiration to strike” or “prolifically experimenting a lot but going nowhere”, but to get finished even artists have to make some decisions at some point and check things off the task list to finally ship something.

Ah, can you smell the [opponent processing](/2023/02/17/18-opponent-processing/) at play…? 
If you try to [maximize](/2023/02/17/18-opponent-processing/#bio-economies) for one end of the spectrum, what are you missing from the other?

Ok, back to programming…

---

Mirror of the Self *is a fortnightly newsletter series investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

*If you are new to this series, start here: [01 • A secular definition of sacredness](/2022/09/30/01-a-secular-definition-of-sacredness/). 
Overview and synopsis of articles 01-13: [Previously… — A Recap](/2023/01/06/previously-a-recap/). 
Overview and synopsis of articles 14-26: [Previously… — recap #2](/2023/04/28/previously-recap-%232/).*

*Another great way to start is my recent presentation [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/).*

[^1]: Yes, there is also one tab with ChatGPT open. I’m not so much using it to write code for me, but it’s often helpful to identify keywords I should search for to find appropriate APIs or algorithms, if I don’t know their names.
[^2]: It did not feel like that last week.
[^3]: You might not feel that at all. Apparently, there are many software developers who either don’t have this sensibility at all, or just don’t feel particularly stimulated to do something about it. As there is always a higher priority item on the long list of outstanding tasks, why bother with this low priority of something not feeling quite right? I can’t tell if that’s because most software developers work on things they never really intend to “live in” themselves, as they primarily write for other people. I can tell that this is certainly a looked for quality when hiring software engineers.
