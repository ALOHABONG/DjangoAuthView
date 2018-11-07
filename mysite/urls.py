"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from blog.views import UserCreateView, UserCreateDoneTemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(),name='logout'),
    url(r'^password_change/$', views.PasswordChangeView.as_view(template_name='blog/password_change.html'),
        name='password_change'),
    url(r'^password_change/done/$', views.PasswordChangeDoneView.as_view(template_name='blog/password_change_done.html'),
        name='password_change_done'),
    url(r'^password_reset/$', views.PasswordResetView.as_view(
        template_name='blog/password_reset.html',
        email_template_name='blog/password_reset_email.html'
        ),
        name='password_reset'),
    url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^register/$', UserCreateView.as_view(), name='register'),
    url(r'^register/done/$', UserCreateDoneTemplateView.as_view(), name='register_done'),
    url(r'', include('blog.urls')),
]
