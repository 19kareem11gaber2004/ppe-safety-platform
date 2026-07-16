from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    SAFETY_OFFICER = "safety_officer"
    VIEWER = "viewer"