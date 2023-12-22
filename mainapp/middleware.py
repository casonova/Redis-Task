from django.core.cache import cache
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user = request.user
            print(user)
            user_groups = user.groups.all()

            request_key = f"user_{user.id}_request_count"
            print(request_key)
            request_count = cache.get(request_key)
            print(request_count)

            if request_count is None:
                cache.set(request_key, 0, 60)
                request_count = 0

            request_limit = 0

            for group in user_groups:
                if group.name == "GOLD":
                    request_limit = 10
                    break
                elif group.name == "BRONZE":
                    request_limit = 5
                    break
                elif group.name == "SILVER":
                    request_limit = 2
                    break

            if request_count < request_limit:
                cache.set(request_key, request_count + 1, 60)
            else:
                response_data = {"msg": "Too many requests, you are blocked"}
                renderer = JSONRenderer()
                rendered_response = renderer.render(response_data)
                return HttpResponse(
                    rendered_response, content_type="application/json", status=429
                )

        response = self.get_response(request)
        return response
