from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from forms import LoginForm


class LoginView(View):
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = LoginForm()
        pass

    def post(self, request):
        pass

