from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from MyAccounts.models import User
from AuthByInheritence.settings import AUTH_USER_MODEL

@csrf_exempt
def myfuncview(request):
    if request.method == "POST":
        return HttpResponse("posted")
    elif request.method == "GET":


        return render(request, 'MyAccounts/index.html', context={})



class myclassview(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(myclassview, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'MyAccounts/index.html', context={})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'status': True})
        return JsonResponse({'status': False})
