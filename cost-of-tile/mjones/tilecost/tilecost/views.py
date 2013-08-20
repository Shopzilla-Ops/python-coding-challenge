from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    """The home route, mapped to the "/" url route
    Handles our form submission and processing
    """
    if request.POST:
        post = request.POST.mixed()
        length = float(post['feetLength'])
        width = float(post['feetWidth'])
        cost = float(post['tileCost'])
        area = length * width
        totalcost = cost * area
        return { 'totalCost' : totalcost }
    else:
        return { 'totalCost' : False }
