from django.core.cache import cache
def add_register_period_task(name):
    key = "__REGISTER_PERIODIC_TASKS"
    value = cache.get(key, [])
    value.append(name)
    cache.set(key, value)


def get_register_period_tasks():
    key = "__REGISTER_PERIODIC_TASKS"
    return cache.get(key, [])
