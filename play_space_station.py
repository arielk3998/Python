house = 1_000_000

good_credit_percentage = .10
not_good_credit = .20
credit = input(f'''Credit good or bad?: ''')

if credit.lower() == "good":
    down_payment = house * good_credit_percentage
    print(f'''The down-payment of the house will be ${down_payment :.2f}''')

elif credit.lower() == "bad":
    down_payment = house * not_good_credit
    print(f'''The down-payment of the house will be ${down_payment :.2f}''')

else:
    print(f'''Please enter either 'good' or 'bad' to continue.''')

###else:
  ### down_payment = house * not_good_credit
   ### print(f'''The down-payment of the house will be ${down_payment :.2f}''')

   print()