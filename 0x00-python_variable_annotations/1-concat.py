"""Module that concatenates two strings."""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string to be concatenated.
        str2 (str): The second string to be concatenated.

    Returns:
        str: The concatenated string.

    Example:
        >>> concat("Hello", "World")
        'HelloWorld'
    """
    return str1 + str2
