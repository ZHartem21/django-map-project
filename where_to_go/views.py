# views.py
from django.shortcuts import render
from places.models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def index(request):
    all_places = Place.objects.all()
    features = []
    for place in all_places:
        details_url = reverse('place-name', args=(place.pk, ))
        place_feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lon, place.lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': details_url,
            }
        }
        features.append(place_feature)

    serialized_places = {
        'places': {
            'type': 'FeatureCollection',
            'features': features,
        }
    }
    return render(request, 'index.html', context=serialized_places)


def place_details(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return JsonResponse(
        {
            'title': place.title,
            'imgs': [image.image_file.url for image in place.images.all()],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lng': place.lon,
                'lat': place.lat,
            }
        },
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2,
        }
    )
