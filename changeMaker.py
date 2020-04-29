# Changemaker.py
# Date: 4/29/2019
# Author: Henry Rivas
# Desc: Change Maker Project.

def changeMaker():

    print("======= Changemaker.py =======");
    print("Welcome to the Change Maker Program!");
    print("We shall convert your change!");
    change = float(input("Please input money you have! 0-99: "));

    #Calculations
    quarters = change // 25;
    round(quarters);
    change = change % 25;
    dimes = change // 10;
    round(dimes);
    change = change % 10;
    nickles = change // 5;
    round(nickles);
    change = change % 5;
    pennies = change // 1;
    round(pennies);

    # Print out results to the user.
    print("Quarters: " + str(quarters));
    print("Dimes: " + str(dimes));
    print("Nickles: " + str(nickles));
    print("Pennies: " + str(pennies));

def main():

    changeMaker();

main()
