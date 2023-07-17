from django.urls import path
from app.views import *

app_name = "a"
urlpatterns = [
    path("a/", a, name="a"),
    path("b/", b, name="b")
]
