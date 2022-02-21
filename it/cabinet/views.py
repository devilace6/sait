from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import Profile
from django.shortcuts import get_object_or_404
def cabinet(request):
    return render(request, 'cabinet/user_profile.html')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'cabinet/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'cabinet/create_profile.html'
    fields = ['profile_pic', 'bio', 'vk', 'instagram']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')