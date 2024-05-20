# Auctions Fetcher

This Python project fetches and processes auction data from the Hypixel Skyblock API. It continuously retrieves and validates auction data, providing real-time notifications for items meeting specified criteria.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Requirements

- Python 3

## Installation

**1. Clone the repository:**
```bash
git clone https://github.com/egfs1/hypixel-auctions-fetcher.git
cd hypixel-auctions-fetcher
```

**2. Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate.bat`
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

**1. Run the application:**
```bash
python main.py
```

**2. Stopping the application:**
- Press `Ctrl+C` to stop the program.

## Configuration

**1. Items list:** The list of items for which you want to receive notifications. Each `Item` has the following parameters:

- `name`: The substring of the item's name.
- `price`: The max price of the item.
- `tier`: The min tier of the item.
- `stars`: The min stars of the item. (`0` by default)
- `enchantments`: The list of enchantments of the item. (`[]` by default)
- `level`: The min level of a **Pet**. (`0` by default)
- `lock_tier`: Blocks the script to retrieve an item with higher `tier` than provided. (`False` by default)
- `lock_stars`: Blocks the script to retrieve an item with higher `stars` than provided. (`False` by default)
- `lock_level`: Blocks the script to retrieve an item with higher `level` than provided. (`False` by default)

```py
# items.py at line 16
items = [
    Item(name="Baby Yeti", price=30000000, tier=Tier.LEGENDARY, level=90),
]
```