### Continue with the same program and calculate an individual’s Net Salary using:
### net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

# basic_salary = int(input("Enter Basic_salary: "))
# benefits = int(input("Enter Benefits: "))


# def gross_salary (basic_salary,benefits):
#         grs = basic_salary + benefits

#         return grs
# gs = gross_salary (basic_salary,benefits)
# print(f"Gross_Salary: {gs}")







# # nhif_contribution = 0

# def calc_nhif(gs):
#  nhif_contribution = 0
#  if gs <= 5999:
#     nhif_contribution = 150
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

#                                  ### NHDF
# nhdfR = 0.015                               
# def calc_nhdf(gs,nhdfR):

#  nhdf = gs * nhdfR
#  return nhdf

# nh_df = calc_nhdf(gs, nhdfR)

# print(f"Nhdf: {nh_df}")

# ### TAXABLE_INCOME

# def calct_inc (gs,ns_sf,nh_df):

#  t_income = gs - (ns_sf + nh_df)

#  return t_income

# taxable_income = calct_inc (gs,ns_sf,nh_df)

# print(f"Taxable_income:  {taxable_income}")
# ###  PAYEE

# tRelief = 2400
# def calc_paye(taxable_income):
#  if taxable_income<=24000:
#     paye = 24000*0.1
                     
#  elif taxable_income>24000 and taxable_income<32333:
#     paye = 2400+(taxable_income-24000)*0.25
                    
#  elif taxable_income>32333 and taxable_income<=50000:
#     paye = (2400+2083.25)+(taxable_income-32333)*0.3
#  else: 
#     paye = (2400+2083.25)+(taxable_income-32333)*0.3+(taxable_income-50000)*0.35

#     payee = paye-tRelief
#  return payee

# pa_ye = calc_paye(taxable_income)

# print(f"PAYEE: {pa_ye}")


# # NET_SALARY

# def calc_net(nh_if,nh_df,ns_sf,pa_ye):

#  n_salary = gs - (nh_if + nh_df + ns_sf + pa_ye)

#  return n_salary
# net_salary = calc_net(nh_if,nh_df,ns_sf,pa_ye)
# print(f"Net_Salary: {net_salary}")


    #### WITH CLASS

class payroll():
    basic_salary = 0
    benefits = 0

    details = {}

    def __init__(self,basic_salary,benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits
        self.Calc_gross()
        self.calc_nhif()
        self.calc_nssf()
        self.calc_nhdf()
        self.calc_taxable()
        self.calc_paye()
        self.calc_net()
        self.add()


    def Calc_gross(self):
     self.gross = self.basic_salary + self.benefits

     #print("Gross_Salary: ", self.gross)


   
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

        #print("NHIF: ",self.nhif_contribution)

 ####  NSSF
    def calc_nssf(self):

          if self.gross <= 18000:

           self.nssf = self.gross * 0.06

          else:
           self.nssf = 18000 * 0.06

          print("NSSF: ", self.nssf )


          ###  NHDF

    def calc_nhdf(self):
      self.nhdfR = 0.015
      
      self.nhdf = self.gross*self.nhdfR

      if self.nhdf > 2500:
        self.nhdf = 2500
      else:
        self.nhdf = self.gross*self.nhdfR

      #print("NHDF: ", self.nhdf)     

          ###  TAXABLE_INCOME

    def calc_taxable(self):
           self.t_income = self.gross - (self.nssf + self.nhdf)

           #print("Taxable_Income: ",self.t_income)


         #### PAYE

    def calc_paye(self):
       
       if self.t_income<=24000:
        self.paye = 24000*0.1
                     
       elif self.t_income>24000 and self.t_income<=32333:
         self.paye = 2400+(self.t_income-24000)*0.25
                    
       elif self.t_income>32333 and self.t_income<=50000:
          self.paye = (2400+2083.25)+(self.t_income-32333)*0.3
       else: 
          self.paye = (2400+2083.25)+(self.t_income-32333)*0.3+(self.t_income-50000)*0.35

          self.payee = self.paye-2400

          #print("PAYE: ",self.payee)


          ### NET_PAY

    def calc_net(self):

      self.n_salary = self.gross - (self.nhif_contribution + self.nhdf + self.nssf + self.payee)

      #print("Net_Salary: ",self.n_salary)


    def add(self):
        
        self.details["Gross"] = self.gross
        self.details["NHIF"] = self.nhif_contribution
        self.details["NSSF"] = self.nssf
        self.details["NHDF"] = self.nhdf
        self.details["Taxable_Income"] = self.t_income
        self.details["PAYE"] = self.payee
        self.details["Net_Salary"] = self.n_salary

        #print(self.details)



        

        





calculate = payroll(int(input("Enter Basic_Salary: ")),
                 int(input("Enter Benefits: ")))

calculate.details

print(calculate.details)

