from django.urls.conf import path
from django.contrib.auth import views as auth_views
from .views import LoginView, LogoutView
from .forms import EmailValidationForm


urlpatterns = [
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(
        template_name='edc_base/accounts/login.html'), name='logout_url'),

    path('change-password/', auth_views.PasswordChangeView.as_view(
            template_name='edc_base/accounts/password_reset_change.html',
            success_url='/'), name='change_password'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='edc_base/accounts/password_reset_email.html',
            form_class=EmailValidationForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='edc_base/accounts/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='edc_base/accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='edc_base/accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
