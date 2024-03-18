from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticated
from Api.permisions import IsSuperUser

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="Document for blog api",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email='akromjonrustamov56@gmail.com')
    ),
    public=True,
    permission_classes = (IsAuthenticated, IsSuperUser),
)