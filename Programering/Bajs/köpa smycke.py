guld = 1000
silver = 500
järn = 200

stålar = int(input("hur mycke cash haru? ")) 
if stålar >= guld: 
    print("du har banne mej råd me ett guldsmycke förfan")
elif stålar >= silver: 
    print("amen du har råd me ett silversmycke, d va inte så dåligt")
elif stålar >= järn:
    print("pfft jävla bonde du har bara råd me ett järnsmycke fyfan, gå o köp en jävla spade istället fattiglapp")
elif stålar < järn:
    print("skaffa ett jobb fyfan")
