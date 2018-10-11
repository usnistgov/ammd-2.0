""" AMMD user views
"""

from core_main_app.utils.rendering import render


def landing_page(request):
    """ Landing page for the website

        Parameters:
            request:

        Returns:
    """
    context = {}

    assets = {
        "css": ['css/landing.css'],
    }

    return render(request,
                  "ammd/user/landing.html",
                  context=context,
                  assets=assets,
                  use_theme=False)
