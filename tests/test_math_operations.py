import pytest
from picguard import add

def test_add():
    # 测试正常的加法
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_edge_cases():
    # 测试边界条件
    assert add(1e6, 1e6) == 2e6
    assert add(-1e6, -1e6) == -2e6
