from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def greeting(request):
    name = request.query_params.get("name", "world")
    return Response({"message": f"Hello, {name}!"})
