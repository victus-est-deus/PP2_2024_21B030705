import json

with open("C:/Users/oralb/Downloads/sample-data.json", 'r') as file:
    data = json.load(file)


interfaces = data['imdata']

print("Interface Status")
print('-'*80)


for interface in interfaces:
    attributes = interface['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']

    print(f"{dn:<50} {description:<20} {speed:<6} {mtu}")
