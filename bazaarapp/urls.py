
from django.urls import path
from bazaarapp import views


urlpatterns=[
    path('login/',views.LoginView.as_view(),name="signin"),
    path('create/',views.CategoryCreateView.as_view(),name="create"),
    path("categorylist/",views.CategoryListView.as_view(),name="catlist"),
    path("detail/<int:pk>/",views.CategoryDetailView.as_view(),name="detail"),
    path('delete/<int:pk>',views.CategoryDeleteView.as_view(),name="delete")
    ]
