import subprocess

with open("output.txt","wb") as f:
    subprocess.check_call(["python","Python_practice.py"],stdout=f)

with open("kk.txt","wb") as f:
    subprocess.check_call(["python","Python_practice.py"],stdout=f)
