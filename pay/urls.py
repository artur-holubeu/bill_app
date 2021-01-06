from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pay/<int:pk>", views.bill_payment, name='bill_payment'),
    path("pay-success/<int:pk>", views.bill_success, name='pay_success'),
    path("delete/<int:pk>", views.bill_deletion, name='bill_deletion')
]
