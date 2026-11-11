class Task:

    def __init__(self, content, date, done=False):
        if not content:
            raise ValueError("待办内容不能为空")
        self.content = content
        self.date = date
        self._done = done

    def mark_done(self):
        self._done = True

    @property
    def done(self):
        return self._done

    def __str__(self):
        if self._done:
            return f"内容{self.content} 日期{self.date} 已完成"
        else:
            return f"内容{self.content} 日期{self.date} 未完成"
