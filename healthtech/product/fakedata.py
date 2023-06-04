import json
import random
import datetime

name = [
    "widstar running sneakers",
    "girl zada gray flip flop sandal",
    "girl primotoo open toe synthetiflip flop sandal",
    "girl zada orange flip flop sandal",
    "lips too too demand open toe synthetiwedge heel",
    "lips too too skip synthetibaet flats",
    "lips too too imbody natura wedge sandal",
    "lips too too jit riding boot",
    "lips too too effort tan anke boot",
    "lips too too fynn rose god thong sandal",
    "lips too too jayden round toe synthetigray over the knee boot",
    "lips too too janee brown extended kneehigh riding boot",
    "lips too too inga wedge sandal",
    "lips too ripped synthetigreen fashion sneakers",
    "men and aqua shoes",
    "degree by refex heathered stretch yoga legging",
    "ana maddy round toe canvas bootie",
    "ana open toe synthetisandals",
    "ana michael open toe synthetiwedge heel",
    "ana vicky round toe synthetibronze anke boot",
    "axny apha round toe synthetibrown anke boot",
    "axny anise round toe synthetianke boot",
    "axny graham round toe synthetimid caf boot",
    "axny tuner round toe synthetibootie",
    "axny idona open toe synthetiplatform heel",
    "aerosoes redwood pump faux patent",
    "aerosoes loipowp sandals",
    "aerosoes ride with me souch boot combo faux leather",
    "aerosoes moasses round toe synthetiboot",
    "aerosoes creativity boot faux leather",
    "aerosoes stone push faux leather",
    "aerosoes ename round toe canvas brown winter boot",
    "aerosoes base board side sandal red faux leather",
    "aerosoes highight brown sides sandal",
    "aerosoes rock soid natura fabric",
    "aerosoes caendar bootie brown",
    "aerosoes barricade duck boot brown tan combo",
    "aerosoes may push wedge sandal tan combo fabric",
    "aerosoes time limit loafer faux leather"
]


# name = ["Fitbit", "Apple Watch", "Garmin", "Omron", "Withings", "Samsung Health", "MyFitnessPal", "Lifesum"]

slug_set = set()

products = []
for i, name_value in enumerate(name):
    template = {
        "model": "product.brand",
        "id": i + 1,
        "fields": {
            "name": name_value,
            # "img": 'img',
            "slug": name_value.lower().replace(" ", "-"),
            "description": "I am Eslam Essam",
            "is_active": True,
            "is_featured": False,
            "category": [i + 1],
            "brand": i + 1,
            "created_at": datetime.datetime.now().isoformat()
        }
    }

    products.append(template)

# Save the list of products in a JSON file
with open("healthtech/fixtures/db_product_fixture_50.json", "w") as f:
    json.dump(products, f, indent=4)
