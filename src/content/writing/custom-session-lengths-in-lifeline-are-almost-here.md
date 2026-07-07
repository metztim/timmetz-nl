---
title: "Custom session lengths in Lifeline are here"
description: "With our app Lifeline, you can work in 25-minute sessions based on the Pomodoro Technique. Unlike many other Pomodoro timer apps, ours provides flexibility, as you don’t have to stop after completing a 25-minute cycle."
pubDate: 2021-01-05
sourceName: "Saent"
tags: ["saent","lifeline-pomodoro-technique-product"]
---

With [our app Lifeline](https://apps.apple.com/app/apple-store/id1526186940?pt=118017664&ct=saent-blog&mt=8), you can work in 25-minute sessions based on [the Pomodoro Technique](/writing/pomodoro-technique). Unlike many other Pomodoro timer apps, ours provides flexibility, as you don't have to stop after completing a 25-minute cycle. This allows you to follow different types of work rhythms.

Another unique aspect of Lifeline is the visual progress bar at the top of your screen. The full width of this line represents 25 minutes while you're in a session. This way, you get a real feel for your progress.

Until now, this visual progress bar always represented 25 minutes. You could continue for a second cycle within the same session, but the bar would just start filling up from the left side of the screen again.

We're changing this with the upcoming release of custom session lengths.

## Here's how custom session lengths will work

_Custom session length >_ will be available as a fold-out from the Lifeline menu, similar to the expandable menu for starting meetings.

![](/images/saent/custom-session-lengths-in-lifeline-are-almost-here/60852d7a7650bcc1da08f062_imgs-2Fapp-2Ftimmetz-2FOifbEPHy0j.webp)

_The Custom session length menu item will work similar to the existing Start meeting._

Initially, the fold-out menu will have the following options:

-   10 minutes
-   50 minutes
-   90 minutes
-   Enter length
-   Until next meeting

After using these options for a while, Lifeline remembers your most popular lengths.

For example, if you mostly do sessions of 50, 75, and 90 minutes, the 10 minutes option will disappear from the list, and the menu will now look like this:

-   50 minutes
-   75 minutes
-   90 minutes
-   Enter length
-   Until next meeting

When you choose _Until next meeting_, Lifeline will automatically start a session that lasts until your next meeting event.

You can also quickly adjust your session length in the session label window that shows up at the start of your sessions.

![](/images/saent/custom-session-lengths-in-lifeline-are-almost-here/60852d7adb95583e1efa310d_imgs-2Fapp-2Ftimmetz-2Fz4TX6S4s5e.webp)

_Very rough mockup for adjusting your session length in the session label window._

You will still earn tomatoes whenever you hit 25-minutes of uninterrupted focus, regardless of what session length you've set. We understand this could be confusing, especially for new users. That's why, by default, custom session lengths are turned off, and you need to turn them on in _Preferences_.

### Use cases

Here are some — but certainly not all — ways in which you can use custom sessions:

-   **You want to focus for 50 or even 90 minutes.** In theory, you can already do this with Lifeline using the default, 25-minute cycles. In reality, you will then often find yourself deciding to take a break earlier when you hit 25 or 50 minutes. By setting the session length to 50 or 90 minutes, you make a real commitment to go for a long session.
-   **You want to work on a few smaller tasks that each take 10 or 15 minutes.** In this case, shorter cycles allow you to label each specific task and ensure you don't spend too much time on a small item.
-   **You want your session length to exactly match the time you have available before your next meeting.** You might have 10, 20, or 35 minutes before your next meeting. With the _Custom session length > Until next meeting_ option, you'll be able to do that with one click.

## Want to use custom session lengths already? You can!​

While the full functionality described above is still under development, the current [macOS App Store version of Lifeline](https://apps.apple.com/app/apple-store/id1526186940?pt=118017664&ct=saent-blog&mt=8) already includes a hidden, basic implementation of custom session length!

To access the feature, follow these steps:

1.  [Download the latest version](https://apps.apple.com/app/apple-store/id1526186940?pt=118017664&ct=saent-blog&mt=8) from the macOS App Store (1.3)
2.  Hold down the _option_ key, then left-click the Lifeline tray icon.
3.  You'll now see a menu option called _Developer options >_.
4.  Go there and select _Allow cycle customization_.
5.  Once you've checked this option, you'll see an item called _Custom cycle length:_ under _Basics_ in _Preferences_.
6.  Set this field to your desired length. The minimum is 10 minutes, the maximum 90.
7.  Your visual progress bar at the top of the screen will now represent that duration instead of the default 25 minutes.

Note that this basic implementation has some small issues, but nothing critical. For example, if you have midway point signals turned on, they will still ring at 12.5 minutes. The visual bar will also not empty and start over once you reach the end of your cycle length.

**The full implementation of custom session lengths will be a paid Lifeline feature and become available later in Q1.**

If you have questions, ideas, or feedback about custom session lengths, do get in touch with us [on Twitter](http://twitter.com/getsaent) or [by email](mailto:support@saent.com). 🙏
