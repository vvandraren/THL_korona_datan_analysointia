from get_data import current_week
import matplotlib.pyplot as plt


def plot_weekly_cases_country(df):

    cw = current_week()
    df.plot(x="week", y="Kaikki Alueet")

    plt.xlim(left=0, right=52+cw)
    plt.show()


def plot_weekly_cases_all(df):
    cw = current_week()
    df.plot(x="week")

    plt.xlim(left=0, right=52 + cw)
    plt.show()


def plot_weekly_vaccinations_country(df):

    cw = current_week()
    df.plot(x="week", y="Kaikki alueet")

    plt.xlim(left=0, right=cw)
    plt.show()


def plot_weekly_vaccinations_all(df):
    cw = current_week()
    df.plot(x="week")

    plt.xlim(left=0, right=cw)
    plt.show()


def plot_daily_second_vaccinations(df):
    print(df.dtypes)
    df.plot(x="date",)

    plt.show()


def predict_second_vaccination_coverage(x, y):

    plt.plot(x, y)
    plt.show()
