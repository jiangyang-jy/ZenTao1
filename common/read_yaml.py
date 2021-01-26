import yaml


def get_yaml(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as fp:
        f = fp.read()
        print(type(f))
    d = yaml.load(f)
    print("读取到yaml文件数据")
    print(d)
    return d


if __name__ == '__main__':
    yaml_file = r"E:\ZenTao\case\test_data.yml"
    get_yaml(yaml_file)
