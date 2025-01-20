x = """(%d,'001U800000FZxuGIAT',2,'short',0,'','','USD',0,'n8n Dealer','no_relationship',0,'','','','','','',0,'','bizintegrations-prod.com',1731563059,'',1731563059,0,1),\n"""

l = []
for i in range(3000010, 3100010):
    l.append(x%i)

with open("account.sql", "w") as file:
    for a in l:
        file.write(a)
