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
from django.conf.urls import url, include
from django.contrib import admin

from core_parser_app.tools.modules.discover import discover_modules

urlpatterns = [
    url(r'^', include("core_main_app.urls")),
    url(r'^', include("core_website_app.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^curate/', include("core_curate_app.urls")),
    url(r'^parser/', include("core_parser_app.urls")),
    url(r'^dashboard/', include("core_dashboard_app.urls")),
    url(r'^query-ontology/', include("core_explore_tree_app.urls")),
    url(r'^schema_viewer/', include("core_schema_viewer_app.urls")),
    url(r'^visualization/', include("core_visualization_app.urls")),
    url(r'^core-explore-common/', include("core_explore_common_app.urls")),
    url(r'^core-explore-example/', include("core_explore_example_app.urls")),
    url(r'^core-explore-keyword/', include("core_explore_keyword_app.urls")),
    url(r'^', include('core_module_blob_host_app.urls')),
    url(r'^', include('core_module_advanced_blob_host_app.urls')),
    url(r'^', include('core_module_remote_blob_host_app.urls')),
]
discover_modules(urlpatterns)