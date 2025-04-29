#PowerShell command

>>> from shop_app import Product, Category
>>> product = Product(name='Lime', description='Lime', price= 5.00)
>>> category1 = Category(name='Продукты', description='Продукты питания', product=product)
>>> product.save()
>>> category1.save()
>>> category1 = Category(name='Продукты', description='Продукты питания', product=2)
