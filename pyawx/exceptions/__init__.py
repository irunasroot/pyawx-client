"""
exceptions/__init__.py
Comments: 
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2021, iRunAsRoot
"""


class ValueReadOnly(Exception):
    pass


class ValueNotAllowed(Exception):
    pass


class UnauthorizedAccess(Exception):
    pass


class UnknownEndpoint(Exception):
    pass
