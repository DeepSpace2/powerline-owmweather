![PyPI](https://img.shields.io/pypi/v/powerline-owmweather?color=blue&logo=python&logoColor=green&style=plastic)
[![Downloads](https://static.pepy.tech/personalized-badge/powerline-owmweather?period=week&units=international_system&left_color=black&right_color=blue&left_text=Downloads/Week)](https://pepy.tech/project/powerline-owmweather)
# powerline_owmweather 🌦

A light-hearted Powerline segment for fetching and showing the weather in the current location (either by IP geolocation or by setting a location, see [Configuration](#configuration) below)

- [Motivation](#motivation)
- [Requirements](#requirements)
- [Installation](#installation)
- [Activiation](#activiation)
- [Configuration](#configuration)
- [Changelog](#changelog)
- [TODO](#todo)

## Motivation

The built-in weather segment is using Yahoo Weather API which is no longer available so I decided to create an almost drop-in replacement using [OpenWeather](https://openweathermap.org/).

## Requirements

 - [Powerline](https://github.com/powerline/powerline)
 - A (free) [OpenWeather](https://openweathermap.org/) account and API key with the "Current Weather Data" plan enabled.
 
 ## Installation
 
 ```
 pip install powerline-owmweather
 ```
 
 ## Activiation
 
 The very minimum required to activate the segment is to add the following to `.config/powerline/themes/shell/default.json`:
 
 ```
 {
    "function": "powerline_owmweather.weather",
    "args": {
        "openweathermap_api_key": API_KEY
    }
 }
 ```
 
 ## Configuration
 
 The following optional `args` are available:
 
| Argument | Type | Description | Default
| --- | --- | --- | --- |
| `location_query` | string | Location in format CITY, 2-LETTERS-COUNTRY-CODE | Retrived using IP geolocation | 
| `units` | string | Temperature units, should be one of `"C"`, `"F"`, `"K"` | `"C"` |
| `temp_format` | string | A Python format string that accepts `temp` as an argument | `"{temp:.0f}"` |
| `ttl_in_minutes` | integer | Time in minutes for which location and weather are cached. <br>**Warning: The lower the value the slower your terminal will be** | 60 |

The highlight group used is `weather_temp`.

## Changelog

### 0.1.1 - Oct. 31 2020
* Fixed a bug that prevented setting a custom `ttl_in_minutes`
* Added debug logs

### 0.1.0 - Oct. 31 2020
Initial release

## TODO

 - [ ] Support icons (?)
 - [ ] Support weather description ("cloudy", "windy", etc)
