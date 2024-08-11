from django.urls import path
from .views import MembersListCreate, MembersRetrieveUpdateDestroy

urlpatterns = [
    path('members/', MembersListCreate.as_view(), name='members-list-create'),
    path('members/<int:pk>/', MembersRetrieveUpdateDestroy.as_view(), name='members-detail'),
]