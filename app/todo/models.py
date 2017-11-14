# -*- coding: utf-8 -*-
"""todo models."""
import datetime as dt

from app.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Todo(Model):
    """A todo for a user"""
    __tablename__ = 'todo'
    todoname = Column(db.String(80), nullable=False)
    content = Column(db.String(200), nullable=False)
    is_done = Column(db.Boolean(), default=False)
    is_delete = Column(db.Boolean(), default=False)
    create_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow())

    def __init__(self, todoname, content, **kwargs):
        """create instance."""
        db.Model.__init__(self, todoname=todoname, content=content, **kwargs)

    def __repr__(self):
        return '<TODO({0})>'.format(self.todoname)







