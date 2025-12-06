# app/models/__init__.py

from .asset import Asset
from .custom_user import CustomUser
from .request import Request, RequestImage, URGENCY_LEVELS, DEPARTAMENTS  # Incluindo URGENCY_LEVELS
from .status import Status, STATUS

__all__ = [
    "Asset",
    "CustomUser",
    "Request",
    "RequestImage",
    "Status",
    "STATUS",    
    "URGENCY_LEVELS",
    "DEPARTAMENTS"
]
