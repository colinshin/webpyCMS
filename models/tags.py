# -*- coding: utf-8 -*-
from peewee import CharField, SmallIntegerField, DateTimeField

from models.base import BaseModel
from datetime import datetime


class Tags(BaseModel):
    name = CharField()
    status = SmallIntegerField(default=0)
    createTime = DateTimeField(default=datetime.now)
    updateTime = DateTimeField(default=datetime.now)

