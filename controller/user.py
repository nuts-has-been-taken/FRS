from service.user import create_user_s
def get_user_c():
    pass

def create_user_c(img, name, phone):
    # Set user params

    user_params = {
        'name':name,
        'phone':phone,
    }

    return create_user_s(img=img, user_params=user_params)