""" Visit API
"""
from ammd.components.visit.models import Visit


def update_sessions(visit, session_key, date):
    """ Save or Updates the sessions associated to the user visits.

    Args:
    Visit object

    Returns:

    """
    # update sessions and date associated to a user visit
    if session_key not in visit.sessions:
        visit.sessions.append(session_key)
        visit.related_date.append(date)
        upsert(visit)


def upsert(visit):
    """ Save or Updates the id the Visit object.

    Args:
    Visit object

    Returns:

    """
    return visit.save_object()


def upsert_visit_object(user, session_key, date):
    """ Create or Updates the sessions of the Visit object.

    Args:
    user: represents the user who is visiting the app
    session_key: list of key sessions of the user

    Returns:

    """
    visit = Visit.get_by_user(user)
    if visit:
        # Visit model for this user already exist
        update_sessions(visit, session_key, date)
    else:
        # Visit for this user does not exist => create an object that will represent the user and its sessions
        visit = Visit(user=user, sessions=[session_key], related_date=[date])
        upsert(visit)


def get_all_visits():
    """ Return all Visits objects from the database.

    Returns:

    """
    return Visit.get_all()


def delete_visits():
    """ Remove all Visits objects from the database.

    Returns:

    """
    return Visit.delete_objects()
