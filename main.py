import sys
from storage import load, save
from datetime import date, datetime
from task import Task
from pathlib import Path

today = date.today().isoformat()

def add(path):
    if len(sys.argv) == 4:
        try:
            d = datetime.strptime(sys.argv[3], "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("日期格式错误")
            return
        else:
            datas = load(path)
            datas.append(Task(sys.argv[2], d))
            save(path, datas)
            print("已添加")
    elif len(sys.argv) < 4:
        print("缺少参数")
    else:
        print("命令不合法")
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

def done(path):
    if len(sys.argv) > 3:
        print("命令不合法")
    elif len(sys.argv) < 3:
        print("缺少参数")
    else:
        try:
            number = int(sys.argv[2])
        except ValueError:
            print("序号得是数字")
        else:
            datas = load(path)
            if number > len(datas) or number < 1:
                print("没有这条")
            else:
                data = datas[number - 1]
                data.mark_done()
                save(path, datas)
                print("已确认")
    return

def delete(path):
    if len(sys.argv) > 3:
        print("命令不合法")
    elif len(sys.argv) < 3:
        print("缺少参数")
    else:
        try:
            number = int(sys.argv[2])
        except ValueError:
            print("序号得是数字")
        else:
            datas = load(path)
            if number > len(datas) or number < 1:
                print("没有这条")
            else:
                del datas[number - 1]
                save(path, datas)
                print("已删除")
    return

def edit(path):
    if len(sys.argv) > 4:
        print("命令不合法")
    elif len(sys.argv) < 4:
        print("缺少参数")
    else:
        try:
            number = int(sys.argv[2])
        except ValueError:
            print("序号得是数字")
        else:
            datas = load(path)
            if number > len(datas) or number < 1:
                print("没有这条")
            else:
                data = datas[number - 1]
                data.content = sys.argv[3]
                save(path, datas)
                print("已修改")
    return

def main():
    x = sys.argv
    if len(x) < 2:
        print("未输入命令")
    else:
        if x[1] == "add":
            add(Path(__file__).resolve().parent/ "reminders.json")
        elif x[1] == "show":
            show(Path(__file__).resolve().parent/ "reminders.json")
        elif x[1] == "done":
            done(Path(__file__).resolve().parent/ "reminders.json")
        elif x[1] == "delete":
            delete(Path(__file__).resolve().parent/ "reminders.json")
        elif x[1] == "edit":
            edit(Path(__file__).resolve().parent/ "reminders.json")
        else:
            print("命令不合法")

if __name__ == "__main__":
    main()