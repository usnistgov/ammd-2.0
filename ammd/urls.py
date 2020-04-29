"""ammd URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin

from core_parser_app.tools.modules.discover import discover_modules
from ammd.views.admin import views as admin_views

urlpatterns = [
    re_path(r'^', include("core_main_app.urls")),
    re_path(r'^', include("core_website_app.urls")),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^curate/', include("core_curate_app.urls")),
    re_path(r'^parser/', include("core_parser_app.urls")),
    re_path(r'^dashboard/', include("core_dashboard_app.urls")),
    re_path(r'^query-ontology/', include("core_explore_tree_app.urls")),
    re_path(r'^schema_viewer/', include("core_schema_viewer_app.urls")),
    re_path(r'^visualization/', include("core_visualization_app.urls")),
    re_path(r'^core-explore-common/', include("core_explore_common_app.urls")),
    re_path(r'^core-explore-example/', include("core_explore_example_app.urls")),
    re_path(r'^core-explore-keyword/', include("core_explore_keyword_app.urls")),
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^file-preview/', include("core_file_preview_app.urls")),
    re_path(r'^federated/search/', include("core_federated_search_app.urls")),
    re_path(r'^federated_search/', include("core_explore_federated_search_app.urls")),
    re_path(r'^', include('core_module_blob_host_app.urls')),
    re_path(r'^', include('core_module_advanced_blob_host_app.urls')),
    re_path(r'^', include('core_module_remote_blob_host_app.urls')),
    re_path(r'^visits-hits/$', admin_views.get_visits_number, name='get_visits_number'),
]
discover_modules(urlpatterns)
