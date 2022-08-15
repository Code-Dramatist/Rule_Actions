import os
File_Path = ["Direct_Rule","Proxy_Rule","Reject_Rule"]

for Path in File_Path:
    file_name = os.listdir("./"+Path)
    os.remove("./"+Path+"/"+Path+".rule")
    for file in file_name:
        f = open("./"+Path+"/"+file).read()
        f_merge = open("./"+Path+"/"+Path+".rule","a+")
        f_merge.write(f)
    f_merge.close()    
