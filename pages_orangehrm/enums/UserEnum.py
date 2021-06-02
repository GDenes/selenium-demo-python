from enum import Enum


class UserEnum(Enum):
    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, usr, pasw):
        self.user_name = usr
        self.password = pasw

    SYSTEM_ADMIN = '_ohrmSysAdmin_', 'sysadmin'
    ESS_USER = 'linda', 'linda.anderson'
