import helper
import kits
import pytest




@pytest.mark.parametrize("name", [
    pytest.param(
        "a",  id="Check 1 symbol - low border"   #excpected 201
    ),
    pytest.param(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC",  id="Check 511 symbols - high border" #excpected 201
    ),
    pytest.param(
        "QWErty",  id="Check english letters" #excpected 201
    ),
    pytest.param(
        "Мария", id="Check russian letters" #excpected 201
    ),
    pytest.param(
        "%,",  id="Check special symbols" #excpected 201
    ),
    pytest.param(
    "Человек и КО",  id = "Check backspace" #excpected 201
    ),
    pytest.param(
    "123",  id = "Check string with numbers" #excpected 201
    ),
])

def test_create_kits_with_different_names(name):
    # Arrange

    created_user = kits.create_new_user().json()['authToken']
    kit_body = helper.modify_create_kit_body(name)

    # Act
    kits_create_result = kits.create_kit(created_user, kit_body )

    # Assert
    assert kits_create_result.status_code == 201
    assert kits_create_result.json()["name"] == name

@pytest.mark.parametrize("name", [
    pytest.param(
        "",  id="Check 0 symbols" #excpected 400
    ),
    pytest.param(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD",  id="Check 512 symbols - too high" #excpected 400
    ),
      pytest.param(
    123,  id = "Check with other type - int" #excpected 400
    ),
])

def test_create_kits_with_different_negative_names(name):
    # Arrange

    created_user = kits.create_new_user().json()['authToken']
    kit_body = helper.modify_create_kit_body(name)

    # Act
    kits_create_result = kits.create_kit(created_user, kit_body )

    # Assert
    assert kits_create_result.status_code == 400

def test_create_kits_without_param_name():
    # Arrange
    created_user = kits.create_new_user().json()['authToken']
    kit_body = {}
    # Act
    kits_create_result = kits.create_kit(created_user, kit_body)

    # Assert
    assert kits_create_result.status_code == 400
