from django.shortcuts import render,redirect
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
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 데이터 저장 3가지 방법
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title = title ,content = content)
    article.save()
    # 유효성 검사와 가독성이 좋은 2번 방법을 주로 선택
    #3
    # Article.objects.create(title = title ,content = content)
    return redirect('articles:detail', article.pk)
    # return redirect('articles:index')
def delete(request, pk):
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')

def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. 어떤 게시글 수정할지 조회
    article = Article.objects.get(pk=pk)
    # 2. 사용자로부터 받은 새로운 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 3. 기존 게시글 데이터를 사용자로 받은 데이터로 새로 할당
    article.title = title
    article.content = content
    # 4. 저장
    article.save()

    return redirect('articles:detail', article.pk)

    