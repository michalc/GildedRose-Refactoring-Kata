# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                pass

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = \
                    0 if item.sell_in < 1 else \
                    item.quality + 3 if item.quality < 49 and item.sell_in < 6 else \
                    item.quality + 2 if item.quality < 49 and item.sell_in < 11 else \
                    item.quality + 1 if item.quality < 50 else \
                    item.quality 
                item.sell_in -= 1

            elif item.name == "Aged Brie":
                item.quality = \
                    item.quality + 2 if item.quality < 49 and item.sell_in < 1 else \
                    item.quality + 1 if item.quality < 50 else \
                    item.quality
                item.sell_in -= 1

            else:
                item.quality = \
                    item.quality - 2 if item.quality > 1 and item.sell_in < 1 else \
                    item.quality - 1 if item.quality > 0 else \
                    item.quality
                item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
