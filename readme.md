# LWNVDA

An NVDA add-on that improves the usability of *Lone Wolf*, the submarine simulator by GMA Games.

## Requirements

This add-on relies on Lone Wolf's text highlighting feature.

To configure the game:

1. Open **Options → Speech / Screen Reader**.
2. Select **"No screen reader" (or unsupported)**.
3. When prompted, enable text highlighting.

## How it works

This add-on suppresses redundant announcements that would otherwise occur, such as repeated "selected" messages and duplicate reading of game text.

It also ensures that arrow keys used for controlling the submarine (e.g. depth) are no longer treated as text navigation keys by NVDA.

The result is a smoother experience, similar to the game's built-in support for SAPI5 or its direct integration with JAWS and Window-Eyes.

## Why use this add-on instead of SAPI5?

Lone Wolf already includes built-in SAPI5 speech output, originally intended for players without a supported screen reader.

Using SAPI5 directly may seem like the simplest option. However, there are a few practical advantages to using NVDA with this add-on:

* Access to a wider range of voices and speech settings
* More consistent behavior across different systems
* Improved responsiveness on modern Windows versions

On newer systems, the game's SAPI5 output can introduce noticeable lag, regardless of the selected voice. In comparison, NVDA generally provides a more responsive experience.

## Known issues

After selecting the experience level in the game, the message “press g for more information on the level you selected” is displayed.

This message is only provided through the game's direct speech system (SAPI5 / JAWS / Window-Eyes integration) and is not exposed via the text output used in text highlighting mode.

Because of this limitation, NVDA cannot detect or announce this message. All other in-game text and interactions are handled correctly by this add-on.

## Building the add-on

Requirements:

- Python 3.13
- uv

Build the add-on with:

```bash
uv sync
uv run scons
```
