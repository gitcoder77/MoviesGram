from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from moviesgram.forms import MovieForm
from moviesgram.models import Movie, Category, Review, Language
from users.models import Profile


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
        context["langs_menu"] = langs_menu
        return context


def AddCategory(request):
    print("Add Category now")
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        add = Category(name=name, slug=slug)
        if add:
            add.save()
            messages.info(request, f'Category {name} Added Successfully')
            return redirect('moviesgram:AddMovie',)
        else:
            messages.info(request, 'Category Not Added Successfully')
            return redirect('moviesgram:AddMovie')
    return render(request, 'add_category.html')



def AddLanguage(request):
    print("Add Category now")
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        add = Language(name=name, slug=slug)
        if add:
            add.save()
            messages.info(request, f'Language {name} Added Successfully')
            return redirect('moviesgram:AddMovie')
        else:
            messages.info(request, 'Language Not Added Successfully')
            return redirect('moviesgram:AddMovie')
    return render(request, 'add_language.html')



def CategoryView(request, cats):
    category = get_object_or_404(Category, slug=cats.replace('-', ' '))
    category_movies = Movie.objects.filter(category=category)
    return render(request, 'categories.html', {'cats': cats.title, 'category_movies': category_movies})


def LanguageView(request, langs):
    language = get_object_or_404(Language, slug=langs.replace('-', ' '))
    language_movies = Movie.objects.filter(language=language)
    return render(request, 'languages.html', {'langs': langs.title, 'language_movies': language_movies})


def MovieDetail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie.html', {'movie': movie})


def add_movie(request):
    category = Category.objects.all()
    language = Language.objects.all()
    user_name = request.session.get('username', '')
    if request.method =='POST':
        name = request.POST.get('name')
        actor = request.POST.get('actor')
        language_id = request.POST.get('language')
        release_date = request.POST.get('release_date')
        category_id = request.POST.get('category')
        desc = request.POST.get('desc')
        img = request.FILES.get('img')  # Use get to handle missing files
        youtube = request.POST.get('youtube')
        added_by = user_name
        print(img)
        
        language_instance = Language.objects.get(id=language_id)
        category_instance = Category.objects.get(id=category_id)
        add = Movie(name=name, desc=desc, img=img, actor=actor,release_date=release_date, youtube=youtube, added_by = added_by,category=category_instance, language = language_instance)
        if add:
            add.save()
            messages.info(request, 'Movie Added Successfully')
            return redirect('moviesgram:index')
        else:
            messages.info(request, 'Movie Not Added Successfully')
            return redirect(add_movie)
    return render(request, 'add_movie.html',{'category' : category, 'language': language,'user_name':user_name})


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
    user_name = request.session['username']
    user_movies = Movie.objects.filter(added_by=user_name)
    return render(request, 'dashboard.html', {'user_movies': user_movies})


def updatemovie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    print("movie", movie)
    if form.is_valid():
        form.save()
        return redirect('users:dashboard')
    return render(request, 'editmovie.html', {'form': form, 'movie': movie})


def delete(request,movie_id):
    if request.method=='POST':
        movie=Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('users:dashboard')
    return render(request,'deletemovie.html')
