from faker import Faker
from your_project.models import Product

fake = Faker()

def create_fake_product():
    product_name = fake.unique.first_name()
    description = fake.text()
    price = fake.random_number(decimals=2, min_value=10, max_value=1000) 
    category = fake.random_element(elements=("Electronics", "Clothing", "Home", "Sports")) 
    availability = fake.random_element(elements=("In Stock", "Out of Stock")) 

    product = Product(
        name=product_name,
        description=description,
        price=price,
        category=category,
        availability=availability
    )
    product.save()
    return product
