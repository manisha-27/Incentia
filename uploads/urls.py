from django.urls import path

from . import views

urlpatterns = [
    path('',views.UploadList.as_view()),
    path('<int:pk>', views.UploadDetail.as_view())
]
