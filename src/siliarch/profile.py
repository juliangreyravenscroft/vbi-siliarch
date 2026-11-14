
max_memory_bytes = 2**63 - 1


def validate_memory_bytes(value: object) -> int:
    if type(value) is not int:
        raise ValueError("memory_bytes must be an integer")

    if not 1 <= value <= max_memory_bytes:
        raise ValueError("memory_bytes is outside the allowed range")

    return value
