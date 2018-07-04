from django.db import migrations
from datetime import datetime, timedelta


def create_ships(apps, schema_editor):
    Ship = apps.get_model('ships', 'Ship')
    data = [["SM1", 1500], ["SM2", 2500], ["SM3", 2500], ["LG1", 16000], ["MD1", 10000]]
    ships = []
    for name, capacity in data:
        ships.append(Ship(name=name, capacity=capacity))
    Ship.objects.bulk_create(ships)

    Terminal = apps.get_model('ships', 'Terminal')
    Terminal(name="T1", capacity=30000, initial=9540).save()
    Terminal(name="T2", capacity=10000, initial=1450).save()

    Terminal = apps.get_model('ships', 'Terminal')
    Demand = apps.get_model('ships', 'Demand')
    T1 = Terminal.objects.get(name="T1")
    T2 = Terminal.objects.get(name="T2")
    initial_date = datetime(2018, 1, 1)
    demand_set = []
    for i in range(40):
        date = initial_date + timedelta(days=i)
        demand_set.append(Demand(terminal=T1, date=date, demand=850))
        demand_set.append(Demand(terminal=T2, date=date, demand=200))
    for i in range(40, 80):
        date = initial_date + timedelta(days=i)
        demand_set.append(Demand(terminal=T1, date=date, demand=1000))
        demand_set.append(Demand(terminal=T2, date=date, demand=150))
    for i in range(80, 120):
        date = initial_date + timedelta(days=i)
        demand_set.append(Demand(terminal=T1, date=date, demand=750))
        demand_set.append(Demand(terminal=T2, date=date, demand=200))
    for i in range(120, 240):
        date = initial_date + timedelta(days=i)
        demand_set.append(Demand(terminal=T1, date=date, demand=650))
        demand_set.append(Demand(terminal=T2, date=date, demand=250))
    Demand.objects.bulk_create(demand_set)

    Terminal = apps.get_model('ships', 'Terminal')
    Ship = apps.get_model('ships', 'Ship')
    Unload = apps.get_model('ships', 'Unload')
    initial_date = datetime(2018, 1, 1)
    data = {
        "SM1": [9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139, 149, 159, 169, 179, 189, 199, 209, 219],
        "SM2": [24, 49, 74, 99, 124, 149, 174, 199, 224],
        "SM3": [32, 37, 61, 66, 71, 76, 81, 107, 113],
        "LG1": [4, 44, 84, 124, 164, 199, 234],
    }
    unloads = []
    for name in data:
        ship = Ship.objects.get(name=name)
        for i in data[name]:
            date = initial_date + timedelta(days=i)
            unloads.append(Unload(ship=ship, terminal=T1, date=date, quantity=ship.capacity))

    MD1_unloads = [2, 42, 82, 114, 146, 178, 210]
    MD1 = Ship.objects.get(name="MD1")
    for i in MD1_unloads:
        date = initial_date + timedelta(days=i)
        unloads.append(Unload(ship=MD1, terminal=T2, date=date, quantity=MD1.capacity))
    Unload.objects.bulk_create(unloads)


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_ships),
    ]