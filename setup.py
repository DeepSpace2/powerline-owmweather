from setuptools import setup

setup(
    name         = 'powerline-owmweather',
    description  = 'A Powerline segment for fetching and showing the weather in the current location',
    version      = '0.1.0',
    keywords     = 'powerline weather segment terminal cli',
    license      = 'MIT',
    author       = 'DeepSpace2',
    author_email = 'deepspace2@gmail.com',
    url          = 'https://github.com/DeepSpace2/powerline-owmweather',
    packages     = ['powerline_owmweather'],
    classifiers  = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)