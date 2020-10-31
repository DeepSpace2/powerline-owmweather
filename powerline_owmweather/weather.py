
import json
import urllib.parse
import time

from functools import lru_cache

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


@lru_cache()
def _weather(pl, *, openweathermap_api_key, location_query=None, units='C', temp_format='{temp:.0f}', **kwargs):
    if not location_query:
        location_data = json.loads(urllib_read('https://ipapi.co/json'))
        location_query = '{}, {}'.format(location_data['city'], location_data['country_code'])

    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(urllib.parse.quote(location_query), temp_units_names.get(units, 'metric'), openweathermap_api_key)
    raw_response = urllib_read(weather_url)
    # print(raw_response)
    if not raw_response:
        pl.error('Failed to get response')
        return None

    response = json.loads(raw_response)
    try:
        condition = response['weather'][0]['main'].lower()
        # condition_code = int(condition['code'])
        # condition_code = 0
        temp = float(response['main']['temp'])
    except (KeyError, ValueError):
        pl.error('openweathermap returned malformed or unexpected response: {0}', repr(raw_response))
        return None
    
    return [
            {
                'contents': temp_format.format(temp=temp) + temp_units_representation[units],
                'highlight_groups': ['wearher_temp_gradient', 'weather_temp', 'weather'],
                'divider_highlight_group': 'background:divider'
            }
    ]

def weather(*args, **kwargs):
    return _weather(*args, ttl_in_minutes=time.time() // (kwargs.get('ttl_in_minutes', 60) * 60), **kwargs)