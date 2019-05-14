from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Images

# Create your views here.


def images_today(request):
    date = dt.date.today()
    images = Images.todays_images()
    return render(request, 'all-images/today-images.html', {"date": date, "images": images})



def welcome(request):
    return render(request, 'welcome.html')


def images_of_day(request):
    date = dt.date.today()
    images = Images.todays_images()

    return render(request, 'all-images/today-images.html', {"date": date,"images": images})

def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_images(request, past_date):
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
        day = convert_dates(date)
        html = f'''
        <html>
            <body>
                <h1>Images for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
        return HttpResponse(html)


def past_days_images(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_today)

    images = Images.days_images(date)
    return render(request, 'all-images/past-images.html', {"date": date, "images": images})
def search_results(request):
    
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})


def image(request, image_id):
    try:
        article = Images.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-images/image.html", {"image": image})
