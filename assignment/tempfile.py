from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
from faker.providers import DynamicProvider


fake_data = defaultdict(list)        
    products_provider = DynamicProvider(
        provider_name="products",
        elements=["shape", "size", "location", "price"],
    )

    fake = Faker()

    # then add new provider to faker instance
    fake.add_provider(products_provider)

    # now you can use:
    fake.products()
    # 'dr.'