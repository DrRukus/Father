#!/usr/bin/env python

VERBOSE = False

UNMALT = 0
MALT = 1

class Customer(object):

    def __init__(self, customerNum, preferences, numFlavors):
        self.customerNum = customerNum
        self.preferences = preferences
        self.numLikes = int(preferences[0])
        self.likes = []
        self.satisfied = False
        for i in range(1, numFlavors + 1):
            self.likes.append(None)
        for i in range(1, self.numLikes * 2, 2):
            self.likes[int(preferences[i]) - 1] = preferences[i + 1]

    def GetCustomerNum(self):
        return self.customerNum

    def GetPreferences(self):
        return self.likes

    def IsSatisfied(self):
        return self.satisfied

    def Satisfaction(self, true=True):
        self.satisfied = True if true else False

def IsTherePrefConflict(customer, pref, customers):
    conflict = False
    otherNum = None
    for others in customers:
        if others.GetCustomerNum() == customer:
            continue
        #print "\n============================="
        #print int(pref[1])
        #print int(pref[0])
        #print others.GetPreferences()[int(pref[0])]
        #print "=============================\n"
        if others.GetPreferences()[int(pref[0])]:
            if int(pref[1]) != int(others.GetPreferences()[int(pref[0])]):
                conflict = True
                otherNum = others.GetCustomerNum()
    
    return [conflict, customer, otherNum]

with open("inputFiles/milkshakes.txt") as inputFile:

    inputLines = inputFile.readlines()
    numberOfLines = len(inputLines)
    cases = int(inputLines[0])
    lineNum = 1

    # Each iteration is one case; should loop cases times
    while lineNum < numberOfLines - 1:
        numFlavors = int(inputLines[lineNum])
        flavors = []
        for i in range(0, numFlavors):
            flavors.append('0')
        if VERBOSE:
            print flavors
        numCustomers = int(inputLines[lineNum + 1])
        if VERBOSE:
            print "Number of Flavors: {0}".format(numFlavors)
            print "Number of Customers: {0}".format(numCustomers)
        customers = []
        for customerNum in range(0, numCustomers):
            prefs = inputLines[lineNum + customerNum + 2].rstrip().split(" ")
            customers.append(Customer(customerNum, prefs, numFlavors))
            if VERBOSE:
                print customers[customerNum].GetPreferences()

        flavors = []
        for i in range(0, numFlavors):
            flavors.append('0')

        conflictPairs = {}
        for customerNum in range(0, len(customers)):
            for flavorNum in range(0, numFlavors):
                if VERBOSE:
                    print customers[customerNum].GetPreferences()[flavorNum]
                if customers[customerNum].GetPreferences()[flavorNum]:
                    response = IsTherePrefConflict(customerNum, 
                                                  [flavorNum, customers[customerNum].GetPreferences()[flavorNum]],
                                                  customers)
                    if not response[0]:
                        flavors[flavorNum] = customers[customerNum].GetPreferences()[flavorNum]
                        customers[customerNum].Satisfaction()
                        break
                    else:
                        conflictPairs[str(response[1])] = [str(response[2]), flavorNum]
                
        for customer, conflictData in conflictPairs.iteritems():
            if customers[int(conflictData[0])].IsSatisfied():
                if VERBOSE:
                    print "Conflict Zone"
                    print "################################################"
                    print customer
                    print conflictData
                    print customers[int(customer)].GetPreferences()[conflictData[1]]
                flavors[conflictData[1]] = customers[int(customer)].GetPreferences()[conflictData[1]]
                customers[int(customer)].Satisfaction()
            
        impossible = False
        for customer in customers:
            if not customer.IsSatisfied():
                impossible = True

        if '1' in flavors:
            

        print flavors if not impossible else "Impossible!"

        lineNum = lineNum + 2 + int(inputLines[lineNum + 1])   
