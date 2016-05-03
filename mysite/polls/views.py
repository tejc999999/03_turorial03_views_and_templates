# -*- coding: utf-8 -*-
# ビュー

# 他ファイルからのコード読み込み
# JavaのimportやC言語のincludeと同様
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
# 1つ上のフォルダmodelsから読み込み(.modules)
from .models import Question

# index用のビュー、HttpRequestを受け取り、HttpResponseを返す
# 初期表示画面
def index(request):
    # pub_dateの降順でDBからQuestionを取得
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # テンプレートを読み込み
    template = loader.get_template('polls/index.html')
    # 取得した複数のQuestionを辞書登録
    context = {
        'latest_question_list': latest_question_list,
    }
    # render()を使わないパターン
    # return HttpResponse(template.render(context, request))
    # render()を使うパターン
    return render(request, 'polls/index.html', context)


# detail用のビュー
# 詳細表示画面
def detail(request, question_id):
    # pkを受け取ったIDとして検索、取得データがない場合は404を受け取る
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# results用のビュー
# 投票結果画面
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# vote用のビュー
# 投票画面？
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
