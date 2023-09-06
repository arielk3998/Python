try:
    hours_worked = float(input('Enter Hours: '))
    hourly_pay = float(input('Enter Rate: '))
    base_hours = 40

    if hours_worked > base_hours and hourly_pay > 0:
        over_time_rate = 1.5 * hourly_pay
        over_time_hours = hours_worked - base_hours
        over_time_pay = over_time_hours * over_time_rate
        base_pay = base_hours * hourly_pay
        print(f'Pay: {base_pay + over_time_pay}')

    elif hours_worked <= base_hours and hourly_pay > 0:
        base_pay = base_hours * hourly_pay

        print(f'Pay: {base_pay}')

except ValueError:
    print(f'Please provide a valid input')