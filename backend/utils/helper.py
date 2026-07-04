import datetime


def timestamp() -> str:
    return datetime.datetime.now().isoformat()


def truncate_text(text: str, max_len: int = 100) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."
