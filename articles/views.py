from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def articles_view(request):
    articles = Article.objects.all()
    return render(request, "articles/articles_page.html", {"articles": articles})


@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()

            messages.success(request, "Article created successfully!")
            return redirect("articles")
    else:
        form = ArticleForm()

    return render(request, "articles/add_article_page.html", {"form": form})


@login_required
def detailed_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, "articles/detailed_article.html", {"article": article})


@login_required
def delete_article(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    messages.success(request, "Article deleted successfully!")
    return redirect("articles")


def article_edit(request, id):
    article = Article.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")

        if title and body:
            article.title = title
            article.body = body
            article.save()
            messages.success(request, "Article updated successfully!")
            return redirect("detailed_article", id=id)
        else:
            messages.error(request, "Title and body are required.")

    return render(request, "articles/edit_article_page.html", {"article": article})
