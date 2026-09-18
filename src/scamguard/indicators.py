import re

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

FINANCIAL_WORDS = {
    "payment",
    "refund",
    "prize",
    "lottery",
    "bank transfer",
    "send money",
    "claim your reward",
    "investment",
}


def find_financial_indicators(message):
    text = message.lower()
    findings = []

    for phrase in FINANCIAL_WORDS:
        if phrase in text:
            findings.append(phrase)

    return findings

URL_PATTERN = r"https?://[^\s<>"]+'

def find_url_indicators(message):
    return re.findall(URL_PATTERN, message)

SUSPICIOUS_URL_WORDS = {
    "login",
    "verify",
    "verification",
    "secure",
    "update",
    "confirm",
    "account",
    "password",
    "reward",
    "claim",
}

def find_suspicious_url_words(url):
    text = url.lower()
    findings = []

    for word in SUSPICIOUS_URL_WORDS:
        if word in text:
            findings.append(word)

    return findings

IP_URL_PATTERN = r"https?://(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?"

def find_ip_url_indicators(message):
    return re.findall(IP_URL_PATTERN, message)
