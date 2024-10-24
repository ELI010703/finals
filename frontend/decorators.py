from functools import wraps
from django.contrib.auth.decorators import user_passes_test

def admin_required(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return user_passes_test(
            lambda u: u.groups.filter(name='Admin').exists(),
            login_url='/login'
        )(*args, **kwargs)
    return wrapper if function is None else wrapper(function)

def staff_required(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return user_passes_test(
            lambda u: u.groups.filter(name='Staff').exists(),
            login_url='/login'
        )(*args, **kwargs)
    return wrapper if function is None else wrapper(function)
