#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""djangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import unicode_literals
from django.conf.urls import url,include
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import admin
from article.models import Article
from todo.models import Todo
from todo.todoViews import todoLanguage
from article.articleViews import articleLanguage
from users.userViews import userLanguage
from comment.commentViews import commentLanguage

from .language import *


context = {}
allArticles = 0
myTodos = 0
myArticles = 0
lang = en
def mainPage(req): 
    check(req)
    global lang
    global context
    context['lang'] = lang
    return render(req,"index.html",context)
    


def search(req):
    keywords = req.GET.get('keywords')
    if(keywords):
        articles = Article.objects.filter(title__contains = keywords)
        global context
        global lang
        context['articles'] = articles
        context['lang'] = lang
        return render(req,'allarticles.html',context)

def check(req):
    global context
    if(req.user.is_authenticated):
        allInfo(req)
        context = {
            "allArticles":allArticles,
            "myTodos":myTodos,
            "myArticles":myArticles
             }
    else:
        global allArticles
        allArticles = len(Article.objects.all())
        context = {"allArticles":allArticles}


def allInfo(req):
    global allArticles
    global myTodos
    global myArticles
    allArticles = len(Article.objects.all())
    myTodos = len(Todo.objects.filter(author = req.user))
    myArticles = len(Article.objects.filter(author = req.user))

def language(req):
    global lang
    global context
    if(lang['language'] == "ENGLISH"): lang = en
    else: lang = tr
    context['lang'] = lang

    todoLanguage(lang)
    articleLanguage(lang)
    userLanguage(lang)
    commentLanguage(lang)
    print()
    return redirect(req.GET.get("currentPage"))


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url('users/', include("users.userRoutes")),
    url("articles/",include("article.articleRoutes")),
    url("todos/",include("todo.todoRoutes")),
    url('search/',search,name = 'search'),
    url('comments/',include('comment.commentRoutes')),
    url('language/',language,name = "language"),
    url("",mainPage,name="mainPage")
]