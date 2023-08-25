from django.urls import path
from .views import (
    notes_view,
    notes_detail_view,
    notes_create_view,
    notes_update_view,
    notes_delete_view,
    SearchListView,
)

urlpatterns = [
    path("", notes_view),
    path("<int:pk>/", notes_detail_view),
    path("create/", notes_create_view),
    path("<int:pk>/update/", notes_update_view),
    path("<int:pk>/delete/", notes_delete_view),
    path("search/", SearchListView.as_view(), name="search"),
]
