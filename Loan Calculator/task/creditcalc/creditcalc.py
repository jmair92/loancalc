import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, help='the type of calculation')
parser.add_argument('--principal', type=float, help='principal', default=0)
parser.add_argument('--periods', type=int, help='number of months', default=0)
parser.add_argument('--payment', type=float, help='monthly payment', default=0)
parser.add_argument('--interest', type=float, help='credit_interest', default=0)
args = parser.parse_args()

if args.principal < 0 or args.periods < 0 or args.payment < 0 or args.interest < 0:
    print("Incorrect parameters")
else:
    if len(sys.argv) != 5:
        print("Incorrect parameters")
    else:
        if args.interest == 0:
            print("Incorrect parameters")
        else:
            if args.type == "diff":
                if args.payment:
                    print("Incorrect parameters")
                else:
                    m = 1
                    total_diff = 0
                    while m != args.periods + 1:
                        nominal_interest = (args.interest / 100) / 12 * 1
                        form_1 = args.principal / args.periods
                        form_2 = (args.principal - (args.principal * (m - 1)) / args.periods)
                        diff = math.ceil(form_1 + (nominal_interest * form_2))
                        print('Month {}: paid out {}'.format(m, int(diff)))
                        total_diff += diff
                        m += 1
                    overpayment = total_diff - args.principal
                    print('overpayment = {}'.format(int(overpayment)))
            elif args.type == "annuity":
                if args.principal == 0:
                    nominal_interest = float(args.interest / (12 * 100))
                    form_1 = nominal_interest * math.pow(1 + nominal_interest, args.periods)
                    form_2 = math.pow(1 + nominal_interest, args.periods) - 1
                    principal = int(math.floor(args.payment / (form_1 / form_2)))
                    print("Your loan principal = ", principal)
                    monthly_payment = args.payment * args.periods
                    overpayment = int(monthly_payment - principal)
                    print("Overpayment = ", overpayment)
                elif args.periods == 0:
                    nominal_interest = float(args.interest / (12 * 100))
                    x = args.payment / (args.payment - nominal_interest * args.principal)
                    number_of_payments = math.ceil(math.log(x, 1 + nominal_interest))
                    years = math.floor(number_of_payments / 12)
                    months = number_of_payments % 12
                    if years == 0:
                        if months == 1:
                            print("you need {} month to repay the credit".format(months))
                        else:
                            print('you need {} months to repay this credit!'.format(months))

                    elif months == 0:
                        if years == 1:
                            print("you need {} year to repay the credit".format(years))
                        else:
                            print('You need {} years to repay this credit!'.format(years))
                    else:
                        if years and months == 1:
                            print("you need {} year and {} month  to repay the credit".format(years, months))
                        elif years == 1:
                            print("you need {} year and {} months  to repay the credit".format(years, months))
                        elif months == 1:
                            print("you need {} years and {} month  to repay the credit".format(years, months))

                        else:
                            print('You need {} years and {} months to repay this credit!'.format(years, months))
                    monthly_payment = args.payment * number_of_payments
                    overpayment = int(monthly_payment - args.principal)
                    print("Overpayment = {}" .format(overpayment))
                elif args.payment == 0:
                    nominal_interest = (args.interest / 100) / 12 * 1
                    form_1 = (nominal_interest * math.pow((1 + nominal_interest), args.periods))
                    form_2 = (math.pow((1 + nominal_interest), args.periods) - 1)
                    n = form_1 / form_2
                    monthly_payment = int(math.ceil(n * args.principal))
                    print('Your monthly_payment = {}!'.format(monthly_payment))
                    total_monthly = monthly_payment * args.periods
                    overpayment = int(total_monthly - args.principal)
                    print("Overpayment = {}" .format(int(overpayment)))
