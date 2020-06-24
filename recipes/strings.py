"""This module contains various tools for string operations."""

import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """Create a random string with given length and given characters."""
    return ''.join(random.choice(chars) for _ in range(size))


def fillzeros(string, desiredlength=1):
    """Pad the given string with zeros for desired length is reached."""
    return (str(string).zfill(desiredlength))


def contains_any(string, candidates=[]):
    """Return True if a string contains any of the given candidate strings."""
    for candidate in candidates:
        if candidate.lower() in string.lower():
            return True
    return False
