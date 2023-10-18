import xml.etree.ElementTree as Et

# Define the XML input as a string
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

# Parse the XML input string into an ElementTree object
stuff = Et.fromstring(input)

# Find all elements with the path 'users/user' and store them in a list
lst = stuff.findall('users/user')

# Print the count of 'user' elements found
print('User count:', len(lst))

# Loop through each 'user' element in the list
for item in lst:
    # Print the text content of the 'name' element
    print('Name', item.find('name').text)

    # Print the text content of the 'id' element
    print('Id', item.find('id').text)

    # Print the value of the 'x' attribute of the 'user' element
    print('Attribute', item.get("x"))
