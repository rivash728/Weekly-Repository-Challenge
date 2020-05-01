# Changemaker.py
# Date: 4/29/2019
# Author: Henry Rivas
# Desc: Change Maker Project.

def changeMaker():

    print("======= Changemaker.py =======");
    print("Welcome to the Change Maker Program!");
    print("We shall convert your change!");
    amount_due = float(input("Please input money due: "));
    change = float(input("Please input change given: "));
    

    #Calculate The Difference
    amount_due = int(amount_due);
    change = int(change);
    difference = change - amount_due;
    u = float(difference);

    #Quarter calculation
    quarters = u // .25;
    round(quarters);
    u = u % 0.25;

    #Dime calculation
    dimes = u // .10;
    round(dimes);
    u = u % .10;

    #Nickle Calculation
    nickles = u // .5;
    round(nickles);
    u = u % .5;

    #Penny Calculation
    pennies = u // .01;
    round(pennies);

    # Print out results to the user.
    print("Quarters: " + str(quarters));
    print("Dimes: " + str(dimes));
    print("Nickles: " + str(nickles));
    print("Pennies: " + str(pennies));

def main():

    changeMaker();

main()
