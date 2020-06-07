from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth import login, logout

class SignupView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request, user)
            return redirect('/posts')
        return render(request, 'accounts/signup.html', { 'form': form })

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', { 'form': form })


class LoginView(View):
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/posts')
        return render(request, 'accounts/login.html', { 'form': form })

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', { 'form': form })

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('/posts')

# @csrf_exempt
# def signup_view(request):
#     if request.method == 'POST':
#          form = UserCreationForm(request.POST)
#          if form.is_valid():
#              user = form.save()
#              #  log the user in
#              login(request, user)
#              return redirect('/posts')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', { 'form': form })


# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('/posts')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', { 'form': form })


# def logout_view(request):
#     if request.method == 'POST':
#             logout(request)
#             return redirect('/posts')

