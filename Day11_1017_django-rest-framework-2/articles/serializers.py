from rest_framework import serializers
from .models import Article,Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content',)

    comment_set = CommentDetailSerializer(many = True, read_only = True)
    comment_count = serializers.IntegerField(source = 'comment_set.count', read_only = True)
   
   
   
   
    class Meta:
        model = Article
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerial(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    article = ArticleTitleSerial(read_only = True)
    class Meta:
        model = Comment
        fields = '__all__'
        # 외래 키 데이터를 유효성 검사에서 제외하고 결과 데이터에 포함하고 싶을 때 사용
        # read_only_fields = ('article',)
    
