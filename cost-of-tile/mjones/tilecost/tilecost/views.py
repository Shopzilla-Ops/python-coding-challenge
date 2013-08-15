from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    if request.POST:
        post = request.POST.mixed()
        length = int(post['feetLength'])
        width = int(post['feetWidth'])
        cost = int(post['tileCost'])
        area = length * width
        totalcost = cost * area
        return { 'totalCost' : totalcost }
    else:
        return { 'totalCost' : False }
