from django.urls import path
from . import views
app_name = 'abc_app'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('post/',views.CreatePhotoView.as_view(),name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    path('post_view/',views.IndexPost.as_view(),name='post_view'),
    path('photos/<int:category>',views.CategoryView.as_view(),name = 'photos_cat'),
    path('user-list/<int:username>',views.UserView.as_view(),name = 'username_list'),
    path('photo-detail/<int:pk>',views.DetailView.as_view(),name = 'photo_detail'),
    path('mypage/',views.MypageView.as_view(),name = 'mypage'),
    path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name = 'photo_delete'),
    path('contact/',views.ContactView.as_view(),name='contact'),
]