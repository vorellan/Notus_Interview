# global
from datetime import timedelta
# django
from django.core import serializers
from django.db.models import Max, Min
from django.http import HttpResponse
from django.shortcuts import render
# local
from ships.models import Ship, Terminal, Demand, Unload


def main(request):
    ship_set = Ship.objects.all()
    terminal_set = Terminal.objects.all()
    start_date = Demand.objects.all().aggregate(Min('date'))['date__min']
    end_date = Demand.objects.all().aggregate(Max('date'))['date__max']
    end_date += timedelta(days=1)
    table_data = {
        i: {
            terminal.id: [0 for j in range(ship_set.count() + 2)]
            for terminal in terminal_set
        }
        for i in daterange(start_date, end_date)
    }
    for terminal in terminal_set:
        for j in daterange(start_date, end_date):
            table_data[j][terminal.id][-1] += terminal.initial

    for demand in Demand.objects.all():
        table_data[demand.date][demand.terminal_id][0] = demand.demand
        for j in daterange(demand.date, end_date):
            table_data[j][demand.terminal_id][-1] -= demand.demand
    ship_aux_list = [i.id for i in ship_set]
    for unload in Unload.objects.all():
        j = ship_aux_list.index(unload.ship_id)
        table_data[unload.date][unload.terminal_id][j + 1] = unload.quantity
        for j in daterange(unload.date, end_date):
            table_data[j][unload.terminal_id][-1] += unload.quantity
    table_data = [
        [i.strftime("%d/%m/%Y")] +
        [k for j in terminal_set for k in table_data[i][j.id]]
        for i in table_data
    ]

    context = {
        "ship_set": ship_set,
        "terminal_set": terminal_set,
        "table_data": table_data,
        "ships_length": len(ship_set) + 2,
    }

    return render(request, "main.html", context)


def show_ship(request, ship_id):
    ship = Ship.objects.get(id=ship_id)
    data = serializers.serialize("json", [ship,])
    return HttpResponse(data, content_type='application/json')

def show_terminal(request, terminal_id):
    terminal = Terminal.objects.get(id=terminal_id)
    data = serializers.serialize("json", [terminal,])
    return HttpResponse(data, content_type='application/json')


def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)
