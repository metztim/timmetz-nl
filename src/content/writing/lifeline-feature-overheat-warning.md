---
title: "Overheat warning (Lifeline feature)"
description: "As a Lifeline user, I want to get nudged when I've been in a session for too long without a break. This feature addresses that need."
pubDate: 2021-07-23
sourceName: "Saent"
tags: ["saent"]
---

_We're going to "work in the open" starting from this post. We'll share memo's, feature specifications, and other communication that can be of interest to others here on the blog._

## Description

**Status: released in Lifeline version 1.4.8**

Working for too long without a break hurts instead of benefits my ability to concentrate. So, when I emerge in deep work, I want to get nudged when I've been in a Lifeline session for too long without a break.

### Thesis

[Research shows 90-minutes](/writing/pomodoro-technique) is the maximum amount of time anyone can focus optimally. Beyond that point, focus goes downhill rapidly. Taking a break after 90 minutes is always better than continuing, **even though it might not feel that way in the moment**.

### Specifications

#### Requirements

The visual Lifeline bar at the top of your screen already visualizes session length, so we can also use it to indicate when you've passed the 90-minute point. We'll do this by extending the Lifeline bar with 10-minute increments at a time once you've passed the 90-minute mark, regardless of the original session length you chose when you started the session.

Once you pass the 90-minute mark, your entire bar will slowly start to turn red (#e8212d) over a period of 10 minutes. So at point 90:01, it starts to morph from blue, and it finishes to full red at the 100:00 mark.

Once you reach 100 mins, you get a notification similar in style to the end session notification, but with the following text:

🔥 _You're overheating! 🔥  
Taking a break after 90-minutes is essential for maintaining optimal focus throughout the day. What would you like to do?_

_Keep going | End session | Take a break_

![](/images/saent/lifeline-feature-overheat-warning/60f8b91c74ffa72b142e891e_end_session_notification.webp)

_The standard end session notification of Lifeline_

###### **Preferences**

We'll add an option to turn on and off the overheat warning in Preferences under Sessions > "During sessions, show..." We'll place it below "end of session label confirmation" and label it "overheat warning." By default, we will turn it **on**.

![](/images/saent/lifeline-feature-overheat-warning/60f8b95378f461179460c420_preferences.webp)

##### **Data tracking requirements**

Put a tracker on the option in Preferences to see how many users turn on or off this functionality. Ideally, we'd see the total percentage of users that have this option turned over time.
