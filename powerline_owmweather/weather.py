import json
import urllib.parse
import time

from functools import lru_cache
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from powerline.lib.url import urllib_read, urllib_urlencode

temp_units_names = {
    'C': 'metric',
    'F': 'imperial',
    'K': 'standard'
}

temp_units_representation = {
        'C': '°C',
        'F': '°F',
        'K': 'K',
}

state = {'prev_location_query':  None}


def _fetch_location(pl):
    pl.debug('Fetching location')
    location_request = Request('https://ipapi.co/json', headers={'user-agent': 'curl/7.64.0'})
    try:
        location_response = urlopen(location_request, timeout=10).read().decode('utf-8')
        pl.debug('location response: {0}', location_response)
    except HTTPError as e:
        pl.error('Error fetching location: {0}', e)
        pl.debug('Using previous known location: {0}', state['prev_location_query'])
        location_query = state['prev_location_query']
    else:
        location_json = json.loads(location_response)
        location_query = '{}, {}'.format(location_json['city'], location_json['country_code'])
        state['prev_location_query'] = location_query
    return location_query


def _fetch_weather(pl, location_query, units, openweathermap_api_key):
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(urllib.parse.quote(location_query),
                                                                                                  temp_units_names.get(units, 'metric'),
                                                                                                  openweathermap_api_key)
    raw_response = urllib_read(weather_url)
    if not raw_response:
        pl.error('Failed to get response')
        return None
    pl.debug('weather response: {0}', raw_response)
    try:
        weather_json = json.loads(raw_response)
        return {
            'condition': weather_json['weather'][0]['main'].lower(),
            'temp': float(weather_json['main']['temp']) 
            }
    except (json.decoder.JSONDecodeError, KeyError, TypeError):
        pl.error('openweathermap returned malformed or unexpected response: {0}', raw_response)
        return None


@lru_cache()
def _weather(pl, *, openweathermap_api_key, location_query=None, units='C', temp_format='{temp:.0f}', ttl=None):
    pl.debug('_weather called with arguments {0}', locals())
    location_query = location_query or _fetch_location(pl)    
    pl.debug('Fetching weather for {0}', location_query)
    weather_dict = _fetch_weather(pl, location_query, units, openweathermap_api_key)
    if weather_dict:
        return [
                {
                    'contents': temp_format.format(temp=weather_dict['temp']) + temp_units_representation[units],
                    'highlight_groups': ['weather_temp'],
                    'divider_highlight_group': 'background:divider'
                }
        ]


def weather(*args, **kwargs):
    try:
        ttl_in_minutes = kwargs.pop('ttl_in_minutes')
    except KeyError:
        ttl_in_minutes = 60
    if ttl_in_minutes == 0:
        return _weather(*args, ttl=time.time(), **kwargs)
    return _weather(*args, ttl=time.time() // (ttl_in_minutes * 60), **kwargs)
