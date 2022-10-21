"""
Filename    : ReturnStatus.py
Description : Collection of IntEnums that contain the status codes
"""

from enum import IntEnum

class codes(IntEnum):
    SUCCESS = 1
    NOT_EXISTS = 2
    EXISTS = 3
    EMPTY_NAME = 4
    INVALID = 5

class methods(IntEnum):
    ADD = 10
    DELETE = 20
    RENAME = 30
    CHANGE = 40