# Basic1 Workbench for FreeCAD

A simple FreeCAD workbench that creates a 10x10x10 box.

## Installation (via Addon Manager)

1. Open **FreeCAD**
2. Go to **Tools → Addon Manager**
3. Search for **Basic1** (or click **"Install from GitHub"** / **"Configure..."** and add the repository: `https://github.com/Safwatsohail/freeCAD`)
   - Note: Because this is not yet listed in the official community repository index, use the **Addon Manager → ⚙️ (settings) → Custom repositories** option and add:
     - Name: `Basic1`
     - URL: `https://github.com/Safwatsohail/freeCAD`
4. Click **Install/Update**
5. **Restart FreeCAD** completely

## Manual installation (alternative)

On macOS, copy this folder to:

```
~/Library/Application Support/FreeCAD/Mod/Basic1/
```

On Windows:

```
C:\Users\<YourName>\AppData\Roaming\FreeCAD\Mod\Basic1\
```

On Linux:

```
~/.local/share/FreeCAD/Mod/Basic1/
```

Make sure the folder contains `init.py`, `InitGui.py`, `Basic1Gui.py`, `Basic1Icon.xpm`, and `package.xml`.

## Usage

1. **Restart FreeCAD**
2. In the **workbench dropdown** (top center of the window), select **Basic1**
3. Create a new document: **File → New** (or **Cmd/Ctrl + N**)
4. In the **Basic1** menu (top) or the **Basic1 Tools** toolbar, click **Box**
5. A 10x10x10 box named **"Box"** appears in the Tree view and 3D view

## Files

| File | Purpose |
|------|---------|
| `init.py` | Module initialization, runs at FreeCAD startup |
| `InitGui.py` | Registers the **Basic1** workbench |
| `Basic1Gui.py` | Defines the **Box** command (`Basic1_Box`) |
| `Basic1Icon.xpm` | Workbench icon |
| `package.xml` | Addon Manager metadata (format 2) |

## License

MIT