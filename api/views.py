from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .models import Contact
# from .serializers import ContactSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'all_items': '/',
        # 'Search by Category': '/?category=category_name',
        # 'Search by Subcategory': '/?subcategory=category_name',
        # 'Add': '/create',
        # 'Update': '/update/pk',
        # 'Delete': '/item/pk/delete'
    }

    return Response(api_urls)
