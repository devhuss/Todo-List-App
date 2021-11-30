
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update/<int:id>', views.update, name="update"),
    path('add', views.addTodo, name="add"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('complete/<int:id>', views.completeTodo, name='complete'),
    path('updated/<int:id>', views.updateTodo, name="updated"),

]



