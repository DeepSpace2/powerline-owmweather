from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name         = 'powerline-owmweather',
    description  = 'A Powerline segment for fetching and showing the weather in the current location',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    version      = '0.5',
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
