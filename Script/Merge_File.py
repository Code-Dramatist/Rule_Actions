import os
File_Path = ["Direct_Rule","Proxy_Rule","Reject_Rule"]

for Path in File_Path:
    if not os.path.exists(Path):
        os.system(r"touch {}".format(Path))
        print("创建目录{}成功".format(Path))
    try:
        os.remove("./"+Path+"/"+Path+".rule")
        print("旧规则移除成功")
    except FileNotFoundError:
        print("无旧规则")
    file_name = os.listdir("./"+Path)
    for file in file_name:
        f = open("./"+Path+"/"+file).read()
        f_merge = open("./"+Path+"/"+Path+".rule","a+")
        f_merge.write(f)
    f_merge.close()    
