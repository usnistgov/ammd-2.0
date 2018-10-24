""" AMMD user views
"""

from core_main_app.utils.rendering import render


def landing_page(request):
    """ Landing page for the website

        Parameters:
            request:

        Returns:
    """
    assets = {
        "css": ["css/landing.css",
                "core_explore_tree_app/user/css/loading_background.css"],

        "js": [
            {
                "path": 'ammd/user/js/landing.js',
                "is_raw": False
            },
        ]
    }

    return render(request,
                  "ammd/user/landing.html",
                  assets=assets,
                  use_theme=False)
