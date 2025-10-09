from .user import UserView           
from .asset import AssetView
from .request import RequestView 
from .status import StatusView
from .dashboard import StatusDashboardView
from .ticketsByDepartament import TicketsByDepartamentView

__all__ = [
    "UserView",
    "AssetView",
    "RequestView",
    "StatusView",
    "StatusDashboardView",
    "TicketsByDepartamentView",
]
