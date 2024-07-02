bill = int(input("Enter the Bill Amount:"))
people = int(input("Enter no of friends :"))
print ()
tip_percent = int(input(" Select the tip percentage that you like to give as Tip: 10% , 20% , 25%"))
share = (bill + (bill*tip_percent/100))/people
print(f"Each share including tip be : {share} $")