from django.shortcuts import render


def home(request):

    template = 'westeros/home.html'
    context = {}

    return render(request, template, context)


def women(request):

    template = 'westeros/women.html'
    context = {}

    return render(request, template, context)


def men(request):

    template = 'westeros/men.html'
    context = {}

    return render(request, template, context)


def kids(request):

    template = 'westeros/kids.html'
    context = {}

    return render(request, template, context)


def merchandising(request):

    template = 'westeros/merchandising.html'
    context = {}

    return render(request, template, context)


def contact(request):

    template = 'westeros/contact.html'
    context = {}

    return render(request, template, context)


def wishlist(request):

    template = 'westeros/wishlist.html'
    context = {}

    return render(request, template, context)


def compare(request):

    template = 'westeros/compare.html'
    context = {}

    return render(request, template, context)


def product(request):

    template = 'westeros/product.html'
    context = {}

    return render(request, template, context)


def cart(request):

    template = 'westeros/cart.html'
    context = {}

    return render(request, template, context)


def checkout(request):

    template = 'westeros/checkout.html'
    context = {}

    return render(request, template, context)


def register(request):

    template = 'westeros/register.html'
    context = {}

    return render(request, template, context)


def profile(request):

    template = 'westeros/profile.html'
    context = {}

    return render(request, template, context)


def auth(request):

    template = 'westeros/auth.html'
    context = {}

    return render(request, template, context)


def blog(request):

    template = 'westeros/blog.html'
    context = {}

    return render(request, template, context)


def post(request):

    template = 'westeros/post.html'
    context = {}

    return render(request, template, context)


def page_not_found(request):

    template = '404.html'
    context = {}

    return render(request, template, context)
