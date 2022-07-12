#region Modules

import argparse
import os
import subprocess 
from sys import platform
import warnings

#endregion

#region Arguments

argumentParser = argparse.ArgumentParser(description="The arguments for the Python build script.")
argumentParser.add_argument('-l', '--launch', dest = 'launchEditor', default = "False", help = "Whether to run the editor or not once built.")
arguments = argumentParser.parse_args()

#endregion

#region Functions

def Build(): 
    # GNU/Linux
    if platform == "linux" or platform == "linux2":
        subprocess.run(['sh', 'Build.sh'], shell=False)
    
    # macOS & Darwin
    elif platform == "darwin":
        subprocess.run(['sh', 'Build.sh'], shell=False)

    # Windows
    elif platform == "win32":
        warnings.warn("Script not designed for Windows!")
        subprocess.run(['sh', 'Build.sh'], shell=False)


def Launch():
    print("Running the Wicked Engine editor!")
    os.system('cd ../../Build/ && ./Editor')

#endregion

#region Launch

if __name__ == "__main__":
    Build()

    if arguments.launchEditor == "True":
        Launch()

#endregion