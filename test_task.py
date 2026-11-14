from task import Task
import pytest



def test_1_task():    
    t = Task("买菜", "2026-11-12")
    assert t.content == "买菜"
    assert t.date == "2026-11-12"
    assert t.done is False

def test_2_task():
    t = Task("买菜", "2026-11-12")
    t.mark_done()
    assert t.done is True

def test_3_task():
    t = Task("买菜", "2026-11-12")
    assert str(t) == "内容买菜 日期2026-11-12 未完成"
    t.mark_done()
    assert str(t) == "内容买菜 日期2026-11-12 已完成"

def test_empty_content():
    with pytest.raises(ValueError):
        Task("", "2026-11-12")
    