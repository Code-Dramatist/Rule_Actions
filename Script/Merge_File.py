import os
File_Path = ["Direct_Rule","Proxy_Rule","Reject_Rule"]

def file_remove_same(input_file, output_file):
    """
        针对小文件去重
    :param input_file: 输入文件
    :param out_file: 去重后出文件
    :return:
    """
    with open(input_file, 'r', encoding='utf8') as f, open(output_file, 'a', encoding='utf8') as ff:
        data = [item.strip() for item in f.readlines()]  # 针对最后一行没有换行符，与其他它行重复的情况
        new_data = list(set(data))
        ff.writelines([item + '\n' for item in new_data if item])  # 针对去除文件中有多行空行的情况


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
        f_merge = open("./"+Path+"/"+Path+"_pre.rule","a+")
        f_merge.write(f)
        file_remove_same("./"+Path+"/"+Path+"_pre.rule","./"+Path+"/"+Path+".rule")
    f_merge.close()    


