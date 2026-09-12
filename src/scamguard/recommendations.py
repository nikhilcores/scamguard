RECOMMENDATIONS = {
    "urgency": (
        "Take your time and verify the message through "
        "an official source before acting."
    ),
    "threat": (
        "Do not act because of the threat. Verify the claim "
        "through an official source."
    ),
    "credential": (
        "Do not share passwords, OTPs, PINs, or verification "
        "codes through a message."
    ),
    "financial": (
        "Verify the payment or financial request independently "
        "before sending money."
    ),
    "url": (
        "Avoid opening the link until you verify where it "
        "leads and who sent it."
    ),
}


def get_recommendation(indicator_type):
    return RECOMMENDATIONS.get(
        indicator_type,
        "Verify the message before taking action.",
    )
