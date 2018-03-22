from django.conf.urls import url
from django_filters.views import FilterView
from .models import Partner
from .filters import PartnerFilter

from . import views

urlpatterns = [
    url(r'^$', 
        views.PartnersListView.as_view(),
        name='list'
    ),
    url(r'^(?P<pk>\d+)/$',
        views.PartnersDetailView.as_view(),
        name='detail'
    ),
    url(r'^toggle_waitlist/(?P<pk>\d+)/$',
        views.PartnersToggleWaitlistView.as_view(),
        name='toggle_waitlist'
    ),
    url(r'^filter/$',
        views.PartnersFilterView.as_view(filterset_class=PartnerFilter),
        #FilterView.as_view(filterset_class=PartnerFilter),
        name='filter'
    ),
]
