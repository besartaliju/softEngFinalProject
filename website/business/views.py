from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.views import generic

# Create your views here.
class UserFormView(View):
    form_class = UserForm
    template_name = 'business/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #clean and normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            #returns user object
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('business:index')
        return render(request, self.template_name, {'form': form})

def IndexView(ListView):
    template_name = 'business/index.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all()

def DetailView(DetailView):
    model = Post
    template_name = 'business/detail.html'

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor....'
    user.save()
