from HubBaseUnified.bin.HB.HubBase import *
from HubBaseUnified.bin.VB.VersionBacklog import *
from HubBaseUnified.bin.HBJE.JsPort import *
from HubBaseUnified.bin.HBUT.Main import *

print("HubBaseLauncher v0.0.1.0.0 (.py - 0.0.2.0.11; .js - 0.0.1.0.00)")
LaunchOptions = {1: "hb", 2: "jsport", 3: "vb", 4: "hbut"}
print(LaunchOptions)
LaunchOptionInput = int(input("What to launch?[1,2,3,4] -- "))
LaunchOptionInput = LaunchOptions[LaunchOptionInput]
if LaunchOptionInput == "hb":
    prList, modules = Setup_HubBase()
    User = Enter()
    Code(prList, User)
elif LaunchOptionInput == "jsport":
    print("HubBase-onJS PyPort 0.0.1.0.01 (default, May 18 2026, 18:50:26)")
    P1(10)
    P2()
    P3()
    print("Original programms:")
    OP1()
elif LaunchOptionInput == "vb":
    view_log()
elif LaunchOptionInput == "hbut":
    Showcase()