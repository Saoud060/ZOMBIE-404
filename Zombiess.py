import os
import platform

os.system('git pull')

# Display a message indicating that the tool is working
#print("Wait, working on the tool...")

adina = platform.architecture()[0]
if adina == "32bit":
    exit("Coming soon for 32-bit architecture")
elif adina == "64bit":
    __import__("BS")
