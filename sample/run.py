import subprocess

# Start the first client in the foreground
subprocess.Popen(["python3", "client.py"])

# Start the other 10 clients in the background with their input redirected from a file
for i in range(1, 11):
    subprocess.Popen(["python3", "client.py"], stdin=open("input{}.txt".format(i), "r"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
