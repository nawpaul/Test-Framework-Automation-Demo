
"""#Ultility=k#####Utilities contain the various reusable classes and methods for overall
 run of the test suite. An example of a utility class could be a TestListener implementation
  to capture screenshots in case of failures###
 ( represent those clasees and method which can be reuses again without the need of writing
  into our test case again and again by excluding the business layer (test cases) from the technical
   layer of the framework

Asserts ( ) are validations or checkpoints for an application. Assertions state confidently that application behavior
is working as expected. Assertion are the key aspect of verification  coz as soon as the is a failure encounter
 in the verifcation the script exit but we loop all of the value to verify that all the script run even if the
 is a verifcation failure. Anything which is independent of the driver references goes to the utility coz we
 don't wanna change or wrap around any method. It's good to keep all the log in one file into ur classes instead
 of a print statement"""
