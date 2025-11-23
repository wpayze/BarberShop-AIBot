from enum import Enum

# ---------------------------------------------
# User roles inside a business
# ---------------------------------------------
class UserRole(str, Enum):
    OWNER = "OWNER"
    MANAGER = "MANAGER"
    STAFF = "STAFF"

# ---------------------------------------------
# Booking status
# ---------------------------------------------
class BookingStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    NO_SHOW = "NO_SHOW"

# ---------------------------------------------
# Booking source (where it came from)
# ---------------------------------------------
class BookingSource(str, Enum):
    ONLINE = "ONLINE"
    ADMIN_PANEL = "ADMIN_PANEL"
    WHATSAPP = "WHATSAPP"
    PHONE = "PHONE"
