import subprocess

#####run a application as a sub process
##subprocess.run("notepad")

###use shell=True for shell commands
##subprocess.run("start chrome youtube.com", shell=True)

###run subprocess
##x = subprocess.run("python pyScript.py" , stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
##print(x.stdout.decode())



###run
##x = subprocess.run('python pyScript.py "hello from argz"' , stdout=subprocess.PIPE, shell=True)
##print("after run")
##print(x)
##print(x.stdout.decode())

##x = subprocess.run('python pyScript.py "hello from argz"', stdout=subprocess.PIPE, check=True, shell=True).stdout.decode()
##print(x)


#####Popen
##x = subprocess.Popen('python pyScript.py "hello from argz"' , stdout=subprocess.PIPE, shell=True)
##print("after run")
#####Popen obj
##print(x)
#####wait for process compleated
##x.wait()
#####read and decode stdout
##print(x.stdout.read().decode())
