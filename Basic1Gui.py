from PySide import QtCore
import FreeCAD
import FreeCADGui


def MakeBox():
    doc = FreeCAD.ActiveDocument
    if doc is None:
        FreeCAD.Console.PrintError("Basic1: No active document. Please create one first.\n")
        return
    box = doc.addObject("Part::Box", "Box")
    box.Length = 10
    box.Width = 10
    box.Height = 10
    doc.recompute()


class _MakeBoxCmd:
    """Command to create a box"""

    def Activated(self):
        MakeBox()

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP("Basic1_Box", "Box")
        ToolTip = QtCore.QT_TRANSLATE_NOOP("Basic1_Box", "Create a box")
        return {
            'MenuText': MenuText,
            'ToolTip': ToolTip,
            # Use FreeCAD's built-in Part_Box icon (no external file needed)
            'Pixmap': 'Part_Box'
        }

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None


FreeCADGui.addCommand('Basic1_Box', _MakeBoxCmd())