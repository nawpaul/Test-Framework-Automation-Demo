
"""Page ( )####Pages are a set of classes, named based on the name of the webpage. For e.g.,
 Login-Page, Home-Page, are so named because of the webpage they represent.
The Login-Page will contain the public methods to perform login, and private attributes
for username and password fields. The private attributes for username and password fields will
help maintain encapsulation of the unwanted information for the tests####
 = is a class provided by Selenium WebDriver to support Page Object Design patterns.
  this design pattern in Selenium creates an object repository for storing all web elements.
  A page object is an object-oriented class that serves as an interface to a page of your
   Application Under Test(AUT). It helps reduce code duplication and improves test case maintenance.
***The main advantage of Page Object Model is that if the UI changes for any page, it don’t require
us to change any tests, we just need to change only the code within the page objects (Only at one place).
 Many other tools which are using selenium, are following the page object model.
  ******You have to find the common trigger points that will open in a new window or the
   linking points btw the pages in order to reduce the object creation within our test cases"""



"""#reports ( test cases)= It provides advanced filters and screenshots of all the tests and displays them for each step. It helps in depositing the logs inside the reports, which are user-generated or system-generated so that in the future when you access the report, you can directly view the logs from there rather than rerunning the test cases= These reports help you to identify the information about test cases and the status of a project. Provides the overal html reports for your stakeholders .
C:\python-selenium\TestFrameworkDemo --browser chrome --url http://yatra.com --html=reports/report3.html
..... this is how u create reports within the embedded folder"""



"""#Test data ( )= Allow u to pass multiple set of data to the same script and allow u to exceute 
the script with multiple set of data DDT Data driven test approach=Data set stores the data files, 
Script reads test data from external data sources and executes test based on it.=data input can be 
anything:MS Excel files, Data base, Text files, XML files=Data created or selected to satisfy the
 execution preconditions and input content required to execute one or more test cases.. File data 
 help u to read data in the data file.We can use ddt to externalise the data into the csv file, 
 json file, yml file and the excel file"""
