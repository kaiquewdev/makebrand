# -*- coding: utf-8 -*-

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))
response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2011'

## your http://google.com/analytics id
response.google_analytics_id = None


response.menu = [
    (T('Home'), False, URL('default','index'), [])
    ]