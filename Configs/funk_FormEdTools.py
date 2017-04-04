#python

# =============================================================================
# Script: v0.01 (c:2017-30-25 m:2017-30-25)
# Author: funk
# 
# Tools which make the form editor easier to use
# =============================================================================

import lx
from PySide import QtGui

args = lx.args()
clipboard = QtGui.QApplication.clipboard()

if args[0] == 'copy':
    currentCommand = lx.eval('select.attr ?')
    clipboard.setText(currentCommand)

elif args[0] == 'paste':
    currentGroup = lx.eval('select.attr ?')
    clipboardText = clipboard.text()

    lx.eval('select.attr {%s} set' % clipboardText)
    lx.eval('attr.duplicate')
    lx.eval('attr.parent {%s}' % currentGroup)

elif args[0] == 'pasteFormReference':
    clipboardText = clipboard.text()

    if not "/" in clipboardText:
        lx.eval('attr.addFormRef')
        lx.eval('attr.controlFormRef {%s}' % clipboardText)

elif args[0] == 'pasteFormTail':
    clipboardText = clipboard.text()

    if not "/" in clipboardText:
        currentGroup = lx.eval('select.attr ?')
        lx.eval('attr.catCreate {%s} {%s} tail 127' % (clipboardText, currentGroup) )

elif args[0] == 'pasteFormHead':
    clipboardText = clipboard.text()

    if not "/" in clipboardText:
        currentGroup = lx.eval('select.attr ?')
        lx.eval('attr.catCreate {%s} {%s} head 127' % (clipboardText, currentGroup) )

