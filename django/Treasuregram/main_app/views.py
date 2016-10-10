from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Gold Nugget"
    value = 1000
    context = {
        "treasure_val" : value,
        "treasure_name" : name
    }
    return render(request, 'index.html', {'treasures' : treasures})

class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material =  material
        self.location = location

treasures = {
    Treasure('Gold Nugget', 1000, 'gold', 'Curly\'s Creek, NM'),
    Treasure('Coffee', 500, 'coffee grounds', 'Badasas City, CA'),
    Treasure('Silver', 5000, 'silver', "Silver falls, CA")
}
