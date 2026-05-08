# Lone Wolf add-on for NVDA
# makes the Lone Wolf submarine simulator by GMA Games more usable with NVDA.
# Suppresses redundant selection announcements and speaks only relevant game text.
# Also prevents arrow keys from being treated as text navigation keys when controlling the submarine's depth and direction.
#
# Copyright (C) 2026 Karl Eick
# Released under GPL v2 or later.

import appModuleHandler
import speech
import api
import keyboardHandler
from logHandler import log

_original_speakSelectionChange = speech.speakSelectionChange


class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		speech.speakSelectionChange = self.filtered_speakSelectionChange
		self._gesturesBound = False

	def isMainWindow(self):
		"""Limit add-on behavior to the main game window to avoid unwanted effects in secondary windows, such as the help viewer."""
		try:
			fg = api.getForegroundObject()
			title = getattr(fg, "name", "") or ""
			return "Lone Wolf" in title
		except Exception:
			log.exception("Error while checking Lone Wolf foreground window")
			return False

	def filtered_speakSelectionChange(self, oldInfo, newInfo, *args, **kwargs):
		"""Speak only game text in main window."""
		try:
			if self.isMainWindow():
				text = newInfo.text
				if text:
					speech.speakText(text)
				return
		except Exception:
			log.exception("Error in selectionChange")

		return _original_speakSelectionChange(oldInfo, newInfo, *args, **kwargs)

	def event_gainFocus(self, obj, nextHandler):
		"""Bind arrow keys to be ignored, not treated as text navigation keys."""
		try:
			if self.isMainWindow():
				if not self._gesturesBound:
					self.bindGestures(
						{
							"kb:upArrow": "ignoreKey",
							"kb:downArrow": "ignoreKey",
							"kb:leftArrow": "ignoreKey",
							"kb:rightArrow": "ignoreKey",
						}
					)
					self._gesturesBound = True
			else:
				if self._gesturesBound:
					self.clearGestureBindings()
					self._gesturesBound = False
		except Exception:
			log.exception("Error in focus handling")

		nextHandler()

	def script_ignoreKey(self, gesture):
		"""Pass arrow keys directly to the game (NVDA+F2 behavior)."""
		try:
			keyboardHandler.passNextKeyThrough = True
			gesture.send()
			keyboardHandler.passNextKeyThrough = False
		except Exception:
			log.exception("Error in ignoreKey script")

	def terminate(self):
		"""Restore original speech hook."""
		speech.speakSelectionChange = _original_speakSelectionChange
