import os,sys
import sqlite3
import pyttsx
from urllib2 import urlopen
import json
import googlemaps
import time
#gui_init
import the_gui_thing as gui
connection=sqlite3.connect("keywords.db",check_same_thread=False)
cursor=connection.cursor()
universal_pos=(600,300)

class inandout:
    mouth = pyttsx.init()
    mouth.setProperty('rate', 160)
    x = mouth.getProperty('voices')
    voices = mouth.setProperty('voices',x)
    def _mouth(self,y):
        self.mouth.say(y)
        gui.textdisp(y,universal_pos)
        self.mouth.runAndWait()
        pass
    def ears(self):
        x=raw_input("enter what you want")
        return x
class all_tools:
        #defult location
        my_location = ("13.106845307581308", "80.13495774473995")
        sample_location = ("", "")
        stack = []
        def_radius = 2000
        g = googlemaps.Client(key='gmaps API-key')
        weather_api_key = "wunderground-API key"
        location = "chennai"
        def netwrok_status(self):
            try:
                x=urlopen('http://www.google.com',timeout=5)
                return True
            except:return  False
        def en(self,x):
            return x.encode('ascii')

        def get_weather(self):
            request = (
                "http://api.wunderground.com/api/{0:s}/conditions/current/forecast10day/lang:english/q/{1:s}.json".format(
                    self.weather_api_key, self.location))
            data = urlopen(request)
            json_data = data.read()
            all_data = json.loads(json_data)
            return all_data

        def current_weather(self):
            weather = ""
            gui.textdisp("Aquiring weather info....",universal_pos)
            a = self.get_weather()
            current_obs = a['current_observation']
            c = current_obs['observation_location']
            wea_list = {"now":self.en(current_obs['weather']), "temperature": current_obs['temp_c'],
                        "feels like": self.en(current_obs['feelslike_c'])}
            for i in wea_list:
                a = i + ':' + str(wea_list[i])
                weather = weather + a + '\n'
            return weather

        def forecast_weather(self,a):
            print "forecast for next few days...:"
            forecast_obs = a['forecast']
            forecast = forecast_obs['txt_forecast']
            l = forecast['forecastday']
            for i in l:
                print i['title'], ':\n', i['fcttext']
            pass
        pass

        def current_location(self):
            full_data =self.g.reverse_geocode(self.my_location)
            y = full_data[0]['formatted_address']
            return y

        pass
class the_brains(all_tools,inandout):
    stk=[]
    flag = 0
    n=None
    al=all_tools()
    i=inandout()
    def __init__(self):
        import the_gui_thing as gui
        if os.path.isfile('keywords.db'):
            gui.textdisp("Database file successfully loaded",universal_pos)
            time.sleep(3)
            pass
        else:
            gui.textdisp("Database file not found",universal_pos)
            time.sleep(3)
        if self.al.netwrok_status():
            gui.textdisp("Connections are online",universal_pos)
            time.sleep(3)
        else:gui.textdisp("Only offline services are available, will inform when we are good to go",universal_pos)
        gui.textdisp("System initialisation complete",universal_pos)
        time.sleep(3)
        pass
    def add_keywords(self):
        fu = raw_input("enter function_name")
        y = raw_input("enter key1")
        z = raw_input("enter key2")
        cursor.execute("INSERT INTO all_tools (key1,key2,function_name) VALUES(?,?,?)", (y, z, fu))
        connection.commit()
        gui.textdisp("keyword successfully added",universal_pos)
        time.sleep(2)
        self.flag=2
        return 0
    def get_data(self):
        data_list=str(self.i.ears())
        return data_list
    def computation(self,x):
        print"here"
        self.flag=0
        dat=list(cursor.execute("SELECT key1,key2 FROM all_tools").fetchall())
        all_data=[i for a in dat for i in a]
        if ("add"and"keyword"or"keywords") in x:self.add_keywords()
        if "quit" in x:
            gui.textdisp("goodbye then",universal_pos)
            time.sleep(3)
            sys.exit()
        for y in x.split(" "):
            if y in all_data:
                self.flag +=1
                self.stk.append(y)
                if self.flag==2:
                    key2=self.stk.pop()
                    key1=self.stk.pop()
                    m=(cursor.execute("SELECT function_name FROM all_tools"
                                          " WHERE key1 =? AND key2 =?",(key1,key2,)).fetchall())
                    o= self.al.en(m[0][0])
                    n=getattr(self.al,"%s"%self.en(o))()
                    j._mouth(n)

        if self.flag==(0 or 1):
                gui.textdisp("im not programmed to do that kinda stuff",universal_pos)
        pass
j=inandout()
b=the_brains()
if __name__=="__main__":
    while 1:
        b.computation(b.get_data())
