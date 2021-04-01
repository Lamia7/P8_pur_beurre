from django.core.management.base import BaseCommand
from django.db import IntegrityError

from progress.bar import ShadyBar

from search.models import Product, Category, Favorite
from search.api import Api


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """Feeds the database with data from API"""

        self.clear_db()

        # Launches import of data from API
        print("Data import from API launched. Please wait...")
        myapi = Api()
        products = myapi.avoid_empty()

        if products is not None:
            self.stdout.write(
                self.style.SUCCESS("Products import from API : DONE")
            )
        else:
            self.stdout.write(
                self.style.ERROR("Products import from API : ERROR")
            )
            return

        with ShadyBar(
            "Inserting to database...",
            max=len(products), suffix="%(percent)d%%"
        ) as bar:
            for product in products:
                name = product.get(
                    "product_name_fr"
                    )[:150].strip().lower().capitalize()
                brands = product.get("brands")[:150].upper()
                barcode = product.get("code")[:13].strip()
                url = product.get("url")
                image_url = product.get("image_url")
                image_small_url = product.get("image_small_url")
                nutriscore = product.get("nutriscore_grade")[0].upper()
                categories = categories = [
                    name.strip().lower().capitalize()
                    for name in product["categories"].split(",")
                ]

                # Get some of the nutriments keys/values
                nutriments_list = [
                    "energy_100g",
                    "sugars_100g",
                    "sodium_100g",
                    "fat_100g",
                    "salt_100g",
                ]

                nutriments_dict = {}

                for nutriment in nutriments_list:
                    nutriment_value = product.get("nutriments").get(nutriment)
                    if isinstance(nutriment_value, float) is True:
                        value = nutriment_value
                    else:
                        value = 0
                    nutriments_dict[nutriment] = value

                product_obj = Product(
                    name=name,
                    brands=brands,
                    barcode=barcode,
                    url=url,
                    image_url=image_url,
                    image_small_url=image_small_url,
                    nutriscore=nutriscore,
                    energy_100g=nutriments_dict.get("energy_100g"),
                    sugars_100g=nutriments_dict.get("sugars_100g"),
                    sodium_100g=nutriments_dict.get("sodium_100g"),
                    fat_100g=nutriments_dict.get("fat_100g"),
                    salt_100g=nutriments_dict.get("salt_100g"),
                )

                try:
                    product_obj.save()

                    # Save categories, linking them to Product obj
                    saved_categories = []
                    for category in categories:
                        cat_obj = Category(name=category)
                        if category not in saved_categories:
                            # Avoid duplicated categories
                            saved_categories.append(category)
                            try:
                                cat_obj.save()
                            except IntegrityError:  # Avoid duplicated cat
                                cat_obj = Category.objects.get(name=category)

                            # add() Django method to link manytomany relation
                            product_obj.categories.add(cat_obj)
                            product_obj.save()

                except IntegrityError:
                    continue
                bar.next()

    def clear_db(self):
        """Clears the database"""

        product_obj = Product.objects.all()
        product_obj.delete()

        cat_obj = Category.objects.all()
        cat_obj.delete()

        favorite_obj = Favorite.objects.all()
        favorite_obj.delete()
