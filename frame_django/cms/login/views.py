from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from forms import LoginForm


class LoginView(View):
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args):
        form = LoginForm()
        return render(request, "login/login.html", {'form': form})

    def post(self, request):
        pass

