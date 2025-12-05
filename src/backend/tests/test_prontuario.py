def test_build_prontuario():
    from backend.app.services.prontuario_service import build_prontuario
    p = build_prontuario("testuser")
    assert isinstance(p, dict)
    assert p.get("user_id") == "testuser"
