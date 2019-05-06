# _*_ coding: utf_8 _*_


# 有两行数据，存在txt文件里面：
#
# url:http://47.107.168.87:8080/futureloan/mvc/api/member/register@mobile:18688773467@pwd:123456
#
# url:http://47.107.168.87:8080/futureloan/mvc/api/member/recharge@mobile:18688773467@amount:1000
#
# 请利用上课所学知识，把txt里面的两行内容，写一个函数，返回如下格式的数据：
#
# [{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register','mobile':'18688773467','pwd':'123456'},
#
# {'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','mobile':'18688773467','amount':'1000'}]
#
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！！！！
#
# 多思考多讨论！

def date_txt(file):
    file_1=open(file)
    file_2=file_1.readlines()
    file_1.close()
    null_list=[]
    null_dict={}
    for item in file_2:
        file_3=item.strip().split("@")
        for item_2 in file_3:
            item_3=item_2.split(":",1)
            null_dict[item_3[0]]=item_3[1]
        null_list.append(null_dict)
    return null_list

if __name__ == '__main__':
    res=date_txt("date.txt")
    print(res)


#从字符串’abcdba‘中找出第一个不重复的字符，方法不限

# date = "abcda"
# count=0
# for item in range(len(date)):
#     for item_1 in range(len(date)-1):
#         if date[item]==date[item_1] :
#             print("{}重复".format(date[count]))
#         else:
#             break
#     count = item_1 + 1
# print("第一个不重复的是{}：".format(date[count]))
#


