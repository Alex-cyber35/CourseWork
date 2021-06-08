import requests
import json


def func():

    text = requests.post("https://api.waqi.info/search/?token=df2ca8f214faae22b2effd8c5130041f024967a6&keyword=Chelyabinsk")

    JsonData = text.text

    dictData = json.loads(JsonData)

    ParseDone = dictData["data"]

    return [ParseDone[9]['aqi']] + [str(ParseDone[9]['time']['stime'])]

    # функция возвращает список, где под индексом [0] - уровень загрязненности, а под [1] время последнего обновления




#print(func())
#print(func()[0]) вывод значения aqi отдельно
#print(func()[1]) вывод значения stime внутри time отдельно






#print("Привет! Вот такой показатель на данный момент:\t" + ParseDone[9]['aqi'])
#print("0-50 ХОРОШО\n" "51-100 УДОВЛИТВОРИТЕЛЬНОЕ\n" "101-150 НЕЗДОРОВЫЙ ДЛЯ ЧУВСТВИТЕЛЬНЫХ ГРУПП\n"
      #"151-200 НЕЗДОРОВЫЙ\n" "201-300 ОЧЕНЬ НЕЗДОРОВЫЙ\n" "300+ ОПАСНЫЙ")

#print("Последнее обновление было:\t" + ParseDone[9]['time']['stime'])
