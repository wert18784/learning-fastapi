# https://fastapi.tiangolo.com/tutorial/testing/
import pytest
from app import schemas
from jose import jwt
from app.config import settings


# each test should be able to be run independetly of each other

# testing root url hello world path
def test_root(client):
    res = client.get("/")
    print(res.json())
    assert res.json().get("message") == "Hello World"
    assert res.status_code == 200


# you want pytest to stop on first failure pass -x flag
# see prints -s flag


def test_create_user(client):
    # must add trailing / for routes
    res = client.post(
        "/users/", json={"email": "hello123@gmail.com", "password": "password123"}
    )
    print(res.json())

    # validates userOut schema pydantic model
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201


def test_login_user(
    test_user, client
):  # use test_user fixure so that test is independent
    # must use data keyword instead of jason because route only accepts form data
    res = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    # validating token
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    # validating decoded token has correct user id
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrongemail@gmail.com", "password123", 403),
        ("sanjeev@gmail.com", "wrongpassword", 403),
        ("wrongemail@gmail.com", "wrongpassword", 403),
        (None, "password123", 422),
        ("sanjeev@gmail.com", None, 422),
    ],
)
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    # assert res.json().get("detail") == "Invalid Credentials"
