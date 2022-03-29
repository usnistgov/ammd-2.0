from django.utils.deprecation import MiddlewareMixin
from ammd.components.visit import api as visit_api
from datetime import datetime


class GetVisits(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        active_user = request.user
        current_session = request.session.session_key

        session_date = datetime.today()
        # Create a Visit or add a session to the existing Visit object if the associated user has already visited the site
        if current_session:
            visit_api.upsert_visit_object(
                str(active_user), current_session, session_date
            )
