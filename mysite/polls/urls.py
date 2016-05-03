# -*- coding: utf-8 -*-
# URLマッピング

from django.conf.urls import url

from . import views

# 名前空間polls設定
app_name = 'polls'
# アクセスされたURLに対して、応答するビューを指定
urlpatterns = [
    # ex: /polls/
    # http://○○/polls/ にアクセスされた場合、ビューindexに渡す
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # http://○○/polls/番号/ にアクセスされた場合、ビューdetailに渡す
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # http://○○/polls/番号/result にアクセスされた場合、ビューresultsに渡す
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # http://○○/polls/番号/vote にアクセスされた場合、ビューvoteに渡す
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]