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


def test_url_detection():
    result = analyze_message(
        "Check this link: https://example.com"
    )

    types = [
        indicator["type"]
        for indicator in result["indicators"]
    ]

    assert "url" in types

def test_multiple_urls():
    result = analyze_message(
        "Visit https://example.com and "
        "https://example.org"
    )

    url_indicators = [
        indicator
        for indicator in result["indicators"]
        if indicator["type"] == "url"
    ]

    assert len(url_indicators) == 1
    assert len(url_indicators[0]["matches"]) == 2

def test_detects_suspicious_url_words():
    result = analyze_message(
        "Please verify your account at https://example.com/login"
    )

    assert "verify" in result["suspicious_url_words"]
    assert "account" in result["suspicious_url_words"]
    assert "login" in result["suspicious_url_words"]

def test_detects_multiple_suspicious_url_words():
    result = analyze_message(
        "Claim your reward and confirm your password at https://example.com/claim"
    )

    assert "reward" in result["suspicious_url_words"]
    assert "confirm" in result["suspicious_url_words"]
    assert "password" in result["suspicious_url_words"]
    assert "claim" in result["suspicious_url_words"]
