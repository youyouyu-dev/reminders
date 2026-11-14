import sys
from storage import load, save
from datetime import date, datetime
from task import Task
from pathlib import Path
import logging

logging.basicConfig(
    filename=Path(__file__).resolve().parent / "main.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    
)

today = date.today().isoformat()

def check(n):
    c = False
    if len(sys.argv) == n:
        c = True
        return c
    elif len(sys.argv) < n:
        print("缺少参数")
        logging.warning("缺少参数")
        return c
    else:
        print("命令不合法")
        logging.warning("命令不合法")
        return c

def add(path):
    if check(4):
        try:
            d = datetime.strptime(sys.argv[3], "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            logging.warning("日期格式错误")
            return
        else:
            datas = load(path)
            datas.append(Task(sys.argv[2], d))
            save(path, datas)
            logging.info(f"已添加 {sys.argv[2]}")
            return 
    else:
        pass
    return

def show(path):
    n = 0
    datas = load(path)
    if datas == []:
        print("文件为空")
    else:
        for data in datas:
            n = n + 1
            if data.date == today:
                print(f"{n}.{data} [今天]")
            else:
                print(f"{n}.{data}")
    return

def found(path):
    nf = True
    try:
        number = int(sys.argv[2])
    except ValueError:
        logging.warning("序号得是数字")
        print("序号得是数字")
        return nf
    else:
        datas = load(path)
        if number > len(datas) or number < 1:
            logging.warning("没有这条")
            print("没有这条")
            return nf
        else:
            d = {}
            d["datas"] = datas
            d["number"] = number
            return d


def done(path):
    if check(3):
        d = found(path)       
        if not isinstance(d, dict):
            pass
        else:
            datas = d["datas"]
            number = d["number"]
            data = datas[number - 1]
            data.mark_done()
            save(path, datas)
            logging.info(f"已确认第 {number} 条: {data.content}")
            print("已确认")
    else:
        pass
    return

def delete(path):
    if check(3):
        d = found(path)       
        if not isinstance(d, dict):
            pass
        else:
            datas = d["datas"]
            number = d["number"]
            data = datas[number - 1]        
            del datas[number - 1]
            save(path, datas)
            logging.info(f"已删除第 {number} 条: {data.content}")
    else:
        pass
    return

def edit(path):
    if check(4):
        d = found(path)       
        if not isinstance(d, dict):
            pass
        else:
            datas = d["datas"]
            number = d["number"]
            data = datas[number - 1]        
            data.content = sys.argv[3]
            save(path, datas)
            logging.info("已修改")
    else:
        pass
    return

def main():
    path = Path(__file__).resolve().parent/ "reminders.json"
    x = sys.argv
    if len(x) < 2:
        logging.warning("未输入命令")
    else:
        if x[1] == "add":
            add(path)
        elif x[1] == "show":
            show(path)
        elif x[1] == "done":
            done(path)
        elif x[1] == "delete":
            delete(path)
        elif x[1] == "edit":
            edit(path)
        else:
            logging.warning("命令不合法")

if __name__ == "__main__":
    main()