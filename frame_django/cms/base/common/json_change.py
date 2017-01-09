# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:08
# @Last Modified time: 2017-01-04 16:14:18
import json
#################################
# python列表、字典与json字符串互转
################################
'''
json_str = json.dumps(python_list)
python_list = json.loads(json_str)


sort_keys————以键排序；
indent————缩进；
json_str = json.dumps(python_dict[, sort_keys=True[, indent=4]])
python_dict = json.loads(json_str)
'''


# 接收一个QuerySet/RawQuerySet对象 -> [dict, dict, ...]
def to_list(objs):
    obj_list = []
    for o in objs:
        obj_list.append(o.toDict())
    return obj_list


# 接收一个QuerySet/RawQuerySet对象 -> [dict, dict, ...] -> json字符串
def to_json_list_str(objs):
    obj_list = []
    for o in objs:
        obj_list.append(o.toDict())
    json_list_str = json.dumps(obj_list, ensure_ascii=False)
    return json_list_str


# 接收一个ValuesQuerySet对象 -> [dict, dict, ...] -> json字符串
def values_to_json_list_str(objs):
    obj_list = list(objs)
    json_list_str = json.dumps(obj_list, ensure_ascii=False)
    return json_list_str


# 接收一个QuerySet/RawQuerySet对象 -> dict -> json字符串
def to_json_str(obj):
    json_str = json.dumps(obj[0].toDict())
    return json_str


"""
simplejson模块，类似于内建json模块
simplejson.loads(request.raw_post_data)
json.loads(request.body)
"""
