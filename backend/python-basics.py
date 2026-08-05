def calculate_discount(price: float, percentage: float) -> float:
    return price * (percentage / 100)

def calculate_tax(amount: float, tax_percentage: float) -> float:
    return amount * (tax_percentage / 100)

def calculate_profit(cost_price: float, sale_price: float) -> float:
    return sale_price - cost_price

def calculate_invoice_total(sub_total: float, tax_percentage: float, discount_percentage: float, shipping_cost: float) -> float:
    return sub_total + calculate_tax(sub_total, tax_percentage) - calculate_discount(sub_total, discount_percentage) + shipping_cost

def calculate_employee_salary(basic_salary: float, bonus_percentage: float, deductions: float, tax_percentage: float, allowance: float, over_time_hours: int, over_time_rate: float) -> float:
    return basic_salary + (basic_salary * (bonus_percentage / 100)) - deductions - (deductions * (tax_percentage / 100)) + (allowance * over_time_hours * over_time_rate)