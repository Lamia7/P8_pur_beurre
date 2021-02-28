from django.core.management.base import BaseCommand
from django.db import IntegrityError

from progress.bar import ShadyBar

from search.models import Product, Category
from search.api import Api


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """Feeds the database with data from API"""
        
        self.clear_db()

        myapi = Api()
        products = myapi.avoid_empty()
        #print(products)

        if products is not None:
            self.stdout.write(self.style.SUCCESS(
                "Products import from API : DONE"))
        else:
            self.stdout.write(self.style.ERROR(
                "Products import from API : ERROR"))
            return

        with ShadyBar('Inserting to database...', max=len(products)) as bar:
            for product in products:
                #print("TYPEOFPRODUCT: ", type(product))
                name = product.get("product_name_fr")[
                    :150].strip().lower().capitalize()
                #print("CONTENTNAME", name, type(name))
                brands = product.get("brands")[:150].upper()
                #print("CONTENT BRANDS", brands, type(brands))
                barcode = product.get("code")[:13].strip()
                #print("BARCODE", type(barcode))
                #print("BARCODE PRINT", barcode)
                url = product.get("url")
                image_url = product.get("image_url")
                image_small_url = product.get("image_small_url")
                nutriscore = product.get("nutriscore_grade")[0].upper()
                #print("NUTRISCOREHELLOE", type(nutriscore))
                #print("NUTRISCOREHELLOE", nutriscore)
                categories = categories = [name.strip().lower().capitalize()
                                        for name in product['categories'].split(',')]

                nutriments_list = [
                    "energy_100g",
                    "sugars_100g",
                    "sodium_100g",
                    "fat_100g",
                    "salt_100g"
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
                    # categories=set_categories()
                )

                try:
                    product_obj.save()

                    # Save categories, linking them to Product obj
                    saved_categories = []
                    for category in categories:
                        cat_obj = Category(name=category)
                        if not category in saved_categories:  # Avoid duplicated categories
                            saved_categories.append(category)
                            try:
                                cat_obj.save()
                            except IntegrityError:  # Avoid duplicated cat
                                cat_obj = Category.objects.get(name=category)

                            product_obj.categories.add(cat_obj)  # add() Django method to link manytomany relation
                            product_obj.save()

                    #print("HELLOPRODUCT", product_obj.name, product_obj.url,
                        #product_obj.sugars_100g, product_obj.categories.all())
                
                except IntegrityError:
                    continue
                bar.next()


    def clear_db(self):
        """Clears the database"""

        product_obj = Product.objects.all()
        product_obj.delete()

        cat_obj = Category.objects.all()
        cat_obj.delete()

        #favorite_obj = Favorite.objects.all()
        #favorite_obj.delete()
