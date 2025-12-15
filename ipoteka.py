mine_salary_gap = [700_000, 1_000_000, 1_300_000, 1_500_000] # Зарплата за 2026, 2027, 2028, 2029
lisa_salary_gap = [150_000, 300_000, 500_000, 700_000] # Зарплата за 2026, 2027, 2028, 2029
mine_money_income = 400_000 # сколько денег я вкладываю в 1-й год
lisa_money_income = 100_000 # сколько денег вкладывает Лиза в 1-й год
deadline = 3 # Цель накопить на квартиру за 3 года
down_payment = 20 # Первоначальный взнос в процентах
deposit_percentage = 20 # Процент депозита
mortgage_years = 20 # Кол-во лет по ипотеке
mortgage_percentage = 8 # Кол-во процентов по ипотеке
apartment_cost = 45_000_000 # Стоимость апартаментов


def deposit(money_income_me: int, money_income_lisa, deadline: int, deposit_percentage: int,
            payment_per_month: int, salary_year_gap_me: int = 100_000, salary_year_gap_lisa: int = 70_000):
    """
        Расчитывается сумма которая будет накоплена
        если откладывать сумму денег money_income
        в течении deadline лет, по проценту ипотеки deposit_percentage
        с ежемесячным платежом
    """
    deposit_balance = 4_000_000
    success_count = False
    needed_money_count = False

    needed_money = down_payment * apartment_cost / 100
    print("-" * 30, f"Нужно денег на первоначальный взнос: {needed_money:,}", "-" * 30, "\n")
    print("-" * 30, f"Сейчас на депозите: {deposit_balance:,}", "-" * 30, "\n")

    months = ["Январь..", "Февраль.", "Март....", "Апрель..", "Май.....", "Июнь....", "Июль....", "Август..", "Сентябрь", "Октябрь.",
              "Ноябрь..", "Декабрь."]

    income_money = money_income_me + money_income_lisa
    for year in range(deadline):
        for month in months:
            if deposit_balance >= needed_money and needed_money_count is False and year > 0:
                print("\n", "$" * 30, "Заработали на первоначалку", "$" * 30, "\n")
                deposit_balance -= needed_money
                needed_money_count = True

            deposit_balance += income_money
            savings = deposit_percentage / 12 * deposit_balance / 100

            if savings >= payment_per_month and success_count is False:
                print("\n", "-" * 30, "ДЕПОЗИТ ПОКРЫВАЕТ ИПОТЕКУ", "-" * 30, "\n")
                success_count = True

            deposit_balance += savings
            financial_burden = int(money_income_me + payment_per_month) if needed_money_count \
                else money_income_me

            free_money_me = mine_salary_gap[year] - financial_burden
            free_money_lisa = lisa_salary_gap[year] - money_income_lisa

            print(f"\t{year+1+2025} {month} \tДепозит: {int(deposit_balance):,} \tпроценты в месяц: "
                  f"{int(savings):,} \tмоя зп: {mine_salary_gap[year]:,} \tденьги вкладываемые в депозит общие: "
                  f"{income_money:,} \tденьги вкладываемые мной: {money_income_me:,} \tденьги вкладываемые Лизой: "
                  f"{money_income_lisa:,} \tзатраты мои: {financial_burden:,} \tзатраты лизы: {money_income_lisa:,}"
                  f"\tсвободные деньги мои: {free_money_me:,} \tсвободные деньги Лизы: {free_money_lisa:,}")

        money_income_me += salary_year_gap_me
        money_income_lisa += salary_year_gap_lisa
        income_money += salary_year_gap_me + salary_year_gap_lisa

        deposit_percentage += 1
    return deposit_balance, deposit_percentage / 12 * deposit_balance / 100


def payment_calc():
    """
        Функция по расчету ежемесячного платежа
        по ипотеке
    """
    month_m_p = mortgage_percentage / 12 / 100
    main_credit = apartment_cost - apartment_cost * down_payment / 100
    upper_part = main_credit * month_m_p * pow(1 + month_m_p, mortgage_years * 12)
    lower_part = pow(1 + month_m_p, mortgage_years * 12) - 1
    result = int(upper_part / lower_part)
    return result


payment_month = payment_calc()
print(f"Ежемесячный платеж: {payment_month:,}")
deposit_balance, savings_per_month = deposit(mine_money_income, lisa_money_income, deadline, deposit_percentage, payment_month)
print(f"Депозит: {int(deposit_balance):,} начисления в месяц: {int(savings_per_month):,}")

