from .models import Products, Insta_images
from orders.models import OrderItem, Cart


# context processpr
def main_context_processor(request):
    insta_images = Insta_images.objects.all()
    products = Products.objects.all()
    cart_obj = Cart.objects.get(user=request.user)
    order_item = OrderItem.objects.filter(cart=cart_obj)
    return{
        "insta_images": insta_images,
        "products": products,
        "cart_item": order_item,
    }
