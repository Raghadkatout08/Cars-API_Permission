# cars_api/middleware.py

from django.db import connection

class CloseDBConnectionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        connection.close()  # Explicitly close the connection
        return response
