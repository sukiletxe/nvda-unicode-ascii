# unicodeAscii (Convert Unicode strings to ASCII, thanks to Unidecode).
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
# The structure of this file and the getSelection function are from FEN Reader by Javi Dominguez.
# Copyright 2021 by Sukil Etxenike <sukiletxe@yahoo.es>

import os
import sys

import globalPluginHandler
import api
import ui
import textInfos
from scriptHandler import script, getLastScriptRepeatCount
from speechDictHandler import dictionaries, SpeechDictEntry
dirAddon=os.path.dirname(__file__)
sys.path.append(os.path.abspath(dirAddon))
from unidecode import unidecode
import addonHandler
sys.path.remove(dirAddon)
addonHandler.initTranslation()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = "Unicode ASCII"
    def getSelection(self):
        obj=api.getFocusObject()
        treeInterceptor=obj.treeInterceptor
        if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
            obj=treeInterceptor
        try:
            info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
        except :
            info=None
        if not info or info.isCollapsed:
            return(None)
        else:
            return(info.text)

    def add_to_dict(self, pattern, replacement):
        dictionaries['default'].append(SpeechDictEntry(pattern, replacement, ''))
        dictionaries['default'].save()

    def decode(self, text):
        if text is not None:
            decoded = unidecode(text, errors = 'preserve')
            return decoded
        else:
            return None
    
    def decode_selection_or_clipboard(self):
        try:
            text = self.getSelection() or api.getClipData() # The joys of short circuiting.
            decoded = self.decode(text)
            return text, decoded            
        except:
            return None, None

    @script(
        gesture = "kb:control+NVDA+n",
        # Translators: A message  in input help or in the input gestures dialog.
        description = _("Decodes the selected text or clipboard (in that order of search) to ASCII. If pressed twice it copies the result to the clipboard")
    )
    def script_decode_selection_or_clipboard(self, gesture):
        text, decoded = self.decode_selection_or_clipboard()
        if decoded is not None:
            if getLastScriptRepeatCount() == 0:
                ui.message(decoded)
            else:
                api.copyToClip(decoded, notify = True)    
        else:
            ui.message(
                # Translators: An error message.
                _("No text in clipboard nor in selection")
            )

    @script(
        gesture = "kb:control+shift+NVDA+n",
        # Translators: A message  in input help or in the input gestures dialog.
        description = _("Decodes the selection or the clipboard (in that order of search), and adds them to the default dictionary")
        )
    def script_decode_and_add_to_dict(self, gesture):
        text, decoded = self.decode_selection_or_clipboard()
        if decoded is not None:
            self.add_to_dict(text, decoded)
            ui.message(
                # Translators: A message indicating the success of the operation of decoding a string and adding it to the default dictionary.
                _("Decoded and added to default dictionary")
            )
        else:
            ui.message(
                # Translators: An error message.
                _("No text in clipboard nor in selection")
            )
            