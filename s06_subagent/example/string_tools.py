import re


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    Steps:
    1. Convert to lowercase
    2. Replace spaces with hyphens
    3. Remove non-alphanumeric characters (except hyphens)
    4. Collapse consecutive hyphens into one
    5. Strip leading/trailing hyphens

    Example:
        >>> slugify("Hello World!")
        'hello-world'
        >>> slugify("Python 3.10 & Beyond")
        'python-310-beyond'
    """
    text = text.lower()
    text = text.replace(" ", "-")
    text = re.sub(r"[^a-z0-9-]", "", text)
    text = re.sub(r"-{2,}", "-", text)
    text = text.strip("-")
    return text