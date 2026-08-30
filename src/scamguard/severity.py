SEVERITY_LEVELS = {
    "urgency": "medium",
    "threat": "high",
    "credential": "high",
    "financial": "medium",
}


def get_severity(indicator_type):
    return SEVERITY_LEVELS.get(indicator_type, "low")
