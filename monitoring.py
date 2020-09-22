import requests
import pandas as pd
from cslib import engineer_features
import json
import numpy as np
import matplotlib.pyplot as plt


country = "all"  # set country for monitoring


def get_targets(country):
    df = pd.read_csv("./data/cs-train/ts-data/ts-"+country+".csv")
    X, y, dates = engineer_features(df)
    dates_new = []
    targets_new = []
    for i, date in enumerate(dates):
        date = str(date)
        year,month,day = date.split("-")
        date = day+"."+month+"."+year
        if "15." in date:  # always test for 15th day of month
            dates_new.append(date)
            targets_new.append(y[i])
    return targets_new, dates_new


def get_predictions(country, dates):
    predictions = []
    for date in dates:
        request = {"date": date,
                   "country": country}
        r = requests.post("http://0.0.0.0:8080/predict",
                          json=request)
        res = json.loads(r.text)
        predictions.append(res["prediction"])
    return predictions


def get_rmse(acts, preds):
    mse = 0
    for i, y in enumerate(acts):
        pred = preds[i]
        mse = mse + (pred-y)*(pred-y)
    return np.sqrt(mse)


y, dates = get_targets(country)
baseline = np.mean(y)
baseline_pred = [baseline]*len(y)
predictions = get_predictions(country, dates)
print("Baseline RMSE: " + str(get_rmse(y, baseline_pred)))
print("Model RMSE: " + str(get_rmse(y, predictions)))

plt.scatter(predictions, y)
plt.axhline(y=baseline, color='r', linestyle='-')
plt.show()
