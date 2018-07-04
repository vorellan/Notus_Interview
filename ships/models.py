# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import CASCADE,  CharField, DateTimeField, DateField, ForeignKey, IntegerField, Model


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_at']


class Ship(BaseModel):
    name = CharField(max_length=10, help_text="The ship's name")
    capacity = IntegerField(help_text="The capacity of the ship.")


class Terminal(BaseModel):
    name = CharField(max_length=10, help_text="The name of the terminal")
    capacity = IntegerField(help_text="The capacity of the terminal.")
    initial = IntegerField(help_text="The initial capacity contained in the terminal")


class Demand(BaseModel):
    terminal = ForeignKey('Terminal', on_delete=CASCADE, db_index=True)
    date = DateField()
    demand = IntegerField()


class Unload(BaseModel):
    ship = ForeignKey(Ship, on_delete=CASCADE, db_index=True)
    terminal = ForeignKey(Terminal, on_delete=CASCADE, db_index=True)
    date = DateField()
    quantity = IntegerField()
