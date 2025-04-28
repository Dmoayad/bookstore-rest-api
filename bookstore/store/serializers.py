from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import (
    Article,
    Author,
    Genre,
    Book,
    Customer,
    Order,
    OrderItem,
    Review,
)




class ArticleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Article
       fields = ['id', 'title', 'author', 'email']


   def validate(self, attrs):
       unknown = set(self.initial_data) - set(self.fields)
       if unknown:
           raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
       return attrs


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__' # Or list specific fields: ['id', 'name', 'biography', 'birth_date']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__' # Or list specific fields: ['id', 'name', 'description']

class BookSerializer(serializers.ModelSerializer):
    # You can nest serializers to include related data
    author = AuthorSerializer(read_only=True) # Read-only to display author details
    genre = GenreSerializer(read_only=True)   # Read-only to display genre details

    class Meta:
        model = Book
        fields = '__all__' # Or list specific fields: ['id', 'title', 'author', 'isbn', 'genre', 'publication_date', 'price', 'stock']

    # You might need to override create/update if you want to handle
    # creating/updating nested relationships here (e.g., creating an author
    # when creating a book, though it's often better to manage them separately).
    # def create(self, validated_data):
    #     author_data = validated_data.pop('author') # Example if you were creating author
    #     author = Author.objects.create(**author_data)
    #     book = Book.objects.create(author=author, **validated_data)
    #     return book


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' # Or list specific fields: ['id', 'name', 'email', 'address', 'phone_number']

class OrderSerializer(serializers.ModelSerializer):
    # Nest OrderItemSerializer to display items within an order
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__' # Or list specific fields: ['id', 'customer', 'order_date', 'total_amount', 'status', 'items']

    def get_items(self, obj):
        # This method retrieves and serializes the related OrderItems
        items = obj.items.all()
        return OrderItemSerializer(items, many=True).data

    # You will likely need to override create to handle creating OrderItems
    # when an order is created.
    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     order = Order.objects.create(**validated_data)
    #     for item_data in items_data:
    #         OrderItem.objects.create(order=order, **item_data)
    #     return order


class OrderItemSerializer(serializers.ModelSerializer):
    # You can nest BookSerializer to display book details within an order item
    book = BookSerializer(read_only=True) # Read-only to display book details

    class Meta:
        model = OrderItem
        fields = '__all__' # Or list specific fields: ['id', 'order', 'book', 'quantity', 'price']

    # You might need to handle creating OrderItems within the Order create method

class ReviewSerializer(serializers.ModelSerializer):
    # Nest CustomerSerializer and BookSerializer if you want to display
    # customer and book details with the review.
    customer = CustomerSerializer(read_only=True) # Read-only to display customer details
    book = BookSerializer(read_only=True)       # Read-only to display book details

    class Meta:
        model = Review
        fields = '__all__'