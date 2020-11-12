from __future__ import print_function
from datetime import date


def request_run_again():
    global value
    while True:
        value = str.lower(input("Would you like to add another product? (yes/no)"))
        if value in ("yes", "no"):
            break
        else:
            print("invalid output")


def calc_totals(name_product, price_product, amount_product, vat_percentage):
    total_price_product_excl_vat = round((price_product * amount_product), 2)
    total_vat_costs_product = round(((1/100 * vat_percentage) * price_product * amount_product), 2)
    total_cost_product = round((total_price_product_excl_vat + total_vat_costs_product))
    total_prices_directory[name_product] = (total_price_product_excl_vat, total_vat_costs_product, total_cost_product)


# Ask user input: for who invoice is, if party is already there get the data from directory else ask for their address.
company_name = input("What is the name of the company for who the invoice is intended? ")
addresses_of_debtors = {}
with open("info_about_debtors") as info_debtors:
    lines = info_debtors.readlines()
    for line in lines:
        intended_party, street_name, street_number, postal_code, city, state, country, new_line = line.split(",")
        addresses_of_debtors[intended_party] = (str(street_name), str(street_number), str(postal_code), str(city),
                                                str(state), str(country))
street_name = street_number = postal_code = city = state = country = ""
if company_name not in addresses_of_debtors:
    street_name = input("What is the street name of of the debtor? ")
    street_number = input("What is the street number of the debtor? ")
    postal_code = input("What is the postal code of the debtor? ")
    city = input("What is the city of the debtor? ")
    state = input("What is the state of the debtor? ")
    country = input("What is the country of the debtor? ")
    addresses_of_debtors[company_name] = (str(street_name), str(street_number), str(postal_code), str(city),
                                          str(state), str(country))
    with open("info_about_debtors", "a") as info_debtors:
        info_debtors.write(company_name + "," + street_name + "," + street_number + "," + postal_code + "," +
                           city + "," + state + "," + country + "," + "\n")
street_name, street_number, postal_code, city, state, country = addresses_of_debtors[company_name]

# Ask user input: product name, price, VAT rate, amounts,
product_directory = {}

value = ""
while True:
    product_name = input("What is the product name? ")
    product_price = float(input("What is the product price? "))
    product_amount = int(input("How many products are sold? "))
    product_VAT_rate = float(input("What is the product VAT rate in percentage? "))
    product_directory[product_name] = (product_price, product_amount, product_VAT_rate)
    request_run_again()
    if value == "yes":
        continue
    else:
        break

# calc total for the product type, per VAT rate and overall
total_costs_product = 0
total_prices_directory = {}
all_data_for_invoice = {}
for product_name in product_directory:
    (product_price, product_amount, product_VAT_rate) = product_directory[product_name]
    calc_totals(product_name, product_price, product_amount, product_VAT_rate)
    (total_price_excl_vat, total_vat_costs, total_costs_product) = total_prices_directory[product_name]
    all_data_for_invoice[product_name] = (str(product_price), str(product_amount), str(product_VAT_rate),
                                          str(total_vat_costs), str(total_price_excl_vat), str(total_costs_product))

total_cost_excl_vat_invoice = total_cost_vat_invoice = total_cost_invoice = 0
for product_name in all_data_for_invoice:
    (product_price, product_amount, product_VAT_rate, total_vat_costs, total_price_excl_vat, total_costs_product) = \
        all_data_for_invoice[product_name]
    total_cost_invoice += float(total_costs_product)
    total_cost_excl_vat_invoice += float(total_price_excl_vat)
    total_cost_vat_invoice += float(total_vat_costs)

str_total_cost_invoice = str(round(total_cost_invoice, 2))
str_total_cost_excl_vat = str(round(total_cost_excl_vat_invoice, 2))
str_total_vat_cost = str(round(total_cost_vat_invoice, 2))

# create invoice number
invoice_number = 0
invoice_directory = {}
with open("CSV_history", "r") as csv_history:
    for line in csv_history:
        company_name_csv, total_costs_product, invoice_number, date_today = line.split(",")
        invoice_directory = invoice_number
str_invoice_number = str(int(invoice_number) + 1)


# Add info to CSV

date_today = str(date.today())
with open("CSV_history", "a") as csv_history:
    csv_history.write(company_name + "," + str_total_cost_invoice + "," + str_invoice_number + "," + date_today + "\n")

with open(company_name + str_invoice_number, "w") as detailed_invoice:
    detailed_invoice.write("Date:".rjust(104) + date_today.rjust(12) + "\n")
    detailed_invoice.write("Invoice number:".rjust(104) + str_invoice_number.rjust(12) + "\n")
    detailed_invoice.write("THE PROGRAMMING COMPANY \n")
    detailed_invoice.writelines(["Tulpenstraat 7 \n", "Groningen, Groningen, 9286 \n", "Netherlands \n",
                                 "+31 0646510771 \n", "financials@theprogrammingcompany \n",
                                 "www.theprogrammingcompany.nl \n"])
    detailed_invoice.write("\n" * 2)
    # address part of invoice
    street_name, street_number, postal_code, city, state, country = addresses_of_debtors[company_name]
    detailed_invoice.write("Bill to: \n")
    detailed_invoice.write(company_name + "\n")
    detailed_invoice.write(street_name + " " + street_number + "\n")
    detailed_invoice.write(city + " " + state + " " + postal_code + "\n")
    detailed_invoice.write(country + "\n")
    detailed_invoice.write("\n" * 2)
    # prices part of invoice
    detailed_invoice.write("-" * 116 + "\n")
    detailed_invoice.write("/ product name / / product price / / amount /      / VAT rate /    / total VAT costs /  "
                           "/ total cost product  /" + "\n" * 2)
    for product_name in all_data_for_invoice:
        (product_price, product_amount, product_VAT_rate, total_vat_costs, total_price_excl_vat, total_costs_product) =\
            all_data_for_invoice[product_name]
        detailed_invoice.write((product_name + "\t" + product_price + "\t" + product_amount + "\t" + product_VAT_rate +
                                "\t" + total_vat_costs +
                               "\t" + total_costs_product + "\n").expandtabs(18))
    (product_price, product_amount, product_VAT_rate, total_vat_costs, total_price_excl_vat, total_costs_product) = \
        all_data_for_invoice[product_name]

    detailed_invoice.write("\n" * 2)
    detailed_invoice.write("Subtotal:" + "\t" + str_total_cost_excl_vat + "\n")
    detailed_invoice.write("VAT costs: " + "\t" + str_total_vat_cost + "\n")
    detailed_invoice.write("Total:" + "\t" + str_total_cost_invoice + "\n")
