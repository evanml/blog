import django_filters
from .models import Photo

class PhotoFilter(django_filters.FilterSet):
    gallery = django_filters.AllValuesFilter(field_name='gallery__title', label='Gallery', widget=django_filters.widgets.LinkWidget())


    class Meta:
        model = Photo
        fields = ['gallery']
