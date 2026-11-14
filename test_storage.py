from storage import load, save
from task import Task
import pytest

def test_load_save(tmp_path):
    p = tmp_path / "demo.json"
    t = Task("11", "2026-11-12")
    f = Task("22", "2026-11-14")
    tf = [t, f]
    save(p, tf)
    assert len(load(p)) == 2
    assert load(p)[0].content == "11"
    assert load(p)[1].content == "22"

def test_load_notfound(tmp_path):
    assert load(tmp_path / "notfound.json") == []

def test_load_notjson(tmp_path):
    p = tmp_path / "demo.txt"
    with open(p, "w", encoding="utf-8") as f:
        f.write("不是json")
    with pytest.raises(SystemExit):
        load(p)


