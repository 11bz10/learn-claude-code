"""Greeting module for demonstrating Python best practices."""


def greet(name: str) -> None:
    """Print a greeting message to the given name.

    Args:
        name: The person or entity to greet.
    """
    message = "Hello, " + name
    print(message)


if __name__ == "__main__":
    greet("Claude")