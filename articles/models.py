from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set = 역시 장고가 자동으로 생성, ForeignKey가 설정되면서 관계가 설정되었기때문

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  #일반적으로 pk를 받아오려는 클래스와 이름 같게 설정, ForeignKey로 1:N 관계 설정
    # article을 Foreignkey로 설정하면 장고가 자동으로 article_id =를 만들어줌
