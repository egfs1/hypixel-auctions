from tier import Tier

class Item:
    def __init__(self, name, price, tier, stars=0, enchantments=[], level=0, lock_tier=False, lock_stars=False, lock_level=False):
        self.name = name
        self.price = price
        self.tier = tier
        self.stars = stars
        self.enchantments = enchantments
        self.level = level
        self.lock_tier = lock_tier
        self.lock_stars = lock_stars
        self.lock_level = lock_level


items = []