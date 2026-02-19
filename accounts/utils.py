def is_user(user):
    return user.groups.filter(name='user').exists() or user.is_superuser

def is_admin(user):
    return user.groups.filter(name='admin').exists() or user.is_superuser