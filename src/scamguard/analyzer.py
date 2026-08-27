from .indicators import find_urgency_indicators


def analyze_message(message):
    if not message or not message.strip():
        raise ValueError("Message cannot be empty.")

    urgency = find_urgency_indicators(message)

    indicators = []

    if urgency:
        indicators.append({
            "type": "urgency",
            "matches": urgency,
        })

    return {
        "message": message,
        "indicators": indicators,
        "score": 0,
    }
