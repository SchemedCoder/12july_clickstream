import random
import uuid
from faker import Faker
from datetime import datetime

fake = Faker()

EVENT_TYPES = [
    "page_view",
    "product_view",
    "add_to_cart",
    "checkout",
    "purchase",
    "search"
]

DEVICES = [
    "Desktop",
    "Mobile",
    "Tablet"
]

BROWSERS = [
    "Chrome",
    "Firefox",
    "Edge",
    "Safari"
]

PAGES = [
    "/",
    "/products",
    "/checkout",
    "/search",
    "/cart",
    "/profile",
    "/orders"
]


def generate_event():

    return {

        "event_id": str(uuid.uuid4()),

        "timestamp": datetime.utcnow().isoformat(),

        "user_id": random.randint(1000, 9999),

        "session_id": str(uuid.uuid4()),

        "country": fake.country(),

        "city": fake.city(),

        "device": random.choice(DEVICES),

        "browser": random.choice(BROWSERS),

        "page": random.choice(PAGES),

        "event_type": random.choice(EVENT_TYPES),

        "product_id": random.randint(1, 500),

        "price": round(random.uniform(10, 1500), 2)
    }


if __name__ == "__main__":

    print(generate_event())
