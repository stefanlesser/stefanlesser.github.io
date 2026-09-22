---
title: "Infrastructure"
date: 2024-09-06T17:00:57Z
---

*Infrastructure* is one of these terms that we software people like to throw around as if everybody knew exactly what it means. As usual, it’s a term that comes with lots of assumptions, some of which we may want to take a closer look at.

This is [what Wikipedia has to say about it](https://en.wikipedia.org/wiki/Infrastructure):

> Infrastructure is the set of facilities and systems that serve a country, city, or other area, and encompasses the services and facilities necessary for its economy, households and firms to function. Infrastructure is composed of public and private physical structures such as roads, railways, bridges, tunnels, water supply, sewers, electrical grids, and telecommunications (including Internet connectivity and broadband access). In general, infrastructure has been defined as “the physical components of interrelated systems providing commodities and services essential to enable, sustain, or enhance societal living conditions” and maintain the surrounding environment.

As is not uncommon for us software people, we once again picked a term from architecture as a metaphor to represent something supposedly similar in software.

I also found this bit about its etymology useful:

> The word is a combination of the Latin prefix infra-, meaning “below”, as many of these constructions are underground (for example, tunnels, water and gas systems, and railways), and the French word structure.

### Infrastructure is what we depend on

The whole point of something we consider infrastructure seems to be that it provides us with something that we can reliably depend upon. In the physical world that means “commodities and services”, and that maps intuitively well to software.

While I was at it, I looked up [how Wikipedia defines “commodity”](https://en.wikipedia.org/wiki/Commodity):

> In economics, a commodity is an economic good, usually a resource, that specifically has full or substantial fungibility: that is, the market treats instances of the good as equivalent or nearly so with no regard to who produced them.

Notice how deep we are already in economic language.

Of course, infrastructure is *[functional](/2024/01/19/on-simplicity-%235-hiding-complexity/#utility-first)* [and delivers](/2024/01/19/on-simplicity-%235-hiding-complexity/#utility-first) *[utility](/2024/01/19/on-simplicity-%235-hiding-complexity/#utility-first)*. It is no coincidence that the quintessential exemplars for infrastructure in English even share the name “utilities”. “Full or substantial fungibility” says a lot about the [categorical identity](/2024/03/01/on-simplicity-%238-identity/) of infrastructure. It has become so replaceable that it no longer carries any kind of unique identity that we would build an individual connection with. Infrastructure is supposed to be *useful*. Nothing else. That’s the point.

But not everything that is replaceable and useful automatically becomes infrastructure. Something else is needed.

If we depend on something, we want it to be dependable, which means trustworthy and reliable. We want it to function in a stable and predictable manner. We don’t want any surprises with infrastructure, because surprises here usually mean trouble. Naturally, “infrastructure” carries the image of something static, rigid, and inflexible. These are exactly the properties you want from a strong and stable foundation that you can build upon. (Funny how we can’t get enough of these architecture metaphors.)

Simultaneously, though, reliable and dependable infrastructure makes us take it for granted. We forget how it came to be. And [we become ignorant of how it works](/2024/01/19/on-simplicity-%235-hiding-complexity/#cultivated-ignorance). If it is in fact reliable, if it just works, then why should we bother? Put few people in charge of maintaining it, who need to know it to a certain depth. Everybody else can use the freed up capacity to do something else that builds on top of it, something presumably more important. That’s how we scale to higher and higher levels of productivity. But that’s also how we amass higher and higher layers of structure and sediment below us.

Naturally, we are a lot more excited about *what* infrastructure makes possible than *how* it does that. So we spend most of our time thinking about what to build on top of it, rather than about the price we pay for it to exist in the first place, and for it to keep working reliably in the future. And as long as it keeps fulfilling our expectations, we have no reason to worry about it. That’s what we built it for.

### Infrastructure wants to grow horizontally

While the original definition for architecture above implies physicality (“public and private physical structures”) and locality (“serve a country, city, or other area”), we know that in software those are different beasts.

In its physical incarnation infrastructure implies spanning a larger area and delivering utility to multiple beneficiaries. Embedded in an economic framework, this leads us directly to cost, scale, and efficiency. Infrastructure needs some level of acceptable efficiency. We can’t afford to maintain infrastructure that overall does not deliver a net benefit to the communities it serves.

This causes interesting effects. For one, infrastructure wants to expand. Because that is how it becomes more efficient. Scaling effects like network effects reduce cost per user and may attract more customers to participate in the first place (eg. the usual phone network example — it gets better the more people are using it, because you can reach more people). This establishes a strong positive feedback loop, which is the main story arc in the wet dreams of many tech startup founders. Once successfully established, infrastructure only gets stronger over time.

As infrastructure expands, it reaches into more and more environments it is less and less adapted to. The fact that “everybody uses it now” helps convince skeptics, late adopters, and laggards to overlook certain shortcomings and motivate themselves to adopt it. It usually helps that by this time it has grown so large and its efficiency has improved so much that it is now also much cheaper. The wider it spreads, the easier it becomes for it to spread even more.

### Infrastructure needs to stay around

Another interesting effect that applies to infrastructure is best described with the [Lindy effect](https://en.wikipedia.org/wiki/Lindy_effect):

> The Lindy effect proposes the longer a period something has survived to exist or be used in the present, the longer its remaining life expectancy. Longevity implies a resistance to change, obsolescence, or competition, and greater odds of continued existence into the future.

What stayed around, stays around. Infrastructure is built to be depended on. If it has made it for long enough, it will more likely persist even longer. In practice that means over time something can justify its existence less on the utility it provides and more on the fact that it’s been around for so long. Everybody now considers it infrastructure, is familiar with it, and “this is how we have always done it” becomes a harder to beat argument. Infrastructure has a built-in tendency to overstay its welcome.

The longer it stays around, the more we rely on it. The more we rely on it, the more we depend on it. The more we depend on it, the stronger it becomes. The stronger it becomes, the harder it becomes to change or replace. To a point where people believe it’s impossible to replace, and we shouldn’t even try. The progression towards this point happens gradually and often invisibly.

We tend to see infrastructure as something that enables. We save time and effort and can focus on what we can build on top of it. We can work on novel things reaching new heights instead of dealing with boring boilerplate or reinventing perfectly fine wheels that already exist. It helps us scale and to be efficient. It makes us more productive.

We rarely consider established infrastructure as something that locks us into one particular branch of a design space, that prevents us from exploring alternatives, and that makes us dependent and vulnerable to foreign influence, control, and exploitation. And if we do consider these things at all, we usually believe that the opportunities of what we can build on it outweigh the risks.

Until they don’t.

Like a star collapsing into a black hole, entrenched infrastructure sticks around and gains mass. The more mass it has, the more it gains. When do we cross the event horizon where we can no longer escape its gravitational pull? And when does unbounded growth turn into a cancer that leads to system collapse?

We usually do not concern ourselves with negative aspects of infrastructure dependencies. Its benefits are much more salient to us than its risks. We like to think about exciting possibilities in the future more than we like to think about hypothetical threats in the present. Until those threats become real. Then, of course, it is often too late to deal with them swiftly.

### Infrastructure resists change — by design

The world is not static. Everything around us changes all the time. Sometimes we run into situations where things around us changed so dramatically that existing infrastructure gets in the way. It is in these situations that we suddenly become aware of the problems with perfectly reliable infrastructure. Once our requirements change we find ourselves in a situation where we are no longer productive, and where infrastructure makes us inefficient and potentially even restricts our agency.

Suddenly, its benefits turn into issues. We used to like its rigidity and inflexibility, because stability prevents surprises. But now we want something we weren’t able to predict. Its rigid and inflexible nature is now a problem we have to work around, making us less productive. The former blessing has turned into a curse.

What can we do? If we’re lucky, we can improve existing infrastructure to add what is missing and make it compatible with what we want. But often that is not straightforward and leads to suboptimal workarounds that everyone knows should be “done properly at some point”, and never will. Widely deployed infrastructure is by definition difficult to change. Because that is precisely what we designed it to be.

We want stable infrastructure we can rely on. Until we don’t anymore. Then we want it to be easy to tear down and replace. We can’t have both.

Choose your dependencies wisely.

---

[Share](/2024/09/06/infrastructure/)

Mirror of the Self *is a series of essays investigating the connection between creators and their creations, trying to understand the process of crafting beautiful objects, products, and art.*

*Using recent works of cognitive scientist John Vervaeke and design theorist Christopher Alexander, we embark on a journey to find out what enables us to create meaningful things that inspire awe and wonder in the people that know, use, and love them.*

***Series**: [Mirror of the Self](/series/mirror-of-the-self/) • [On simplicity…](/series/on-simplicity/) • [Voices on software design](/series/voices-on-software-design/) 
**Presentations**: [Finding Meaning in The Nature of Order](/2023/05/05/finding-meaning-in-the-nature-of-order/)*
