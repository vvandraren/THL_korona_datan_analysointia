import get_data
import print_data
import data_analysis


def main():
    wc = get_data.get_weekly_cases()
    wv = get_data.get_weekly_vaccinations()
    dsv = get_data.get_daily_second_vaccinations()
    dfv = get_data.get_daily_first_vaccinations()

    #print_data.plot_weekly_cases_country(wc)
    #print_data.plot_weekly_cases_all(wc)

    #print_data.plot_weekly_vaccinations_country(wv)
    #print_data.plot_weekly_vaccinations_all(wv)
    #print_data.plot_daily_second_vaccinations(dsv)

    dff = data_analysis.lr_first_vaccination_coverage(dfv)
    print()
    x, y = data_analysis.lr_second_vaccination_coverage(dsv)
    print()
    #print_data.predict_second_vaccination_coverage(x, y)
    data_analysis.predict_coverage(dfv, dsv)


if __name__ == '__main__':
    main()
