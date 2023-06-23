"""#Test cases(conftest, test_search) Test cases= allow us to execute test cases and are created using elements locator.####Tests are a set of classes, named based on the test to be conducted for each webpage. For e.g., LoginTest, is so named because of the test method that would be used to test the Login page/action.
The LoginTest will contain the public methods annotated with “@Test” to test the login functionality.
The LoginTest will instantiate the LoginPage class, using the PageFactory.initElements method, and then
will invoke the LoginPage log in method with data parameters for username and password which will set
 the values in the username and password fields in the web application, and click on the submit button.
 Validations need to be inserted post the submit button click so that the login can be validated.
 Boolean values are returned from the Login-Page, and assertions are performed at the test level for validations.##"""



"""Conftest ( )= Helps you to write tests against structured configuration data. 
That this file serves as a means of providing fixtures for an entire directory and fixtures define 
in this conftest file can be used by any test in that package without needing to import them because pytest
 will automatically discover them. """
