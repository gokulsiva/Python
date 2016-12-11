import pickle

f = open("shoplistfile.data", "wb")
shoplist = ['apple', 'orange', 'mango']
pickle.dump(shoplist, f)
f.close()
del shoplist


f = open("shoplistfile.data", "rb")
stored = pickle.load(f)
f.close()

print stored


