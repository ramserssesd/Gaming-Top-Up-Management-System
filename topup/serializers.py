from rest_framework import serializers
from .models import TopUpOrder, TopUpProduct, Game

class TopUpOrderSerializer(serializers.Serializer):
    gamename = serializers.CharField()
    game_id = serializers.CharField()
    product_name = serializers.CharField()
    product_id = serializers.IntegerField()
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    user_email = serializers.EmailField()
    payment_status = serializers.ChoiceField(choices=['pending', 'success', 'failed'])

    def validate(self, data):
        try:
            game = Game.objects.get(name=data['gamename'], game_id=data['game_id'], is_active=True)
        except Game.DoesNotExist:
            raise serializers.ValidationError("Game is inactive or does not exist.")

        try:
            product = TopUpProduct.objects.get(id=data['product_id'], game=game, name=data['product_name'], price=data['product_price'])
        except TopUpProduct.DoesNotExist:
            raise serializers.ValidationError("Product not found or mismatched with the game.")

        data['product'] = product
        return data

    def create(self, validated_data):
        return TopUpOrder.objects.create(user_email=validated_data['user_email'],product=validated_data['product'],
            status=validated_data['payment_status'])
