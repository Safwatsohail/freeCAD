# Basic1 workbench module initialization.
# This file is executed when FreeCAD is started (in console mode and before the GUI loads).
import FreeCAD

if FreeCAD.GuiUp:
    FreeCAD.Console.PrintMessage("Basic1 workbench module loaded\n")