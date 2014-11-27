from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html', vars())

def login(request):
    next = request.GET.get('next', '/')
    if is_safe_url(next, request.get_host()):
        if request.user.is_authenticated():
            return redirect(request.GET.get('next', '/'))
        return render(request, 'core/login.html', {'next': request.GET.get('next', '/')})
    return redirect('core.views.home')
    
def logout(request):
    logout(request)
    return redirect('core.views.home')