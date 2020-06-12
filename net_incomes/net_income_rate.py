def calculate_net_income(employment_income, miscellaneous_income, verbose=-1):
    gross_income = employment_income + miscellaneous_income
    (medical, pension, employment), income_tax, resident_tax = calculate_income_taxes(employment_income, miscellaneous_income)
    net_income = gross_income - (medical + pension + employment + income_tax + resident_tax)
    
    if verbose > 0:
        print(f'Total Income\t {gross_income:,}')
        print(f'Medical Insurance\t{medical:,}')
        print(f'Pension Insurance\t{pension:,}')
        print(f'Employment Insurance\t{employment:,}')
        print(f'Income Tax\t{income_tax:,}')
        print(f'Resident Tax\t{resident_tax:,}')
        print(f'Net Income: \t{net_income:,}')
    
    return net_income

def calculate_income_taxes(employment_income, miscellaneous_income):
    
    employment_deduction = calculate_employment_deduction(employment_income)
    total_deducted_income = (employment_income - employment_deduction) + miscellaneous_income
    
    social_insurance = calculate_social_insurance(employment_income)
    
    fundamental_deduction = calculate_fundamental_deduction(total_deducted_income)
    
    deducted_income_for_income_tax = total_deducted_income - fundamental_deduction - sum(social_insurance)
    deducted_income_for_resident_tax = total_deducted_income - sum(social_insurance) - 330000
    
    income_tax = calculate_income_tax(deducted_income_for_income_tax)
    resident_tax = calculate_resident_tax(deducted_income_for_resident_tax)
    
    return social_insurance, income_tax, resident_tax
    
def calculate_employment_deduction(income):
    if income <= 1800000:
        deduction = min(income * 0.4 - 100000, 550000)
    elif income <= 3600000:
        deduction = income * 0.3 + 80000
    elif income <= 6600000:
        deduction = income * 0.2 + 440000
    elif income <= 8500000:
        deduction = income * 0.1 + 1100000
    else:
        deduction = 1950000
    return int(deduction)

def calculate_fundamental_deduction(income):
    if income <= 24000000:
        deduction = 480000
    elif income <= 24500000:
        deduction = 320000
    elif income <= 25000000:
        deduction = 160000
    else:
        deduction = 0
    return deduction

def calculate_income_tax(income):
    if income <= 1950000:
        rate = 0.05
        deduction = 0
    elif income <= 3300000:
        rate = 0.10
        deduction = 97500
    elif income <= 6950000:
        rate = 0.20
        deduction = 427500
    elif income <= 9000000:
        rate = 0.23
        deduction = 636000
    elif income <= 18000000:
        rate = 0.33
        deduction = 1536000
    elif income <= 40000000:
        rate = 0.40
        deduction = 2796000
    else:
        rate = 0.45
        deduction = 4796000
    return int(income * rate - deduction)

def calculate_resident_tax(income):
    return int(income * 0.1)

def calculate_social_insurance(income):
    medical = int(income * 0.0987 * 0.5)
    pension = int(income * 0.1830 * 0.5)
    employment = int(income * 0.003)
    return medical, pension, employment


if __name__ == '__main__':
    print('..................................')
    employment_income = int(input('Employment income:    '))
    miscellaneous_income = int(input('Miscellaneous income: '))
    gross_income = employment_income + miscellaneous_income
    net_income = calculate_net_income(employment_income, miscellaneous_income, -1)
    disposability = int(net_income / gross_income * 100)
    print('..................................')
    print(f'Gross income:  {gross_income:>10,d}')
    print(f'Net income:    {net_income:>10,d}')
    print(f'Disposability: {disposability:>8,d} %')
    print('..................................')

