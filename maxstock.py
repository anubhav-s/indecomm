"""
Solution to coding problem by Indecomm
"""

import csv
from csv import DictReader
import collections
import os
import re
import string

class StockSharePrice:
    def getMaxCompanyStockDetails(self, csv_file_read):
        """
        Returns a dict with company name as key and their corresponding max share price details as values which is a
        key for another set of values having year and month in a list.
        This code also deals with the scenarios where a company has maximum value share price for multiple years.
        Dictionary structure :
            {Company Name: {max share price : [[month of max share price , year of max share price]]}
        eg. {'Company A': {51 : [(' Nov', '2013')]}, 'Company B': {16 : [(' Aug', '2000')]}, 'Company C': {201 : [(' Jan', '1990')]}}

        """
        try:
            with open(csv_file_read, 'rb') as f:
                reader = DictReader(f, delimiter = ',')

                # First line of the csv file contains the column headers of the data
                # First column --------------> year
                # Second column -------------> month
                year = reader.fieldnames[0]
                month = reader.fieldnames[1]

                if (not year.lower() == 'year'):
                    print "Please enter the fields in the CSV file"
                    return

                row_length = len(reader.fieldnames)
                maxPriceCompanyDetailsDict = collections.OrderedDict()
                maxPriceDetails = {0 : []}
                pattern = re.compile('^[1-9][0-9][0-9][0-9]$')

                # traversing from 3rd column till last to get a list of company names in a dictionary
                for i in xrange(2,row_length):
                    maxPriceCompanyDetailsDict[reader.fieldnames[i]] = maxPriceDetails

                companyNamesList = maxPriceCompanyDetailsDict.keys() # List of companies

                # traversing each row in the CSV through the reader object
                for row in reader:

                    matchObj = re.match(pattern, str(row[year].strip()))

                    if (row_length < len(row)):
                        print "Field Name missing from the csv. Please input correct CSV file."
                        pass
                    elif(matchObj == None):
                        print "Incorrect value of the year"
                        pass
                    else:
                        for company in companyNamesList:
                            value_list , tempList = [] , []
                            try:
                                # try block to check for literals like 'abc'
                                currentSharePrice = int(row[company])

                                if (currentSharePrice < 0):
                                    print "Negative Value of a share is not possible..."
                                    pass
                                elif (currentSharePrice is None or currentSharePrice is ''):
                                    print "Wrong or No value "
                                    pass
                                else:
                                    maxSharePriceDetails = maxPriceCompanyDetailsDict[company]

                                    if int(currentSharePrice) > int(maxSharePriceDetails.keys()[0]):
                                        tempDict = {}
                                        priceList = int(currentSharePrice)
                                        value_list.append(row[month].strip())
                                        value_list.append(row[year].strip())
                                        tempList.append(tuple(value_list))
                                        tempDict[currentSharePrice] = tempList
                                        maxPriceCompanyDetailsDict[company] = tempDict
                                    elif (currentSharePrice == maxSharePriceDetails.keys()[0]):
                                        value_list.append(row[month])
                                        value_list.append(row[year])
                                        maxPriceCompanyDetailsDict[company][currentSharePrice].append(tuple(value_list))
                                    else:
                                        pass

                            except ValueError, v:
                                    # Exception raised in case currentSharePrice is literal
                                    pass
                            except Exception, exp:
                                    pass
                print maxPriceCompanyDetailsDict
                return maxPriceCompanyDetailsDict

        except IOError,ex:
            print 'Error in opening CSV file' +'\n'+ex

        except Exception,e:
            print e

        finally:
            f.close()
            
