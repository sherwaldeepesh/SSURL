from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'ssurl.hostsconf.urls', name='wildcard'),
)


'''
from ssurl.hostsconf import urls as redirect_urls
host_patters = [
    host(r'www', settings.ROOT_URLCONF, name='www),
    host(r'(?!www).*, redirect_urls, name= 'wildcard'),
]
'''