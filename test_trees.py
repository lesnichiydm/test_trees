import pytest
from main import TreeStore


@pytest.fixture
def ts_object():
    ts = TreeStore([
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ])
    return ts


def test_get_all(ts_object):
    assert ts_object.get_all() == ts_object._ts_list


def test_get_item(ts_object):
    assert ts_object.get_item(7) == {"id":7,"parent":4,"type":None}


def test_get_children(ts_object):
    assert ts_object.get_children(4) == [
        {"id":7,"parent":4,"type":None},
        {"id":8,"parent":4,"type":None},
    ]
    assert ts_object.get_children(5) == []


def test_get_all_parents(ts_object):
    assert ts_object.get_all_parents(7) == [
        {"id":4,"parent":2,"type":"test"},
        {"id":2,"parent":1,"type":"test"},
        {"id":1,"parent":"root"},
    ]
