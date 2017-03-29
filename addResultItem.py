# coding=utf8
# 将地址添加到结果栏

def addResultItem(Qt_Result, list):
    # 先清除所有结果
    Qt_Result.clear()
    # 循环
    i = 0
    length = len(list)

    if length != 0:
        while i < length:
            s = 'ID: ' + str(list[i]['id']) + ', ' + list[i]['title']
            Qt_Result.addItem(s)
            i += 1