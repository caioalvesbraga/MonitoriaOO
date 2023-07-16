from django.urls import path
from . import views

#Aqui são definidas as rotas que realizam o CRUD

urlpatterns = [
    path('',views.home, name='home'),
    #path('login/',views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('aluno/<int:pk>', views.customer_aluno, name='aluno'),
    path('deletar_aluno/<int:pk>', views.deletar_aluno, name='deletar_aluno'),
    path('add_aluno/', views.add_aluno, name='add_aluno'),
    path('update_aluno/<int:pk>', views.update_aluno, name='update_aluno'),
]
