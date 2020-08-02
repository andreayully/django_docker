from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import EquipoCreateView, EquipoDetailView

urlpatterns = {
    path('equipo/', EquipoCreateView.as_view(), name="create"),
    path('equipo/<int:pk>/', EquipoDetailView.as_view(), name="details"),

}
urlpatterns = format_suffix_patterns(urlpatterns)
