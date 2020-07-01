from django.conf.urls import url
from accounts.views import LoginView, LogoutView, SignupView

app_name = 'accounts'

urlpatterns = [
    url("^signup/$", SignupView.as_view(), name='signup'),
    url("^login/$", LoginView.as_view(), name="login"),
    url("^logout/$", LogoutView.as_view(), name="logout"),
]

