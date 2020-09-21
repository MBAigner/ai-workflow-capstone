
import os
from os import path

LOG_PATH = os.path.join("..", "logs")
TRAIN_LOG = "train_log.csv"
PREDICT_LOG = "predict_log.csv"


def update_train_log(tag, dates, rmse, runtime, version, version_note, test):
    file = path.join(LOG_PATH, TRAIN_LOG)
    if not path.exists(file):
        f = open(file, "w")
        f.write("tag;dates;rmse;runtime;version;version_note;source\n")
        f.close()
    f = open(file, "a")
    row = ";".join([tag, str(dates), str(rmse["rmse"]), str(runtime), str(version), version_note,
                    "test" if test else "prod"])
    f.write(row + "\n")
    f.close()


def update_predict_log(country,y_pred,y_proba,target_date, runtime, version, test):
    file = path.join(LOG_PATH, PREDICT_LOG)
    if not path.exists(file):
        f = open(file, "w")
        f.write("country;y_pred;y_proba;target_date;runtime;version;source\n")
        f.close()
    f = open(file, "a")
    row = ";".join([str(country), str(y_pred), str(y_proba), str(target_date), str(runtime),
                    str(version), "test" if test else "prod"])
    f.write(row + "\n")
    f.close()
