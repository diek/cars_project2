from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _

from .forms import EmailSMSForm, ProfileForm, UserForm

from .models import Profile


@transaction.atomic
def edit_user(request, core_user_id):
    user = get_object_or_404(User, id=core_user_id)
    p_user = get_object_or_404(Profile, id=core_user_id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=p_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect(reverse('user_profile:user_detail', kwargs={'core_user_id': core_user_id}))
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=p_user)
    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def add_email_sms(request, core_user_id):
    user = get_object_or_404(User, id=core_user_id)
    if request.method == 'POST':
        form = EmailSMSForm(request.POST)
        if form.is_valid():
            contact_data = form.save()
            contact_data.users.add(user.id)
            messages.success(request, _('Your profile contact information was successfully updated!'))
            return redirect(reverse('user_profile:user_detail', kwargs={'core_user_id': core_user_id}))
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = EmailSMSForm()
    return render(request, 'profiles/add_contact_info.html', {
        'form': form,
        'user': user,
    })


def user_detail(request, core_user_id):
    user = get_object_or_404(User, id=core_user_id)
    email_sms = user.secondaryemailsms_set.all()
    return render(request, 'profiles/user_profile.html', {'user': user, 'email_sms': email_sms})


def list_users(request):
    users = User.objects.all()
    return render(request, 'profiles/users.html', {'users': users})
