from django.urls import path
from .views import (
    NewsView,
NewsDetailsView,
AboutUs,
Contact,
)

app_name = "appearance"

urlpatterns = [
    path("", NewsView.as_view(), name="index"),
    path("new/<int:pk>", NewsDetailsView.as_view(), name="new_details"),
    path("about/", AboutUs.as_view(), name="about_us"),
    path("contact/", Contact.as_view(), name="contact"),
]