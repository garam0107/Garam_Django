from django.shortcuts import render
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1. 사용자 요청으로부터 입력 데이터를 추출
    # 2. 추출한 입력 데이터를 활용해 DB에 저장 요청
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 데이터 저장 3가지 방법
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title = title ,content = content)
    article.save()

    #3
    # Article.objects.create(title = title ,content = content)