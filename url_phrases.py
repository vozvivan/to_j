#!/usr/bin/python3.5m
try:
	from urllib.parse import urlparse
except ImportError:
	from urlparse import urlparse


with open('/home/ivan/Загрузки/taxi/url_popup', 'r', encoding='utf-8') as urls, \
     open('/home/ivan/Загрузки/taxi/taxi_popups', 'w') as patterns:
	for url in urls:
		url = url.split()		
		if not url:
			continue
		parsed_uri = urlparse(url[0])
		strin = ''		
		try:	
			strin = parsed_uri.netloc[parsed_uri.netloc.index('www.')+4:]
		except ValueError:
			strin = parsed_uri.netloc
		patterns.write('{} @ #phrases\n'.format(strin))

