from models import Alert


NEXT_STEPS = {
    "critical": "Investigate immediately and take corrective action.",
    "warning": "Review the affected system and monitor the metric closely.",
    "info": "Review the metric and confirm whether any action is needed.",
}


def generate_explanation(alert: Alert) -> str:
    """Generate a descriptive explanation and recommended next step for an alert.

    Args:
        alert: The alert whose severity, source, title, and metric are described.

    Returns:
        An explanation including the metric's threshold comparison, the next
        step for the severity, and the uppercase resolver or an acknowledgement
        placeholder if no resolver is set.

    Raises:
        KeyError: If the alert's severity has no recommended next step.
        TypeError: If the metric values cannot be compared or the severity is
            unhashable.
        AttributeError: If a non-null resolver has no upper method.
    """
    if alert.metric_value > alert.threshold:
        comparison = "exceeded"
    elif alert.metric_value < alert.threshold:
        comparison = "fell below"
    else:
        comparison = "reached"

    next_step = NEXT_STEPS[alert.severity]
    explanation = (
        f'This {alert.severity} alert from {alert.source} is titled "{alert.title}". '
        f"The {alert.metric_name} metric {comparison} its threshold: the current value is "
        f"{alert.metric_value}, compared with a threshold of {alert.threshold}. "
        f"Recommended next step: {next_step}"
    )
    resolved_by = getattr(alert, "resolved_by", None) 
    acknowledged_by = (
        resolved_by.upper() if resolved_by is not None else "Not yet acknowledged"
    )
    return explanation + f" Acknowledged by: {acknowledged_by}."