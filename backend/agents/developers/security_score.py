def security_score_node(state):

    reviews = state.get(
        "security_review",
        []
    )

    score = 10

    for item in reviews:

        review = item["review"].upper()

        if "FAIL" in review:
            score -= 1

    return {
        "security_score": max(score, 0)
    }