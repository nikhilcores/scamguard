from src.scamguard.analyzer import analyze_message


def test_empty_message():
    try:
        analyze_message("")
        assert False
    except ValueError:
        assert True


def test_urgency_detection():
    result = analyze_message(
        "Act now to verify your account."
    )

    assert "urgency" in [
        indicator["type"]
        for indicator in result["indicators"]
    ]


def test_credential_detection():
    result = analyze_message(
        "Send your password and OTP to continue."
    )

    types = [
        indicator["type"]
        for indicator in result["indicators"]
    ]

    assert "credential" in types


def test_financial_detection():
    result = analyze_message(
        "You won a prize. Send money to claim your reward."
    )

    types = [
        indicator["type"]
        for indicator in result["indicators"]
    ]

    assert "financial" in types


def test_risk_score_exists():
    result = analyze_message(
        "Urgent! Your account will be blocked."
    )

    assert 0 <= result["score"] <= 100
    assert result["risk_level"] in {
        "low",
        "medium",
        "high",
    }
