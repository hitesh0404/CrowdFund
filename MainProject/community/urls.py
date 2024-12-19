from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('add-motive/',login_required(views.CreateMotive.as_view()),name="create_motive"),
]