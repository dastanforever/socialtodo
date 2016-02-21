


from socialtodo.lib.base import BaseController
from tg import expose
from socialtodo.model import auth


class AuthController(BaseController):

    @expose('socialtodo.templates.index')
    def dashboard(self, **kw):
        return dict(page='index')

    @expose('socialtodo.templates.profile')
    def profile(self, username, **kw):
        return dict(username=username)