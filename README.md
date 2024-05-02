This package lets you easily see errors and warnings in the Maya console.  
![image](/documentation/images/script_editor_highlighting_example.png)  
it's quite simple, e.g. the line `// https://www.autodesk.com/maya-arnold-not-available-error` will be colored as an error  

### install
You can use either of the following installation methods

#### Plug-in version
* Edit your environment variables to add the `plug-ins` folder to your list of plugin locations. This can be done by adding the `plug-ins` folder location (for example `C:\Users\JohnDoe\Documents\maya-script-editor-highlighter\src\plug-ins`, or wherever you decided to put it) to the `MAYA_PLUG_IN_PATH` environment variable.

#### userSetup.py version
* Edit your environment variables to add the `scripts` folder to your list of scripts locations. This can be done by adding the `scripts` folder location (for example `C:\Users\JohnDoe\Documents\maya-script-editor-highlighter\src\scripts`, or wherever you decided to put it) to the `PYTHONPATH` environment variable.

### Usage
1. Enable the highlight plugin (if you chose the plug-in version)
2. Open script editor.
3. It won't work until you get focus on the script editor, this means you'll need to activate focus on a different part of the GUI, then back on the script editor. To do this, simply click on the viewport then back on the script editor.

### Thanks
Thanks to Vincent Touache and Remi Deletrain for the original idea for this package and for the original version on the code.
Thanks to Hannes Delbeke for his contribution, as well as for more information on other highlighting methods : https://hannesdelbeke.github.io/wiki/tech%20art/maya/Maya%20script%20editor%20syntax%20highlight/ 
