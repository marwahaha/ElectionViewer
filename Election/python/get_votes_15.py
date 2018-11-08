import sqlite3
import sys

# Opens connection to database
conn = sqlite3.connect("db/election.db")
c = conn.cursor()

# Uses the second command line argument as the consituency id
# Command is "python3 get_con_names.py x" where x is the con id
con_id = sys.argv[1]

command = """
SELECT Results15.Party_ID, Results15.Votes FROM Results15
WHERE Results15.Con_ID = ?
ORDER BY Results15.Votes DESC;
"""

# Outputs the party id, then a space then their vote
for line in c.execute(command, (con_id,)):
    print(str(line[0]) + " " + str(line[1]))


# Closes the connection
conn.close()
