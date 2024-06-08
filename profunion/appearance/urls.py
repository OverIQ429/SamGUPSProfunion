from django.urls import path
from .views import (
    NewsView,
NewsDetailsView,
AboutUs,
Contact,
Index,
)

app_name = "appearance"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("new/", NewsView.as_view(), name="new"),
    path("new/<int:pk>", NewsDetailsView.as_view(), name="new_details"),
    path("about/", AboutUs.as_view(), name="about_us"),
    path("contact/", Contact.as_view(), name="contact"),
]