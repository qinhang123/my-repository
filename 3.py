class FibonacciIterator:
    def __init__(self,limit):
        self.limit = limit
        self.b = 0
    def __iter__(self):
        if self.limit == 0:
            return iter([])
        if self.limit == 1:
            return iter([0])
        if self.limit == 2:
            return iter([0,1,1])
        result = [0,1,1]
        for num in range(3,self.limit):
            if result[num - 1] + result[num - 2] > self.limit:
               return iter(result)
            result.append(result[num - 1] + result[num - 2])

    def __next__(self):
        result = [0,1,1,2]
        a = self.b
        self.b += 1
        if self.limit == 0:
            return None
        if self.limit == 1:
            return 0
        if self.limit == 2:
            if result[a] > self.limit:
                raise StopIteration  
            return result[a]
        for num in range(3,self.limit):
            result.append(result[num - 1] + result[num - 2])
        if result[a] > self.limit:
            raise StopIteration   
        return result[a]
       
 
scores = [85, 92, 78, 65, 88, 92, 70, 60, 55, 92]
new_scores = list(dict.fromkeys(scores))
new_scores.sort(reverse=True)


def analyze_scores(scores):
    """
    处理学生成绩列表
    输入：[85, 92, 78, 65, 88, 92, 70, 60, 55, 92]
    要求：
    1. 计算平均分（保留2位小数）
    2. 找出所有最高分的学生索引
    3. 统计分数段：优秀(90-100)、良好(80-89)、及格(60-79)、不及格(0-59)
    4. 去除重复分数后降序返回
    """
    #求平均分
    average = sum(scores) / len(scores)
    #找最高分对应学生的索引
    #思路： 先把最高分找出来，然后和列表中的分数作对比，相同的就取出对应分数的索引放入新列表中
    max_score = max(scores)
    max_index = []
    for i , score in enumerate(scores):
        if max_score == score:
            max_index.append(i)
    #统计分数等级
    dict_grade = {}
    for score in scores:
        if score >= 90:
            dict_grade['优秀']  = dict_grade.get('优秀',0) + 1
        elif score >= 80:
            dict_grade['良好']  = dict_grade.get('良好',0) + 1
        elif score >= 60:
            dict_grade['及格']  = dict_grade.get('及格',0) + 1
        elif 0<= score < 60:
            dict_grade['不及格']  = dict_grade.get('不及格',0) + 1
        else:
            print("无效分数,不予统计")
    #出掉重复数字
    new_scores = list(dict.fromkeys(scores))
    #降序
    new_scores.sort(reverse=True)
    #以一个字典的数据类型输出比较合适

    return {
        '平均分' : f"{average:.2f}", #保留两位小数
        "分数最高学生对应的索引" : max_index,
        "分数等级" : dict_grade,
        "去重后降序列表" : new_scores
    }

print(analyze_scores([85, 92, 78, 65, 88, 92, 70, 60, 55, 92]))
inv1 = {"apple": 10, "banana": 5, "orange": 8}
inv2 = {"banana": 3, "grape": 7, "apple": 2}

def merge_inventory(inv1, inv2):
    """
    合并两个仓库库存
    inv1 = {"apple": 10, "banana": 5, "orange": 8}
    inv2 = {"banana": 3, "grape": 7, "apple": 2}
    返回合并后的字典，相同商品数量相加
    """
    combine_dict = {}
    for key , value in inv1.items():
        if key not in combine_dict and key not in inv2 :
            combine_dict[key] = value
        elif key not in combine_dict and key in inv2:
            combine_dict[key] = value + inv2[key]
    inv2.update(combine_dict)
    return inv2


li = '[2024-01-15 10:30:25]'

import transformers
import peft
import scipy

import sklearn
import gensim
import torch
import pandas
import numpy








