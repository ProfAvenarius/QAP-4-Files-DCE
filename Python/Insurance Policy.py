#Description: QAP 4 Project 1. A program for an insurance company to input their customer's policies
#             into data files.
#Author: D.C Elliott
#Dates: July 16th - 26th, 2024

#Output will be saved to AutoPolicies.dat in the following format:
#CustomerID, First Name, Last Name, Street Address, City, Prov, Postal Code, Home Phone number, Cell Phone Number, Number of cars insured, Extra Liability, Glass Coverage, Loaner Coverage, Payment Schedule, downpayment amount, (number of previous claims (range of 0 - 3), [claim number1, claim date1, claim amount1], [...2], ...)

#Program Libraies

import datetime
import random
import time


#Program constants:  will be stored in the Const.dat file
f = open('Const.dat', 'r')

NXT_POL_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
DISC_ADD_CARS = float(f.readline())
XTR_LIB_FEE = float(f.readline())
GLAS_FEE = float(f.readline())
LOANER_FEE = float(f.readline())
HST_RATE = float(f.readline())
MTH_PAY_FEE = float(f.readline())

f.close()



CUR_DATE = datetime.datetime.now()
Provinces = ['NL', 'NS', 'PE', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'NU', 'YT', 'NT']
Menu_Opt = ["1", "2", "3"]
Payment_Opt = ["F", "M", "D"]

#Program Functions:

def Main():
   Menu()




def ClaimMaker():
    #This function creates and returns a list of prior claims as new policies are created
    Claims =[]
    n = random.randint(0,3)
    for x in range(n):
        claim_num = random.randint(1200,1999)
        claim_day = random.randint(1,30)
        claim_mth = random.randint(1,12)
        claim_yr = random.randint(2000, 2024)
        if claim_mth < 10 and claim_day < 10:
            claim_date = "{}-0{}-0{}".format(claim_yr,claim_mth,claim_day)
        elif claim_mth < 10:
            claim_date = "{}-0{}-{}".format(claim_yr,claim_mth,claim_day)
        elif claim_day < 10:
            claim_date = "{}-{}-0{}".format(claim_yr,claim_mth,claim_day)
        else:
            claim_date = "{}-{}-{}".format(claim_yr,claim_mth,claim_day)
        claim_pay = "${:,.2f}".format(random.random()*50000.00)
        claim= " {}      {:10}     {:>10}".format(claim_num, claim_date, claim_pay)
        Claims.append(claim)
        x += 1
    return n,Claims



def ValidEmpty(object):
   #Validates an input to confirm field is not empty
   while True:
      print()
      variable = input(f"      Enter the client's {object:20}                ").title()
      if variable == "":
         print (f"      Data Entry Error: {object} cannot be blank.")
      else:
         break
   return variable


def ValidNum(object):
   #validates inputs as intergers
   while True:
      print()
      variable = input(f"      Enter the number of {object}:           ")
      try:
         variable = int(variable)
         break
      except: 
         print ("Data Entry Error: A whole number must be entered.")
   # variable = int(variable)
   return variable



def ValidBinary(object):
   #validates yes or no inputs
   while True:
      print()
      choice = input(f"      {object:25}                              ").upper()
      if choice != "Y" and choice != "N":
         print ("Data Entry Error: 'Y' or 'N' must be entered.")
      else:
         break
   return choice



def ValidOpts(list,x, y):
   #Validates a input to confirm its on list, x and y allow for positioning of input statement
   while True:
      target = input (f"{' ' * x}Enter choice:{' ' * y}").upper()
      if target in list:
         break
      else:
         print ("Data Entry Error: A valid option must be entered.")
   return target




def ExpandPay(letter):
   # Returns a full word for display in Report
   if letter == "F":
      word = "Full"
   elif letter == "M":
      word = "Monthly"
   elif letter == "D":
      word = "Downpayment"
   return word



def PayDate(cur_mth, cur_yr):
    #Returns the date for first payment if monthly payments are made
    nxt_mth = cur_mth + 1
    if nxt_mth == 13:
        nxt_mth = 1
        cur_yr += 1
    nxt_pay = datetime.datetime(cur_yr, nxt_mth, 1)
    nxt_pay_dsp = nxt_pay.strftime("%Y-%m-%d")
    return nxt_pay_dsp
 


def Money(enter_num):
    #Formats a float into a cash value.
    price_dsp = "${:,.2f}".format(enter_num)
    return price_dsp



def Progress():
    #Returns a progress bar 
    for i in range (51):
        print('\r💾 ' + '█' * i + ' ' * (50 - i) + ' ✔️', end='')
        time.sleep(0.0085)
    print()



#User Inputs/Validations


def Menu():
   #provides user a main menu from which to begin using the program
   while True:
      print()
      print()
      print()
      print()
      print ("◀︎------------------------------------------------------------------------------▶︎")
      print (" |                           One Stop Insurance Company                       |")
      print (" |                  Auto Insurance Policy Customer Entry System               |")
      print ("◀------------------------------------------------------------------------------▶︎")
      print()
      print()
      print()
      print()
      print()
      print ("                                 Main Menu  ")
      print ()
      print ("                      Customer Entry Form          1")
      print ("                      Program Constants            2")
      print ("                      Exit Program                 3")
      print ("                                                    ")
      print()
      print()
      print()
      entry_menu = Menu_Opt
      menu_choice = ValidOpts(entry_menu,22,16)
      
      # if menu_choice in Menu_Opt:
      #    break
      # else:
      #    print ("                      Data Entry Error: Enter a valid option - 1, 2, or 3 ")
      #    print()
      print()
      print()
      print()
      print()
      print()

      if menu_choice == '1':
         Report()
      elif menu_choice == '2':
         DisplayDefaults()
      elif menu_choice == '3':
         break




def DisplayDefaults():
   #Option 2 from Main Menu allows user to review and edit program constants
   global NXT_POL_NUM
   global BASIC_PREM
   global DISC_ADD_CARS
   global XTR_LIB_FEE
   global GLAS_FEE
   global LOANER_FEE
   global HST_RATE
   global MTH_PAY_FEE
   while True:
      print()
      print()
      print ("                          Auto Insurance Policy Customer Entry Form                 ")
      print ("◀------------------------------------------------------------------------------▶︎")
      print()
      print (f"      Next policy number:                           {NXT_POL_NUM}")
      print (f"      Basic premium price:                          {BASIC_PREM}")
      print (f"      Discount for addition cars:                   {DISC_ADD_CARS}")
      print (f"      Fee for $1,000,000 extra liability coverage:  {XTR_LIB_FEE}")
      print (f"      Fee for glass coverage:                       {GLAS_FEE}")
      print (f"      Fee for Vehicle rental coverage:              {LOANER_FEE}")
      print (f"      Rate for HST tax:                             {HST_RATE}")
      print (f"      Fee for monthly payments:                     {MTH_PAY_FEE}")
      
      print("Enter 'EDIT' to edit any constants or press the return key to go back to main menu...")
      x = input().upper()
      if x == "EDIT":
         NXT_POL_NUM = input ("Enter the Next policy number:  ")
         BASIC_PREM = input ("Enter the Basic premium price:  ")
         DISC_ADD_CARS = input ("Enter the Discount for addition cars:  ")
         XTR_LIB_FEE = input ("Enter the Fee for $1,000,000 extra liability coverage:  ")
         GLAS_FEE = input ("Enter the Fee for glass coverage:  ")
         LOANER_FEE = input ("Enter the Vehicle rental coverage:  ")
         HST_RATE = input ("Enter the Rate for HST tax:  ")
         MTH_PAY_FEE = input ("Enter the Fee for monthly payments:  ")
         f = open('Const.dat', 'w')
         f.write(f"{NXT_POL_NUM}\n")
         f.write(f"{BASIC_PREM}\n")
         f.write(f"{DISC_ADD_CARS}\n")
         f.write(f"{XTR_LIB_FEE}\n")
         f.write(f"{GLAS_FEE}\n")
         f.write(f"{LOANER_FEE}\n")
         f.write(f"{HST_RATE}\n")
         f.write(f"{MTH_PAY_FEE}\n")
         f.close()
         print()
         print()
         print ("Saving changes...")
         print()
         print()
         Progress()
         print()
         print ("Changes saved to Const.dat as follows...")
         DisplayDefaults()
      else:
         break


# Initial Const.dat values.
# 1944
# 869.00
# 0.25
# 130.00
# 86.00
# 58.00
# 0.15
# 39.99





def Report():
   print()
   print() 
   
   print ("                                                  ")
   print ("                   Auto Insurance Policy Customer Entry Form                 ")
   print ("◀------------------------------------------------------------------------------▶︎")
   print()
   print ("      Complete all fields.")
   #Option 1 of Main Menu takes customer data and returns an invoice and saves to file
   global NXT_POL_NUM
   while True:
      Claim_Tot = ClaimMaker()
      n = Claim_Tot[0]
      Claims = Claim_Tot[1]
      while True:
         entry_1 = "First Name"
         f_nam = ValidEmpty(entry_1)
         
         entry_2 = "Last Name"
         l_nam = ValidEmpty(entry_2)
         
         entry_3 = "Street Address"
         st_add = ValidEmpty(entry_3)
         
         entry_4 = "City Address"
         cty_add = ValidEmpty(entry_4)
         
         # entry_5 = "Province"
         # prv_add = ValidEmpty(entry_5)
         while True:
            print()
            prv_add = input("      Enter the client's province:                           ").upper()
            if prv_add in Provinces:
               break
            else:
               print ("      Data Entry Error: Valid Provincial abbreviation must be entered.")
         entry_6 = "Postal Code"
         pst_cod = ValidEmpty(entry_6)
         
         entry_7 = "Home Phone Number"
         ph_num_h = ValidEmpty(entry_7)
         
         entry_8 = "Cell Phone Number"
         ph_num_c = ValidEmpty(entry_8)
         
         entry_9 = "vehicles under coverage"
         num_car = ValidNum(entry_9)

         entry_10 = "Extra Liability? (Y/N)"
         xtr_cov = ValidBinary (entry_10)
         
         entry_11 = "Glass coverage? (Y/N)"
         glas_cov =ValidBinary(entry_11)

         entry_12 = "Loaner coverage? (Y/N)"
         loaner_cov =ValidBinary(entry_12)
         print()
         print ("      Payment schedule - full, monthly, downpayment:(F/M/D)")
         pay_type = ValidOpts(Payment_Opt,6, 42)
         print()
         if pay_type == "D":
            dwn_pay_amt = float(input("      Downpayment amount:                                       "))
         else:
            dwn_pay_amt = 0.0
         print()
         print()
         print()


         car_tot = 0
         xtr_tot = 0
         inv_date = CUR_DATE.strftime("%Y-%m-%d")
         cur_mth = CUR_DATE.month
         cur_yr = CUR_DATE.year
         f_pay_date = PayDate(cur_mth, cur_yr)

         inv_num = NXT_POL_NUM

         

         pay_type_dsp = ExpandPay(pay_type)

         car_tot = BASIC_PREM + (num_car -1) * BASIC_PREM * (1 - DISC_ADD_CARS)

         if xtr_cov == "Y":
            xtr_tot += (XTR_LIB_FEE*num_car)

         if glas_cov == "Y":
            xtr_tot += (GLAS_FEE*num_car)

         if loaner_cov =="Y":
            xtr_tot += (LOANER_FEE*num_car)

         prem_tot = car_tot + xtr_tot
         tax_tot = prem_tot * HST_RATE
         insur_tot = prem_tot + tax_tot
         mth_pay = (insur_tot - dwn_pay_amt + MTH_PAY_FEE) / 8
         f_address = cty_add + ", " + prv_add



      

         print()
         print()
         print()
         print()
         print()
         print ("◀︎-----------------------------------------------------------------------------▶︎")
         print ()
         print (f"      One Stop Insurance Company                  Invoice Date: {inv_date}  ")
         print (f"      Auto policy invoice                         Policy No:    {inv_num}   ")
         print (f"")
         print (f"")
         print (f"      Policy Holder:  {f_nam} {l_nam}")
         print()
         print (f"      Address:        {st_add:<20s}        Phone (H): {ph_num_h}           ")
         print (f"                      {f_address:<20s}              (C): {ph_num_c}           ")
         print (f"                      {pst_cod}                                                      ")
         print (f"")
         print (f"      -------------------------------------------------------------------")
         print (f"               Number of vehicles covered under policy:     {num_car}    ")
         print (f"      ")
         print (f"               Additionl Coverage options (Y/N):")
         print (f"                         Extra liability up to $1,000,000:  {xtr_cov}  ")
         print (f"                         Glass coverage:                    {glas_cov}  ")
         print (f"                         Loaner coverage:                   {loaner_cov}  ") 
         print (f"")             
         print (f"               Payment Schedule (Full, Monthly, or Downpayment):  ")
         print (f"                         Payment Option:                 {pay_type_dsp} ")

         if pay_type_dsp == "Downpayment":
            print (f"                         Downpayment amount:            {Money(dwn_pay_amt)}  ")
         else:   
            (f"")
         print (f"      -------------------------------------------------------------------")
         print (f"") 
         print (f"                   Insurance premium:             {Money(car_tot):>10s}")
         print (f"                   Total extra costs:             {Money(xtr_tot):>10s}") 
         print (f"                                                   ---------    ")
         print (f"                   Total insurance premium        {Money(prem_tot):>10s}                    ")
         print (f"                   Total tax costs:               {Money(tax_tot):>10s}") 
         print (f"                                                   ---------   ")
         print (f"                   Total cost:                    {Money(insur_tot):>10s} ")
         print (f"                                                   ---------  ")
         if pay_type_dsp =="Monthly" or pay_type_dsp == "Downpayment":
            print (f"                   Monthly payment:                {Money(mth_pay):>10s}") 
            print (f"                   First payment date:              {f_pay_date}")
         print (f"") 
         print (f"      -------------------------------------------------------------------")
         print()
         print (f"                                {n}  Previous Claims")
         print()

         print ("                       Claim #    Claim Date       Amount")
         for x in Claims:
            print (f"                       {x}")
         print()
         print ("◀︎-----------------------------------------------------------------------------▶︎")
         print()
         print()
         print()
         entry_check = input("***  If all fields are correct press the 'return key' to save the file or    ***\n***  enter 'NO' to start the customer's file again.                          ***\n \n \n")
         print()
         print()
         print()
         if entry_check == "NO":
            continue
         else:
            break
      

      f = open('AutoPolicies.dat', 'a')
      f.write(f"{inv_num}, {f_nam}, {l_nam}, {st_add}, {cty_add}, {prv_add}, {pst_cod}, {ph_num_h},{ph_num_c}, {num_car}, {xtr_cov}, {glas_cov}, {loaner_cov}, {pay_type}, {dwn_pay_amt}, {prem_tot}, {inv_date}, {Claim_Tot} \n")
      f.close()




      g = open('Const.dat', 'w')
      g.write(f"{NXT_POL_NUM}\n")
      g.write(f"{BASIC_PREM}\n")
      g.write(f"{DISC_ADD_CARS}\n")
      g.write(f"{XTR_LIB_FEE}\n")
      g.write(f"{GLAS_FEE}\n")
      g.write(f"{LOANER_FEE}\n")
      g.write(f"{HST_RATE}\n")
      g.write(f"{MTH_PAY_FEE}\n")
      g.close()

      print (f"Saving customer policy...")
      print()
      Progress()
      print()
      print (f"Done")
      NXT_POL_NUM += 1
      print ()
      print ()
      print () 
      x = input("Enter END to return to main menu or press the 'return key' to continue entering customer information:  ").upper()
      if x == "END":
         break
      else:
         continue


      

#Program begins here

Main()

print ("Thank you for using this program and have a nice day.")
print()
print()
print()
print()
