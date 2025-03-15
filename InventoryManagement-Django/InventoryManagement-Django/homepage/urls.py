# from django.urls import path
# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     path('', views.HomeView.as_view(), name='home'),
#     path('about/', views.AboutView.as_view(), name='about')
# ]


# from django.urls import path  # Remove the unused 'url' import/
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('logout/', LogoutView.as_view(next_page='logout'), name='logout'),  # ✅ Fix Logout Redirect
]

