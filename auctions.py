import pyperclip
import winsound
import time
import locale
from items import items, Tier, get_color_code

VALIDATED_AUCTIONS = set()
CONSOLE_DEFAULT_COLOR = "\033[0m"
STAR_CHAR = "✪"
locale.setlocale(locale.LC_ALL, 'de_DE')


def validate_and_print_auction(auction):
    if not auction["bin"] or auction["claimed"] or is_already_validated(auction):
        return
    
    VALIDATED_AUCTIONS.add(auction["uuid"])

    for item in items:
        if item.name not in auction["item_name"]:
            continue

        if not has_required_attributes(item, auction):
            continue

        if not has_required_enchantments(item, auction):
            continue

        print_auction(auction, get_color_code(Tier[auction["tier"]]))


def is_already_validated(auction):
    return auction["uuid"] in VALIDATED_AUCTIONS


def has_required_attributes(item, auction):
    stars_count = auction["item_name"].count(STAR_CHAR)

    # Check if the item has the required star count
    if not check_item_attribute(item.stars, stars_count, item.lock_stars):
        return False
    
    # Check if the item has the required tier
    if not check_item_attribute(item.tier.value, Tier[auction["tier"]].value, item.lock_tier):
        return False
    
    # Check if the item has the required level
    if item.level > 0:
        if "Lvl" in auction["item_name"]:
            auction_level = int(auction["item_name"].split("]")[0].split("[Lvl ")[1])
            if not check_item_attribute(item.level, auction_level, item.lock_level):
                return False
        else:
            return False
    
    # Check if the item has the required price
    if item.price < int(auction["starting_bid"]):
        return False
    
    return True


def check_item_attribute(item_attr, auction_attr, lock_attr):
    if lock_attr:
        if item_attr != auction_attr:
            return False
    else:
        if item_attr > auction_attr:
            return False
    return True


def has_required_enchantments(item, auction):
    return all(enchantment in auction["item_lore"] for enchantment in item.enchantments)


def print_auction(auction, color_code):
    print(color_code)
    print(color_code + auction["item_name"])
    print(auction["tier"] + CONSOLE_DEFAULT_COLOR)
    print(locale.format_string("%d", auction["starting_bid"], grouping=True))
    print(f"viewauction {auction['uuid']}")
    print(time.strftime('%H:%M:%S', time.localtime()))
    print("")

    pyperclip.copy(f"viewauction {auction['uuid']}")
    winsound.Beep(1000, 1000)