from time import sleep

from django.http import HttpResponseForbidden
from django.core.cache import cache

from validations import utils
from validations.utils.users import *


class Example:
    # Service itself
    def service(self, request, user_id): 
        strategy = self.decide_strategy(request.user)
        data = strategy.execute(request, user_id)

        return data

    # Decide the strategy
    @staticmethod
    def decide_strategy(user):
        if utils.is_user(user, ALUNO):
            return AlunoStrategy()

        if utils.is_user(user, PROFESSOR):
            return ProfessorStrategy()

    # Other patterns for service mutations
    def service_proxy(self, request, user_id):
        cache_key = f"validations__service_proxy__{user_id}"
        cached_result = cache.get(cache_key)
        
        if cached_result:
            return cached_result

        result = self.service(request, user_id)
        cache.set(cache_key, result, timeout=10)

        return result


# Strategy for ALUNO
class AlunoStrategy:
    def execute(self, request, user_id):
        return {
            'data': 'aluno'
        }


# Strategy for PROFESSOR
class ProfessorStrategy:
    def execute(self, request, user_id):
        return {
            'data': 'professor'
        }


example = Example()
