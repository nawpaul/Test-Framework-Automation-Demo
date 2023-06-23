
"""#Base (base_driver) ####BasePage is a class which contains the reusable methods that will be used by the various pages. For e.g.,
 the BasePage class contains “getWebElement” method which will return a web-element when you pass the locator and the driver instances.
 #####= has the common method that can be use by all of the pages in our application and all the other pages will import all the drivers
 from the basedriver. Thus one can reuse the scripts on this driver that is webdriver. When inheriting the base driver we inhirith the method init
 and supperclass =Base  class helps us to have one place to mention browser initialization rather than mentioning it on the test case i.e holds the methods to inialize
  and terminate the webdriver object. Anything which is dependent of the driver references goes to the base driver. """