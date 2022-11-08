from django.views.generic import View
from django.http import JsonResponse, HttpRequest

from utils.format import FormatDictQuery
from utils.connection import Connection

# Create your views here.


class BaseView(View):
    model = None
    route_name = "Base Route Class"
    template_name = None

    query_formatter = FormatDictQuery()

    columns_on_db = []

    connection = Connection()

    __default_columns = ["active"]

    def get_context(self):
        return {
            "route": self.route_name,
            "body": {}
        }

    def get(self, request: HttpRequest):
        context = self.get_context()
        context["method"] = request.method

        return JsonResponse(context)

    def post(self, request: HttpRequest):
        context = self.get_context()
        context["method"] = request.method

        return JsonResponse(context)

    def get_columns(self):
        return self.columns_on_db + self.__default_columns

