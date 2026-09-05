import FreeCAD
import FreeCADGui


class Basic1WorkBench(FreeCADGui.Workbench):
    "Basic1 workbench object"
    Icon = """
    /* XPM */
    static char * basic1_xpm[] = {
    "16 16 5 1",
    "     c None",
    ".    c #FFFFFF",
    "+    c #000000",
    "@    c #7F4F00",
    "#    c #FFBF00",
    "................",
    "...++++++++++++.",
    "..+@#########++.",
    ".+@#########+@+.",
    ".+++++++++++@#+.",
    ".+#########+##+.",
    ".+###++####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+###+++###+#@+.",
    ".+#########+@+..",
    ".++++++++++++...",
    "................"};
    """

    MenuText = "Basic1"
    ToolTip = "Basic1 workbench"

    def Initialize(self):
        "this function is executed when FreeCAD starts and initializes the workbench"
        from PySide import QtCore
        import Basic1Gui
        cmdlist = ["Basic1_Box"]
        self.appendToolbar(str(QtCore.QT_TRANSLATE_NOOP("Basic1", "Basic1 Tools")), cmdlist)

        self.appendMenu(str(QtCore.QT_TRANSLATE_NOOP("Basic1", "Basic1")), cmdlist)
        FreeCAD.Console.Log("Initializing Basic1 workbench... done\n")

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(Basic1WorkBench())