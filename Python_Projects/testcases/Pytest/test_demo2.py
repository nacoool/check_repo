
import pytest

@pytest.fixture(scope="session")
def fixture1():
    print("this is a fixture setup")
    count1 = 10
    yield count1  # Corrected "yield"
    print("this is a fixture teardown")

@pytest.mark.parametrize("num1", [1, 2])
@pytest.mark.parametrize("num2", [3, 4])
def test_make_calc(fixture1, num1, num2):
    print(f"fixture1: {fixture1}, num1: {num1}, num2: {num2}")
    assert True

import pytest

@pytest.fixture(scope="function")
def setup_function():
    print("\n[SETUP] Function-level fixture")
    yield "Class Data"
    print("\n[TEARDOWN] Function-level fixture")

@pytest.fixture(scope="module")
def setup_module():
    print("\n[SETUP] Module-level fixture")
    yield "Module Data"
    print("\n[TEARDOWN] Module-level fixture")

class TestExample:
    def test_one(self, setup_module, setup_function):
        print("\nRunning test_one")
        assert setup_function == "Class Data"

    def test_two(self, setup_function, setup_module):
        print("\nRunning test_two")
        assert setup_function == "Class Data"

@pytest.fixture
def setup1():
    print("\n[SETUP] Setup1")
    yield
    print("[TEARDOWN] Setup1")

@pytest.fixture
def setup2():
    print("\n[SETUP] Setup2")
    yield
    print("[TEARDOWN] Setup2")

@pytest.mark.usefixtures("setup1", "setup2")
def test_order():
    print("Running test_order")
