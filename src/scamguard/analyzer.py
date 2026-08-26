def analyze_message(message):
    if not message or not message.strip():
        raise ValueError("Message cannot be empty.")

    return {
        "message": message,
        "indicators": [],
        "score": 0,
    }
