---
title: "Lifeline 1.8: MCP support and better breaks"
description: "Lifeline now talks to ChatGPT, Claude, and other AI tools via MCP. Plus: configurable break ratios, debt-based warnings, and AppleScript automation."
pubDate: 2026-04-05
sourceName: "Saent"
tags: ["saent"]
---

Lifeline 1.8 is live in the App Store. Besides the regular bug fixes, two big changes in this release: breaks finally work the way you'd expect them to, and Lifeline now talks to ChatGPT, Claude, and any other AI tool that speaks MCP.

## Your AI assistant can now see (and run) your day

Lifeline has always been about awareness, a visual record of how your day is actually going. But until now, that record lived only inside the app. If you wanted to ask, "How much deep work did I do last week?" you had to look at the bars yourself.

Not anymore. Lifeline 1.8 ships with two new ways for external tools to read and control it:

-   **AppleScript dictionary.** Eight commands for starting sessions, taking breaks, starting meetings, and querying status. Works from the Script Editor, Shortcuts, Raycast, Alfred; anything on macOS that speaks AppleScript.
-   **MCP server (**[**lifeline-mcp**](https://github.com/metztim/lifeline-mcp)**).** A Model Context Protocol server that exposes your Lifeline data and controls to any AI tool that supports MCP. That includes Claude Desktop, Claude Code, ChatGPT, and a growing list of others.

What this allows you to do:

-   Ask Claude `summarize my last week` and get a real answer based on your actual sessions, not a guess.
-   Have ChatGPT start a focus session for you at the end of a planning conversation, without you reaching for the menu bar.
-   Build Shortcuts that start a Lifeline session when you open a specific app, or end one when a meeting ends.

Install the MCP server via npm (`npx lifeline-mcp`) and point your AI tool at it. The repo has setup guides for Claude Desktop, Claude Code, and ChatGPT.

## **A better break experience**

The other half of this release makes some long overdue improvements to breaks.

**Configurable break ratios.** You're no longer stuck with Lifeline's default rhythm. Pick a preset (Pomodoro 5:1, Deep Rest 3:1) or set your own ratio. Work 45 minutes, break 15? Work 90, break 20? It's your call now.

**Debt-based overheat warnings.** Previously, Lifeline warned you to take a break when a session got long. That’s fine if you work in single, long sessions. But reality is messy, and the app would previously reset its overheat warning as soon as you started a new session.

The new system tracks break debt across sessions. The warning fires when the debt across sessions gets high, not when one session runs long.

**Breaks are actually explained now.** We’d often hear “I don’t understand how Lifeline calculates breaks,” or “why can I not take a break at my screen?”

There's now a dedicated Breaks pane in Preferences with a basic explanation of breaks, a link to more information on this blog, and a one-time intro that appears when your first break starts after updating.

## How to update

Lifeline 1.8 is free for existing users. Update from the Mac App Store, or grab a fresh copy at [the App Store listing](https://apps.apple.com/app/saent-lifeline/id1492352560). If you want to hook Lifeline up to your AI tools, start with the [lifeline-mcp repo](https://github.com/metztim/lifeline-mcp).

We'd love to hear how these new features are working for you! Send [an email](mailto:support@saent.com) or find us [on X](https://x.com/getsaent) and let us know your thoughts, ideas, or any questions.

[**Try the latest version**](https://apps.apple.com/app/apple-store/id1526186940?pt=118017664&ct=saent-blog&mt=8) **of Lifeline now from the macOS App Store.**
