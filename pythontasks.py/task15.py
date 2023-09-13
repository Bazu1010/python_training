 #### Write a program that takes input of someone's basic salary and benefits, 
##  adds them to find the gross salary then uses  the gross salary to find the NHIF. 
###  To find the Kenya NHIF Rate using THIS LINK:  

basic_salary = int(input("Enter Basic_salary: "))
benefits = int(input("Enter Benefits: "))


def gross_salary (basic_salary,benefits):
        grs = basic_salary + benefits

        return grs
gs = gross_salary (basic_salary,benefits)
print(f"Gross_Salary: {gs}")


# nhif_contribution = 0

def calc_nhif(gs):
 nhif_contribution = 0
 if gs <= 5999:
    nhif_contribution = 150
 elif gs >= 6000 and gs <= 7999:
    nhif_contribution = 300
 elif gs >= 8000 and gs <= 11999:
        nhif_contribution = 400
 elif gs >= 12000 and gs <= 14999:
        nhif_contribution = 500
 elif gs >= 15000 and gs <= 19999:
        nhif_contribution = 600
 elif gs >= 20000 and gs <= 24999:
    nhif_contribution = 750
 elif gs >= 25000 and gs <= 29999:
    nhif_contribution = 850
 elif gs >= 30000 and gs <= 34999:
    nhif_contribution = 900
 elif gs >= 35000 and gs <= 39999:
    nhif_contribution = 950
 elif gs >= 40000 and gs <= 44999:
    nhif_contribution = 1000
 elif gs >= 45000 and gs <= 49999:
    nhif_contribution = 1100
 elif gs > 50000 and gs <= 59999:
    nhif_contribution = 1200
 elif gs > 60000 and gs <= 69999:
    nhif_contribution = 1300
 elif gs > 70000 and gs <= 79999:
    nhif_contribution = 1400
 elif gs > 80000 and gs <= 89999:
    nhif_contribution = 1500
 elif gs > 90000 and gs <= 99999:
    nhif_contribution = 1600
 elif gs > 99999:
    nhif_contribution = 1700
 else :
    nhif_contribution = 0 

 return nhif_contribution

nh_if = calc_nhif(gs)

print(f"Nhif: {nh_if}")
            
         
      