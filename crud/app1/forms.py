from django.forms import ModelForm
from app1.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer_id','product_id','unit_price','qty','total_price']