# Corrupted UnityPackage Extractor

This is a modified version of gered's UnityPackage Extractor (https://github.com/gered/extractunitypackage) that can handle somewhat broken .unitypackage files.

## Steps:

The steps are for Windows, if you are a Linux/MacOS user I assume that you know how to use the terminal and run python scripts (though the steps are somewhat similar).

1. You need to unzip the .unitypackage file by yourself. I recommend WinRar. If it fails with WinRar the file is completely corrupted.

2. Create a folder named "extracted" and paste the contents of the file inside of the unitypackage (again extract it with WinRar). The content of /extracted should be these randomly named folders.

3. Move the brokenunityfix.py in the same folder as the /extracted folder

4. (Windows only) Press and hold the Shift-Key and right-click in the folder where "brokenunityfix.py" and the "extracted" folder are located and you should have an additional option in the menu to open command window or something like that.

5. Run `python brokenunityfix.py` and wait for it to complete.

6. You should have the extracted files in a new folder called "output" and the list of files that are corrupted in "missingfiles.txt"


## Sidenote

I've removed the original extractor script, you can find it at the original git: https://github.com/gered/extractunitypackage

I am in no way associated with the original script, I just did some modifications so that it can extract corrupted files.

## Disclaimer

I have no great experience with Python. This script is very general and can cause issues. Do not blame me if something goes wrong. I have tested it and it worked for me, but it might not for you. Please do not run this as administrator.
I'm sorry for any kind of illness you may encounter while browsing the source code.
