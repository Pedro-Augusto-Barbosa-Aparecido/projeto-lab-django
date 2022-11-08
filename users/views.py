from django.http import HttpRequest, JsonResponse

from bases.views import BaseView
from .models import User


# Create your views here.


class UserCreateAPIView(BaseView):
    pass


class UserListAPIView(BaseView):
    model = User
    route_name = "user_list_api"

    columns_on_db = ["name", "email"]

    def get(self, request: HttpRequest):
        context = super(UserListAPIView, self).get_context()
        context["method"] = request.method

        query = self.query_formatter.format_for_list_or_get(request.GET, self.get_columns())
        where = False

        if len(query) > 0:
            where = True

        # data = self.model.objects.raw(
        #     "SELECT * FROM user" + " WHERE " + "%s = %s" * (len(query) // 2) if where else "", query)
        context["users"] = []
        for user in self.connection.list("SELECT * FROM User"):
            context["users"].append(user)

        print(context)

        return JsonResponse(context)


class UserDetailAPIView(BaseView):
    pass


class UserDeleteAPIView(BaseView):
    pass


class UserUpdateAPIView(BaseView):
    pass
