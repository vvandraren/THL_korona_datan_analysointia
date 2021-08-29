import requests
import datetime
import pandas as pd

#Siivoa turha toisto eri funktioiden välillä


headers = {"Connection": "keep-alive", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}

def current_week():
    date = datetime.date.today()
    year, week_num, day_of_week = date.isocalendar()
    return week_num


def get_weekly_cases():

    url = "https://sampo.thl.fi/pivot/prod/fi/epirapo/covid19case/fact_epirapo_covid19case.json"
    r = requests.get(url, headers=headers)
    d = r.json()

    width = d['dataset']["dimension"]["size"][0]
    length = d['dataset']["dimension"]["size"][1]

    all_cases = d['dataset']['value']
    cases = []

    n = 0

    while n <= width * length:

        try:
            c = str(all_cases[str(n)])
            cases.append(int(c))
            n += 1

        except KeyError:
            cases.append(0)
            n += 1

    all_weeks = d['dataset']['dimension']["dateweek20200101"]["category"]["label"].values()
    weeks = [x for x in all_weeks]

    all_municipalities = d['dataset']['dimension']["hcdmunicipality2020"]["category"]["label"].values()
    municipalities = [x for x in all_municipalities]

    di = {"week": weeks[:-1]}
    n = 0

    for x in municipalities:
        c = cases[n:n+length]
        d[x] = c[:-1]
        n += length

    index = []
    nn = 0
    while nn < length-1:
        index.append("WC" + str(nn))
        nn += 1

    df = pd.DataFrame(data=di, index=index)

    return df


def get_weekly_vaccinations():

    url = "https://sampo.thl.fi/pivot/prod/fi/vaccreg/cov19cov/fact_cov19cov.json"
    r = requests.get(url, headers=headers)
    d = r.json()

    width = d['dataset']["dimension"]["size"][0]
    length = d['dataset']["dimension"]["size"][1]

    all_vaccinations = d['dataset']['value']
    vaccinations = []

    n = 0

    while n <= width * length:

        try:
            c = str(all_vaccinations[str(n)])
            vaccinations.append(int(c))
            n += 1

        except KeyError:
            vaccinations.append(0)
            n += 1

    all_weeks = d['dataset']['dimension']["dateweek20201226"]["category"]["label"].values()
    weeks = [x for x in all_weeks]

    all_municipalities = d['dataset']['dimension']["area"]["category"]["label"].values()
    municipalities = [x for x in all_municipalities]

    di = {"week": weeks[:-1]}
    n = 0

    for x in municipalities:
        c = vaccinations[n:n+length]
        d[x] = c[:-1]
        n += length

    index = []
    nn = 0
    while nn < length-1:
        index.append("WV" + str(nn))
        nn += 1

    df = pd.DataFrame(data=di, index=index)

    return df


def get_daily_second_vaccinations():
    url = "https://sampo.thl.fi/pivot/prod/fi/vaccreg/cov19cov/fact_cov19cov.json?filter=measure-533164&column=dateweek20201226-525459L"
    r = requests.get(url, headers=headers)
    d = r.json()

    vaccinations = [int(x) for x in d['dataset']['value'].values()]
    dates = list(d['dataset']['dimension']['dateweek20201226']['category']['label'].values())
    dates = dates[:len(dates)-1]


    di = {'date':dates, "vaccinations":vaccinations}

    index = []
    nn = 0
    for x in dates:
        index.append("DSV" + str(nn))
        nn += 1
        len(x) #Tämä on turha lisä jotta for in toimisi, muuta nätimmäksi

    df = pd.DataFrame(data=di, index=index)

    return df


def get_daily_first_vaccinations():
    url = "https://sampo.thl.fi/pivot/prod/fi/vaccreg/cov19cov/fact_cov19cov.json?filter=measure-533170&column=dateweek20201226-525459L"
    r = requests.get(url, headers=headers)
    d = r.json()

    vaccinations = [int(x) for x in d['dataset']['value'].values()]
    dates = list(d['dataset']['dimension']['dateweek20201226']['category']['label'].values())
    dates = dates[:len(dates)-1]


    di = {'date':dates, "vaccinations":vaccinations}

    index = []
    nn = 0
    for x in dates:
        index.append("DSV" + str(nn))
        nn += 1
        len(x) #Tämä on turha lisä jotta for in toimisi, muuta nätimmäksi

    df = pd.DataFrame(data=di, index=index)

    return df
