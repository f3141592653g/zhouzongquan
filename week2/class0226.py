# _*_ coding: utf_8 _*_

# 1、请编程实现字符串的转换：将”sdSdsfdAdsdsdfsfdsdASDSDFDSFa”字符串大写变小写，小写变大写。并且将字符串变为镜像字符串。 例如：字符串里面的’A’变为’Z’,’b’变为’y’ ，镜像的意思就是照镜子，对比了解下。

a="sdSdsfdAdsdsdfsfdsdASDSDFDSFa"
res=a.swapcase()

print("字符串大小写转换后的效果为："+res)
intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
outab = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
str_trantab = str.maketrans(intab,outab)

print("镜像转换之后："+res.translate(str_trantab))

# 2：搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。 比如这个字符串：
# 我的是名字是lemon,今年5岁。
#
# 语法分析后得到结果如下：
#
# 数字：5
#
# 中文：我的名字是、今年、岁
#
# 拼音：lemon
#
# 符号：，。 请编写程序实现该词法分析功能。

a="我的是名字是lemon,今年5岁。"
zm=""
yw=""
zw=""
for item in a:
    if item.isdigit():
        zm=zm+item
    if item.encode('utf-8').isalpha():
        yw=yw+item
    if item.isalpha():
        zw=zw+item
print("字符串:" + yw)
print("数字:" + zm)
print("数字:" + zw)


