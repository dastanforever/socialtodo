


from ming import schema
from ming.odm import MappedClass
from ming.odm import FieldProperty
from session import DBSession
import bcrypt
import datetime

class Notifications(MappedClass):
    
    class __mongometa__:        
        session = DBSession
        name = "notifications"
        indexes = [ ('_id'),
        ]

    _id = FieldProperty(schema.ObjectId)
    typeofnotif = FieldProperty(schema.String)
    by_id = FieldProperty(schema.ObjectId)
    for_id = FieldProperty(schema.ObjectId)
    notifstring = FieldProperty(schema.String)
    datemadeon = FieldProperty(schema.DateTime)

    def readynotif(self, typeofnotif, kw):
        self.by_id = kw['madebyid']
        self.for_id = kw['madeforid']
        self.datemadeon = datetime.datetime.now()

        if typeofnotif == 'friendrequest':
            self.typeofnotif = typeofnotif
            self.notifstring = """{fromuser} has sent you a 
friend request to exchange some todo's.""".format(fromuser=kw['madebyusername'])

        elif typeofnotif == 'friendrequestack':
            self.typeofnotif = typeofnotif
            self.notifstring = """{fromuser} has {status} your friend request.""".format(fromuser=kw['madebyusername'], status=kw['status'])

        elif typeofnotif == 'todorequest':
            self.typeofnotif = typeofnotif
            self.notifstring = """{fromuser} has asked you to do a todo {todotitle}, 
click to view details.""".format(fromuser=kw['madebyusername'], todotitle=kw['todotitle'])

        elif typeofnotif == 'todorequestack':
            self.typeofnotif = typeofnotif
            self.notifstring = """{fromuser} has {status} your todorequest titled {todotitle}.
""".format(fromuser=kw['madebyusername'], todotitle=kw['todotitle'], status=kw['status'])

        return self