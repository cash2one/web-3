# coding:utf-8

def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("已登录")
        else:
            return HttpResponse("请允许浏览器都接受cookie")
    else:
        raise Http404('Only POSTs are allowed')
    request.session.set_test_cookie()
    return render_to_response('foo/login_form.html')
