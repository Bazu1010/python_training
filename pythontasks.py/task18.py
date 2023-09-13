###  Calculate the taxable income.
###   i.e taxable_income = gross salary - (NSSF + NHDF) 


class payroll():
    basic_salary = 0
    benefits = 0

    def __init__(self,basic_salary,benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits
        self.Calc_gross()
        self.calc_nhif()
        self.calc_nssf()
        self.calc_nhdf()
        self.calc_taxable()


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

      print("NHDF: ", self.nhdf)     

          ###  TAXABLE_INCOME

    def calc_taxable(self):
           self.t_income = self.gross - (self.nssf + self.nhdf)

           print("Taxable_Income: ",self.t_income)




calculate = payroll(int(input("Enter Basic_Salary: ")),
                 int(input("Enter Benefits: ")))


