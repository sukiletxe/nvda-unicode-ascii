# unicodeAscii (Convert Unicode strings to ASCII, thanks to Unidecode).
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
# The structure of this file and the getSelection function are from FEN Reader by Javi Dominguez.
# Copyright 2021 by Sukil Etxenike <sukiletxe@yahoo.es>

import globalPluginHandler
import api
import ui
import textInfos
from scriptHandler import script, getLastScriptRepeatCount

from .unidecode import unidecode
import addonHandler
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
    
    def decode(self, text):
        if text is not None:
            decoded = unidecode(text, errors = 'preserve')
            return decoded
        else:
            return None
    
    @script(gesture = "kb:control+NVDA+n", description = _("Decodes the selected text to ASCII. If pressed twice it copies the result to the clipboard"))
    def script_decode_selection(self, gesture):
        selected = self.getSelection()
        decoded = self.decode(selected)
        if decoded is not None:
            if getLastScriptRepeatCount() == 0:
                ui.message(decoded)
            else:
                api.copyToClip(decoded, notify = True)
        else:
            ui.message (_("No selection"))
    
    @script(gesture = "kb:control+shift+NVDA+n", description = _("Decodes the text of the clipboard. If pressed twice, it copies the result."))
    def script_decode_clipboard(self, gesture):
        clipboard = api.getClipData()
        decoded = self.decode(clipboard)
        if decoded is not None:
            if getLastScriptRepeatCount() == 0:
                ui.message(decoded)
            else:
                api.copyToClip(decoded, notify = True)
        else:
            ui.message(_("No text in clipboard"))
