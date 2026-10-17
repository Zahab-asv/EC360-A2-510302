import auth_service

def test_register_new_user():
    assert auth_service.register("a@b.com", "pass123") is True

def test_register_duplicate():
    auth_service.register("c@d.com", "pass123")
    assert auth_service.register("c@d.com", "pass123") is False
