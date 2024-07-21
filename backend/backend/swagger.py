from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Kismat API",
        default_version='v1',
        description="API documentation for the Kismat application",
        terms_of_service="http://kismat.pro:3000/policies/terms/",
        contact=openapi.Contact(email="contact@kismat.pro"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
