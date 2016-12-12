from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor....'
    user.save()
