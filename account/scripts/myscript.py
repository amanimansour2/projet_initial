from  mydatabase.models import Products
def run():
    # Get all products
    all_products = Products.objects.all()
    print all_products
