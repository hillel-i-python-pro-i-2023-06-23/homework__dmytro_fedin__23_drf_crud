from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from .models import Contact
from .serializers import ContactSerializer


@api_view(["GET"])
def api_overview(request):
    api_urls = {"Create": "/create", "Read": "all/", "Update": "/update/pk", "Delete": "/contact/pk/delete"}

    return Response(api_urls)


@api_view(["POST"])
def add_contact(request):
    item = ContactSerializer(data=request.data)

    if Contact.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This data already exists")

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def view_contacts(request):
    if request.query_params:
        contacts = Contact.objects.filter(**request.query_params.dict())
    else:
        contacts = Contact.objects.all()

    if contacts:
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def update_contacts(request, pk):
    contact = Contact.objects.get(pk=pk)
    data = ContactSerializer(instance=contact, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_contacts(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
