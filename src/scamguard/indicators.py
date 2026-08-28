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
    
THREAT_WORDS = {
    "account will be blocked",
    "account has been suspended",
    "legal action",
    "penalty",
    "fine",
    "police",
    "court action",
}


def find_threat_indicators(message):
    text = message.lower()
    findings = []

    for phrase in THREAT_WORDS:
        if phrase in text:
            findings.append(phrase)

    return findings

CREDENTIAL_WORDS = {
    "password",
    "otp",
    "pin",
    "verification code",
    "security code",
    "login details",
}


def find_credential_indicators(message):
    text = message.lower()
    findings = []

    for phrase in CREDENTIAL_WORDS:
        if phrase in text:
            findings.append(phrase)

    return findings
