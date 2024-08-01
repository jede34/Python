import json
import datetime

# Преобразуем строку в объект datetime
birthday_date = datetime.datetime.strptime("12.04", "%d.%m")

person = {
    "name": "Iryna",
    "age": 90,
    "is_adult": True,
    "birthday": birthday_date
}

class RecordEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%d.%m")
        return super().default(obj)

with open("person.json", "w") as file:
    json.dump(person, file, cls=RecordEncoder)
