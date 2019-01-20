from django.core.management.base import BaseCommand
from django.utils import timezone
import requests

class Command(BaseCommand):
    help = 'Get Data from s3'

    def handle(self, *args, **kwargs):
        locations = ['UK', 'England', 'Scotland', 'Wales']
        weather = ['Rainfall', 'Tamx', 'Tmin']
        for l in locations:
            for w in weather:
                s3_data = requests.get('https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{}-{}.json'.format(w, l))
                for row in s3_data.json():
                    data = {
                        'value': row.get('value'),
                        'date': '{}-{}-1'.format(row.get('year'), row.get('month')),
                        'location':l,
                        'wtype': w
                        }
                    requests.post('http://127.0.0.1:8000/api/', json=data)
