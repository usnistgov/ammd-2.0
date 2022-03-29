""" Admin views
"""
import logging

from django.contrib.admin.views.decorators import staff_member_required

from ammd.components.visit import api as visit_api
from core_main_app.utils.rendering import admin_render

logger = logging.getLogger(__name__)


@staff_member_required
def get_visits_number(request):
    """View that allows to see the number of visits in the website.

    Args:
    request:

    Returns:

    """

    # Get all visits
    all_visits = visit_api.get_all_visits()
    hits = 0
    for visit in all_visits:
        sessions = visit.sessions
        # Count the number of sessions associated to the user
        hits = hits + len([v for v in sessions if v is not None])

    context = {"object_name": "Visits"}
    context["visits_hits"] = hits
    context["visits"] = all_visits

    assets = {}
    modals = []

    return admin_render(
        request,
        "ammd/admin/visit/visits_index.html",
        assets=assets,
        context=context,
        modals=modals,
    )
