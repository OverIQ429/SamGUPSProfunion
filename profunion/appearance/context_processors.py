from .forms import UserLoginForm

def login_form(request):
    return {'login_form': UserLoginForm()}