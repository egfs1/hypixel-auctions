from enum import Enum

class Tier(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
    MYTHIC = 6
    DIVINE = 7
    SPECIAL = 8
    VERY_SPECIAL = 9

def get_tier_color(tier_str):
    match Tier[tier_str]:
        case Tier.COMMON:
            return ""
        case Tier.UNCOMMON:
            return "\033[1;32m"
        case Tier.RARE:
            return "\033[1;34m"
        case Tier.EPIC:
            return "\033[0;35m"
        case Tier.LEGENDARY:
            return "\033[1;33m"
        case Tier.MYTHIC:
            return "\033[1;35m"
        case Tier.DIVINE:
            return "\033[1;36m"
        case Tier.SPECIAL:
            return "\033[1;31m"
        case Tier.VERY_SPECIAL:
            return "\033[1;31m"