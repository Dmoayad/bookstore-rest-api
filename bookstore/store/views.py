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
from .serializers import (
    ArticleSerializer,
    AuthorSerializer,
    GenreSerializer,
    BookSerializer,
    CustomerSerializer,
    OrderSerializer,
    OrderItemSerializer,
    ReviewSerializer,
)
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class ArticleViewSet(viewsets.ModelViewSet):


   serializer_class = ArticleSerializer
   queryset = Article.objects.all()
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows genres to be viewed or edited.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # You could add custom actions here, e.g., for listing reviews
    # @action(detail=True, methods=['get'])
    # def reviews(self, request, pk=None):
    #     book = self.get_object()
    #     reviews = book.reviews.all()
    #     serializer = ReviewSerializer(reviews, many=True)
    #     return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order items to be viewed or edited.
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]