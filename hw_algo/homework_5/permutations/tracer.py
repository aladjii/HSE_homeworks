def trace_recursion(func):
    depth = 0

    def wrapper(*args, **kwargs):
        nonlocal depth
        print("  " * depth + f"→ Вход в {func.__name__}{args}")
        depth += 1
        result = func(*args, **kwargs)
        depth -= 1
        print("  " * depth + f"← Выход из {func.__name__}{args} = {result}")
        return result

    return wrapper
