---
title: Categories Everywhere
date: 2019-12-20
categories:
- Universal Structure
---

Part 3 of my *Universal Structure* blog chain. Start [here]({{< ref "structure-and-behavior" >}}).

---

## Language
Human language, spoken or written, is an amazingly sophisticated invention that has evolved over centuries. We can describe concepts, transmit those descriptions through space and time, and create shared understanding. It's not perfect, but it does work reasonably well to help us communicate.

It's no coincidence that we "talk" to computers with programming *languages*. Let's forget about programming for a moment and focus just on human language. \
Why is it worth analyzing human language to understand how we think?

Language is about finding symbols (aka names) for things, and then somehow trying to create shared understanding that such a symbol means the same thing to you and me. If you ever wondered *why* naming things is in the top 2 of hardest things in computer science, you're about to find out.

## Categories
We don't just talk about things we can easily point at. However, that's how it usually starts when we learn to speak as a small child. You see a cat, your parents say "cat", and over time you hopefully learn to associate that utterance and a little later the symbol `cat` with that [fuzzy, irrational thing that vibrates](#vibrating). 

Over time you'll learn, mostly still by pointing at things that look similar, that there are many `cat`s and they can be quite different from each other. Turns out the symbol `cat` doesn't refer to just one thing, but to a whole category of things. Cats come in different sizes and colors, and some of them behave quite differently. And somehow they are all `cat`s.

Except those that are called `dog`s. And as you get over your initial confusion about this, you add to your vocabulary and start perceiving similarities and differences between things trying to figure out which of these differences cause them to have different names and therefore belong in different categories. 

Isn't it amazing how good we are at knowing which thing we're looking at? If you don't think that's a big deal then try to describe precisely what makes cats `cat`s and dogs `dog`s. It appears easy at first, but soon you'll run into weird edge cases.

We're just getting started. If we want to, we can distinguish between different `cat`s! We can prepend words to the familiar category `cat`, and say "black cat" or "Siamese cat". All these still belong to the `cat` category, but not all cats belong to the `black cat` category. And so we learn how to move down a taxonomy and be more *specific*, paying attention to less obvious differences.

We also learn that both `cat` and `dog` belong to the same `animal` category. As do lots of other things. We can not just move down the taxonomy and be more specific, we can also [move up and be more *generic*]({{< ref "the-art-of-abstraction" >}}), ignoring more obvious differences between objects and creating more abstract categories.

As categories become more abstract, they become harder to define because they no longer map directly to something you can point at. Quick, think of an `animal`! You can't. You can only think of a specific animal. You can't even think about a `cat`. You will think about a specific cat. Which color did your imagined cat have? Which color does a generic cat have?

Most of the time we don't realize this little trick our mind plays on us. We talk about abstract concepts all the time, but we still think in very specific terms about them. Specific examples become _prototypes_[^prototype-theory] for generic categories in our mind.

Categories are how we *structure* our language, our thoughts, and our reality. Categories help us make sense of our experiences. Categories define meaning. That makes them kind of important. Not just for linguists.

You have now successfully completed your "Hello, conceptual world!" tutorial. If this reminds you of programming languages with their type or class hierarchies, you begin to understand why I find the connection between linguistics and programming fascinating. And if you can see a little problem there with deciding what belongs into which category, and our inability to think in generic concepts, we are going to have a great time together in the upcoming parts of this series.

## Linguistics and Programming
Linguists look for coherent universal patterns across languages. They compare different languages, preferably from cultures that might differ a lot from ours. They examine the categories that have formed in some languages but not in others, and which objects belong to a category and which do not.

Language is a window into the _conceptual system_ we use to make sense of the world, the data model of our brain's operating system. Through this window linguists uncover amazing insights into how we think.

> What is reason? \
> How do we make sense of our experience? \
> What is a conceptual system and how is it organized? \
> Do all people use the same conceptual system? \
> If so, what is that system? \
> If not, exactly what is there that is common to the way all human beings think?
> 
> — [George Lakoff: _Women, Fire, and Dangerous Things_](#lakoff-1987)[^book-title]

As programmers we constantly invent symbols and name things, and debate about the properties and boundaries of the categories we define. We obsess about hierarchical taxonomies, jump up and down the ladder of abstraction, specialize and generalize along the way, modeling the world around us in software. We can model (almost?) everything. And we do it in an environment that gives us that cozy feeling that we do all that with mathematical precision.

It is not far-fetched to assume that on the lowest levels brains must work somewhat like computers. So all these insights about conceptual systems must be useful for software development somehow.

As it turns out, brains do not at all work like computers. And that's exactly why these insights are so useful for designing software…

---

[Next article in this blog chain _Universal Structure_.]({{< ref "categories-structure-our-world" >}})

---

## References

* <a name="vibrating"></a>**Nathan W. Pyle — Strange Planet: G r e a t**\
	Nathan Pyle switches names for everyday categories with surprisingly appropriate unexpected ones in his delightful comic series _Strange Planet_.\
  <https://www.instagram.com/p/BuHSezngbBW/>
* <a name="lakoff-1987"></a>**George Lakoff: _Women, Fire, and Dangerous Things — What Categories Reveal about the Mind_** \
	1987, The University of Chicago Press

[^prototype-theory]: I'm trying to build a bridge to Eleanor Rosch's prototype theory (massively oversimplifying it), which has a lot more to say about how and why we like some things more than others to represent our more generic categories as prototypes.
[^book-title]: George Lakoff's title choice for his perhaps most important work is unfortunate. It is based on one of the four noun classes in the Australian Aboriginal language Dyirbal, which classifies women, water, fire, violence, and exceptional animals in the same "feminine" class. This does, rather ironically, confront us with the fact that a lot of ideology is deeply built into the languages we speak, and therefore also into the way we think.