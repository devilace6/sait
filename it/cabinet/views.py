from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.shortcuts import redirect
from django.contrib import messages

@login_required
def profile(request):
    user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'cabinet/user_profile.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'user1': user})

