from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (delete_append,DownloadTableAppendView, ReportofAppends, AboutMeView, RegisterView, logout_view, AvatarUpdateView, UsersList, UserDetail, Create_Append, All_Appends, CheckAppens, Check_All_Appends, MyAppends, ReportofProfiles, DownloadTableView, CreateNew)

app_name = "myauth"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="myauth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login"),
    #path('login/',login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register", RegisterView.as_view(), name="register"),
    path("avatar_update/<int:pk>/", AvatarUpdateView.as_view(), name="avatar_update"),
    path("users_list/", UsersList.as_view(), name="users_list"),
    path("user_detail/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path("create_append/<int:pk>/", Create_Append.as_view(), name="create_append"),
    path("appends/", All_Appends.as_view(), name="all_appends"),
    path("appends/check/<int:pk>/", CheckAppens.as_view(), name="check_appends"),
    path("appends_list/", Check_All_Appends.as_view(), name="check_all_appends"),
    path("my_appends/", MyAppends.as_view(), name="my_appends"),
    path("report/", ReportofProfiles.as_view(), name="report_users"),
    path("report/order/", ReportofAppends.as_view(), name="report_appends"),
    path('append/<int:append_id>/delete/', delete_append, name='delete_append'),
    path('report/download_table/', DownloadTableView.as_view(), name='download_table'),
    path('report/order/download_table/', DownloadTableAppendView.as_view(), name='download_table'),
    path('create/', CreateNew.as_view(), name='create_news')
]