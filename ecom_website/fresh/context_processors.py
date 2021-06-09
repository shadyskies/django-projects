from .models import Products, Insta_images
from orders.models import OrderItem, Cart


# context processpr
def main_context_processor(request):
    insta_images = Insta_images.objects.all()
    products = Products.objects.all()
    return{
        "insta_images": insta_images,
        "products": products,
    }
