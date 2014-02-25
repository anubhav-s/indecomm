import unittest
import maxstock
from maxstock import StockSharePrice
from os import remove

class MaxSharePriceTestCase(unittest.TestCase):
     #Populate sample data into a csv file and test the method 'findMaxSharePriceDetails' by verifying
     #  that the result it returns, matches the expected result. Delete the file in the end.
    def setUp(self):
        data = """Year,Month,Company A,Company B,Company C,Company D
1990, Jan, 10, 15, 200, xxxxxx
1990, Feb, 10, 15, 200, 500
1990, Mar, 10, 15, 16,
1990, Apr, 10, 15, 16, 200
1990, May, 40, 10, 15, 200
1990, Jun, 40, 10, 15, 200
1990, Jul, 40, 10, 15, 200
1990, Aug, 40, 16, 15, 200
1990, Sep, 40, 10, 15, 200
1990, Oct, 50, 10, 15, 200
, Nov, 51, 10, 15, 16
1990, Dec, 20, 10, 16, 200
1991, Jan, 50, 60, 40, 300
1991, Feb, 10, 15, 200, 500
1991, Mar, 10, 15, 16,
1991, Apr, 10, 15, 16, 200
1991, May, 40, 10, 15, 200
-1991, Jun, 40, 10, 15, 200
1991, Jul, 40, 10, 15, 200
1991, Aug, 40, 16, 15, 200
1991, Sep, 40, 10, 15, 200
1991, Oct, 50, 10, 15, 200
, Nov, 51, 10, 15, 16
1991, Dec, -200, 10, 16, 400"""

        self.csvfile = "sample_data.csv"
        # write the sample data into the csv file
        try:
            with open(self.csvfile, 'wb') as f:
                f.write(data)

        except IOError,e:
            print "Error in opening and writing Csv file..."
            return
        except Exception, ex:
            return
        # below is the expected result
        self.maxSharePricesDict = {'Company A': {50: [('Oct', '1990'), (' Jan', '1991'), (' Oct', '1991')]}, 'Company B': {60: [('Jan', '1991')]}, 'Company C': {200: [('Jan', '1990'), (' Feb', '1990'), (' Feb', '1991')]}, 'Company D': {500: [('Feb', '1990'), (' Feb', '1991')]}}

    def testFindMaxSharePriceDetails(self):
        # assert that the max share price details returned by 'findMaxSharePriceDetails' function matches expected result
        object_StockSharePrice = StockSharePrice()
        self.assertEqual(object_StockSharePrice.getMaxCompanyStockDetails(self.csvfile), self.maxSharePricesDict, 'Output and Expected result not matching')

    def tearDown(self):
        # delete the csv file
        remove(self.csvfile)

if __name__ == "__main__":
    unittest.main()
    
