"""
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
"""
