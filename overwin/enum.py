from enum import Enum
from typing import Any, Type, TypeVar
from django.utils.translation import gettext_lazy as _

TBaseEnum = TypeVar("TBaseEnum", bound="BaseEnum")


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.value, x.name) for x in cls]

class KeyLabelEnum(BaseEnum):
    def __init__(self, key, label):
        self._key = key
        self._label = label

    @property
    def key(self):
        return self._key

    @property
    def label(self):
        return self._label

    @classmethod
    def choices(cls):
        return [(e.key, e.label) for e in cls]

class Role(KeyLabelEnum):
    TANK = ("tank", "タンク")
    DAMAGE = ("damage", "ダメージ")
    SUPPORT = ("support", "サポート")