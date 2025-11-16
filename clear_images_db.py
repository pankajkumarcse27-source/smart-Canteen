#!/usr/bin/env python
"""
Clears image fields for all FoodItem objects and deletes any associated stored files.
Run from project root:
    python clear_images_db.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_project.settings')
django.setup()

from shop.models import FoodItem

count = 0
for item in FoodItem.objects.all():
    # delete stored file if present
    try:
        if item.image:
            item.image.delete(save=False)
    except Exception as e:
        print(f"Warning deleting file for {item.name}: {e}")
    # clear fields
    item.image = None
    item.image_url = ''
    item.save()
    count += 1

print(f"Cleared image fields for {count} FoodItem objects.")
