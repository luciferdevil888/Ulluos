context = {}


def remember(key, value):
    context[key] = value


def recall(key):
    return context.get(key, "")


def clear():
    context.clear()


def all_context():
    return context
