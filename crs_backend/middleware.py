# crs_backend/middleware.py
from datetime import datetime
from django.conf import settings
from django.contrib.auth import logout

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            now = datetime.now()
            last_activity = request.session.get('last_activity')

            if last_activity:
                elapsed_time = (now - datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S")).total_seconds()
                if elapsed_time > settings.SESSION_COOKIE_AGE:
                    logout(request)
                    request.session.flush()  # Optional: clears all session data

            request.session['last_activity'] = now.strftime("%Y-%m-%d %H:%M:%S")

        response = self.get_response(request)
        return response
