#!/usr/bin/env python
#
# Hacker News Droid API: returns nested comments for a given post id in JSON or XML using HTML Parser
#

import os
from google.appengine.ext import webapp
import Formatter
import GAHelper
import APIContent


class HackerNewsNestedCommentsHandler(webapp.RequestHandler):

    #controller main entry
    def get(self, format, id):
        #set content-type
        self.response.headers['Content-Type'] = Formatter.contentType(format)

        referer = ''
        if ('HTTP_REFERER' in os.environ):
            referer = os.environ['HTTP_REFERER']

        returnData = APIContent.getHackerNewsNestedComments(id, format, self.request.url, referer, self.request.remote_addr)

        #track this request
        GAHelper.trackGARequests('/nestedcomments/%s' % (id), self.request.remote_addr, referer)

        if (not returnData):
            returnData = ''

        #output to the browser
        self.response.out.write(Formatter.dataWrapper(format, returnData, self.request.get('callback')))
