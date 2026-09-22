---
title: "Voices on software design: Melvin E. Conway"
date: 2024-04-12T17:01:13Z
series: voices-on-software-design
---

Over the last few weeks I’ve been reading many classic programming papers about simplicity, complexity, and adjacent topics. I thought I’d share some highlights from the papers and a few of my thoughts.

Let’s begin with: [Melvin E. Conway • How Do Committees Invent? (1968)](http://www.melconway.com/Home/Committees_Paper.html)

## How Do Committees Invent?

*Melvin E. Conway · 1968*

Conway is known for *Conway’s Law*, and this is the paper that defined it (highlights mine):

> *The basic thesis of this article is that **organizations which design systems** (in the broad sense used here) **are constrained to produce designs which are copies of the communication structures of these organizations**. We have seen that this fact has important implications for the management of system design. Primarily, we have found a criterion for the structuring of design organizations: a design effort should be organized according to the need for communication.*
>
> *This criterion creates problems because the need to communicate at any time depends on the system concept in effect at that time. Because the design which occurs first is almost never the best possible, the prevailing system concept may need to change. Therefore, **flexibility of organization is important to effective design**.*
>
> *Ways must be found to **reward design managers for keeping their organizations lean and flexible**.*

Conway picks up on the importance of flexibility very early in the history of computing. I, of course, read this as an early realization that the design of software is a [dynamic process](/2023/02/03/16-dynamical-systems/) where the changes we make are reflected back to us and change our perception and understanding of the designed object — [reciprocal realization](/2024/01/05/on-simplicity-%234-reciprocal-realization/). We need to be ready to respond to what we learn along the way and prepare to change ourselves — in this case our team organization — to adapt to the changing needs.

I love how he phrases his suggestion to find ways to *reward* design managers for keeping their organizations flexible. This is not something that can be mandated through rules. We need to think about incentive structures, how we can set up our environment to encourage us to make appropriate choices in the moment.

### Organizational decisions are design decisions

Essentially, what he points out is that the decisions that are made to set up a team to design, develop, and implement something already impact the final design — these organizational decisions are also design decisions! Depending on how the team is set up, coordination efforts and communication paths heavily influence the possible solutions a team can come up with and many branches of the solution space have already been cut off.

> ***[T]he very act of organizing a design team means that certain design decisions have already been made, explicitly or otherwise.** Given any design team organization, there is a class of design alternatives which cannot be effectively pursued by such an organization because the necessary communication paths do not exist. Therefore, there is no such thing as a design group which is both organized and unbiased.*

Another way to interpret this: the team’s communication pathways which are defined in its organizational structure determine the [salience landscape](/2023/02/24/19-here-and-now-ness/#the-function-of-consciousness) of the team — what is considered relevant and what will likely be overlooked. When we cut the scope into separate parts to assign them to different teams and people, whatever these units stand for will be highly salient to everyone, because the structure is salient to everyone.

If you have a “performance” team responsible for making things work fast and efficiently, performance will be salient. If you don’t have such a team, it is up to individuals in teams with different functions to pick up on performance whenever it occurs to them — much more likely that it gets overlooked.

Conway also touches on how the organization structure introduces strong incentives leading to worse designs.

Design work is limited by our individual capacity to comprehend the whole system. Naturally, we gravitate towards [a divide and conquer approach](/2024/01/19/on-simplicity-%235-hiding-complexity/#cultivated-ignorance), thereby making implicit design decisions based on where we define the delegation boundaries. Schedules, budgets, and a culture of risk avoidance further push us towards chopping up the problem early, making premature design decisions that may likely set us up for failure. We are no longer focused on what is best for the design, but driven by external forces.

> *It is a natural temptation of the initial designer — the one whose preliminary design concepts influence the organization of the design effort — to delegate tasks when the apparent complexity of the system approaches his limits of comprehension. This is the turning point in the course of the design. Either he struggles to reduce the system to comprehensibility and wins, or else he loses control of it. The outcome is almost predictable if there is schedule pressure and a budget to be managed.*
>
> *A manager knows that he will be vulnerable to the charge of mismanagement if he misses his schedule without having applied all his resources. This knowledge creates a strong pressure on the initial designer who might prefer to wrestle with the design rather than fragment it by delegation, but he is made to feel that the cost of risk is too high to take the chance. Therefore, he is forced to delegate in order to bring more resources to bear.*

And of course, what happens once a design organization is in place? It will be utilized, whether needed or not, and whether its current organization is appropriate for the next problem or not, leading to even worse designs.

> *Once the organization exists, of course, it will be used. Probably the greatest single common factor behind many poorly designed systems now in existence has been the availability of a design organization in need of work.*

I also liked this little gem of insight, which feels all too familiar from my time working with big organizations:

> *[T]here’s never enough time to do something right, but there’s always enough time to do it over.*

Often it is easier to get a whole new project approved to completely redo something than it is to get the resources to do it properly the first time.

### Design begins sooner than we think

What most people seem to take away from this paper is the structural similarity between a designed result and the organization that designed it.

For me this paper is a powerful expression of how the act of design begins much sooner than we think. Even if we just consider setting up a team and structuring it to get work started on a new thing, we have already designed part of it.

The structural-functional organization of a company is something that requires much more effort to change, just because company culture and processes and multiple stakeholders are involved. It is a complex coordination effort that stands on top of the design effort, yet it has direct impact on the possible directions of the design effort. Keeping the organization structure lean and flexible is required for effective design.

It reminds me of Christopher Alexander’s notion of *non-separateness*. Everything is always part of something larger on a higher level of scale. We might think of the design work as something that applies to the thing that’s being designed. And it’s easy to overlook that we — the designers — are part of that, too. And if we work as part of an organization, we are subject to the organization’s culture and processes, which are also influencing our work and therefore the possible outcomes.

This also points at the importance of deeply understanding the problem to be solved, which requires good communication, if multiple people are involved. Of course, Conway’s focus is on teams — organizing multiple people. But his discoveries align well with a perspective that looks closer at the individual, which we will look at in another paper in the near future.

---

[Share](/2024/04/12/voices-on-software-design-melvin-e.-conway/)

Mirror of the Self *is a weekly newsletter series investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

*If you are new to this series, start here: [On simplicity…](/2023/10/27/on-simplicity/)*

*The previous series starts here: [01 • A secular definition of sacredness](/2022/09/30/01-a-secular-definition-of-sacredness/). 
Overview and synopsis of articles 01-13: [Previously… — A Recap](/2023/01/06/previously-a-recap/). 
Overview and synopsis of articles 14-26: [Previously… — recap #2](/2023/04/28/previously-recap-%232/).*

*Also check out my presentation [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/).*
