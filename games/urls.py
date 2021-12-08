from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', GamesHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addgame/', AddGame.as_view(), name='add_game'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', GamesCategory.as_view(), name='category')
    # path('cats/<int:catid>/', categories),
    # re_path(r'^cal/(?P<year>[0-9]{4})/', calendar)
]