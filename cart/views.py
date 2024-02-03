from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status
from rest_framework import generics
from cart.models import *
from shop.models import *
import datetime
# @permission_classes([IsAuthenticated])
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from cart.serializers import *
from rest_framework.permissions import AllowAny


@permission_classes([IsAuthenticated])
class AddPizzaToCart(APIView):
    Serializer = AddPizzaToCartSerializer
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user

        if user.is_authenticated:
            cart = Cart.objects.all().filter(user=user, is_current=True).first()
            if cart == None:
                date_created = datetime.datetime.now()
                cart = Cart(user=user, is_current=True, date_created=date_created)
                cart_id = cart.cart_id
                cart.save()

            data = request.data

            price = self.calculate_price(data=data)

            pizza = Pizza(creator=user, name=data['name'], price=price)
            pizza.save()
            self.save_pizza_ingredients(data=data, pizza=pizza)

            cp = CartPizza(cart=cart, pizza=pizza, quantity=1)
            cp.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)
    def save_pizza_ingredients(self, data, pizza):
        for k in data.keys():
            ingredient = Ingredient.objects.all().filter(title=k).first()
            if ingredient == None:
                continue
            qty = data[k]
            Ingredient.objects.all().filter(title=k).first()
            pizza_ingredient = PizzaIngredient(pizza=pizza, quantity=qty, ingredient=ingredient)
            pizza_ingredient.save()

    def calculate_price(self, data):
        price = 20000
        for k in data.keys():
            ingredient = Ingredient.objects.all().filter(title=k).values('price').first()
            if ingredient == None:
                continue
            qty = data[k]
            pr = ingredient['price']
            price += qty * pr
        return price

@permission_classes([IsAuthenticated])
class AddPizzaToMyPizza(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user

        if user.is_authenticated:
            data = request.data
            price = self.calculate_price(data=data)
            pizza = Pizza(creator=user, name=data['name'], price=price)
            pizza.save()
            self.save_pizza_ingredients(data=data, pizza=pizza)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)
    def save_pizza_ingredients(self, data, pizza):
        for k in data.keys():
            ingredient = Ingredient.objects.all().filter(title=k).first()
            if ingredient == None:
                continue
            qty = data[k]
            Ingredient.objects.all().filter(title=k).first()
            pizza_ingredient = PizzaIngredient(pizza=pizza, quantity=qty, ingredient=ingredient)
            pizza_ingredient.save()

    def calculate_price(self, data):
        price = 20000
        for k in data.keys():
            ingredient = Ingredient.objects.all().filter(title=k).values('price').first()
            if ingredient == None:
                continue
            qty = data[k]
            pr = ingredient['price']
            price += qty * pr
        return price

@permission_classes([IsAuthenticated])
class GetIngredientsOfPizza(APIView):
    Serializer = GetIngredientsOfPizza
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user
        if user.is_authenticated:
            data = request.data
            pizza_id =data['pizza_id']
            # pizza = Pizza.objects.all().filter()
            return_list = []
            pis = PizzaIngredient.objects.all().filter(PizzaIngredient.pizza.pizza_id.__eq__(pizza_id)).first()
            for pi in pis:
                ingredients = CartPizza.objects.all().filter(Ingredient.ingredient_id.__eq__(pi['ingredient'])).first()
                return_list.append({'name': ingredients.title})
            serializer = GetIngredientsOfPizza(data=return_list)
            return Response(data=serializer, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)

@permission_classes([IsAuthenticated])
class GetActiveCart(APIView):
    def post(self, request, *args, **kwargs):
        # return: {'cart': [{'qty': 1, 'cheese': 4, ...}, ...], 'price': }
        user = request.user  # Get the authenticated user

        if user.is_authenticated:
            cart = Cart.objects.all().filter(user=user, is_current=True).first()
            return_list = []
            price = 0
            if cart != None:
                pizza_cart_list = CartPizza.objects.all().filter(cart=cart)
                for pizza_cart in pizza_cart_list:
                    pizza_name, p, my_dict = self.price_and_ingredients(pizza_cart.pizza_id)
                    price += p
                    my_dict['number'] = pizza_cart.quantity
                    my_dict['pizza_id'] = pizza_cart.pizza_id
                    my_dict['pizza_id'] = pizza_cart.pizza_id
                    my_dict['quantity'] = pizza_cart.quantity
                    my_dict['name'] = pizza_name
                    return_list.append(my_dict)

                data = {'cart': return_list, 'price': price}
                return Response(data={'cart': data, 'price': price}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)

    def price_and_ingredients(self, pizza_id):
        my_dict = {}
        price = 20000
        pizza_name = (Pizza.objects.all().filter(pizza_id=pizza_id).first()).name
        ingredients = PizzaIngredient.objects.all().filter(pizza=pizza_id)
        for i in ingredients:
            ingredient = Ingredient.objects.all().filter(ingredient_id=i.ingredient_id).first()
            if ingredient == None:
                continue
            my_dict[ingredient.title] = i.quantity
            qty = i.quantity
            pr = ingredient.price
            price += qty * pr
        return pizza_name, price, my_dict

# buttons for change value of pizza
@permission_classes([IsAuthenticated])
class AddExistsPizzaToCart(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user

        if user.is_authenticated:
            data = request.data
            pizza_id = data['pizza_id']
            pizza = Pizza.objects.all().filter(pizza_id=pizza_id).first()
            cart = Cart.objects.all().filter(user=user, is_current=True).first()
            cart_pizza = CartPizza.objects.all().filter(cart=cart, pizza=pizza).first()
            if cart_pizza != None:
                CartPizza.objects.filter(cart=cart, pizza=pizza).update(quantity=cart_pizza.quantity + 1)
                return Response(data={}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)

    def price_and_ingredients(self, pizza_id):
        my_dict = {}
        price = 20000
        pizza_name = (Pizza.objects.all().filter(pizza_id=pizza_id).first()).name
        ingredients = PizzaIngredient.objects.all().filter(pizza=pizza_id)
        for i in ingredients:
            ingredient = Ingredient.objects.all().filter(ingredient_id=i.ingredient_id).first()
            if ingredient == None:
                continue
            my_dict[ingredient.title] = i.quantity
            qty = i.quantity
            pr = ingredient.price
            price += qty * pr
        return pizza_name, price, my_dict

@permission_classes([IsAuthenticated])
class SubExistsPizzaFromCart(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user

        if user.is_authenticated:
            data = request.data
            pizza_id = data['pizza_id']
            pizza = Pizza.objects.all().filter(pizza_id=pizza_id).first()
            cart = Cart.objects.all().filter(user=user, is_current=True).first()
            cart_pizza = CartPizza.objects.all().filter(cart=cart, pizza=pizza).first()
            print(cart_pizza)
            if cart_pizza != None:
                if cart_pizza.quantity > 1:
                    CartPizza.objects.filter(cart=cart, pizza=pizza).update(quantity=cart_pizza.quantity - 1)
                else:
                    CartPizza.objects.filter(cart=cart, pizza=pizza).delete()
                return Response(data={}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)

    def price_and_ingredients(self, pizza_id):
        my_dict = {}
        price = 20000
        pizza_name = (Pizza.objects.all().filter(pizza_id=pizza_id).first()).name
        ingredients = PizzaIngredient.objects.all().filter(pizza=pizza_id)
        for i in ingredients:
            ingredient = Ingredient.objects.all().filter(ingredient_id=i.ingredient_id).first()
            if ingredient == None:
                continue
            my_dict[ingredient.title] = i.quantity
            qty = i.quantity
            pr = ingredient.price
            price += qty * pr
        return pizza_name, price, my_dict

@permission_classes([IsAuthenticated])
class DeletePizzaFromMyPizza(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user

        if user.is_authenticated:
            data = request.data
            pizza_id = data['pizza_id']
            Pizza.objects.all().filter(pizza_id=pizza_id).update(creator=None)
            return Response(data={}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([IsAuthenticated])
class AddMyPizzaToCart(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user

        if user.is_authenticated:
            data = request.data
            cart = Cart.objects.all().filter(user=user, is_current=True).first()
            if cart == None:
                date_created = datetime.datetime.now()
                cart = Cart(user=user, is_current=True, date_created=date_created)
                cart.save()

            pizza = Pizza.objects.all().filter(pizza_id=data['pizza_id'])
            cp = CartPizza.objects.all().filter(cart=cart, pizza=pizza, quantity__gt=0)
            if cp != None:
                cp = CartPizza.objects.all().filter(cart=cart, pizza=pizza).update(quantity=cp.quantity + 1)
                cp.save()
            else:
                cp = CartPizza(cart=cart, pizza=pizza, quantity=1)
                cp.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)