from django import forms
from .models import Article
# 필드 정보는 Article 모델에서 정의되어 있기 때문에 재정의를 할 필요가 없기 때문에 Article에서 가져오기
class ArticleForm(forms.ModelForm):
    # ArticleForm의 정보를 작성하는 클래스 meta
    class Meta:
        model = Article
        fields = '__all__'
     