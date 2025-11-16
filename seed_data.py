from shop.models import FoodItem

data = [
    ('Biryani','Delicious Chicken Biryani',150.00,'Main Course','https://images.unsplash.com/photo-1563379091339-03b21ab54a88?w=600&h=400&fit=crop'),
    ('Samosas','Crispy Samosas (Pack of 4)',40.00,'Snacks','https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&h=400&fit=crop'),
    ('Garlic Bread','Buttery Garlic Bread',80.00,'Snacks','https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?w=600&h=400&fit=crop'),
    ('Chicken Tikka','Spiced Chicken Tikka',120.00,'Main Course','https://images.unsplash.com/photo-1599043513267-0fc0b8dd38d4?w=600&h=400&fit=crop'),
    ('Fresh Juice','Freshly Squeezed Orange Juice',50.00,'Beverages','https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=600&h=400&fit=crop'),
    ('Chocolate Cake','Rich Chocolate Cake Slice',60.00,'Desserts','https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600&h=400&fit=crop'),
]

for n,d,p,c,img_url in data:
    obj, created = FoodItem.objects.get_or_create(name=n, defaults={'description':d, 'price':p, 'category':c, 'image_url':img_url})
    if created:
        print('ADDED', n)
    else:
        # Update existing items with image_url if not already set
        if not obj.image_url:
            obj.image_url = img_url
            obj.save()
            print('UPDATED', n, 'with image URL')
print('SEED_DONE')
