# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,render_to_response
from django.contrib import messages

from comment.commentForms import *
from article.models import *
from djangoBlog.language import *

# Create your views here.


context = {}
allArticles = 0
myTodos = 0
myArticles = 0
lang = en

def allInfo(req):
    global allArticles
    global myTodos
    global myArticles
    allArticles = len(Article.objects.all())
    myTodos = len(Todo.objects.filter(author = req.user))
    myArticles = len(Article.objects.filter(author = req.user))
def check(req):
    global context
    global lang
    if(req.user.is_authenticated):
        allInfo(req)
        context = {
            "allArticles":allArticles,
            "myTodos":myTodos,
            "myArticles":myArticles,
            'lang':lang
             }
    else:
        context = {"allArticles":allArticles}

def addComment(req,id):
    form = CommentForm()
    if(req.method == "POST"):
        form = CommentForm(req.POST)
        if(form.is_valid()):
            comment = form.save(commit = False)
            comment.author = req.user
            comment.article = Article.objects.filter(id = id)[0]
            articlee = comment.article
            comment.save()
            messages.success(req,lang['commentAdded'])
            return HttpResponseRedirect("/articles/articledetail/"+id + "/")
        else:
            if(len(comment.content) > 4000):
                messages.success(req,lang['longComment'])
            return HttpResponseRedirect("/articles/articledetail/"+id + "/")
def addCommentComment(req,id):
    form = CommentForm(req.POST)
    articleId = req.POST.get("articleId")
    if(form.is_valid()):
        superComment = Comment.objects.get(id = id)
        content = form.cleaned_data.get("content")
        superComment.comments.append({"author":req.user.username,"content":content,"id":int(id)}) 
        superComment.save()
        messages.success(req,lang['commentAdded'])
        return HttpResponseRedirect("/articles/articledetail/" + articleId + "/")
    else:
        messages.info(req,lang['Comment is not Added'])
        return HttpResponseRedirect("/articles/articledetail/" + articleId + "/")

def commentLanguage(lang2):
    global lang
    global context
    lang = lang2
    context['lang'] = lang