# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:31:48
# @Last Modified time: 2016-12-22 23:45:30
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, DetailView
from forms import LoginForm, EmailRegisterForm
from system.common.validate_code import send_email_code
from system.common.security import create_pwd
from models import SimpleUser, Menu, RoleMenu, UserRole
from base.common.json_change import to_list, to_json_str, to_json_list_str, values_to_json_list_str
import json
"""
@csrf_protect————让表单使用csrf_token
@csrf_exempt————不让表单使用csrf_token
@requires_csrf_token————与csrf_protect类似，但不会拒绝传入的请求
@ensure_csrf_cookie————强制视图发送CSRF cookie
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token, ensure_csrf_cookie

# from django.views.decorators.cache import cache_page

# from django.db.models import Q
# Q(x=xxx)|Q(y=yyy)————x=xxx or y=yyy
"""


class LoginView(View):
    """
    method_decorator————传递 *args 和 **kwargs 给类的装饰器，如果方法不兼容参数集合，会抛出TypeError异常
    @method_decorator(csrf_protect, login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)
    """

    def get(self, request, form_name):
        form = html = None                            # 用未绑定的form类渲染模板（get、post皆可）
        if not form_name:
            form = LoginForm()
            html = "login/email_login.html"
        if form_name == "email_register":
            form = EmailRegisterForm()
            html = "login/email_register.html"
        return render(request, html, {'form': form})  # “首次访问”时，调用from，生成<label><input>等标签内容

    def post(self, request, **kwargs):
        form = html = None                            # form表单绑定接收的数据，进行数据验证（get、post皆可）
        if request.path == '/login/':
            form = LoginForm(request.POST)
            html = "login/login.html"
        if request.path == '/login/email_register':
            form = EmailRegisterForm(request.POST)
            html = "login/email_register.html"
            if form.is_valid():
                u = SimpleUser.objects.filter(
                    email=form.cleaned_data['email'],
                    is_active=0
                ).update(
                    is_active=1,
                    pass_word=create_pwd(form.cleaned_data['pwd'])
                )
                return HttpResponseRedirect("/login")
        return render(request, html, {'form': form})  # “提交的信息不符合要求”时，调用form，反馈错误提示信息


def get_email_code(request):
    email = request.GET.get('email')
    try:
        u = SimpleUser.objects.get(email=email)    # 查询一条要更新的数据
        if u.is_active != 0:
            return HttpResponse("此邮箱已经被注册")
        security_code = send_email_code(email)
        """
        u.is_active = 1                            # 赋值给要更新的字段
        u.save()                                   # 保存
        """
        u = SimpleUser.objects.filter(             # 使用update更新
            email=email
        ).update(
            security_code=security_code
        )
    except Exception, e:
        print(e)
        try:
            security_code = send_email_code(email)
            u = SimpleUser(
                email=email,
                security_code=security_code
            )
            u.save()
        except Exception, e:
            print(e)
            return HttpResponse("邮箱地址不正确")
    return HttpResponse("ok")


class MenuView(TemplateView):
    template_name = 'menu/menuTree.html'

    def get_context_data(self, **kwargs):
        # json_list_str = to_json_list_str(Menu.objects.order_by('parentid', 'menu_order', 'id'))
        """
        ValuesQuerySet————QuerySet的子集————返回[dict, dict, ...]
        """
        json_list_str = values_to_json_list_str(Menu.objects.values())
        return {'menu_list': json_list_str}

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # 直接在视图中渲染数据内容，和网页其它部分一起发送到html文件上（一次性地渲染，还是同一次请求）
        return self.render_to_response(context)


# 返回单个权限信息，json类型
def get_menu(request):
    id = int(request.GET.get("id"))
    user_num = UserRole.objects.raw("""
    SELECT
        ur.id,
        count(ur.id)
    FROM
        role_menu rm,
        user_role ur,
        simple_user u
    WHERE
        ur.user_id=u.id
        AND ur.role_id=rm.role_id
        AND rm.menu_id=%d
    GROUP BY rm.menu_id
    """%id)
    if id == 1:
        m = Menu.objects.filter(id=id)
    else:
        '''
        使用用原生SQL————RawQueryset————RawQuerySet中必须包含id（主键）
        '''
        m = Menu.objects.raw("""
        SELECT
            id, menu_name, type, code, url_code, isvisible, parentid, menu_order,
            parent_name, parent_url_code
        FROM
            menu m,
            (SELECT
                menu_name parent_name, url_code parent_url_code
            FROM menu
            WHERE id = (SELECT parentid FROM menu WHERE id = %d)
            ) t
        WHERE id = %d
        """ % (id, id))
    menu = m[0].toDict()
    try:
        menu['user_num'] = user_num[0].toDict()['user_num']
    except Exception, e:
        print e
        menu['user_num'] = 0
    return HttpResponse(json.dumps(menu))


def delete_menu(request):
    if request.method == 'POST':                                        # 仅处理POST（GET）请求
        id = int(request.POST.get("id"))
        try:
            # Menu.objects.filter(id=id).delete()                       # 删除数据（一或多条）
            Menu.objects.get(id=id).delete()                            # 删除数据（一条）
            result = {'code': 0, 'msg': 'success'}
        except Exception, e:
            print e
            result = {'code': 1, 'msg': 'failure'}
        return HttpResponse(result)
