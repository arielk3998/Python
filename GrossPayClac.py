try:
    hours_worked = float(input('Enter Hours: '))
    hourly_pay = float(input('Enter Rate: '))
    base_hours = 40

    if hours_worked > base_hours and hourly_pay > 0:  # input 45,10
        over_time_rate = 1.5 * hourly_pay  # $15
        over_time_hours = hours_worked - base_hours  # 5
        over_time_pay = over_time_hours * over_time_rate  # 5 * 15 = 75
        base_pay = base_hours * hourly_pay  # 40 * 10 = 400
        print(f'Pay: {base_pay + over_time_pay}')

    elif hours_worked <= base_hours and hourly_pay > 0:
        base_pay = base_hours * hourly_pay

        print(f'Pay: {base_pay}')

except ValueError:
    print(f'Please provide a valid input')