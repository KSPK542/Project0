from __future__ import print_function

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}

def fruits(orderList):
    totalCost=0.0
    for fruitDetail in orderList:
        fruitName = fruitDetail[0]
        if fruitName in fruitPrices:
            totalCost+=(fruitDetail[1]*fruitPrices[fruitName])
        else:
            return 0.0
    return totalCost


def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    
    x=fruits(orderList)
    return x


# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
