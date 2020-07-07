<<<<<<< HEAD
from django.shortcuts import render
from .models import Article


# 이달의 도서 - listView
# 필요 요소: 도서 사진, 기사 제목, 기사 내용, 등록일자, 도서카테고리, 기사카테고리 
# 기능 : 기사카테고리 드롭박스, 페이지네이션, 도서카테고리 박스, 등록일자 년 박스, 등록일자 월 박스

# 이달의 행사 - listView
# 필요 요소: 행사사진, 행사 이름, 기사 내용, 등록일자, 기사카테고리 
# 기능 : 기사카테고리 드롭박스, 검색도구, 페이지네이션

# 이달의 작가 - detailView
# 필요 요소: 행사 사진, 작가사진, 작가등등 작가Id, 기사제목, 기사내용, 기사카테고리 
# 기능 : 기사카테고리 드롭박스
def ThisMonthAuthorListView(request):
    author_info = Article.objects.all()
    return render(request,"articles/author.html",{"author_info":author_info},)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> ade7bc9c06408908f88500ba8c9a11e47d237983
