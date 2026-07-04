def quality_score_node(state):

    score = 10

    review = state.get(
        "architecture_review",
        ""
    ).upper()

    if "POOR" in review:
        score -= 3

    if "BAD" in review:
        score -= 2

    return {
        "quality_score": max(score, 0)
    }