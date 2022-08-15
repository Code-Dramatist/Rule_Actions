import os
File_Path = ["Direct_Rule","Proxy_Rule","Reject_Rule"]

for Path in File_Path:
    if not os.path.exists(Path):
        os.system(r"touch {}".format(Path))
    file_name = os.listdir("./"+Path)
    if not len(file_name) == 0:
        os.remove("./"+Path+"/"+Path+".rule")
    for file in file_name:
        f = open("./"+Path+"/"+file).read()
        f_merge = open("./"+Path+"/"+Path+".rule","a+")
        f_merge.write(f)
    f_merge.close()    
