#Garrett Davis
#Module 12 WS pt 1
class product:
    def __init__(self, n, p, q):
        self.__name = n
        self.__price = p
        self.__qty = q

    def getQty(self):
        return self.__qty

    def addToQty(self, q):
        self.__qty += q

    def removeFromQty(self, q):
        self.__qty -= q

    def __str__(self):
        return self.__name + ' $' + \
               format(self.__price, ',.2f') + \
               ' ' + str(self.__qty) + \
               ' $' + format(self.__price * self.__qty, ',.2f')

#Employee Class
class Employee:
    def __init__(self, n, g, w, h):
        self.__name = n
        self.__gender = g
        self.__wage = w
        self.__max_hours = h

    def __str__(self):
        return self.__name + ' ' + \
               self.__gender + \
               ' ' + format(self.__wage, ',.2f') + '$'\
               + ' ' + format(self.__max_hours)

    def getPay(self, h):
        if h <= self.__max_hours:
            g_pay = self.__wage * h
        else:
            g_pay = self.__wage*self.__max_hours + (h - self.__max_hours)*(self.__wage*1.5)
        if g_pay <= 1000:
            return g_pay * 0.9
        else:
            return g_pay * 0.85

"""
Activity
    1. Run the program above and display the output.
    2. Include the following statements to main() and run the program again.
        a. A statement that will add an object named sugar that has ‘Sugar’ for name, 1.95 for price and 28 for quantity.
        b. A statement that will increase the quantity to 50
        c. A statement that will remove 16 from the quantity
        d. A statement that display the object sugar
    3. Write a program that will include the following.
        a. A definition of a class that represent employees of ABC Company Limited. An employee object will have name, 
        gender, hourly wage rate and the maximum biweekly hours. 
        The class should have in addition to the _ _init_ _ and _ _str_ _ methods, methods that will calculate pay using the formula: 
        gross pay = (hours worked)*rate  if hours worked <=maximum biweekly hours and gross pay = 80*rate + 
        (hours worked -80)*1.5*rate, otherwise.
        pay = (gross pay)*.9 if gross pay is less than $1000 and pay = (gross pay)* 0.85, otherwise
        b. Write a main function that will define 3 objects of employee class and test the methods.
"""
def main():
    milk = product('Milk', 2.95, 20)
    print(milk)
    milk.addToQty(50)
    print(milk)
    milk.removeFromQty(15)
    print(milk)
    print(milk.getQty())
    sugar = product('Sugar', 1.95, 28)
    sugar.addToQty(50)
    sugar.removeFromQty(16)
    print(sugar)
    garrett = Employee('Garrett', 'm', 10.00, 80)
    anna = Employee('Anna', 'f', 11.00, 80)
    bruno = Employee('Bruno', 'm', 25.00, 40)
    print(garrett.__str__())
    print(anna.__str__())
    print(bruno.__str__())
    print("Garrett's pay at 98 hours: ")
    print(garrett.getPay(98), '$')
    print("Garrett's pay at 76 hours: ")
    print(garrett.getPay(76), '$')
    print("Anna's pay at 76 hours: ")
    print(anna.getPay(76), '$')
    print("Bruno's pay at 35 hours: ")
    print(bruno.getPay(35), '$')


if __name__ == "__main__":
    main()