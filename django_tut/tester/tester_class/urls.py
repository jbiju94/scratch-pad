from django.urls import path

from tester_class import views as v

urlpatterns = [
    # Path to admin of one application
    path('', v.home,name="home")
]