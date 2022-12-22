from fastapi import FastAPI
from typing import Union
import pickle
import pandas as pd

app = FastAPI()

@app.get("/prediction/18")
async def read_item(Year: Union[str, None] = '2011',
                    month: Union[str, None] = '08',
                    day: Union[str,None] = '07',
                    hour: Union[str,None] = '18',
                    season: Union[str,None] = '2',
                    holiday: Union[int,None] = 0,
                    workingday: Union[int,None] = 1,
                    weather: Union[int,None]=1,
                    temp: Union[float,None] = 21.5,
                    atemp: Union[float,None] = 24.0,
                    humidity: Union[int,None] = 46,
                    windspeed: Union[float,None] = 23.4,
                    ):
    print(f"hour of the day :{hour}, month: {month}")
    pickled_model = pickle.load(open('bike_rental_model.pkl', 'rb'))
    X_user = pd.DataFrame({'Year': [str(Year)],
                           'month':[str(month)],
                           'day':[str(day)],
                           'hour': [str(hour)],
                           'season':[str(season)],
                           'holiday':[int(holiday)],
                           'workingday':[int(workingday)],
                           'weather': [int(weather)],
                           'temp': [float(temp)],
                           'atemp': [float(atemp)],
                           'humidity': [int(humidity)],
                           'windspeed': [float(windspeed)]
                           })
    pred = pickled_model.predict(X_user)
    print(pred)
    # import ipdb; ipdb.set_trace()
    return {"pred": round(pred[0][0],2)}
