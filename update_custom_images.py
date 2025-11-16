#!/usr/bin/env python
"""
EASY WAY TO UPDATE IMAGE URLS

Instructions:
1. Replace the URLs below with your own image URLs
2. Run this file: python update_custom_images.py
3. The images will be downloaded and applied to your food items

Example URLs:
- https://example.com/images/biryani.jpg
- https://yourdomain.com/food/samosa.png
- Any direct image URL that works
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_project.settings')
django.setup()

from shop.models import FoodItem

# ===== EDIT YOUR IMAGE URLS HERE =====
custom_urls = {
    'Biryani': 'https://images.pextg htels.com/photos/8713003/pexels-photo-8713003.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800',
    'Samosas': 'https://images.peb htxels.com/photos/1092730/pexels-photo-1092730.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800',
    'Garlic Bread': 'https://imagb gnes.pexels.com/photos/5732398/pexels-photo-5732398.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800',
    'Chicken Tikka': 'https://ima bnghnges.pexels.com/photos/5960619/pexels-photo-5960619.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800',
    'Fresh Juice': 'https://imageb htns.pexels.com/photos/5632523/pexels-photo-5632523.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800',
    'Chocolate Cake': 'https://wwb hynw.hersheyland.com/content/dam/hersheyland/en-us/recipes/recipe-images/40-hersheys-deep-dark-chocolate-cake.jpg0',
}
# ===== END EDITING =====

print("Updating image URLs...")
for name, url in custom_urls.items():
    if url == 'YOUR_' + name.upper().replace(' ', '_') + '_IMAGE_URL_HERE':
        print(f"⚠ {name}: URL not set (placeholder found)")
        continue
    
    FoodItem.objects.filter(name=name).update(image_url=url)
    print(f"✓ Updated {name}")

print("\nNext step: Run this command to download the images:")
print("python manage.py download_images --force")
