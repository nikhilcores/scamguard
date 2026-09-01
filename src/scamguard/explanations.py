EXPLANATIONS = {
    "urgency": (
        "The message creates pressure to act quickly "
        "without giving you enough time to verify the request."
    ),
    "threat": (
        "The message uses consequences or fear to pressure "
        "you into taking action."
    ),
    "credential": (
        "The message asks for information such as a password, "
        "OTP, PIN, or verification code."
    ),
    "financial": (
        "The message involves money, payments, rewards, "
        "refunds, or financial transactions."
    ),
}


def get_explanation(indicator_type):
    return EXPLANATIONS.get(
        indicator_type,
        "This indicator may require further review.",
    )
