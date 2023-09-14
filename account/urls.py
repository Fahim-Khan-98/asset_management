from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from account import views



urlpatterns = [
    path('register/', views.Register, name="register"),
    path('login/', views.Login, name="login"),
    path('logout/',views.Logout, name="logout"),

   path('password_change/',auth_views.PasswordChangeView.as_view(template_name="account/password_change_form.html"),name='password_change'),
   path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),name='password_change_done'),
# reset password urls

    # change password urls
    # path('password_change/',auth_views.PasswordChangeView.as_view(template_name="account/password_change_form.html"),name='password_change'),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),name='password_change_done'),


    # reset password urls
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="account/reset_password.html"),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"),name='password_reset_complete'),
  

]
#   *******You can search authentication from stack overflow*******

# https://stackoverflow.com/questions/64622771/passwordresetconfirmview-as-view-in-django-redirect-to-django-administration

#   1.   Submit Email Form                        PasswordResetView.as_view(),

#   2.   Email Sent Success Message               PasswordResetDoneView.as_view()

#   3.   Link to password reset from in mail      PasswordResetConfirmView.as_view()

#   4.   Password succesfully changed messaged    PasswordResetCompleteView.as_view()




# Superuser password
# username = admin
# password = admin



# Normal_User  fahim @@@admin1234