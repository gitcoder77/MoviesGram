from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from moviesgram.models import Movie, Category, Review, Language
from users.forms import UpdateForm
from users.models import Profile
from .forms import MovieForm


# Create your views here.
class index(ListView):
    model = Movie
    template_name = 'index.html'
    cats = Category.objects.all()
    langs = Language.objects.all()
    ordering = ['release_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        langs_menu = Language.objects.all()
        context = super(index, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["langs_menu"]=langs_menu
        return context

# class CategoryList(ListView):
#     model = Category
#     template_name = 'navbar.html'
#     cat_menu = Category.objects.all()
#     context = {'cat_menu': cat_menu }

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = ['name']
    success_url = 'addmovie.html'

class AddLanguageView(CreateView):
    model = Language
    template_name = 'add_language.html'
    fields = ['name']
    success_url = 'addmovie.html'

def CategoryView(request, cats):
    category = get_object_or_404(Category, slug=cats.replace('-',' '))
    category_movies = Movie.objects.filter(category=category)
    return render(request, 'categories.html', {'cats': cats.title, 'category_movies': category_movies})


def LanguageView(request, langs):
    language = get_object_or_404(Language, slug=langs.replace('-', ' '))
    language_movies = Movie.objects.filter(language=language)
    return render(request, 'languages.html', {'langs': langs.title, 'language_movies': language_movies})

# def allMovieCat(request, c_slug=None, ):
#     c_page = None
#     movies_list = None
#     if c_slug != None:
#         c_page = get_object_or_404(Category, slug=c_slug)
#         movies_list = Movie.objects.all().filter(category=c_page, available=True)
#     else:
#         movies_list = Movie.objects.all().filter(available=True)
#         paginator = Paginator(movies_list, 12)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except:
#         page = 1
#     try:
#         movies = paginator.page(page)
#     except(EmptyPage, InvalidPage):
#         movies = paginator.page(paginator.num_pages)
#     return render(request, "category.html", {'category': c_page, 'movies': movies})
#
#
# def allMovieLan(request, l_slug=None, ):
#     l_page = None
#     movies_list = None
#     if l_slug != None:
#         l_page = get_object_or_404(Category, slug=l_slug)
#         movie_list = Movie.objects.all().filter(language=l_slug, available=True)
#     else:
#         movies_list = Movie.objects.all().filter(available=True)
#         paginator = Paginator(movies_list, 12)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except:
#         page = 1
#     try:
#         movies = paginator.page(page)
#     except(EmptyPage, InvalidPage):
#         movies = paginator.page(paginator.num_pages)
#     return render(request, "index.html", {'language': l_page, 'movies': movies})


def MovieDetail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie.html', {'movie': movie})


# def Add_Edit_Movie(request, movie_id=None):
#     if movie_id:
#         movie = Movie.objects.get(pk=movie_id)
#         if movie.added_by != request.user:
#             # Redirect to a page indicating the user is not allowed to edit this movie
#             return redirect('movie_list')
#     else:
#         movie = None
#
#     if request.method == 'POST':
#         # Process the form data for adding/editing the movie
#         pass
#     return render(request, 'add_edit_movie.html', {'movie': movie})


def Movie_Review(request):
    id = request.GET.get('id')
    movie_details = Movie.objects.get(id=int(id))
    user = request.session['username']
    user_detail = Profile.objects.get(username=user)
    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        movie_review = request.POST.get('movie_review')

        movie_reviews = Review(user=user_detail, movie=movie_details, rating=star_rating, review_desp=movie_review)
        movie_reviews.save()

        rating_details = Review.objects.get(movie=movie_details)
        context = {'review': rating_details}
        return render(request, 'moviesgram/movies.html', context)
    rating_details = Review.objects.get(movie=movie_details)
    context = {'review': rating_details}
    return render(request, 'moviesgram/movies.html', context)


def user_movies(request):
    user_movies = Movie.objects.filter(added_by=request.user)
    return render(request, 'dashboard.html', {'user_movies': user_movies})


# class AddMovie(CreateView):
#     model = Movie
#     template_name = 'addmovie.html'
#     fields = ['name','actor','language','category','release_date','img','youtube','desc']
    
class AddMovie(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'addmovie.html'    
    

class MovieEditview(UpdateView):
    model = Movie
    template_name = 'editmovie.html'
    fields = ['name','actor','category','language','desc','release_date','img','youtube']
    success_url = reverse_lazy('MovieEditview')


class DeleteMovieView(DeleteView):
    model = Movie
    template_name = 'deletemovie.html'
    success_url = reverse_lazy('index.html')