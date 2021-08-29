import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def lr_first_vaccination_coverage(df):

    l = list(df['vaccinations'])
    y =np.cumsum(l)

    df['date'] = pd.to_datetime(df['date'])
    x = list(df['date'].map(dt.datetime.toordinal))
    x = np.array(x).reshape(-1, 1)

    model = LinearRegression()
    model.fit(x, y)
    r_sq = model.score(x, y)
    b0 = model.intercept_
    b1 = model.coef_

    x = [int(z) for z in x]
    n = x[-1] + 1

    data = {"date": x, "total vaccinations": y}
    df = pd.DataFrame(data)

    return df


def lr_second_vaccination_coverage(df):

    l = list(df['vaccinations'])
    y =np.cumsum(l)


    df['date'] = pd.to_datetime(df['date'])
    x = list(df['date'].map(dt.datetime.toordinal))
    x = np.array(x).reshape(-1, 1)

    model = LinearRegression()
    model.fit(x, y)
    r_sq = model.score(x, y)
    b0 = model.intercept_
    b1 = model.coef_

    x = [int(z) for z in x]
    y = [int(z) for z in y]

    x_new = add_dates(x, 200)
    y_new = [float(b0 + b1 * z) for z in x_new]

    y_new = y + y_new
    x_new = x + x_new

    return x_new, y_new


def add_dates(dates, n_to_future):

    date = dates[-1]
    n = 0
    new_dates = []

    while n < n_to_future:
        date += 1
        new_dates.append(date)
        n += 1

    return new_dates


def predict_coverage(dfv, dsv):

    first_vaccinations = list(dfv["vaccinations"].values)
    first_vaccinations = [int(x) for x in first_vaccinations]
    first_vaccinations = np.cumsum(first_vaccinations)

    first_dates = list(dfv["date"].values)

    second_vaccinations = list(dsv["vaccinations"].values)
    second_vaccinations = [int(x) for x in second_vaccinations]
    second_vaccinations = np.cumsum(second_vaccinations)

    second_dates = list(dsv['date'].map(dt.datetime.toordinal))

    n = 0

    for x in first_vaccinations:

        if x >= second_vaccinations[-1]:
            break
        else:
            n += 1

    future_vaccinations = first_vaccinations[n:]
    second_vaccinations = list(second_vaccinations) + list(future_vaccinations)

    print(second_vaccinations)

    last_date = second_dates[-1]

    while len(second_dates) != len(second_vaccinations):
        last_date += 1
        second_dates.append(last_date)

    print(second_dates)
    edate = dt.date.fromordinal(second_dates[-1])
    print(edate)

    n = 0

    for x in second_vaccinations:
        if x <= 3837329:
            n += 1
        else:
            print(dt.date.fromordinal(second_dates[n]))
            break







#test()
