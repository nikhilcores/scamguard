from .scoring import calculate_score, get_risk_level
from .severity import get_severity
from .indicators import (
    find_credential_indicators,
    find_financial_indicators,
    find_threat_indicators,
    find_urgency_indicators,
)

def analyze_message(message):
    if not message or not message.strip():
        raise ValueError("Message cannot be empty.")

    urgency = find_urgency_indicators(message)
    threat = find_threat_indicators(message)
    credential = find_credential_indicators(message)
    financial = find_financial_indicators(message)

    indicators = []

    if urgency:
        indicators.append({
            "type": "urgency",
            "severity": get_severity("urgency"),
            "matches": urgency,
        })
    if threat:
        indicators.append({
            "type": "threat",
            "severity": get_severity("threat"),
            "matches": threat,
        })
    if credential:
        indicators.append({
            "type": "credential:,
            "severity": get_severity("credential"),
            "matches": credential,
        })
    if financial:
        indicators.append({
            "type": "financial",
            "severity": get_severity("financial"),
            "matches": financial,
        })

score = calculate_score(indicators)
risk_level = get_risk_level(score)
indicator_count = len(indicators)

    return {
        "message": message,
        "indicators": indicators,
        "indicator_count": indicator_count,
        "score": score,
        "risk_level": risk_level,
    }
