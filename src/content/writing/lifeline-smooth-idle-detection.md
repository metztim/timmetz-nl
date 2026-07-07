---
title: "Smooth idle detection in Lifeline 1.5"
description: "Lifeline's idle detection has been its most-hated feature, but we couldn't think of something better—until now. Here's everything you need to know about the app's new smooth idle detection."
pubDate: 2022-07-14
sourceName: "Saent"
tags: ["saent"]
---

There's one feature in our app Lifeline people have complained about since the software's launch.

When you become inactive—i.e., you stop using your keyboard and mouse—a countdown timer appears in the middle of your screen. It asks whether you're still at your computer. If you're not, Lifeline launches a break when the counter reaches zero. If you are, you make the pop-up go away by using your mouse or keyboard, and your focus session continues.

![Visual of Lifeline's current idle timer countdown.](/images/saent/lifeline-smooth-idle-detection/62cfc3cea659073309903d32_current-idle-countdown.webp)

_Lifeline's current idle timer countdown._

This feature ensures you don't have to worry about manually launching breaks. Just leave your computer, and Lifeline will do it for you. It also keeps your data accurate—sessions don't continue while you're not at your computer.

Here's where things get problematic: imagine that, as part of your session's task, you're watching a YouTube video, writing in a physical notebook, or are just in deep thought.

Since you're not using your mouse or keyboard, Lifeline thinks you're idle and throws up the countdown pop-up every two minutes. You'll have to move your mouse each time this happens or your session ends. It's annoying, but we couldn't think of something better—until now.

## Enter smooth idle detection

A few weeks ago, I was using a meditation app. I set my session time for ten minutes, then kept going after I passed that point. When I opened the app again, it asked whether I wanted to add the extra minutes to my session. 💡

**"We could use the same mechanism for Lifeline!"** I realized.

Instead of warning people _before_ going idle, ask them afterward if they want to mark that period as part of their session or as inactive (break) time.

![](/images/saent/lifeline-smooth-idle-detection/62df4b4f7af237f819d38d24_smooth-idle-detection.webp)

_Lifeline's new smooth idle prompt that appears when you become active again._

Moving the prompt after the fact seems like a subtle change, but it makes a big difference. Say you're watching a YouTube video. Once Lifeline considers you idle, that part of your Lifeline becomes green (as in the example above), but you don't get any pop-up.

Instead, Lifeline asks you to continue your session or end it at the moment you became idle only when you use your mouse or keyboard again.

## When is smooth idle detection available?

Lifeline 1.5 is now available for [download from the MacOS App Store](https://apps.apple.com/app/apple-store/id1526186940?pt=118017664&ct=saent-blog&mt=8) and as an update to existing users.

Please do leave any comments, questions, or concerns you might have about this new feature in the comments below or [in the Saent community](https://community.saent.com/c/feedback/)—we'd love to hear them!
