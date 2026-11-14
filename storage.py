import json
from task import Task
import sys
import logging

def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        datas = json.loads(text) if text.split() else []
    except FileNotFoundError:
        with open(path, "w"):
            logging.info("文件已新建")
            return []
    except json.JSONDecodeError:
        logging.error("文件损坏")
        sys.exit()
        return 
    else: 
        if isinstance(datas, list):
            if all(isinstance(x, dict) for x in datas):
                data = []
                for d in datas:
                    d = Task(d["content"], d["date"], d["done"])
                    data.append(d)
                datas = sorted(data, key= lambda w : w.date, reverse=False)
                return datas
            else:
                logging.error("文件内容错误")
                sys.exit()
        else:
            logging.error("文件内容错误")
            sys.exit()

def save(path, datas):
    data = [{"content": t.content, "date": t.date, "done": t.done} for t in datas]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    return