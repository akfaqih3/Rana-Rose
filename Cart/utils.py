from .models import Cart as CartModel

class Cart:
    
    def __init__(self,request) -> None:
        if request.user.is_authenticated:
            self.cart,create = CartModel.objects.get_or_create(user=request.user,completed=False)
        else :
            self.cart ={}

    def get(self):
        return self.cart