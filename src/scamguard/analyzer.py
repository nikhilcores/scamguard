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
            "matches": urgency,
        })
    if threat:
        indicators.append({
            "type": "threat",
            "matches": threat,
        })
    if credential:
        indicators.append({
            "type": "credential:,
            "matches": credential,
        })
    if financial:
        indicators.append({
            "type": "financial",
            "matches": financial,
        })

    return {
        "message": message,
        "indicators": indicators,
        "score": 0,
    }
