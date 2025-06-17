from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TopUpOrderSerializer
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Sum
from django.utils.timezone import now, timedelta
from django.shortcuts import render
from .models import TopUpOrder, TopUpProduct

class TopUpAPIView(APIView):
    def post(self, request):
        serializer = TopUpOrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response({"message": "Top-up order created.", "order_id": order.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@staff_member_required
def dashboard_view(request):
    top_products = (TopUpProduct.objects.annotate(order_count=Count('topuporder')).order_by('-order_count')[:5])

    today = now().date()
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    daily_revenue = []
    for day in last_7_days:
        revenue = TopUpOrder.objects.filter(status='success',created_at__date=day).aggregate(total=Sum('product__price'))['total'] or 0
        daily_revenue.append((day.strftime('%Y-%m-%d'), revenue))

    start_of_month = today.replace(day=1)
    failed_count = TopUpOrder.objects.filter(status='failed',created_at__date__gte=start_of_month).count()

    return render(request, 'dashboard.html', {'top_products': top_products, 'daily_revenue': daily_revenue, 'failed_count': failed_count,})


