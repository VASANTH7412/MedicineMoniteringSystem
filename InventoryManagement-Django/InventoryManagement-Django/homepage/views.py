import json
from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill

class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        labels = []
        data = []
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')

        low_stock_items = []  # Store low stock items
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
            if item.quantity <= 10:  # Check if stock is low
                low_stock_items.append({"name": item.name, "quantity": item.quantity})

        print("Low Stock Items for Homepage:", low_stock_items)  # Debugging print

        context = {
            'labels': labels,
            'data': data,
            'sales': SaleBill.objects.order_by('-time')[:3],
            'purchases': PurchaseBill.objects.order_by('-time')[:3],
            'low_stock_items': json.dumps(low_stock_items)  # ✅ Convert to JSON before passing to template
        }
        return render(request, self.template_name, context)

# ✅ Added AboutView
class AboutView(TemplateView):
    template_name = "about.html"



