#!/usr/bin/python3

#region Modules

import argparse
import colorama
from colorama import Fore
import os
import shutil
import subprocess
import time

#endregion

#region Variables

dividerFile = open('Text/Divider.txt', 'r')
divider = dividerFile.read()
titleFile = open('Text/Title.txt', 'r')
title = titleFile.read()
versionFile = open('Text/Version.txt', 'r')
version = versionFile.read()

templatePath = r'../Templates/Default/'
templateDestination = f'{os.getcwd()}/Destination'

nameTarget = "_REPLACE_ME_"
nameReplacement = "Default"

#endregion

def Prompt():
    projectName = input("Project name: ")
    templateDestination = f'{os.getcwd()}/{projectName}'
    print(f"Copying files to destination:\n{templateDestination}")

    shutil.copytree(templatePath, templateDestination)

    nameReplacement = projectName

    with open(f'{templateDestination}/Source/main_SDL2.cpp', 'r') as file:
        main_SDL2_DATA = file.read()
        main_SDL2_DATA = main_SDL2_DATA.replace(nameTarget, nameReplacement)

    with open(f'{templateDestination}/Source/main_SDL2.cpp', 'w') as file:
        file.write(main_SDL2_DATA)

if __name__ == '__main__':
    print(f"{Fore.RED}{title}{Fore.WHITE}")
    print(f"{Fore.WHITE}{divider}{Fore.WHITE}")
    print(f"Wicky version: {Fore.YELLOW}{version}{Fore.WHITE}")
    
    # Dramatic effect~
    time.sleep(0.25)

    Prompt()