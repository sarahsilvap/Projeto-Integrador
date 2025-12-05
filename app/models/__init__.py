# app/models/__init__.py

from .asset import Asset
from .custom_user import CustomUser
from .photo import Photo
from .request import Request, RequestImage, URGENCY_LEVELS, DEPARTAMENTS  # Incluindo URGENCY_LEVELS
from .status import Status

__all__ = [
    "Asset",
    "CustomUser",
    "Photo",
    "Request",
    "RequestImage",
    "Status",
    "URGENCY_LEVELS",  # Adicionando URGENCY_LEVELS
    "DEPARTAMENTS"
]
