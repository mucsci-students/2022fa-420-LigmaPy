"""
Filename    : ReturnStatus.py
Description : Collection of IntEnums that contain the status codes
"""

from enum import IntEnum

class codes(IntEnum):
    """ ADD CLASS """
    ADDED_CLASS = 111 #---------------Successfully added class
    ADD_EXISTING_CLASS = 112 #--------Attempted to add an already existing class
    ADD_EMPTY_CLASS = 113 #-----------Class name given was empty
    """ DELETE CLASS """
    DELETED_CLASS = 121 #-------------Successfully deleted class
    DELETE_NOT_EXISTING_CLASS = 122 #-Attempted to delete a class that does not exist
    """ RENAME CLASS """
    RENAMED_CLASS = 131 #-------------Successfully renamed class
    RENAME_CLASS_NOT_EXIST = 132 #----Attempted to change the name of a class that does not exist
    RENAME_NEW_CLASS_EXIST = 133 #----Attempted to change classes name to one that already exists
    RENAME_CLASS_EMPTY = 134 #--------Attempted to change class name to be empty
    
    """ ADD RELATIONSHIP """
    ADDED_RELATIONSHIP = 211 #--------Successfully added a new relationship
    ADD_SRC_NOT_EXIST = 212 #---------The given source class does not exist
    ADD_DEST_NOT_EXIST = 213 #--------The given destination class does not exist
    ADD_INVALID_TYPE = 214 #----------An invalid type was given
    """ DELETE RELATIONSHIP """
    DELETED_RELATIONSHIP = 221 #--------------Successfully deleted the relationship
    DELETE_NOT_EXISTING_RELATIONSHIP = 222 #--Attempted to delete a relationship that does not exist
    DELETE_NOT_EXISTING_SRC = 223 #-----------Source class does not exist
    DELETE_NOT_EXISTING_DEST = 224 #----------Destination class does not exist

    """ ADD METHOD """
    ADDED_METHOD = 311 #--------------Successfully added method to a class
    ADD_NOT_EXISTING_CLASS = 312 #----Attempted to add method to a class that does not exist
    ADD_EXISTING_METHOD = 313 #-------Attempted to add a method that already exists
    """ DELETE METHOD """
    DELETED_METHOD = 321 #--------------------Successfully deleted method from class
    DELETE_METHOD_NOT_EXISTING_CLASS = 322 #--Attempted to delete a method in a non-existing class
    DELETE_NOT_EXISTING_METHOD = 323 #--------Attempted to delete a method that does not exist
    """ RENAME METHOD """
    RENAMED_METHOD = 331 #--------------------Successfully renamed the method
    RENAME_METHOD_CLASS_NOT_EXIST = 332 #-----Attempted to rename a method in a class that does not exist
    RENAME_METHOD_METHOD_NOT_EXIST = 333 #----Attempted to rename a method that does not exist
    RENAME_METHOD_NEW_EXISTS = 334 #----------Attempted to change the method's name to one that already exists

    """ ADD FIELD """
    ADDED_FIELD = 411 #-------------------Successfully added field to a class
    ADD_FIELD_NOT_EXISTING_CLASS = 412 #--Attempted to add a field to a class that does not exist
    ADD_EXISTING_FIELD = 413 #------------Attempted to add a field that already exists 
    """ DELETE FIELD """
    DELETED_FIELD = 421 #---------------------Successfully deleted the field in the class
    DELETE_FIELD_NOT_EXISTING_CLASS = 422 #---Attempted to delete a field in a class that does not exist
    DELETE_FIELD_NOT_EXISTING_FIELD = 423 #---Attempted to delete a field that does not exist
    """ RENAME FIELD """
    RENAMED_FIELD = 431 #-----------------Successfully renamed field
    RENAME_FIELD_CLASS_NOT_EXIST = 432 #--Attempted to rename field in a class that does not exist
    RENAME_FIELD_FIELD_NOT_EXIST = 433 #--Attempted to rename a field that does not exist
    RENAME_FIELD_NEW_EXISTS = 434 #-------Attempted to change the name of a field to one that already exists

    """ ADD PARAMETER(S) """
    ADDED_PARAM = 511 #-------------------Successfully added parameters to a method
    ADD_PARAM_CLASS_NOT_EXIST = 512 #-----Attempted to add parameters to a non-existing class
    ADD_PARAM_METHOD_NOT_EXIST = 513 #----Attempted to add parameter(s) to a method that does not exist
    ADD_PARAM_ALREADY_EXISTS = 514 #------Attempted to add parameter(s) that already exist
    """ DELETE PARAMETER(S) """
    DELETED_PARAM = 521 #-----------------Successfully deleted parameters
    DELETE_PARAM_CLASS_NOT_EXIST = 522 #--Attempted to delete parameter(s) from a class that does not exist
    DELETE_PARAM_METHOD_NOT_EXIST = 523 #-Attemted to delete parameter(s) in a method that does not exist
    DELETE_PARAM_NOT_EXIST = 524 #--------Attempted to delete parameter(s) that do not exist
    """ CHANGE PARAMETER(S) """
    CHANGED_PARAM = 531 #-----------------Successfully changed parameter(s)
    CHANGE_PARAM_CLASS_NOT_EXIST = 532 #--Attempted to change parameter(s) in a class that does not exist
    CHANGE_PARAM_METHOD_NOT_EXIST = 533 #-Attempted to change parameter(s) in a method that does not exist
    CHANGE_PARAM_ALREADY_EXISTS = 534 #---Attempted to change parameter(s) to ones that already exist