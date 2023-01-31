from django.urls import path
from .views import myapiList, myapiDetail

urlpatterns = [
    path("", myapiList.as_view(), name="myapi_list"),
    path("<int:pk>/", myapiDetail.as_view(), name="myapi_detail"),
]