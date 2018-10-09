import os

import yaml


class ReadYaml():
    def __init__(self, filename):
        self.filenamepath = os.getcwd() + os.sep + "Data" + os.sep + filename

    def read_yaml(self):
        with open(self.filenamepath, "r", encoding="utf-8")as f:
            return yaml.load(f)


if __name__ == '__main__':
    datas = ReadYaml("login.yaml").read_yaml()
    print(datas)
    arrs = []
    for data in datas.values():
        print(data)
        arrs.append((data.get("username"), data.get("password"), data.get("expext"), data.get("toast_except")))

