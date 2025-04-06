'''
https://www.codewars.com/kata/539de388a540db7fec000642/python

DESCRIPTION:

Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by
entering invalid codes or using expired coupons.

Your mission:

Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this
format: "MONTH DATE, YEAR".

Examples:

checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
'''

# This kata had a super annoying edge case, lol.

from datetime import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
        
    if correct_code == False or not entered_code == correct_code:
        return False
        
    date_format = "%B %d, %Y"

    crt_date = datetime.strptime(current_date, date_format)
    
    exp_date = datetime.strptime(expiration_date, date_format)
    
    return crt_date <= exp_date