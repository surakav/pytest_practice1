from fixture import StudentDB
import pytest
from pytest import mark
@pytest.fixture(scope='module')
def db():
    print('----------setup----------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('----------teardown----------------')
    db.close()
@pytest.mark.first
def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'
@pytest.mark.skip(reason='Dont need this data')
def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'