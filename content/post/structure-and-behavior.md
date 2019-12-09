---
title: Structure and Behavior
date: 2019-12-06
categories: 
- Universal Structure
---

Part 1 of my blog chain *Universal Structure*.

---

In 2018 I wrote a vision document for a start-up I was planning to found shortly after (*spoiler: I chose to not become a founder and am now an investor instead*). The vision was grand: democratize programming and bring the power of computation to everyone, not just developers.

Part of the vision document described the approach of how we wanted to tackle such a large challenge and cut it up into smaller pieces. In a section titled *"How to (not) democratize programming"* I wrote:

---

### How to Model Modeling
To find a better mental model for describing complex interactive systems, we can break down the process into smaller steps with increasing complexity:

1. **Modeling static structure.** We can significantly reduce complexity by ignoring systems with dynamic behavior and focus on modeling static structure first. These systems can still exhibit behavior, it is just that the behavior is not part of the modeling process, but predefined and implemented with classic techniques instead. _Structure can be modified by the user, behavior only by the developer._
2. **Modeling dynamic behavior.** With better understanding of how to visualize and interact with static structure, we can move on and apply our gained knowledge to modeling dynamic behavior as well. This adds change over time and encoding heuristics as additional dimensions and will introduce new complexities for visualizations and interactions. _Once achieved, both structure and behavior can be modified by the user._
3. **Modeling the modeling process.** The final step is to enable modeling of systems that can be used to model systems themselves — building a tool to build tools. This can unlock additional efficiencies with techniques that resemble meta-programming in classic programming languages.

---

The core idea behind this was born out of the frustration with the current state of apps, which are mostly just more or less fancy views on data. Users can navigate the data in predefined ways and manipulation is limited, if at all possible.

Think of all the shopping or traveling apps that let you browse a catalog of products you can order or book. These apps live in a step 0 I didn't mention above — both structure and behavior are completely specified by the developer; the user is merely allowed to navigate and perhaps search and filter the dataset, hopefully ending in a sale of some kind.

There's nothing wrong with such apps. We just wanted to go further and give everyone the power to design their own structure, then their own behaviors, and ultimately end up with a full-blown tool to build your own systems and tools, hopefully simplifying each step significantly along the way.

Great, so I broke down a giant challenge into three huge ones. It might not have helped us much getting anywhere closer to building anything. It did, however, put me on an unexpected path that produced some surprising insights.

### Making assumptions
When programmers think about the future of programming, it is only natural to start from where we are now. We make assumptions. Some of them automatically, unconsciously, without reflection. For instance, that there has to be a programming language. And that this language will be used to specify behavior.

But I moved that into the second step. That allowed me to free myself from the assumptions and restrictions that come with thinking about modeling dynamic behavior. Instead, I became obsessed with thinking about structure.

### Structuring data
In my mind step 1 was a better way to model the structure of data. In an abstract sense, this seems to be what most non-programmers want to do with computers: deal with data, visualize and manipulate it.

Think of Filemaker or Microsoft Access, although of course, bringing these examples up will frame your thinking in a way that has little to do with what we were up to. Our goal was to help people without a programming background to design data models without having to know anything about data models, databases, schemas, keys, relationships, files, formats, types, etc.

Think of somebody who doesn't have a technical background, yet still uses a computer or smart phone to take notes. This person makes seemingly simple decisions:

- Where do I put this idea?
- Do I create a new note for it?
- Do I append it to an existing note?
- Where in the existing note do I put it?
- Do I create a new headline for it?
- Do I rearrange the content of the existing note?
- Do I split it up into several smaller notes?

They might not know what a data model is, but they are manipulating one right there. 
Sure, this is not anywhere close to what we programmers think of when we read "data model". 
And that's exactly the point.

### Abolishing ceremony
In programming (or database) land, we've created lots of ceremony around data: schemas, types, validation, integrity, transactions, and much more. \
Some of these are necessary to make it work. \
Some of these are useful for the use cases we defined. \
Some of these are helpful to prevent us from making mistakes that could lead to data loss.

Well, *are* they? Or *were* they? \
Now that we all carry pretty capable supercomputers in our pockets, maybe it's time to question some of our assumptions.

What if all that ceremony was optional? \
How could you modify the structure of data without it? \
How could you still do useful stuff with that data? \
And what is *structure* anyway?

And so I grabbed my spelunking gear and climbed down into a massive rabbit hole…

---

[Next article in this blog chain _Universal Structure_]({{< ref "free-your-mind" >}}).