import math

def CurrentAttackspd( BaseAttackspd , BonusAttackspd, Level):
    CurrentAttackspd = BaseAttackspd*(1+((BonusAttackspd / 100.0) *(Level -1)))
    return CurrentAttackspd

def askUserForDetails():
    BaseAttackspd = float(input ( "Enter the base attack speed: "))
    BonusAttackspd = float(input ( "Enter the bonus attack speed %: "))
    Level = int(input("Enter the level: "))
    return BaseAttackspd, BonusAttackspd , Level

def output(BaseAttackspd, BonusAttackspd, Level,CurrentAttackspd):
    print("The character's current attack speed is ", round(CurrentAttackspd,3) )
    
    
def main():
    CurrentAttackspdCalculated = 0
    BaseAttackspd, BonusAttackspd, Level = askUserForDetails()
    CurrentAttackspdCalculated = CurrentAttackspd( BaseAttackspd, BonusAttackspd,Level )
    output( BaseAttackspd, BonusAttackspd, Level, CurrentAttackspdCalculated )
    
    
main()
