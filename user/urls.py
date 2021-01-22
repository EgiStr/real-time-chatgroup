from django.urls import path


from .views import userlogin,logoutUser,settingProfil
urlpatterns = [
    path("login/", userlogin, name="login"),
    path('logout/',logoutUser,name="logout"),
    path('profil/',settingProfil,name='setting'),
]
