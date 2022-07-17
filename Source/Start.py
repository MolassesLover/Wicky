#region Modules

import os
from os.path import exists
import subprocess
import sys

#endregion

#region Variables

rcPath = f"{os.path.expanduser('~')}/.wickyrc"

#endregion

# Checks if the ~/.wickyrc exists.
def Check_RunCom():
    if os.path.exists(rcPath):
        rcProcess = subprocess.Popen([rcPath], stdin=subprocess.PIPE)
        rcProcess.communicate()
