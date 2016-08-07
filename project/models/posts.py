# -*- coding: utf-8 -*-
from datetime import datetime

from project.extensions import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(), nullable=True, unique=True)
    body = db.Column(db.Unicode(), nullable=True, unique=True)
    active = db.Column(db.Boolean, default=False, nullable=False)
    last_modified = db.Column(db.DateTime, nullable=False, default=datetime.now())
    importance = db.Column(db.SmallInteger, nullable=False, default=0)