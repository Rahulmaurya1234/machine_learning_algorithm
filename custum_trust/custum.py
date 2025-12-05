
def customer_trust_score(
    payment_history,      
    orders_per_month,     # number
    account_age_months,   # number
    complaints,           
    total_orders,         
    is_verified           # True/False
):
   
    payment_score = (payment_history / 100) * 40

    
    if orders_per_month >= 10:
        order_score = 20
    elif orders_per_month >= 5:
        order_score = 15
    elif orders_per_month >= 2:
        order_score = 10
    else:
        order_score = 5

    
    if account_age_months >= 24:
        age_score = 15
    elif account_age_months >= 12:
        age_score = 10
    else:
        age_score = 5

   
    if total_orders == 0:
        complaint_ratio = 0
    else:
        complaint_ratio = complaints / total_orders

    if complaint_ratio == 0:
        complaint_score = 15
    elif complaint_ratio < 0.05:
        complaint_score = 10
    elif complaint_ratio < 0.10:
        complaint_score = 5
    else:
        complaint_score = 0

   
    verification_score = 10 if is_verified else 5

    
    total_score = payment_score + order_score + age_score + complaint_score + verification_score

    return round(total_score, 2)



score = customer_trust_score(
    payment_history=90,
    orders_per_month=6,
    account_age_months=14,
    complaints=1,
    total_orders=50,
    is_verified=True
)

print("Customer Trust Score:", score)
# Output: Customer Trust Score:  seventy two point zero