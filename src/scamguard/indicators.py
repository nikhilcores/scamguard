URGENCY_WORDS = {
    "urgent",
    "immediately",
    "act now",
    "right away",
    "final warning",
    "within 24 hours",
}


def find_urgency_indicators(message):
    text = message.lower()
    findings = []

    for phrase in URGENCY_WORDS:
        if phrase in text:
            findings.append(phrase)

    return findings
