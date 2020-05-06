""" Menu configuration for AMMD. The following menus are displayed in addition to those which belong exclusively to AMMD:

  * Main menu

    * Home
    * Browse Data
    * Search Data
    * View Schema
    * Curate Data

  *  Advanced ,menu

    * API Documentation
    * Contact
    * Help
"""

from django.urls import reverse
from ammd.settings import EXPLORE_EXAMPLE_MENU_NAME, EXPLORE_MENU_NAME, \
    EXPLORE_TREE_MENU_NAME, VISUALIZATION_USER_MENU_NAME, CURATE_MENU_NAME, SCHEMA_VIEWER_MENU_NAME, \
    VISUALIZATION_INSITU_USER_MENU_NAME

from menu import Menu, MenuItem

Menu.items["main"] = []
Menu.add_item(
    "main", MenuItem("Home", reverse("core_main_app_homepage"), icon="home", weight=-1000)
)
Menu.add_item(
    "main", MenuItem(EXPLORE_TREE_MENU_NAME, reverse("core_explore_tree_index"))
)
Menu.add_item(
    "main", MenuItem(SCHEMA_VIEWER_MENU_NAME, reverse("core_schema_viewer_index"))
)
Menu.add_item(
    "main", MenuItem(CURATE_MENU_NAME, reverse("core_curate_index"))
)
Menu.add_item(
    "main", MenuItem(EXPLORE_MENU_NAME, reverse("core_explore_keyword_app_search"))
)

Menu.add_item(
    "advanced", MenuItem(EXPLORE_EXAMPLE_MENU_NAME, reverse("core_explore_example_index"))
)
Menu.add_item(
    "advanced", MenuItem(VISUALIZATION_USER_MENU_NAME, reverse("core_visualization_index"))
)
Menu.add_item(
    "admin", MenuItem("VISITS COUNTER", reverse("get_visits_number"), icon="tachometer-alt")
)
Menu.add_item(
    "advanced", MenuItem(VISUALIZATION_INSITU_USER_MENU_NAME, reverse("core_visualization_insitu_index"))
)
