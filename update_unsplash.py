#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_project.settings')
django.setup()

from shop.models import FoodItem

updates = {
    'Biryani': 'https://images.unsplash.com/photo-1585937421456-de4174e01fc8?w=1200&h=800&fit=crop',
    'Samosas': 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=1200&h=800&fit=crop',
    'Garlic Bread': 'https://images.unsplash.com/photo-1573521193529-7a1d16a37937?w=1200&h=800&fit=crop',
    'Chicken Tikka': 'https://images.unsplash.com/photo-1599043513267-0fc0b8dd38d4?w=1200&h=800&fit=crop',
    'Fresh Juice': 'https://images.unsplash.com/photo-1553530666-ba2a8e36cd12?w=1200&h=800&fit=crop',
    'Chocolate Cake': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=1200&h=800&fit=crop'
}

for name, url in updates.items():
    FoodItem.objects.filter(name=name).update(image_url=url)
    print(f'✓ Updated {name}')

print('\n✓ All Unsplash URLs set. Ready to download.')
