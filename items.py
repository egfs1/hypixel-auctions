from enum import Enum


class Item:
    def __init__(self, name, stars, tier, price, enchantments=[], lock_stars=False, lock_tier=False):
        self.name = name
        self.stars = stars
        self.tier = tier
        self.price = price
        self.enchantments = enchantments
        self.lock_stars = lock_stars
        self.lock_tier = lock_tier


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


class Color(Enum):
    COMMON = ""
    UNCOMMON = "\033[1;32m"
    RARE = "\033[1;34m"
    EPIC = "\033[0;35m"
    LEGENDARY = "\033[1;33m"
    MYTHIC = "\033[1;35m"
    DIVINE = "\033[1;36m"
    SPECIAL = "\033[1;31m"
    VERY_SPECIAL = "\033[1;31m"


def get_color_code(tier):
    return {
        Tier.COMMON: Color.COMMON,
        Tier.UNCOMMON: Color.UNCOMMON,
        Tier.RARE: Color.RARE,
        Tier.EPIC: Color.EPIC,
        Tier.LEGENDARY: Color.LEGENDARY,
        Tier.MYTHIC: Color.MYTHIC,
        Tier.SPECIAL: Color.SPECIAL,
        Tier.VERY_SPECIAL: Color.VERY_SPECIAL,
    }[tier].value


items = [
    Item(name = "Ancient Shadow Assassin Leggings", stars = 4, tier = Tier.LEGENDARY, price = 4500000),
    Item(name = "Necrotic Wise Dragon Leg", stars = 0, tier = Tier.LEGENDARY, price = 1600000),
]
