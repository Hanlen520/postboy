#!/bin/env/python
# coding=utf-8
import json
import re
import platform


def remove_annotation(f):
    body = f.read()  
    annos = re.findall(r'!\".*?//.*?\" | //.*? |\/\*.*?\*\/', body, re.S)

    for anno in annos:
        body = body.replace(anno, '')
    return body

def load_json(path):
    """加载json文件,:param path: json文件路径 :return 字典格式"""
    if (platform.python_version()) < '3':
        import codecs
        f = codecs.open(path, encoding='utf-8')
        try:
            return  json.loads(remove_annotation(f))
        except ValueError:
            print("%s --- json decode error" % path)
            return None
    else:
        f = open(path, encoding='utf-8')
        try:
            return  json.loads(remove_annotation(f))
        except json.decoder.JSONDecodeError:
            print("%s --- json decode error" % path)
            return None

    f.close()


if __name__ == '__main__':
    print(json.dumps(load_json('test_remove_anno.txt'), ensure_ascii=False, indent=2))