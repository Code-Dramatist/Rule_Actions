import os

# 文件夹列表
file_paths = ["Direct_Rule", "Proxy_Rule", "Reject_Rule"]


def merge_files(path):
    """
    将文件夹中的所有文件内容合并到一个文件中
    :param path: 文件夹路径
    :return: 合并后的文件路径
    """
    merged_file_path = f"{path}/{os.path.basename(path)}_merged.rule"
    with open(merged_file_path, 'w', encoding='utf8') as out_f:
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf8') as in_f:
                    lines = [line.strip() for line in in_f.readlines() if not line.startswith("#")]
                    out_f.write('\n'.join(lines) + '\n')
    return merged_file_path


def deduplicate_file(input_file, output_file):
    """
    针对小文件去重
    :param input_file: 输入文件
    :param output_file: 去重后输出文件
    :return:
    """
    with open(input_file, 'r', encoding='utf8') as in_f, open(output_file, 'w', encoding='utf8') as out_f:
        data = set(line.strip() for line in in_f.readlines())
        out_f.writelines(line + '\n' for line in sorted(data) if line.strip())

if __name__ == '__main__':
    for path in file_paths:
        # 创建文件夹，如果文件夹不存在
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"创建目录 {path} 成功")

        # 合并文件
        merged_file_path = merge_files(path)

        # 去重
        deduplicate_file(merged_file_path, f"{path}/{os.path.basename(path)}.rule")