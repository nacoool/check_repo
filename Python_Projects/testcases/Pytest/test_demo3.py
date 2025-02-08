import pytest

# Fixture that takes parameters dynamically
@pytest.fixture
def user_role(request):
    role = request.param  # Get the parameter value
    print(f"\n[SETUP] Creating user with role: {role}")
    yield role
    print(f"\n[TEARDOWN] Deleting user with role: {role}")


@pytest.fixture
def user_action(request, user_role):
    action = request.param
    print(f"\n user {user_role} wants to perform following action : {action}")
    yield action
    print(f"\n action completed {action}")

# Parametrized test that passes values to the fixture
@pytest.mark.parametrize("user_role", ["admin", "guest", "editor"], indirect=True)
@pytest.mark.parametrize("user_action", ["login", "signup", "deactivate"], indirect=True)
def test_access_control(user_role, user_action):
    print(f"Testing access control for role: {user_role}")
    assert user_role in ["admin", "guest", "editor"]
    assert user_action in ["login", "signup", "deactivate"]
    
