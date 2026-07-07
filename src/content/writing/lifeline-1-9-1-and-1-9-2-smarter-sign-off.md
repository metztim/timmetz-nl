---
title: "Lifeline 1.9.1 and 1.9.2: A smarter Sign Off Challenge"
description: "Sign Off is now on by default for everyone, and it knows about your meetings. Plus a Check for Updates menu item, a popover that doesn't crowd your panels, and a handful of fixes across both releases."
pubDate: 2026-05-27
sourceName: "Saent"
tags: ["saent"]
---

Lifeline 1.9.1 and 1.9.2 are live in [the App Store](https://apps.apple.com/app/saent-lifeline/id1492352560). Both patches refine the Sign Off Challenge introduced in 1.9: making it visible to everyone, and teaching it to play nice with your calendar.

## Sign Off is on by default now

Sign Off shipped in 1.9 as an opt-in feature. The morning prompt and tray menu only appeared if you flipped a toggle in Preferences first. In practice that meant most people never saw the feature.

1.9.1 flips the default. Sign Off is now on for everyone, so the morning prompt asks when you want to stop work, and the menu bar tray shows today's stop time at a glance. If you turned it off at some point, your preference is preserved.

New users get a one-day grace before the morning prompt appears, so the first day with Lifeline is just about getting familiar with the basics. After that, the daily commitment ritual starts.

You can still turn Sign Off off in _Preferences > Sign off_.

## Sign Off knows about your meetings now

A real scenario that came up after 1.9 shipped: a meeting starts at 8:55, your stop time is set to 9:00, and Sign Off locks the screen five minutes into the call. Force Quit becomes the only escape.

1.9.2 is here to fix that. Sign Off is now meeting-aware.

If a meeting is active when your stop time hits, the lock waits until the meeting ends, plus your usual grace period. If a meeting starts after the lock has already engaged, the lock disengages for the meeting and re-engages once it's over.

The lock screen also previews what's coming. With a meeting starting in twenty minutes, you'll see "Opening at 9:00 for Standup until 9:30" so you know what to expect.

A few details worth knowing:

-   Only meetings on calendars you've enabled as the "meeting" type defer the lock. Personal calendars don't count by default, so a dinner reservation won't keep your computer open.
-   Lifeline meetings (the ones you start inside the app) defer the lock indefinitely. It won't engage until you end the meeting.
-   The Set sheet warns you if your picked stop time sits at or after a scheduled meeting, so you can adjust before committing.
-   The day bar's pink lock zone shifts in real time to reflect the effective lock time during a deferral.

## Smaller fixes across both releases

A handful of other improvements:

-   **Check for Updates is back.** The tray menu now has a Check for Updates item that pings the App Store and tells you whether there's a newer version available.
-   **The Sign Off popover no longer overlaps open panels.** When the warning popover appears while a session or meeting panel is open, it slides out of the way instead of stacking on top.
-   **Tray title refreshes after midnight.** The day's stop time used to show yesterday's value until you clicked the menu. It now refreshes correctly on day rollover.
-   **Strict-break fix for hidden calendars.** If you had a meeting on a calendar you'd hidden in Lifeline, strict break mode could leave the lock blocking that meeting. The safety check now considers all calendars regardless of your visibility toggles.
-   **MCP `add_activity` errors no longer swallowed.** The MCP tool now propagates errors back to your AI client instead of failing silently.

## How to update

Lifeline 1.9.1 and 1.9.2 are free updates. Update from the Mac App Store, or grab a fresh copy at [the App Store listing](https://apps.apple.com/app/saent-lifeline/id1492352560).

We'd love to hear how the meeting-aware Sign Off is working for you. Send [an email](mailto:support@saent.com) or find us on [LinkedIn](https://www.linkedin.com/company/saent), and let us know your thoughts, ideas, or any questions.

[**Try the latest version**](https://apps.apple.com/app/apple-store/id1526186940?pt=118017664&ct=saent-blog&mt=8) **of Lifeline now from the macOS App Store.**
