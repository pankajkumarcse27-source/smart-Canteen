# How to Update Food Images

## Quick Steps:

### Step 1: Edit the URLs file
Open `update_custom_images.py` and replace these lines with YOUR image URLs:

```python
custom_urls = {
    'Biryani': 'https://your-url-here.com/biryani.jpg',
    'Samosas': 'https://your-url-here.com/samosas.jpg',
    'Garlic Bread': 'https://your-url-here.com/garlic-bread.jpg',
    'Chicken Tikka': 'https://your-url-here.com/chicken-tikka.jpg',
    'Fresh Juice': 'https://your-url-here.com/fresh-juice.jpg',
    'Chocolate Cake': 'https://your-url-here.com/chocolate-cake.jpg',
}
```

### Step 2: Run the update script
```bash
python update_custom_images.py
```

### Step 3: Download and apply the images
```bash
python manage.py download_images --force
```

### Step 4: View your changes
Open `http://127.0.0.1:8000/` in your browser and refresh.

---

## Image URL Requirements:
- Must be a valid, working URL
- Must return an image file (JPG, PNG, etc.)
- Must be accessible from your computer
- Examples:
  - Direct image links: `https://example.com/images/food.jpg`
  - Imgur: `https://i.imgur.com/abcd1234.jpg`
  - Google Drive (public): `https://drive.google.com/uc?id=YOUR_FILE_ID`
  - Your own server: `https://yourdomain.com/images/biryani.jpg`

---

## Current Image URLs (in database):
Run this to see what's currently set:
```bash
python manage.py shell -c "from shop.models import FoodItem; [print(f'{i.name}: {i.image_url}') for i in FoodItem.objects.all()]"
```

---

## Database Field Info:
The `FoodItem` model has two image fields:
- `image` — Local image file stored in `media/food_images/`
- `image_url` — Remote URL where the image is fetched from

The `--force` flag overwrites the local image with whatever is at the `image_url`.
