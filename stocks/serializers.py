from rest_framework import serializers

from django.conf import settings
from stocks.models import Product, Stock, StockPosition


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name"]


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPosition
        fields = ["id", "product", "price", "qty"]


class StockSerializer(serializers.ModelSerializer):
    positions = PositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ["id", "name", "address", "positions"]

    def validate(self, attrs):
        count = Student.objects.count()
        if count > settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError()
        return super().validate(attrs)

    def create(self, validated_data: dict):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockPosition.objects.create(stock=stock, **position)

        return stock

    def update(self, instance, validated_data):
        pass
