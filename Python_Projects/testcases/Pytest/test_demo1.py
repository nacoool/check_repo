import pytest
def test_m1():
    a=6
    b=6
    assert a == b, "test is failed"
    
def test_m2():
    a=6
    b=6
    assert a == b, "test is failed"
    
def test_m3():
    a=6
    b=6
    assert a == b, "test is failed"

@pytest.mark.skip(reason="Skipping this test temporarily")
def test_skip():
    assert False  # This test won’t run


@pytest.mark.skipif(5==5, reason="Feature not supported")
def test_skip_conditionally():
    assert False


@pytest.mark.parametrize("a, b, result", [(2, 3, 5), (1, 2, 3), (0, 5, 5)])
def test_add(a, b, result):
    assert a + b == result
    
@pytest.fixture
def sample_data(scope="session"):
    yield {"name": "pytest", "version": 7.0}

def test_fixture(sample_data):
    assert sample_data["name"] == "pytest"

@pytest.fixture(scope="class")
def db_connection():
    print("\n[SETUP] Connecting to DB")
    yield "DB Connection"
    print("\n[TEARDOWN] Closing DB Connection")

def test_query1(db_connection):
    print("/n SQL query1")
    assert db_connection == "DB Connection"
    
def test_query2(db_connection):
    print("/n SQL query2")
    assert db_connection == "DB Connection"
    
def test_query3(db_connection):
    print("/n SQL query2")
    assert db_connection == "DB Connection"


@pytest.fixture(scope="function")
def fixture1():
    print("this is a fixture setup")
    count1 = 10
    yield count1
    print("this is a fixture teardown")

@pytest.mark.parametirize("num1",[1,2])
@pytest.mark.parametirize("num2",[3,4])
def test_make_calc(fixture1, num2, num1):
    import pdb; pdb.set_trace()
    assert True
    