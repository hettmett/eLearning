from functools import wraps
from flask import session, flash, redirect, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, *kwargs)
        flash('Please login')
        return redirect(url_for('auth.login'))

    return wrapper

