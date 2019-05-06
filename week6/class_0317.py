# _*_ coding:utf_8 _*_
# @Time     : 2019/3/17 23:13
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0317.py

from configparser import RawConfigParser


class lernConfig:
    def __init__(self, conf_filePath, encoding):
        self.cf = RawConfigParser()
        self.cf.read(conf_filePath, encoding)  # 读取配置文件

    def get_intValue(self, section, option):
        return self.cf.getint(section, option)

    def get_boolValue(self, section, option):
        return self.cf.getboolean(section, option)

    def get_strValue(self, section, option):
        return self.cf.get(section, option)

    def get_floatValue(self, section, option):
        return self.cf.getfloat(section, option)

    def get_section(self):
        return self.cf.sections()

    def get_option(self, section):
        return self.cf.options(section)


if __name__ == '__main__':
    lc = lernConfig("demo.cfg", "utf_8")
    class_port = lc.get_intValue("class", "class_port")
    print(class_port)

    excel_res = lc.get_boolValue("excel", "res")
    print(excel_res)

    person_name = lc.get_strValue("person_info", "name")
    print(person_name)

    class_pwd = lc.get_floatValue("class", "class_password")
    print(class_pwd)

    sec = lc.get_section()
    print(sec)


