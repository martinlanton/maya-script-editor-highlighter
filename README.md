# maya_template_project
Template project for maya code, including unittest setup

## How to install pytest on Maya?

Pytest can be installed on maya following [this documentation](https://knowledge.autodesk.com/support/maya/downloads/caas/CloudHelp/cloudhelp/2022/ENU/Maya-Scripting/files/GUID-72A245EC-CDB4-46AB-BEE0-4BBBF9791627-htm.html).

###In short, on Windows, from an ***administrator*** command line :
```commandline
mayapy -m pip install <flags> <package>
```
###Which could translate to this :
```commandline
mayapy -m pip install --ignore-installed pytest
```
The ignore install flag is a nice thing to know when you want to ensure you get the latest version or when the package in question is already installed somewhere else.


###On both macOS and Linux, the following command can be used :
```commandline
sudo ./mayapy -m pip install <flags> <package>
```