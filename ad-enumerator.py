# This is a Python script that demonstrates how to perform a basic Active Directory (AD) penetration test.
# Note: This script is for educational purposes only and should not be used for unauthorized access or malicious activities.

import ldap3
import ssl

# Define the target AD server and credentials
target_server = 'ldap://ad-server.com'
username = 'user'
password = 'pass'

# Establish a connection to the AD server
server = ldap3.Server(target_server, get_info=ldap3.ALL)
connection = ldap3.Connection(server, user=username, password=password, auto_bind=True)

# Search for users in the AD
search_base = 'dc=your-domain,dc=com'
search_filter = '(objectClass=user)'
attributes = ['cn', 'mail', 'memberOf']

# Perform the search
connection.search(search_base, search_filter, attributes=attributes)

# Print the results
for entry in connection.entries:
    print(f"User: {entry.cn}, Email: {entry.mail}, Groups: {entry.memberOf}")

# Close the connection
connection.unbind()
