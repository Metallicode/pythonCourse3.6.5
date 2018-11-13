import os

##print(dir(os))
##print(help(os))

###get current working directory path
print(os.getcwd())

###The name of the operating system dependent module imported.
print(os.name)

###string symbol path for "current/parent dir"
print(os.curdir)
print(os.pardir)

###list directory content
print(os.listdir(os.curdir))

###change location (directory)
os.chdir(os.listdir(os.curdir)[1])
print(os.getcwd())

###more arrtibutes
print(os.sep)
print(os.extsep)
print(os.defpath)
print(os.getlogin())
print(os.getpid())


###symbols of varius path strings in current os module..
##print(dir(os.path))

os.chdir(os.pardir)
print(os.getcwd())
path = os.getcwd()

print(os.path.dirname(path))     ###just dir name
print(os.path.exists(path))         ###bool if exists
print(os.path.getatime(path))    ###time of last access of path
print(os.path.getmtime(path))   ###time of last modification of path
print(os.path.getsize(path))       ###size of path
print(os.path.isabs(path))          ###if path is an absolute pathname. on Windows that it begins with a (back)slash.
###Backslash: \
###Forward slash: /
print(os.path.isfile(path))          ###is a file?
print(os.path.isdir(path))           ###is a dir?
print(os.path.join(path, "yolo")) ###add "yolo" to path
print(os.path.split(path))           ###split the path



###NORMAL FILE - Return the _io.TextIOWrapper 
##d = open("file", "w")
##print(d)


###Return the file descriptor for the newly opened file (use st_size for file size)
###O_RDONLY,O_WRONLY,O_RDWR, O_APPEND....
##d2 = os.open("file2", os.O_CREAT)
##print(d2)

###Get the status of the file descriptor d2. Return a stat_result object.
##print(os.fstat(d2))
##print(os.fstat(d2).st_size)




###test for access to path
### mode should be F_OK to test the existence of path, or it can be the inclusive
###OR of one or more of R_OK, W_OK, and X_OK to test permissions
##print(os.access("C:/Users/grysd/Desktop/pyos/not_real_folder", mode=os.F_OK))



###create dir
##os.mkdir("a_new_dir") 
##os.makedirs("a_dir/sub_dir/core_dir")

###Remove (delete) the file path. If path is a directory,
###OSError is raised. Use rmdir() to remove directories.
##
##d = open("file", "w")
##print(d)
##
##d.close()

#####rename
##os.rename("a_dir/sub_dir/core_dir", "a_dir/sub_dir/core_mega_folder")
##input()
#####remove file
##os.remove(d.name)

###delete one folder
##os.rmdir("a_dir/sub_dir/core_mega_folder")

###delete recorsive
##os.removedirs("a_dir/sub_dir/core_mega_folder")

###traverse  topdown=True
##for i in os.walk("python course"):
##    print(i)
##










