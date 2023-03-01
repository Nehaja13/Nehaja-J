#!/usr/bin/python3
"""
Certificates object model
"""
from app import models
from app.models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Certificate(BaseModel, Base):
    """
    Certificates Object representation
    """
    __tablename__ = 'certificates'
    student_name = Column(String(128), nullable=False)
    student_email = Column(String(128), nullable=False)
    school_name = Column(String(128), nullable=True)
    school_major = Column(String(128), nullable=True)
    school_department = Column(String(128), nullable=True)
    school_location = Column(String(128), nullable=True)
    certificate_verify = Column(Boolean, nullable=False, default=False)
    user_id = Column(String(60), ForeignKey('users.id'))
    school_id = Column(String(60), ForeignKey('schools.id'))

    def __init__(self, *args, **kwargs):
        """
        initializes Certificates
        """
        super().__init__(*args, **kwargs)