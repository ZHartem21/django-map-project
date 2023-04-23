# views.py
from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def index(request):
    all_places = Place.objects.all()
    places_prepared = {
        'type': 'FeatureCollection',
        'features': []
    }
    for place in all_places:
        place_feature = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lon, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.pk,
            'detailsUrl': f'places/{place.pk}'
          }
        }
        places_prepared['features'].append(place_feature)

    data = {'places': places_prepared}
    return render(request, 'index.html', context=data)


def place_details(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return JsonResponse({
                "title": place.title,
                "imgs": [image.image_file.url for image in Image.objects.filter(place=place).order_by('number')],
                "description_short": place.description_short,
                "description_long": place.description_long,
                "coordinates": {
                    "lng": place.lon,
                    "lat": place.lat
                }
            },
            safe=False,
            json_dumps_params={
                'ensure_ascii': False,
                'indent': 2
            })