from xrpl.clients import JsonRpcClient
from xrpl.models.requests import LedgerData
import xrpl

# Create a client to connect to the network.
# client = JsonRpcClient("http://192.168.1.19:5005")
#client = JsonRpcClient("http://192.168.1.20:51233")
client = JsonRpcClient("https://s1.ripple.com:51234/")

# Query the most recently validated ledger for info.
#ledger = LedgerData(ledger_index="validated")
ledger = LedgerData(ledger_index="32571", limit=3, type="account", binary=True)
ledger_data = client.request(ledger).result
ledger_data_index = ledger_data["ledger_index"]

'''
test_ledgerEntry = xrpl.models.requests.LedgerEntry(index="7DB0788C020F02780A673DC74757F23823FA3014C1866E72CC4CD8B226CD6EF4", ledger_index="93860697")
ledger_entry = client.request(test_ledgerEntry).result
print(ledger_entry)

'''
print("Ledger: 32571")
# Create a function to run on each API call.
def printLedgerResult():
    print(ledger_data)

# Create a function to write the result of the API call to a file
import json
def printLedgerResultFile():
    f = open("demofile_STATE_DATA_LINES_32571.txt", "a")
    f.write(json.dumps(ledger_data))
    f.write("\n")
    f.close()



# Execute function at least once before checking for markers.
i=0
import datetime
while True:
    i=i+1
    if i%100==1:
        now=datetime.datetime.now()
        print(i, now)
    printLedgerResultFile()
    if "marker" not in ledger_data:
        break
    
    # Specify the same ledger and add the marker to continue querying.
    ledger_marker = LedgerData(ledger_index=ledger_data_index, marker=ledger_data["marker"])
    ledger_data = client.request(ledger_marker).result
