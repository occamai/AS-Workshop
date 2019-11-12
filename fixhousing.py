
f = open("housing.csv")
lines = f.readlines()
f.close()

f = open("nhousing.csv","w")
for ln in lines:
	parts = ln.split()
	nln = ",".join( parts )
	f.write("%s\n" % nln )
f.flush()
f.close()

