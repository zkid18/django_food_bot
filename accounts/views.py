from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             #  log the user in
             return redirect('/posts')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })