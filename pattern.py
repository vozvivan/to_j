#!/usr/bin/python3.5m
try:
	from urllib.parse import urlparse
except ImportError:
	from urlparse import urlparse

from difflib import SequenceMatcher

a = 'ya.ru/str'
b = 'ya8.ru/int'

def merge(l, r):
	s = SequenceMatcher(None, l, r)
	for tag, i1, i2, j1, j2 in s.get_opcodes():
		if tag == 'equal':
			yield l[i1:i2]
		elif tag == 'delete':
			yield '(' + l[i1:i2] + '?)'
		elif tag == 'insert':
			yield '(' + r[j1:j2] + '?)'
		elif tag == 'replace':
			yield '(' + l[i1:i2] + '|' + r[j1:j2] + ')' 
merged = merge(a.split()[0], b.split()[0])
print(''.join(''.join(x) for x in merged))

s = SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
	print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
	         tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
	

with open('/home/ivan/Загрузки/taxi/urls', 'r', encoding='utf-8') as urls, \
     open('/home/ivan/Загрузки/taxi/pattern', 'w') as patterns:
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
		patterns.write('{} @ \'https?:://(www.?){}{}$\'\n'.format(strin, strin, parsed_uri.path[:-1]))
		print('\'{} @ https?:://(www.?){}{}$\''.format(strin, strin, parsed_uri.path[:-1]))

		
