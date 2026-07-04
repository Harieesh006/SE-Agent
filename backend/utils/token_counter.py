def count_tokens(text: str) -> int:
    return len(text.split())


def truncate(text: str, max_tokens: int = 4000) -> str:
    words = text.split()
    if len(words) <= max_tokens:
        return text
    return " ".join(words[:max_tokens])
