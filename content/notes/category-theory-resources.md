---
title: "Category Theory: Resources"
date: 2019-05-24
draft: false
---

# Category Theory: Resources
I’m currently trying to fully understand category theory as it applies to programming. I’m not scared of math, however, I’m also not a mathematician, so I’m looking for an introduction that helps me build intuitive understanding first, and then goes all the way into the formalisms.

Here are the resources I am currently reading that I found the most helpful so far:

## Resources

### Why Category Theory Matters • rs.io
<http://rs.io/why-category-theory-matters/>

Quick intro on why it's useful and lots of links to resources of applications of category theory.

### Category Theory for Programmers • Bartosz Milewski
<https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/>

This is a collection of blog articles (which have also been compiled into a [nicely typeset PDF](https://github.com/hmemcpy/milewski-ctfp-pdf/)) that I found to be an excellent guide in building up intuitive understanding for category theory. It constantly uses examples from both imperative (C++) and functional (Haskell) languages; it sure is helpful to know a little about C++ and Haskell, but I don’t think one needs to be fluent in either of those. The math is kept to a minimum, just enough to understand what’s necessary, without formalities getting in the way. I recommend starting with this one.

Bartosz Milewski also published three YouTube playlists with a video course of the same material, which roughly correspond to the three parts of the book:

- [Category Theory • Bartosz Milewski](https://m.youtube.com/playlist?list=PLbgaMIhjbmEnaH_LTkxLI7FMa2HsnawM_)
- [Category Theory II • Bartosz Milewski](https://m.youtube.com/playlist?list=PLbgaMIhjbmElia1eCEZNvsVscFef9m0dm)
- [Category Theory III • Bartosz Milewski](https://m.youtube.com/playlist?list=PLbgaMIhjbmEn64WVX4B08B4h2rOtueWIL)

I found the videos to be an ideal companion for the book and watch the video before I read the more detailed and polished chapter in the book. The lessons are still good to watch and understand at 1.5x speed.

### Seven Sketches in Compositionality: An Invitation to Applied Category Theory • Brendan Fong, David I. Spivak
<https://ocw.mit.edu/courses/mathematics/18-s097-applied-category-theory-january-iap-2019/lecture-videos-and-readings/18-s097iap19textbook.pdf>

Coming from the opposite end of the spectrum — the mathematical side — this book provides all the formal knowledge to fully understand category theory. It still builds up from practical examples that help with intuitive understanding, but this is clearly a university course textbook with full-on math plus exercises.

I attempted to start with this one and was quite happy, but then I discovered Bartosz Milewski’s video course and then book, which are a much simpler and more pragmatic (for programmers, at least) introduction to category theory. I am planning to finish reading _Seven Sketches_ after I finished Bartosz’ book.

This book also comes with video lectures (which I haven’t watched yet). I’ve found two versions about the same material from as it seems both authors separately:

- [2019 MIT Open Courseware version](https://ocw.mit.edu/courses/mathematics/18-s097-applied-category-theory-january-iap-2019/lecture-videos-and-readings/)
- [2017 LambdaConf version](https://m.youtube.com/watch?v=IBeceQHz2x8)

I haven’t watched either of those video series yet, hoping that my understanding from the first book will suffice to grasp the formal mathematics in _Seven Sketches_.

### Category Theory • nLab
<https://ncatlab.org/nlab/show/category+theory>

With a basic understanding of category theory from the resources above (having worked through just the basic parts introducing categories, functions, and natural transformations is enough), this page offers a very good overview with pointers to lots more details about each concept in category theory, as well as further resources for every level of detail you can wish for.

I just found the very brief first few paragraphs very enlightening, describing the self-referential structure of category theory, which helps building a mental map of how everything relates to everything else.

## Additional resources
A few more resources I came across while looking for good explanations of category theory:

- [What is Applied Category Theory? • Tai-Danae Bradley](https://arxiv.org/pdf/1809.05923.pdf)
	- This looks promising for learning more about actual applications of the concepts.
- [The Catsters' Category Theory Videos](https://www.youtube.com/playlist?list=PLlGXNwjYhXYxKVa67r0pKuYufECy713bv) ([Overview](http://simonwillerton.staff.shef.ac.uk/TheCatsters/))
- [Applied Category Theory Course by John Baez • Azimuth Forum](https://forum.azimuthproject.org/discussion/1717/welcome-to-the-applied-category-theory-course)
	- This goes with the Seven Sketches course/book and might provide just a little more commentary on the material.