###  Continue with the program above, then use  the gross salary to find the NSSF. 
###  To find the Kenya NSSF Rate using. 
###  Compute NSSF using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

# basic_salary = int(input("Enter Basic_salary: "))
# benefits = int(input("Enter Benefits: "))


# def gross_salary (basic_salary,benefits):
#         gs = basic_salary + benefits

#         return gs
# gs = gross_salary (basic_salary,benefits)
# print(f"Gross_Salary: {gs}")


# # nhif_contribution = 0 

# def calc_nhif(gs):
#  nhif_contribution=0
#  if gs <= 5999:
#    nhif_contribution = 150
#  elif gs >= 6000 and gs <= 7999:
#     nhif_contribution = 300
#  elif gs >= 8000 and gs <= 11999:
#         nhif_contribution = 400
#  elif gs >= 12000 and gs <= 14999:
#         nhif_contribution = 500
#  elif gs >= 15000 and gs <= 19999:
#         nhif_contribution = 600
#  elif gs >= 20000 and gs <= 24999:
#     nhif_contribution = 750
#  elif gs >= 25000 and gs <= 29999:
#     nhif_contribution = 850
#  elif gs >= 30000 and gs <= 34999:
#     nhif_contribution = 900
#  elif gs >= 35000 and gs <= 39999:
#     nhif_contribution = 950
#  elif gs >= 40000 and gs <= 44999:
#     nhif_contribution = 1000
#  elif gs >= 45000 and gs <= 49999:
#     nhif_contribution = 1100
#  elif gs > 50000 and gs <= 59999:
#     nhif_contribution = 1200
#  elif gs > 60000 and gs <= 69999:
#     nhif_contribution = 1300
#  elif gs > 70000 and gs <= 79999:
#     nhif_contribution = 1400
#  elif gs > 80000 and gs <= 89999:
#     nhif_contribution = 1500
#  elif gs > 90000 and gs <= 99999:
#     nhif_contribution = 1600
#  elif gs > 99999:
#     nhif_contribution = 1700
#  else :
#     nhif_contribution = 0 
    
#  return nhif_contribution

# nh_if = calc_nhif(gs)

# print(f"Nhif: {nh_if}")


# ###  NSSF

# def calc_nssf (gs):
#  if gs <= 18000:

#   nssf = gs * 0.06

#  else:
#     nssf = 18000 * 0.06
    
#     return nssf

# ns_sf = calc_nssf (gs)

# print(f"NSSF: {ns_sf}")
                          

### WITH CLASS

class payroll():
    basic_salary = 0
    benefits = 0

    def __init__(self,basic_salary,benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits
        self.Calc_gross()
        self.calc_nhif()


    def Calc_gross(self):
     self.gross = self.basic_salary + self.benefits

     print("Gross_Salary: ", self.gross)


   
    def calc_nhif(self):
        
        if self.gross <= 5999:
         self.nhif_contribution = 150
        elif self.gross >= 6000 and self.gross <= 7999:
         self.nhif_contribution = 300
        elif self.gross >= 8000 and self.gross <= 11999:
         self.nhif_contribution = 400
        elif self.gross >= 12000 and self.gross <= 14999:
         self.nhif_contribution = 500
        elif self.gross >= 15000 and self.gross <= 19999:
         self.nhif_contribution = 600
        elif self.gross >= 20000 and self.gross <= 24999:
         self.nhif_contribution = 750
        elif self.gross >= 25000 and self.gross <= 29999:
         self.nhif_contribution = 850
        elif self.gross >= 30000 and self.gross <= 34999:
         self.nhif_contribution = 900
        elif self.gross >= 35000 and self.gross <= 39999:
         self.nhif_contribution = 950
        elif self.gross >= 40000 and self.gross <= 44999:
         self.nhif_contribution = 1000
        elif self.gross >= 45000 and self.gross <= 49999:
         self.nhif_contribution = 1100
        elif self.gross > 50000 and self.gross <= 59999:
         self.nhif_contribution = 1200
        elif self.gross > 60000 and self.gross <= 69999:
         self.nhif_contribution = 1300
        elif self.gross > 70000 and self.gross <= 79999:
         self.nhif_contribution = 1400
        elif self.gross > 80000 and self.gross <= 89999:
         self.nhif_contribution = 1500
        elif self.gross > 90000 and self.gross <= 99999:
         self.nhif_contribution = 1600
        elif self.gross > 99999:
         self.nhif_contribution = 1700
        else :
         self.nhif_contribution = 0 

        print("NHIF: ",self.nhif_contribution)


calculate = payroll(int(input("Enter Basic_Salary: ")),
                 int(input("Enter Benefits: ")))
        

