# FinTech Settlement Project
# Python Developer Test Questions
## Created for a friend Diogenes, good luck Diogenes
Question 1
Create a base class with:
● Three properties initialized at construction
● One empty classmethod
● One empty instance method

Question 2
Create a derived class from the base class
● Inherits all properties and methods from the base class
● Initialize the properties differently from the base class
● Add code to the empty methods
Question 3
Use list comprehension and a lambda function to extract all of the even integers out of a list of
integers
Question 4
Use the next() function to find the first element in a list of dictionaries whose attribute ‘x’ = 5.
Default to an empty dictionary if not found.
Question 5
Given the following JSON document:
{
"
}
● Read in the document from a file
● Find and print:
○ The Payee ID value
○ Any invoices that contain the text “583”
● Change any date/time fields to text in the format ‘%Y-%m-%dT%H:%M:%S’
○ Hint: The format of the date/time fields are integer timestamp. To create a
datetime object from an integer timestamp, use the following:
datetime_obj =
datetime.datetime.fromtimestamp(integer_timestamp / 1e3)
● Write the json document back out to a new file
json.dump(data, open('code_test_out.json', 'w'))