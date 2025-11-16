"""
Script to download images from URLs and assign them to FoodItem records.
This downloads images and saves them locally in media/food_images/
"""
import os
import requests
from pathlib import Path
from django.core.files.base import ContentFile
from shop.models import FoodItem

# Ensure media directory exists
MEDIA_DIR = Path('media/food_images')
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

def download_and_save_image(food_item, url):
    """Download image from URL and save to FoodItem"""
    if not url:
        return False
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Generate filename from food name
            filename = f"{food_item.name.replace(' ', '_').lower()}.jpg"
            
            # Save the image
            food_item.image.save(filename, ContentFile(response.content), save=False)
            food_item.image_url = url
            food_item.save()
            print(f"✓ Downloaded and saved image for '{food_item.name}' from {url}")
            return True
        else:
            print(f"✗ Failed to download image for '{food_item.name}' (HTTP {response.status_code})")
            return False
    except Exception as e:
        print(f"✗ Error downloading image for '{food_item.name}': {e}")
        return False

def update_all_images_from_urls():
    """Update all food items with images from their URLs"""
    food_items = FoodItem.objects.all()
    success_count = 0
    
    for food in food_items:
        # Check if there's an image_url to download from
        if food.image_url and not food.image:
            if download_and_save_image(food, food.image_url):
                success_count += 1
        elif not food.image and not food.image_url:
            print(f"⚠ No image or image_url for '{food.name}'")
    
    print(f"\n✓ Image update complete! Successfully processed {success_count} items.")

if __name__ == '__main__':
    update_all_images_from_urls()
