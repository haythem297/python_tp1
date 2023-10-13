from tqdm import tqdm
#do "conda activate python_tp1" then install it with pip install tqdm
#use command "conda env list" to know how many envirements you have
# command to install is "pip install tqdm"
#librarie for progress bar when you parcours list like also in machine learning with this librarie you know witch line and epoch you in so it returns the positions or progress bar of your cursor
l3 = list(range(2,9,2))
print("l3=",l3)
for i in range (len(l3)):
    print(i,l3[i],"test",sep="-",end=" ")

print("")
for i,v in enumerate(l3):
    print(i, v, "test", sep="-", end=" ")
print("")
#tqdm exemple :
# l4=[100]*1000
# import time
# for v in tqdm(l4):
#     time.sleep(2) # donc sleep sta3melneha bech na3rfou el role mta3 tqdm / tawa tnajjem tchouf el avancement mta3 el cursor mta3ek
#     v=v+1

print(l3[1:3]) # bech y affichi mel cas 1 lel cas 3 fel liste / e5er element execlue hathaka 3lech 4 et 6 bark
print(l3[1:2])
print(l3[1:0])