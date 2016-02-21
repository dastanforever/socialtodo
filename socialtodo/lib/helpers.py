# -*- coding: utf-8 -*-

"""WebHelpers used in socialtodo2."""

from webhelpers import date, feedgenerator, html, number, misc, text
from datetime import datetime
import inspect

def current_year():
  now = datetime.now()
  return now.strftime('%Y')

def icon(icon_name, white=False):
    if (white):
        return html.literal('<i class="icon-%s icon-white"></i>' % icon_name)
    else:
        return html.literal('<i class="icon-%s"></i>' % icon_name)

def makedict(obj):
    userid = obj['_id']
    li = filter(lambda a: not a.startswith('__'), dir(obj))
    li = filter(lambda a: not a.startswith('_'), dir(obj))
    li.remove('query')
    li.remove('password')
    d = dict()

    for x in li:
        if inspect.ismethod(obj[x]) == False:
            d[x] = obj[x]
    d['_id'] = userid
    return d