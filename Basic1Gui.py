import FreeCAD
import FreeCADGui

_IconXpm = """
/* XPM */
static char * basic1_xpm[] = {
"16 16 4 1",
"     c None",
".    c #FFFFFF",
"+    c #0B5FFF",
"#    c #111827",
"................",
"....########....",
"...##++++++##...",
"..##++....++##..",
"..##++..........",
"...##++.........",
"....##++++......",
"......##++++....",
"........##+++...",
"..........++##..",
"..........++##..",
"..##++....++##..",
"...##++++++##...",
"....########....",
"................",
"................"};
"""


def MakeBox():
    """Create a 10x10x10 Part Box in the active document."""
    doc = FreeCAD.ActiveDocument
    if doc is None:
        FreeCAD.Console.PrintError(
            "Basic1: No active document. Please create a new document first (File > New).\n"
        )
        return
    box = doc.addObject("Part::Box", "Box")
    box.Length = 10
    box.Width = 10
    box.Height = 10
    doc.recompute()
    FreeCAD.Console.PrintMessage("Basic1: Box created.\n")


class _MakeBoxCmd:
    """Command to create a box"""

    def Activated(self):
        MakeBox()

    def GetResources(self):
        return {
            'MenuText': 'Box',
            'ToolTip': 'Create a 10x10x10 box',
            'Pixmap': _IconXpm,
        }

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None


FreeCADGui.addCommand('Basic1_Box', _MakeBoxCmd())
