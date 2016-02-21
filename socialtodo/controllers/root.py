# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_

from socialtodo.lib.base import BaseController
from socialtodo.controllers.api import ApiController
from socialtodo.controllers.auth import AuthController
from socialtodo.controllers.error import ErrorController
from socialtodo.model import auth
from socialtodo.model.auth import User as U

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the socialtodo2 application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    api = ApiController()
    auth = AuthController()
    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "socialtodo"


    @expose('socialtodo.templates.front')
    def index(self):
        return dict(page="home")

    @expose()
    def register(self, **kw):
        doc = {'username': kw["username"],
               'emailid': kw["emailid"],
               'password': kw["password"],
               }
        u = auth.User()
        u.register(doc)
        return u

    @expose()
    def login(self, **kw):
        res = auth.User.query.find({'username':kw['regusername']}).first()
        
        redirect('/auth/dashboard')

    @expose('socialtodo.templates.debug')
    def debug(self, **kw):
        #userdata = 1
        userdata = U.query.find().all()
        return dict(userdata=userdata)