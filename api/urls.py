from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import EquipoCreateView

urlpatterns = {
    path('equipo/', EquipoCreateView.as_view(), name="create"),

}
urlpatterns = format_suffix_patterns(urlpatterns)
