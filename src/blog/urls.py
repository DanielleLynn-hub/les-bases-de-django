from django.urls import path
from .views import index, article, a_propos

urlpatterns = [
    path('', index, name="blog-index"),
    path('article-<str:numero_article>/', article, name="blog-article"),
    path('a-propos/', a_propos, name="blog-a-propos"),
]