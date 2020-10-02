from django.urls import path
from django.conf.urls import url
from .views import(
    ItemListView, 
    ItemDetailView, 
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    AuthorItemView
    # CommentView,
    # CommentCreateView,
)
from bj_app.models import BJ_ITEM
from .serializers import ItemCreateSerializer, ItemListSerializer, ItemDetailSerializer

urlpatterns = [
    path('', ItemListView.as_view()),
    path('create', ItemCreateView.as_view(queryset=BJ_ITEM.objects.all(), serializer_class=ItemCreateSerializer)),
    path('<pk>', ItemDetailView.as_view(), name='Details'),
    path('<pk>/update', ItemUpdateView.as_view(), name='Update'),
    path('<pk>/delete', ItemDeleteView.as_view(), name='Delete'),
    path('author/<username>', AuthorItemView.as_view(), name='Author-Post')
    
    # path('<pk>/com', CommentView.as_view()),
    # path('<pk>/com/create', CommentCreateView.as_view()),
]