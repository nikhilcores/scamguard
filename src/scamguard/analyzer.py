from .indicators import (
    find_threat_indicators,
    find_urgency_indicators,
)

def analyze_message(message):
    if not message or not message.strip():
        raise ValueError("Message cannot be empty.")

    urgency = find_urgency_indicators(message)
    threat = find_threat_indicators(message)

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

    return {
        "message": message,
        "indicators": indicators,
        "score": 0,
    }
