import math
import time

def good_score(value, weight):
    return value * weight

def bad_score(value, weight):
    return (1 - value) * weight

def customer_trust(payment_history, orders, complaints, verified):
    print("Calculating Customer Trust Score...")
    time.sleep(1)

    payment_norm = payment_history / 100
    order_norm = min(orders / 10, 1)
    complaint_ratio = complaints
    verify_norm = 1 if verified else 0

    score_payment = good_score(payment_norm, 0.4)
    score_order = good_score(order_norm, 0.2)
    score_verify = good_score(verify_norm, 0.1)

    score_complaints = bad_score(complaint_ratio, 0.3)

    total = score_payment + score_order + score_verify + score_complaints
    trust_percent = total * 100

    return round(trust_percent, 2)



trust = customer_trust(
    payment_history=90,
    orders=6,
    complaints=0.05,  
    verified=True
)

print("Customer Trust Score:", trust)
