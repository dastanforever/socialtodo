############################################################
##
##  The model of a to do list item.
##
##
##
############################################################

import ming
from session import DBSession
from ming import schema
from ming.odm import MappedClass
from ming.odm import FieldProperty, ForeignIdProperty, RelationProperty
import bcrypt, datetime

class toDoItem(MappedClass):
    """docstring for toDoItem
        Indexing fields -
        1. id, title
        2. id
        3. id, starttime
        4. id, endtime.
    """

    class __mongometa__:
        session = DBSession
        name = "todo"
        indexes = [
                ( 'creator_id', ('todoStartDateTime', ming.ASCENDING)),
                ( 'title'),
                ]

    _id = FieldProperty(schema.ObjectId)
    creator_id = FieldProperty(schema.ObjectId)
    parent_id = FieldProperty(schema.ObjectId)
    is_root = FieldProperty(schema.Bool)
    title = FieldProperty(schema.String)
    description = FieldProperty(schema.String)

    typeoftodo = FieldProperty(schema.String)   # 'organizational', 'user'
    name = FieldProperty(schema.String)

    requestedto = FieldProperty(schema.ObjectId)#  First a user reuests. If accepted then assigned.
    assignedto = FieldProperty(schema.ObjectId) #  If None, then delete todo.


    dateTimeCreated = FieldProperty(schema.DateTime)
    todoStartDateTime = FieldProperty(schema.DateTime)
    todoEndDateTime = FieldProperty(schema.DateTime)
    priority = FieldProperty(schema.Int)

    creator = RelationProperty('User')

    def register_todo(self, doc):
        self.username = doc['username']
        self.title = doc['title']
        self.description = doc['description']
        self.dateTimeCreated = datetime.datetime.now()
        self.set_time(doc['todoStartDateTime'], doc['todoEndDateTime'])
        self.priority = doc['priority']


    def set_time(self, todoStartDateTime, todoEndDateTime):
        ####### various Modifications to be made.
        self.todoStartDateTime = todoStartDateTime
        self.todoEndDateTime = todoEndDateTime
