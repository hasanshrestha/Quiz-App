from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.adminLogin, name="adminLogin"), #landing page
    path('index/', views.index, name="index"), 
    path('adminIndex/', views.adminIndex, name="adminIndex"), 
    path('show', views.showQuestions, name="showQuestions"),
    #path('index/', views.adminLoginPost, name="adminLoginPost"),
    path('logggin/', views.PostAdminLogin, name="PostAdminLogin"),
    path('create/', views.createQuestions, name="createQuestions"),
    path('add/', views.addQuestions, name="addQuestions"),
    path('edit/<int:qid>', views.editQuestion, name="editQuestion"),
    path('update/', views.updateQuestion, name="updateQuestion"),
    path('delete/<int:qid>', views.deleteQuestion, name="deleteQuestion"),

    path('register/', views.register, name="register"),
    path('userregister/', views.userRegister, name="userRegister"),
    path('userlogin/', views.userLogin, name="userLogin"),
    path('userProfile/', views.userProfile, name="userProfile"),
    path('takeTest/', views.takeTest, name="takeTest"),
    path('sendemail/', views.sendemail, name="sendemail"),
    path('logout/', views.logout, name="logout"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

    path('getUsersCount/', views.getUsersCount, name="getUsersCount"),
    path('getQuestionCount/', views.getQuestionCount, name="getQuestionCount"),

] 
urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

