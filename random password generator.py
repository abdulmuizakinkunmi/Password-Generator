import random
print('RANDOM PASSWORD GENERATOR')
while True:
    instruction=input('Press Y if you want to generate a password: ')
    if instruction=='y':
        a=['AZ','BX','CJ','JB','FR','QM','FZ','YT','XR','TB','WD','FG','LK','RM','VR']
        b=['xc','nh','cv','qr','op','sd','qs','ui','dt','gt','kg','bv','lq','vo','co']
        c=['10','29','38','47','56','13','24','35','46','68','79','80','98','43','81']
        d=['!','@','#','$','%','^','&','*','_','-',':','<','>','?',';']
        print(random.choice(a)+random.choice(b)+random.choice(c)+random.choice(d))
    else:
        quit()
