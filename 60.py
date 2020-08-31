import os
s=[p for p in os.listdir('New folder') if os.path.isfile('New folder/'+p)]
print(s)
