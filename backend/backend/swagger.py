from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Kismat API",
        default_version='v1',
        description="API documentation for the Kismat application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@kismat.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

# This adds JWT authentication support to Swagger UI
swagger_ui_settings = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False
}
