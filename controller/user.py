from service.user import create_user_s, update_user_info_s, del_user_s, get_user_by_name_s, del_all_user_s

# Get
def get_user_c(name:str):
    return get_user_by_name_s(name)

# Create
def create_user_c(imgs, name, phone, identity):
    # Set user params
    user_params = {
        'name':name,
        'phone':phone,
        'identity':identity,
    }

    return create_user_s(imgs=imgs, user_params=user_params)

# Update
def update_user_info_c(name, phone, identity):
    # Set user params
    user_params = {
        'name':name,
        'phone':phone,
        'identity':identity,
    }
    return update_user_info_s(user_params=user_params)

# Delete
def del_user_c(name: str):
    return del_user_s(name)

def del_all_user_c():
    return del_all_user_s()