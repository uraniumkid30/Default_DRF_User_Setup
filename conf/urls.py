from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = "Custom Administration"

admin.autodiscover()
app = "applications."
urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"api/{settings.API_VERSION}/", include(f'{app}urls', namespace="apis")),
    path(f'api/{settings.API_VERSION}/schema/', SpectacularAPIView.as_view(), name='schema'),
    # # Optional UI:
    path(f'api/{settings.API_VERSION}/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name="schema"), name='swagger-ui'),
    path(f'api/{settings.API_VERSION}/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
