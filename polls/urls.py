from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'sorter'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tag_list/', views.TagListView, name='tag_list'),
    path('<int:pk>/tag_contents', views.TagContentsView, name='tag_contents'),
    path('<int:pk>/', views.EditFolderView, name='edit_folder'),
    path('<int:pk>/view/', views.FolderContentsView, name='detail'),
    path('<int:pk>/view_source/<int:pk1>', views.SourceView, name='source'),
    path('<int:pk>/add_source/', views.NewSourceView, name='new_source'),
    path('<int:pk>/delete_folder/', views.DeleteFolderView, name='delete_folder'),
    path('create_folder/', views.CreateFolderView, name='create_folder'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('sorter/<int:pk>/importance_change/', views.ImportanceChangeView, name='importance_change'),

    #profile start
    #profile urls
    path("accounts/profile/edit/", views.edit_profile, name = 'edit_profile'),
    path("accounts/profile/", views.Profile_View, name = 'profile'),
    path("accounts/profile/password_change", views.PasswordChangeView, name = 'password_change')

    #path("create_folder/", views.SignUpView.as_view(), name="create_folder"),

    
    #profile end

]   