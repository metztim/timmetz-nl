---
title: "EmojiFinder"
description: "Menu bar emoji and Unicode search for Apple Silicon Macs, a fork of Glyphfinder"
status: active
role: "Maintainer"
startDate: 2026-09-18
url: "https://github.com/metztim/EmojiFinder/releases/latest"
repo: "https://github.com/metztim/EmojiFinder"
tags: ["macos", "tools", "open-source"]
sortOrder: 9
---

EmojiFinder is a macOS menu bar app for finding emoji and Unicode characters: press a shortcut, type a word, copy the character. It is a fork of [Glyphfinder](https://github.com/ueberdosis/glyphfinder) by [überdosis](https://ueberdosis.io), a small paid app I used daily for years. überdosis discontinued it in 2022 and only ever shipped an Intel build, so on an Apple Silicon Mac without Rosetta it no longer starts.

The fork rebuilds the app on a current Electron so it runs natively on M-series Macs, and adds a few small improvements: the emoji list is current through Unicode 17, search results are ranked so the obvious emoji comes first instead of dozens of look-alike symbols, and the license key is gone. The design and most of the code are still überdosis's work. The [download](https://github.com/metztim/EmojiFinder/releases/latest) and the [source](https://github.com/metztim/EmojiFinder) are on GitHub.
