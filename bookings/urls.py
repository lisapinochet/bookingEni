from django.urls import path

from bookings import views

urlpatterns = [
    path('', views.BookingList.as_view(), name='booking_list'),
    path('my/', views.my_booking_list, name='booking_my'),
    path('booking/create/', views.BookingCreate.as_view(), name='booking_form'),
    path('booking/<int:pk>/cancel', views.cancel_booking, name='booking_cancel'),
]