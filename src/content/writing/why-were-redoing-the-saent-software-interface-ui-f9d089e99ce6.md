---
title: "Why We’re Redoing The Saent Software Interface (UI)"
description: "Before we get going: If you just want to see the new Saent UI, and don’t care about how we got there, just scroll straight through to the…"
pubDate: 2016-01-15
sourceName: "Medium"
mediumUrl: "https://medium.com/en-route-to-saenthood/why-we-re-redoing-the-saent-software-interface-ui-f9d089e99ce6"
tags: ["medium", "saent"]
---

![](/images/medium/b2a8238726b72f94dd6e1942.webp)

*Before we get going: If you just want to see the new Saent UI, and don’t care about how we got there, just scroll straight through to the chapter called “The Saent Interaction Engine” :)*

Often, doing what’s right in the long-term is difficult in the short-term. This applies on the individual level, like going to the gym, which might not be fun now, but can improve your health down overall, as well as to big corporations. Companies are often faced with deciding whether to do things that cause short-term pain (like spending money on R&D at the expense of their quarterly numbers) to chase long-term wins (like opening up a whole new product category).

We’ve recently come up against such a decision with Saent.

## **If it ain’t broke, why fix it?**

The beta testing of our software with a handful of Indiegogo backers largely triggered positive responses. On the whole, people liked how the software worked and reported that it was helpful and useful. Naturally some issues occurred, and we knew there were aspects we had to fine-tune, yet after a few weeks of watching usage metrics go up, use of Saent suddenly stalled. What was going on? Why were people excitedly using Saent for a few weeks, and then dropping off?

As we dug into this issue, we realized the UI (user interface) was the problem. As we made changes that were necessary to improve the core function of Saent, the software paradoxically started to become more difficult to use. Even though we weren’t adding a bunch of new features and succumbing to [*feature creep*](http://www.urbandictionary.com/define.php?term=feature+creep), small tweaks were nonetheless causing Saent to feel bloated because our UI was too rigid and not accommodating of what we needed to accomplish. Perhaps more importantly, we realized that the existing user interface was no longer meeting our vision for what Saent is — a vision that had itself evolved since the app was initially conceived.

![](/images/medium/d55cd6ea48a08b071fe823b7.webp)

The interface had been designed in the first half of 2015, worlds away from where we are now. Our vision for the product has changed quite a bit, both based on the insights we gained during [the crowdfunding campaign](https://medium.com/en-route-to-saenthood/34-mistakes-we-made-during-our-crowdfunding-campaign-8fdf877015d1#.pndkvq1ey), as well as from user testing over the past months. In addition, we never felt the UI was *as* unique as the overall [brand and device](http://saent.com) itself. It wasn’t *bad*, but it was just another software interface.

## **How to fix things**

Initially we considered sticking with the existing UI, but making some big and bold changes within that framework. But as we thought about it, we arrived at the inevitable: better to redo the entire interface.

This brings us back to the start of the article, the difficult decision: we’re close to shipping ([kind of…](http://status.saent.com/)), and redoing the entire UI is not easy, nor without risk. If you change anything in a product, you might unexpectedly break something somewhere else. This means we might not be able to deliver the software to our backers before the end of January, which is already a revised timeline *and* comes on top of a [second delay of the hardware](https://medium.com/saent-status-updates/saent-s-mea-culpa-the-curse-of-hardware-crowdfunding-28cf6cfbe542#.o6560wzcp). Not good.

So why consider this UI change in the first place? Why not just first ship what we had and then take it from there?

The first reason is that we strongly believe in what ad man [Raymond Rubicam](https://en.wikipedia.org/wiki/Raymond_Rubicam) once said:

> *“The client remembers an outstanding job years after he has forgotten that it was two months late.”*

It goes without saying, delays suck and should be avoided as much as possible. But we want the first user experience to be great and special. This doesn’t mean everything has to be perfect (then we would never ship), but if we find a substantially better way of doing things and it’s within reach, we think long-term gain should trump short-term pain. Which brings us to the second point…

As we were developing, testing and improving our product over the course of 2015, we started thinking of Saent as a person, a friend, if you will. Someone who speaks to you in the first person and helps you through your day. Sometimes by being tough, often helpful, and of course personal, informal and at times, funny.

## **Hi, I’m Saent!**

We started incorporating this tone of voice into parts of the software, and people liked it. Unfortunately, our original UI was not created with this in mind, so it ended up looking something like this:

![](/images/medium/22673022d521fb45179ca124.webp)

Personality? Kinda. Our existing UI doesn’t have many natural places for Saent to express itself.

In addition, the tests made clear something we already knew in our gut, but weren’t sure how to address: *everyone works in a slightly different way*.

- Some people like to set a clear goal at the start of the day, others don’t.
- Some like to work in 25 minute “sprints,” others prefer 50 minutes.
- Marketers think Facebook is Good (not a distraction), designers think it’s Evil (a distraction).
- And so on.

To make matters worse, these preferences can even change for one individual over the course of a day. That lead to a complicated *Settings* screen that some users felt compelled to visit often:

![](/images/medium/6db3bf29e48e9dcc87123a9b.webp)

That’s a lot of buttons and sliders for an application that shouldn’t distract you!

Finally, one other interesting thing happened: those fifty early beta testers started to report that Saent was becoming a *distraction*! The main source of this was our Leaderboard, since people started obsessively checking their score and how they were doing compared to others. They also felt there was too much to do and too much choice, even after the necessary improvements we introduced based on the testing feedback.

![](/images/medium/bc60f007610f45656593fe94.webp)

The Leaderboard is an aspect of Saent that people like, but many also found it overwhelming.

We had to find a better way.

## **The Saent Interaction Engine**

As all of these ideas floated around our heads over weeks and months, we began thinking about a “contextual” dashboard; instead of a bunch of fixed elements, as shown below, what if the dashboard items changed based on the time of day, the activity in your previous session, your personal work habits, and so on? This was our driving thought when we came out of the first “UI redesign brainstorm.”

![](/images/medium/0e9d76e4fba3c8fc092823e6.webp)

The existing Saent dashboard shows you everything, whether you need it or not.

This concept matured over the course of the following weekend, and it turned into something much bolder: what if we made the *entire* app contextual? One core problem most of our current and future users face is distraction in the form of information overload, which manifests itself in too much choice and too much to do. Saent shouldn’t add to that burden.

This was a key insight, but one piece of the puzzle was still missing: the interaction with Saent as a person. Ideally we would build something like Siri or an AI like the one in the movie *Her*. A friend who can help you “get through your workday” in the best possible way. But voice-driven systems are definitely out of the question for us now (and perhaps also not suitable for our purposes), so we started thinking about a text-based option. As we did, we realized there is a global “standard” for visualizing digital, text-based interaction between different parties. It’s used from the USA to China, from Europe to Africa, and everyone with a smartphone is familiar with it:

![](/images/medium/44040bba126fe47d3c585218.webp)

Left to right, iMessage, WhatsApp, WeChat, Siri.

You “talk” on the right, the other party on the left. And that was our *Eureka!* moment.

![](/images/medium/558df33fe821aebd43eec036.webp)

*The interaction progresses downwards; on the left is the opening screen of our app. That moves upwards and the conversation with Saent starts from there.*

By adapting the general UI of the messaging apps everyone is already familiar with, we can let Saent “talk” to you. Saent is on the left, your options (generally framed as responses) are on the right. This truly gives Saent a personality and allows for all kinds of fun interactions. But this is not merely entertaining and superficial.

![](/images/medium/f7896f71e96298b5356ea8c2.webp)

The options you’re presented with on the right are not fixed, nor do they show up completely at random:

- Have you already checked out the leaderboard in your previous break? You will not be presented with that option for at least a few hours.
- Did you run into any sites and apps Saent doesn’t know yet in your previous session? Saent will ask you to categorize them (mark them as either *Good* or *Evil*).
- Did you indicate you want to be asked a specific question at the start of your day? Saent will make sure to do so in the morning.

As we started exploring and taking this further, we realized there are many more advantages to such a simple, yet powerful text-based interface. Here are a handful of examples…

## **1. Changing your session length**

With the original interface, here are the steps required to start a session with a new session length instead of your default (something which turned out to happen often):

![](/images/medium/836cb07a102535c2bd8ee6b0.webp)

The existing flow: first go to Settings, then use a slider to set the right time, and then navigate back to the dashboard to start a new session (or of course, [hit the button](http://saent.com)).

And then, if you wanted to run your next session back at your original default length, you’d have to go through this same process *again*.

Here’s how this will work in the new interface; you just click on the dotted underlined *50 minutes* and change to the desired time:

![](/images/medium/1e30eda39e0fe0d57b73b5bf.webp)

*In the new UI, you can start a session and choose how long it should last, all from the same screen.*

In addition, the new interface now allows Saent to intelligently suggest you to change your session length based on whether you’ve failed at your current default length:

![](/images/medium/0975cb204971601a7a0eda74.webp)

## **2. Getting help or giving feedback**

In case you need help on a certain aspect of the app, our former UI would cater to this just like most desktop applications do, with a help menu:

![](/images/medium/9de3419af13848c0fad0386e.webp)

And again, as with most traditional apps, it would not always be possible to know exactly what you’d need help with, so you might have to search [our knowledge base](http://help.saent.com) yourself for the right article. With our new interaction model, you can now ask for an explanation on almost anything, right in the software.

![](/images/medium/c5080d178d417f7e1d309e68.webp)

Categorizing apps and sites in the current Saent app happens in session (distracting) or on an often overloaded dashboard (confusing). In the new UI, this task is made simpler and kept in the context of your previous session.

Saent will know exactly what you need help with, and, as you “master” the workings of the app, these options will slowly disappear from your interactions; one less choice for you to worry about!

It’s also much easier for Saent to learn by asking for feedback on almost anything, for example after a failed session:

![](/images/medium/f85013bb984a13f4362dd4bf.webp)

The additional touch points between users and Saent like the one above will allow Saent to learn more about how you work and help you to work smarter and be more productive.

## **3. Installing an integration**

In the near future, we’ll also start adding integrations with other (productivity) applications: Saent might award you extra points for completing specific functions within another app. Your status in your favorite communication tool might go to “busy” when you’re in a session. Maybe Saent will remind you what you need to get done today based on your to-do list in a task management app.

Previously, installing such an integration would have probably worked through a [*wizard*](https://en.wikipedia.org/wiki/Wizard_%28software%29) with a string of popup windows. No more with the new UI:

![](/images/medium/a2e2ebda9ee5dc395f55e720.webp)

Here’s an example of what an integration could look like in our new UI.

Now integrations with other apps can truly be baked into the Saent experience, which creates smoother, more efficient workflows and adds value to both Saent and to the other apps you already use.

## **4. What to do during a break**

Right from the very first concept of Saent (back when it [was called SANE](https://medium.com/en-route-to-saenthood/en-route-to-saenthood-4-the-damn-name-fb4ec3871fb0#.tdqw1t8wv)…) , the idea was not only to focus on, well, focus. The concept also touched on what to do during your oh so important breaks. Help you refuel? Find inspiration? Properly relax?

Along the way, we parked this idea. We couldn’t immediately figure out how to nicely integrate this into the software. Unexpectedly, the new interface turned out to be able to accommodate this concept perfectly. It has a very clear rhythm of *session / break*, *session / break*, and so on. While you’re working, only the essential information is displayed in the app, and no other options are available:

![](/images/medium/9676a646e871ce2ea2164f4f.webp)

*The entire app screen changes as you enter into a work session.*

Similarly, an Evil (distracting) site will be simply, but clearly marked as such…

![](/images/medium/12b64c5523557f4d56eeb06e.webp)

Yet when you finish a session, Saent can now ask what you’d like to do during your break.

We can offer two great options here. One is to take an offline break, away from the computer without screen time. Saent will then overlay your entire screen and start a timer (based on your input):

![](/images/medium/8b9686d05896b034cb896c3d.webp)

Alternatively, you can ask Saent to inspire you during your break. This will lead you to our curated content section, where you will find tons of useful content on productivity, work/life balance and other interesting topics. This section is hand-curated by [our in-house librarian](https://medium.com/en-route-to-saenthood/how-we-plan-to-put-a-librarian-to-work-at-our-tech-startup-e06fbc5fab3a#.z1hol6440)!

## **WHEN?**

We hope by now you only have one burning question left: *WHEN?* When can I try the new Saent?

A lot of the technical features necessary to run the above were already included in the original version of the software, so we can build on those. Creating the interaction engine is something completely new though, but we’re [making good progress](http://status.saent.com) on both OS X and Windows.

Our current expectation is to be inviting people to the beta test of this new UI before the end of this month (January). We’ll then be further expanding these invitations to the rest of our Indiegogo backers over the course of February, assuming we don’t run into any major problems. We’ll of course communicate this progress here in our dedicated [*Saent Status Updates*](https://medium.com/saent-status-updates) publication.

Please do let us know your thoughts about this new UI; any and all feedback is welcome!

*For an accurate and frequently updated estimate of our delivery timelines, you can check out our* [*product status page here*](http://status.saent.com/)*.*

---

## Ready to give Saent a try?

[**Download the free app now**](http://download.saent.com/) to start working smarter, being more focused, and developing better work habits.

![](/images/medium/23424b1e180cb2b2e2c8d613.jpg)

You can download the free version of the Saent app now by clicking the image above.

Or [buy your Saent button](http://www.saent.com/product/saent/) (now shipping!) with a 12-month subscription to the Premium Saent app included!
