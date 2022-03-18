#!/usr/bin/python3
import json # json структура

from flask import Flask, request # http сервер

app = Flask(__name__) #создаём экземпляр класса

#читаем файл и сохраняем данные в память 
data = []
f = open('RU.txt', 'r', encoding='utf-8')
for line in f:
    data.append(line.split('\t'))


#Главная страница
@app.route('/')
def hello_world():
    return "Hello World!"


# task 1
# http://127.0.0.1:8000/task1?id=451811
@app.route('/task1', methods=['GET'])
def task1():

    try:
        val = int(request.args.get('id'))
    except ValueError:
        return "Task1: '" + str(request.args.get('id')) + "' is not a int"
    except Exception:
        return "Task1: Error"
    else:
    	# Интерполяционный поиск
        low = 0
        high = (len(data) - 1)
        while low <= high and val >= int(data[low][0]) and val <= int(data[high][0]):
            index = low + int(((float(high - low) / ( int(data[high][0]) - int(data[low][0]))) * ( val - int(data[low][0]))))
            if int(data[index][0]) == val:
                return json.dumps(data[index], ensure_ascii=False)
            if int(data[index][0]) < val:
                low = index + 1
            else:
                high = index - 1

        return "Task1: no solve"

   
# task 2
# http://127.0.0.1:8000/task2?num=2&count=3
@app.route('/task2', methods=['GET'])
def task2():
    try:
        num = int(request.args.get('num'))
        count = int(request.args.get('count'))
    except ValueError:
        return "Task2: '" + str(request.args.get('num'))  + "' or '" + str(request.args.get('count')) + "' is not a int"
    except Exception:
        return "Task2: Error"
    else:

        if (num>0) and (count>0) and (len(data)>num*count-1):
            temp_data = []

            for i in range(count):
                temp_data.append(data[(num-1)*count+i])

            return json.dumps(temp_data, ensure_ascii=False)
        else:
            return "Task2: out of range"


# Словарь часовых поясов с файла timeZones.txt
timezone = {
    "Africa/Abidjan": 0.0,
    "Africa/Accra": 0.0,
    "Africa/Addis_Ababa": 3.0,
    "Africa/Algiers": 1.0,
    "Africa/Asmara": 3.0,
    "Africa/Bamako": 0.0,
    "Africa/Bangui": 1.0,
    "Africa/Banjul": 0.0,
    "Africa/Bissau": 0.0,
    "Africa/Blantyre": 2.0,
    "Africa/Brazzaville": 1.0,
    "Africa/Bujumbura": 2.0,
    "Africa/Cairo": 2.0,
    "Africa/Casablanca": 1.0,
    "Africa/Ceuta": 1.0,
    "Africa/Conakry": 0.0,
    "Africa/Dakar": 0.0,
    "Africa/Dar_es_Salaam": 3.0,
    "Africa/Djibouti": 3.0,
    "Africa/Douala": 1.0,
    "Africa/El_Aaiun": 1.0,
    "Africa/Freetown": 0.0,
    "Africa/Gaborone": 2.0,
    "Africa/Harare": 2.0,
    "Africa/Johannesburg": 2.0,
    "Africa/Juba": 2.0,
    "Africa/Kampala": 3.0,
    "Africa/Khartoum": 2.0,
    "Africa/Kigali": 2.0,
    "Africa/Kinshasa": 1.0,
    "Africa/Lagos": 1.0,
    "Africa/Libreville": 1.0,
    "Africa/Lome": 0.0,
    "Africa/Luanda": 1.0,
    "Africa/Lubumbashi": 2.0,
    "Africa/Lusaka": 2.0,
    "Africa/Malabo": 1.0,
    "Africa/Maputo": 2.0,
    "Africa/Maseru": 2.0,
    "Africa/Mbabane": 2.0,
    "Africa/Mogadishu": 3.0,
    "Africa/Monrovia": 0.0,
    "Africa/Nairobi": 3.0,
    "Africa/Ndjamena": 1.0,
    "Africa/Niamey": 1.0,
    "Africa/Nouakchott": 0.0,
    "Africa/Ouagadougou": 0.0,
    "Africa/Porto-Novo": 1.0,
    "Africa/Sao_Tome": 0.0,
    "Africa/Tripoli": 2.0,
    "Africa/Tunis": 1.0,
    "Africa/Windhoek": 2.0,
    "America/Adak": -10.0,
    "America/Anchorage": -9.0,
    "America/Anguilla": -4.0,
    "America/Antigua": -4.0,
    "America/Araguaina": -3.0,
    "America/Argentina/Buenos_Aires": -3.0,
    "America/Argentina/Catamarca": -3.0,
    "America/Argentina/Cordoba": -3.0,
    "America/Argentina/Jujuy": -3.0,
    "America/Argentina/La_Rioja": -3.0,
    "America/Argentina/Mendoza": -3.0,
    "America/Argentina/Rio_Gallegos": -3.0,
    "America/Argentina/Salta": -3.0,
    "America/Argentina/San_Juan": -3.0,
    "America/Argentina/San_Luis": -3.0,
    "America/Argentina/Tucuman": -3.0,
    "America/Argentina/Ushuaia": -3.0,
    "America/Aruba": -4.0,
    "America/Asuncion": -3.0,
    "America/Atikokan": -5.0,
    "America/Bahia": -3.0,
    "America/Bahia_Banderas": -6.0,
    "America/Barbados": -4.0,
    "America/Belem": -3.0,
    "America/Belize": -6.0,
    "America/Blanc-Sablon": -4.0,
    "America/Boa_Vista": -4.0,
    "America/Bogota": -5.0,
    "America/Boise": -7.0,
    "America/Cambridge_Bay": -7.0,
    "America/Campo_Grande": -4.0,
    "America/Cancun": -5.0,
    "America/Caracas": -4.0,
    "America/Cayenne": -3.0,
    "America/Cayman": -5.0,
    "America/Chicago": -6.0,
    "America/Chihuahua": -7.0,
    "America/Costa_Rica": -6.0,
    "America/Creston": -7.0,
    "America/Cuiaba": -4.0,
    "America/Curacao": -4.0,
    "America/Danmarkshavn": 0.0,
    "America/Dawson": -7.0,
    "America/Dawson_Creek": -7.0,
    "America/Denver": -7.0,
    "America/Detroit": -5.0,
    "America/Dominica": -4.0,
    "America/Edmonton": -7.0,
    "America/Eirunepe": -5.0,
    "America/El_Salvador": -6.0,
    "America/Fort_Nelson": -7.0,
    "America/Fortaleza": -3.0,
    "America/Glace_Bay": -4.0,
    "America/Goose_Bay": -4.0,
    "America/Grand_Turk": -5.0,
    "America/Grenada": -4.0,
    "America/Guadeloupe": -4.0,
    "America/Guatemala": -6.0,
    "America/Guayaquil": -5.0,
    "America/Guyana": -4.0,
    "America/Halifax": -4.0,
    "America/Havana": -5.0,
    "America/Hermosillo": -7.0,
    "America/Indiana/Indianapolis": -5.0,
    "America/Indiana/Knox": -6.0,
    "America/Indiana/Marengo": -5.0,
    "America/Indiana/Petersburg": -5.0,
    "America/Indiana/Tell_City": -6.0,
    "America/Indiana/Vevay": -5.0,
    "America/Indiana/Vincennes": -5.0,
    "America/Indiana/Winamac": -5.0,
    "America/Inuvik": -7.0,
    "America/Iqaluit": -5.0,
    "America/Jamaica": -5.0,
    "America/Juneau": -9.0,
    "America/Kentucky/Louisville": -5.0,
    "America/Kentucky/Monticello": -5.0,
    "America/Kralendijk": -4.0,
    "America/La_Paz": -4.0,
    "America/Lima": -5.0,
    "America/Los_Angeles": -8.0,
    "America/Lower_Princes": -4.0,
    "America/Maceio": -3.0,
    "America/Managua": -6.0,
    "America/Manaus": -4.0,
    "America/Marigot": -4.0,
    "America/Martinique": -4.0,
    "America/Matamoros": -6.0,
    "America/Mazatlan": -7.0,
    "America/Menominee": -6.0,
    "America/Merida": -6.0,
    "America/Metlakatla": -9.0,
    "America/Mexico_City": -6.0,
    "America/Miquelon": -3.0,
    "America/Moncton": -4.0,
    "America/Monterrey": -6.0,
    "America/Montevideo": -3.0,
    "America/Montserrat": -4.0,
    "America/Nassau": -5.0,
    "America/New_York": -5.0,
    "America/Nipigon": -5.0,
    "America/Nome": -9.0,
    "America/Noronha": -2.0,
    "America/North_Dakota/Beulah": -6.0,
    "America/North_Dakota/Center": -6.0,
    "America/North_Dakota/New_Salem": -6.0,
    "America/Nuuk": -3.0,
    "America/Ojinaga": -7.0,
    "America/Panama": -5.0,
    "America/Pangnirtung": -5.0,
    "America/Paramaribo": -3.0,
    "America/Phoenix": -7.0,
    "America/Port-au-Prince": -5.0,
    "America/Port_of_Spain": -4.0,
    "America/Porto_Velho": -4.0,
    "America/Puerto_Rico": -4.0,
    "America/Punta_Arenas": -3.0,
    "America/Rainy_River": -6.0,
    "America/Rankin_Inlet": -6.0,
    "America/Recife": -3.0,
    "America/Regina": -6.0,
    "America/Resolute": -6.0,
    "America/Rio_Branco": -5.0,
    "America/Santarem": -3.0,
    "America/Santiago": -3.0,
    "America/Santo_Domingo": -4.0,
    "America/Sao_Paulo": -3.0,
    "America/Scoresbysund": -1.0,
    "America/Sitka": -9.0,
    "America/St_Barthelemy": -4.0,
    "America/St_Johns": -3.5,
    "America/St_Kitts": -4.0,
    "America/St_Lucia": -4.0,
    "America/St_Thomas": -4.0,
    "America/St_Vincent": -4.0,
    "America/Swift_Current": -6.0,
    "America/Tegucigalpa": -6.0,
    "America/Thule": -4.0,
    "America/Thunder_Bay": -5.0,
    "America/Tijuana": -8.0,
    "America/Toronto": -5.0,
    "America/Tortola": -4.0,
    "America/Vancouver": -8.0,
    "America/Whitehorse": -7.0,
    "America/Winnipeg": -6.0,
    "America/Yakutat": -9.0,
    "America/Yellowknife": -7.0,
    "Antarctica/Casey": 11.0,
    "Antarctica/Davis": 7.0,
    "Antarctica/DumontDUrville": 10.0,
    "Antarctica/Macquarie": 11.0,
    "Antarctica/Mawson": 5.0,
    "Antarctica/McMurdo": 13.0,
    "Antarctica/Palmer": -3.0,
    "Antarctica/Rothera": -3.0,
    "Antarctica/Syowa": 3.0,
    "Antarctica/Troll": 0.0,
    "Antarctica/Vostok": 6.0,
    "Arctic/Longyearbyen": 1.0,
    "Asia/Aden": 3.0,
    "Asia/Almaty": 6.0,
    "Asia/Amman": 2.0,
    "Asia/Anadyr": 12.0,
    "Asia/Aqtau": 5.0,
    "Asia/Aqtobe": 5.0,
    "Asia/Ashgabat": 5.0,
    "Asia/Atyrau": 5.0,
    "Asia/Baghdad": 3.0,
    "Asia/Bahrain": 3.0,
    "Asia/Baku": 4.0,
    "Asia/Bangkok": 7.0,
    "Asia/Barnaul": 7.0,
    "Asia/Beirut": 2.0,
    "Asia/Bishkek": 6.0,
    "Asia/Brunei": 8.0,
    "Asia/Chita": 9.0,
    "Asia/Choibalsan": 8.0,
    "Asia/Colombo": 5.5,
    "Asia/Damascus": 2.0,
    "Asia/Dhaka": 6.0,
    "Asia/Dili": 9.0,
    "Asia/Dubai": 4.0,
    "Asia/Dushanbe": 5.0,
    "Asia/Famagusta": 2.0,
    "Asia/Gaza": 2.0,
    "Asia/Hebron": 2.0,
    "Asia/Ho_Chi_Minh": 7.0,
    "Asia/Hong_Kong": 8.0,
    "Asia/Hovd": 7.0,
    "Asia/Irkutsk": 8.0,
    "Asia/Jakarta": 7.0,
    "Asia/Jayapura": 9.0,
    "Asia/Jerusalem": 2.0,
    "Asia/Kabul": 4.5,
    "Asia/Kamchatka": 12.0,
    "Asia/Karachi": 5.0,
    "Asia/Kathmandu": 5.75,
    "Asia/Khandyga": 9.0,
    "Asia/Kolkata": 5.5,
    "Asia/Krasnoyarsk": 7.0,
    "Asia/Kuala_Lumpur": 8.0,
    "Asia/Kuching": 8.0,
    "Asia/Kuwait": 3.0,
    "Asia/Macau": 8.0,
    "Asia/Magadan": 11.0,
    "Asia/Makassar": 8.0,
    "Asia/Manila": 8.0,
    "Asia/Muscat": 4.0,
    "Asia/Nicosia": 2.0,
    "Asia/Novokuznetsk": 7.0,
    "Asia/Novosibirsk": 7.0,
    "Asia/Omsk": 6.0,
    "Asia/Oral": 5.0,
    "Asia/Phnom_Penh": 7.0,
    "Asia/Pontianak": 7.0,
    "Asia/Pyongyang": 9.0,
    "Asia/Qatar": 3.0,
    "Asia/Qostanay": 6.0,
    "Asia/Qyzylorda": 5.0,
    "Asia/Riyadh": 3.0,
    "Asia/Sakhalin": 11.0,
    "Asia/Samarkand": 5.0,
    "Asia/Seoul": 9.0,
    "Asia/Shanghai": 8.0,
    "Asia/Singapore": 8.0,
    "Asia/Srednekolymsk": 11.0,
    "Asia/Taipei": 8.0,
    "Asia/Tashkent": 5.0,
    "Asia/Tbilisi": 4.0,
    "Asia/Tehran": 3.5,
    "Asia/Thimphu": 6.0,
    "Asia/Tokyo": 9.0,
    "Asia/Tomsk": 7.0,
    "Asia/Ulaanbaatar": 8.0,
    "Asia/Urumqi": 6.0,
    "Asia/Ust-Nera": 10.0,
    "Asia/Vientiane": 7.0,
    "Asia/Vladivostok": 10.0,
    "Asia/Yakutsk": 9.0,
    "Asia/Yangon": 6.5,
    "Asia/Yekaterinburg": 5.0,
    "Asia/Yerevan": 4.0,
    "Atlantic/Azores": -1.0,
    "Atlantic/Bermuda": -4.0,
    "Atlantic/Canary": 0.0,
    "Atlantic/Cape_Verde": -1.0,
    "Atlantic/Faroe": 0.0,
    "Atlantic/Madeira": 0.0,
    "Atlantic/Reykjavik": 0.0,
    "Atlantic/South_Georgia": -2.0,
    "Atlantic/St_Helena": 0.0,
    "Atlantic/Stanley": -3.0,
    "Australia/Adelaide": 10.5,
    "Australia/Brisbane": 10.0,
    "Australia/Broken_Hill": 10.5,
    "Australia/Darwin": 9.5,
    "Australia/Eucla": 8.75,
    "Australia/Hobart": 11.0,
    "Australia/Lindeman": 10.0,
    "Australia/Lord_Howe": 11.0,
    "Australia/Melbourne": 11.0,
    "Australia/Perth": 8.0,
    "Australia/Sydney": 11.0,
    "Europe/Amsterdam": 1.0,
    "Europe/Andorra": 1.0,
    "Europe/Astrakhan": 4.0,
    "Europe/Athens": 2.0,
    "Europe/Belgrade": 1.0,
    "Europe/Berlin": 1.0,
    "Europe/Bratislava": 1.0,
    "Europe/Brussels": 1.0,
    "Europe/Bucharest": 2.0,
    "Europe/Budapest": 1.0,
    "Europe/Busingen": 1.0,
    "Europe/Chisinau": 2.0,
    "Europe/Copenhagen": 1.0,
    "Europe/Dublin": 0.0,
    "Europe/Gibraltar": 1.0,
    "Europe/Guernsey": 0.0,
    "Europe/Helsinki": 2.0,
    "Europe/Isle_of_Man": 0.0,
    "Europe/Istanbul": 3.0,
    "Europe/Jersey": 0.0,
    "Europe/Kaliningrad": 2.0,
    "Europe/Kiev": 2.0,
    "Europe/Kirov": 3.0,
    "Europe/Lisbon": 0.0,
    "Europe/Ljubljana": 1.0,
    "Europe/London": 0.0,
    "Europe/Luxembourg": 1.0,
    "Europe/Madrid": 1.0,
    "Europe/Malta": 1.0,
    "Europe/Mariehamn": 2.0,
    "Europe/Minsk": 3.0,
    "Europe/Monaco": 1.0,
    "Europe/Moscow": 3.0,
    "Europe/Oslo": 1.0,
    "Europe/Paris": 1.0,
    "Europe/Podgorica": 1.0,
    "Europe/Prague": 1.0,
    "Europe/Riga": 2.0,
    "Europe/Rome": 1.0,
    "Europe/Samara": 4.0,
    "Europe/San_Marino": 1.0,
    "Europe/Sarajevo": 1.0,
    "Europe/Saratov": 4.0,
    "Europe/Simferopol": 3.0,
    "Europe/Skopje": 1.0,
    "Europe/Sofia": 2.0,
    "Europe/Stockholm": 1.0,
    "Europe/Tallinn": 2.0,
    "Europe/Tirane": 1.0,
    "Europe/Ulyanovsk": 4.0,
    "Europe/Uzhgorod": 2.0,
    "Europe/Vaduz": 1.0,
    "Europe/Vatican": 1.0,
    "Europe/Vienna": 1.0,
    "Europe/Vilnius": 2.0,
    "Europe/Volgograd": 3.0,
    "Europe/Warsaw": 1.0,
    "Europe/Zagreb": 1.0,
    "Europe/Zaporozhye": 2.0,
    "Europe/Zurich": 1.0,
    "Indian/Antananarivo": 3.0,
    "Indian/Chagos": 6.0,
    "Indian/Christmas": 7.0,
    "Indian/Cocos": 6.5,
    "Indian/Comoro": 3.0,
    "Indian/Kerguelen": 5.0,
    "Indian/Mahe": 4.0,
    "Indian/Maldives": 5.0,
    "Indian/Mauritius": 4.0,
    "Indian/Mayotte": 3.0,
    "Indian/Reunion": 4.0,
    "Pacific/Apia": 13.0,
    "Pacific/Auckland": 13.0,
    "Pacific/Bougainville": 11.0,
    "Pacific/Chatham": 13.75,
    "Pacific/Chuuk": 10.0,
    "Pacific/Easter": -5.0,
    "Pacific/Efate": 11.0,
    "Pacific/Fakaofo": 13.0,
    "Pacific/Fiji": 12.0,
    "Pacific/Funafuti": 12.0,
    "Pacific/Galapagos": -6.0,
    "Pacific/Gambier": -9.0,
    "Pacific/Guadalcanal": 11.0,
    "Pacific/Guam": 10.0,
    "Pacific/Honolulu": -10.0,
    "Pacific/Kanton": 13.0,
    "Pacific/Kiritimati": 14.0,
    "Pacific/Kosrae": 11.0,
    "Pacific/Kwajalein": 12.0,
    "Pacific/Majuro": 12.0,
    "Pacific/Marquesas": -9.5,
    "Pacific/Midway": -11.0,
    "Pacific/Nauru": 12.0,
    "Pacific/Niue": -11.0,
    "Pacific/Norfolk": 12.0,
    "Pacific/Noumea": 11.0,
    "Pacific/Pago_Pago": -11.0,
    "Pacific/Palau": 9.0,
    "Pacific/Pitcairn": -8.0,
    "Pacific/Pohnpei": 11.0,
    "Pacific/Port_Moresby": 10.0,
    "Pacific/Rarotonga": -10.0,
    "Pacific/Saipan": 10.0,
    "Pacific/Tahiti": -10.0,
    "Pacific/Tarawa": 12.0,
    "Pacific/Tongatapu": 13.0,
    "Pacific/Wake": 12.0,
    "Pacific/Wallis": 12.0
}



# task 3
# http://127.0.0.1:8000/task2?city1=Ефремово&city2=Вороново
@app.route('/task3', methods=['GET'])
def task3():
    try:
        city_name_1 = str(request.args.get('city1'))
        city_name_2 = str(request.args.get('city2'))
    except ValueError:
        return "Task3: '" + str(request.args.get('city1')) + "' or '" + str(request.args.get('city2')) + "' is not a string"
    except Exception:
        return "Task3: Error"
    else:
        #поиск записей с наибольшим населением
        max_1 = -1
        max_2 = -1
        max_i1 = -1
        max_i2 = -1
        for i, value in enumerate(data):
            if city_name_1 in value[3].split(','):
                if int(value[14]) > max_1:
                    max_1=int(value[14])
                    max_i1=i
            if city_name_2 in value[3].split(','):
                if int(value[14]) > max_2:
                    max_2=int(value[14])
                    max_i2=i


        #формирование структуры для ответа
        strin=""
        if (max_i1<0) and (max_i2<0):
            all =["'" + str(request.args.get('city1')) + "' no solve", "'" + str(request.args.get('city2')) + "' no solve", "no solve"]
        else:
            if (max_i1<0):
                all =["'" + str(request.args.get('city1')) + "' no solve", data[max_i2], "no solve"]
            else:
                if (max_i2<0):
                    all =[data[max_i2], "'" + str(request.args.get('city2')) + "' no solve", "no solve"]
                else:
    
                    if data[max_i1][4]>=data[max_i2][4]:
                        strin=strin+"Город, расположенный севернее: " + str(city_name_1 + ". ")
                    else:
                        strin=strin+"Город, расположенный севернее: " + str(city_name_2 + ". ")

                    if data[max_i1][17]!=data[max_i2][17]:
                        strin=strin + "Часовой пояс разный: " + str(abs(timezone[data[max_i1][17]]-timezone[data[max_i2][17]])) + ". "
                    else:
                        strin=strin + "Часовой пояс одинаковый. "
                
                    
                    all =[data[max_i1], data[max_i2], strin]

        return json.dumps(all, ensure_ascii=False)


# task 4 - Дополнительно задание, поиск названия города по его началу 
# http://127.0.0.1:8000/task4?city=Ефрем
@app.route('/task4', methods=['GET'])
def task4():
    try:
        city = str(request.args.get('city'))
    except ValueError:
        return "Task4: '" + str(request.args.get('city')) + "' is not a string"
    except Exception:
        return "Task4: Error"
    else:
        all=[]
        for line in data:
            for i in line[3].split(','):
                if i.startswith(city):
                    all.append(i)
        
        return json.dumps(all, ensure_ascii=False)



#Запуск сервера (проверка, что это исполняемое приложение, а не модуль) 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)

