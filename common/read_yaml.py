import yaml


def readyml(filePath):
    '''读取yaml文件'''
    f = open(filePath, "r", encoding="utf-8")
    y = f.read()
    data = yaml.load(y)
    print("读取yaml转字典:%s"%data)
    return data

if __name__ == '__main__':
    # read_yaml.py 和 yml文件在一个文件夹，可以直接读取到
    # read_yaml.py 和 yml文件 不在一个文件夹用绝对路径
    import os
    # 读取当前脚本的路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(os.path.dirname(cur_path), "case", 'data_demo.yml')
    print(yaml_path)

    a = readyml(yaml_path)
    print(a['test_add_param_demo'])