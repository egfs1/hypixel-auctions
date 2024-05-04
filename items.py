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


class Item:
    def __init__(self, name, stars, tier, price, enchantments=[], lock_stars=False, lock_tier=False):
        self.name = name
        self.stars = stars
        self.tier = tier
        self.price = price
        self.enchantments = enchantments
        self.lock_stars = lock_stars
        self.lock_tier = lock_tier

    def get_color_code(self):
        match self.tier:
            case Tier.COMMON:
                return ""

            case Tier.UNCOMMON:
                return "\033[1;32m"

            case Tier.RARE:
                return "\033[1;34m"

            case Tier.EPIC:
                return "\033[1;35m"

            case Tier.LEGENDARY:
                return "\033[1;33m"

            case Tier.MYTHIC:
                return "\033[1;35m"

            case Tier.DIVINE:
                return "\033[1;36m"

            case Tier.SPECIAL, Tier.VERY_SPECIAL:
                return "\033[1;31m"


items = [
    Item(name = "Ancient Shadow Assassin Leggings", stars = 4, tier = Tier.LEGENDARY, price = 4500000),
    Item(name = "Necrotic Wise Dragon Leg", stars = 0, tier = Tier.LEGENDARY, price = 1600000),
]
