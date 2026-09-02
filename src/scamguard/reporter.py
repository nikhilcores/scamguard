def format_report(result):
    lines = [
        "ScamGuard",
        "─────────",
        "",
        f"Risk: {result['risk_level'].upper()}",
        f"Score: {result['score']}/100",
        f"Indicators: {result['indicator_count']}",
        "",
    ]

    if not result["indicators"]:
        lines.append("No suspicious indicators found.")
        return "\n".join(lines)

    lines.append("Findings:")
    lines.append("")

    for indicator in result["indicators"]:
        lines.append(
            f"[{indicator['severity'].upper()}] "
            f"{indicator['type'].title()}"
        )

        lines.append(
            f"Matches: {', '.join(indicator['matches'])}"
        )

        lines.append(
            f"Why: {indicator['explanation']}"
        )

        lines.append(
            f"Advice: {indicator['recommendation']}"
        )

        lines.append("")

    return "\n".join(lines)
