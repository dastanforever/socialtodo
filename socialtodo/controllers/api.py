

from socialtodo.lib.base import BaseController
from socialtodo.model.auth import User as U
from tg import expose
from socialtodo.lib import helpers
import json

class ApiController(BaseController):
    
#    @expose('json')
#    def get_friends(self):

#    @export('json')
#    def get_todo(self):

    @expose('json')
    def get_user_info(self, **kw):
        res = 'None'
        if 'username' in kw:
            q = kw['username'].encode('ascii', 'ignore')
            if U.query.find({'username':q}).count() > 0:
                res = U.query.find({'username':q}).first()
        return dict(userinfo=helpers.makedict(res))



#    @expose('json')
#    def get_schedule(self):
