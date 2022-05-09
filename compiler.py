import os


a = input("num")
os.system(f"python -m PyQt5.uic.pyuic -x ./PyQt5/{a}.ui -o ./PyQt5/output.py")