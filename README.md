![PyPI](https://img.shields.io/pypi/v/powerline-owmweather?color=blue&logo=python&logoColor=green&style=plastic)
[![Downloads](https://static.pepy.tech/personalized-badge/powerline-owmweather?period=week&units=international_system&left_color=black&right_color=blue&left_text=Downloads/Week)](https://pepy.tech/project/powerline-owmweather)
# powerline_owmweather 🌦

A light-hearted Powerline segment for fetching and showing the weather in the current location (either by IP geolocation or by setting a location, see [Configuration](#configuration) below).

**Keep in mind that powerline_owmweather is in early, rapid development stage so its API/configuration format may change.**

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
 
The very minimum required to activate the segment is to add the following to your theme JSON:
 
```
{
   "function": "powerline_owmweather.weather",
   "args": {
       "openweathermap_api_key": API_KEY
   }
}
```
 
and the following to your colorscheme JSON (the colors can be customized):
 
```
"groups": {
      ...,
      "owmweather": {
          "fg": "gray9",
          "bg": "gray2",
          "attrs": []
    }
}
```
 
## Configuration
 
The following optional `args` are available:
 
| Argument | Type | Description | Default
| --- | --- | --- | --- |
| `condition_as_icon` | boolean | If `true`, condition will be displayed as an icon (if one of known conditions).<br>If `false` condition will be displayed as a string | `true` |
| `location_query` | string | Location in format CITY, 2-LETTERS-COUNTRY-CODE | Retrived using IP geolocation | 
| `show `| string | Comma-separated string specifies what data to show.<br>Can include `"condition"`, `"temp"` | `"temp"` |
| `temp_format` | string | A Python format string that accepts `temp` as an argument | `"{temp:.0f}"` |
| `ttl_in_minutes` | integer | Time in minutes for which location and weather are cached.<br>**Warning: The lower the value the slower your terminal will be** | 60 |
| `units` | string | Temperature units.<br>Should be one of `"C"`, `"F"`, `"K"` | `"C"` |

## Changelog

### 0.2 - Nov. 1 2020
* Added ability to display temperature, condition and different combinations
* Added ability to display condition as either icons or strings

### 0.1.1 - Oct. 31 2020
* Fixed a bug that prevented setting a custom `ttl_in_minutes`
* Added debug logs

### 0.1.0 - Oct. 31 2020
Initial release

## TODO

 - [x] Support icons
 - [x] Support weather description ("cloudy", "windy", etc)
 - [ ] Support configurable information to display:
   - [x] Temperature
   - [x] Condition
   - [ ] Wind speed/direction
   - [ ] Humidity
   - [ ] Pressure
