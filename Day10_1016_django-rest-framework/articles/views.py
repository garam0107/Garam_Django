from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 
from .models import Article
from .serializers import ArticleListSerializer,ArticleSerializer

@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serialzer = ArticleListSerializer(articles, many = True)
        return Response(serialzer.data)
    elif request.method == 'POST':
        serialzer = ArticleSerializer(data= request.data)
        if serialzer.is_valid():
            serialzer.save()
            # 저장 성공 후 201 상태 코드를 반환
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사가 실패 하면 400 상태 코드를 반환
        return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk =article_pk)
    if request.method == 'GET':
        # Queryset이 아니므로 many 옵션 x
        serialzer = ArticleSerializer(article)
        return Response(serialzer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)