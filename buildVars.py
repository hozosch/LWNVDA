from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries
from site_scons.site_tools.NVDATool.utils import _


addon_info = AddonInfo(
	addon_name="LWNVDA",

	addon_summary=_("Lone Wolf support App Module"),

	addon_description=_("""Makes Lone Wolf, the submarine simulator by GMA Games, more usable with NVDA.
The game should be configured to use the "no screen reader" (or unsupported) option and have text highlighting enabled.
This add-on suppresses redundant announcements, providing a smoother experience similar to SAPI5 or the game's direct support for JAWS and Window-Eyes.
List and dialog boxes in the game are already accessible without this add-on, so it makes only minimal adjustments."""),

	addon_version="1.0.0",

	addon_changelog=_("""initial release"""),

	addon_author="Karl Eick <hozosch@web.de>",

	addon_url="https://github.com/hozosch/LWNVDA",

	addon_sourceURL="https://github.com/hozosch/LWNVDA",

	addon_docFileName="readme.html",

	addon_minimumNVDAVersion="2019.3",

	addon_lastTestedNVDAVersion="2026.1",

	addon_updateChannel=None,

	addon_license="GPL 2 or later",

	addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)


pythonSources: list[str] = [
	"addon/appModules/*.py",
]

i18nSources: list[str] = pythonSources + ["buildVars.py"]

excludedFiles: list[str] = []

markdownExtensions: list[str] = ["markdown.extensions.fenced_code"]

brailleTables: BrailleTables = {}

symbolDictionaries: SymbolDictionaries = {}

speechDictionaries: SpeechDictionaries = {}

baseLanguage: str = "en"
