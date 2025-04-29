from django.http import HttpResponseForbidden
from django.shortcuts import render

from validations import services, utils
from validations.utils.users import *


# View itself
def example(request, user_id):
    context, template = factory(request, user_id)
    print(context)
    return render(request, template, context)


# Factory design pattern
def factory(request, user_id):
    context = {
        # Services used by everyone
    }

    if utils.is_user(request.user, ALUNO):
        context = {
            **context,
            # Services only for ALUNO
            'data': services.example.service_proxy(request, user_id) # With proxy
        }
        return context, "template/aluno.html"

    if utils.is_user(request.user, PROFESSOR):
        context = {
            **context,
            # Services only for PROFESSOR
            'data': services.example.service(request, user_id) # Without proxy
        }
        return context, "template/professor.html"
