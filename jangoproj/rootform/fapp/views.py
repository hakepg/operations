from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def create_user_form(req):
    return render(req, 'user.html', {'userform': UserForm()})


def save_user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print('form is valid..')  # does nothing, just trigger the validation
        else:
            print('form is invalid..')
    else:
        form = UserForm()
    return render(request, 'userform.html', {'userform': form})
