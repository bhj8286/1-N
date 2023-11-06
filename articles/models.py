from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  #일반적으로 pk를 받아오려는 클래스와 이름 같게 설정, ForeignKey로 1:N 관계 설정
    # article을 foreignkey로 설정하면 장고가 자동으로 article_id를 만들어줌
