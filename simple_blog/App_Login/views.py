from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    form = UserCreationForm()
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form, 'registerd':registered}
    return render(request, 'App_Login/sign_up.html', context=dict)
