from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.decorators.http import require_POST

from accounts.utils import is_admin
from bookings.models import Booking


# Create your views here.
class BookingList(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model=Booking

    def test_func(self):
        return is_admin(self.request.user)

@login_required
def my_booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('status', '-start_at')
    return render(request, 'bookings/booking_my.html', {'bookings':bookings})

class BookingCreate(LoginRequiredMixin, generic.CreateView):
    model=Booking
    fields=['start_at', 'end_at', 'resource']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Spécifier les widgets pour les dates
        form.fields['start_at'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['end_at'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        # Assigner automatiquement l'utilisateur connecté
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # redirige vers mes_reservations de l'utilisateur connecté
        return reverse('booking_my')

@login_required
@require_POST #empêche l'annulation via URL directe
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)

    booking.status='02'
    booking.save()
    return redirect('booking_my')