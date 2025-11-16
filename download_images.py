"""
Script to download sample food images and assign them to FoodItem records.
This saves them locally in media/food_images/ instead of hotlinking.
"""
import os
import requests
from pathlib import Path
from django.core.files.base import ContentFile

# Ensure media directory exists
MEDIA_DIR = Path('media/food_images')
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

# Sample image URLs (using picsum and placeholder alternatives)
image_sources = {
    'Biryani': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTajz7dRbTo3giRInUr6Xvw9BaDAtK3MK6GA&s',
    'Samosas': 'https://images.news18.com/ibnkhabar/uploads/2022/09/samosa-1-2.jpg',
    'Garlic Bread': 'https://content.jwplatform.com/thumbs/nmc5Ad4i-720.jpg',
    'Chicken Tikka': 'https://signatureconcoctions.com/wp-content/uploads/2024/05/Chicken-Tikka-1-scaled.jpg,
    'Fresh Juice': 'https://static.vecteezy.com/system/resources/thumbnails/029/283/229/small/a-front-view-fresh-fruit-cocktails-with-fresh-fruit-slices-ice-cooling-on-blue-drink-juice-co-free-photo.jpg',
    'Chocolate Cake': 'https://www.hersheyland.com/content/dam/hersheyland/en-us/recipes/recipe-images/40-hersheys-deep-dark-chocolate-cake.jpg',
}

from shop.models import FoodItem

for food_name, url in image_sources.items():
    try:
        food = FoodItem.objects.get(name=food_name)
        filename = f"{food_name.replace(' ', '_').lower()}.jpg"
        
        # Download the image
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            # Save to media directory
            food.image.save(filename, ContentFile(response.content), save=True)
            print(f"✓ Downloaded and assigned image for {food_name}")
        else:
            print(f"✗ Failed to download image for {food_name} (status {response.status_code})")
    except FoodItem.DoesNotExist:
        print(f"✗ Food item '{food_name}' not found")
    except Exception as e:
        print(f"✗ Error processing {food_name}: {e}")

print("IMAGE_DOWNLOAD_DONE")
