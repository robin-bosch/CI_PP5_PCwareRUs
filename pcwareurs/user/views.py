'''
User views
'''
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from user.forms import AddressForm

from user.models import Address

# Create your views here.
def user_overview(request):
    '''
    User overview
    '''
    if request.user.is_authenticated:
        address_list = Address.objects.filter(user=request.user, is_used=False)
        return render(request, 'user/user_overview.html', {'address_list': address_list})


def add_address(request):
    '''
    Adds address
    '''

    if request.user.is_authenticated:

        if request.method == 'POST':
          
            form = AddressForm(request.POST)
            
            if form.is_valid():
                Address.objects.create(
                    user=request.user,
                    street=form.cleaned_data['street'],
                    city=form.cleaned_data['city'],
                    state=form.cleaned_data['state'],
                    zip=form.cleaned_data['zip'],
                    country=form.cleaned_data['country']
                )

                return redirect('user_overview')
            print(form.errors)
            return render(request, 'user/add_address.html', {'error_message': 'Invalid input'})
        return render(request, 'user/add_address.html')
    # TODO: Add restricted access message
    return redirect('home')


def edit_address(request, address_id):
    '''
    Edit Address
    '''
    if request.user.is_authenticated:
        address = get_object_or_404(Address, pk=address_id)

        if address.user == request.user:

            if request.method == 'POST':
            
                form = AddressForm(request.POST)
                
                if form.is_valid():
                    if address.is_used:
                        Address.objects.create(
                            user=request.user,
                            street=form.cleaned_data['street'],
                            city=form.cleaned_data['city'],
                            state=form.cleaned_data['state'],
                            zip=form.cleaned_data['zip'],
                            country=form.cleaned_data['country']
                        )
                    else:
                        address.street = form.cleaned_data['street']
                        address.city = form.cleaned_data['city']
                        address.state = form.cleaned_data['state']
                        address.zip = form.cleaned_data['zip']
                        address.country = form.cleaned_data['country']
                        address.save()

                    return redirect('user_overview')
                print(form.errors)
                return render(request, 'user/edit_address.html', {'error_message': 'Invalid input'})
            return render(request, 'user/edit_address.html', {'address': address})
        # TODO: Add restricted access message
        return redirect('user_overview')
    # TODO: Add restricted access message
    return redirect('home')


def delete_address(request, address_id):
    if request.user.is_authenticated:
        address = get_object_or_404(Address, pk=address_id)

        if address.user == request.user:

            if request.method == 'DELETE':
                pass
