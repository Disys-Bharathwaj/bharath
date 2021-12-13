restaurants=[{"nonveg":[{"name":"dindigul thalapakathi","recommened":"chicken briyani,price:Rs.289","starters":["mutton liver,price:Rs.289","mutton sukka,price,price:Rs.319","kuchi mutton,price:339","pallipalayam chicken roast,price:Rs.329"],"Briyani variety":["Thalappatti special mutton briyani[boneless],price:Rs.359","mutton briyani[bone-in],price:Rs.339","chicken briyani[bone-in],price:Rs.289","chicken 65 briyani,price:Rs.309"],"rating":5},
                       {"name":"Anjappar","recommened":"chicken biryani,price:Rs.275","starters":["mutton kola,price:Rs.70/perpc","mutton sukka varval,price:Rs.310","chicken lolipop,price:288","anjappar poricha kozhi,price:325","kadai 65,price:Rs.222"],"Briyani variety":["mutton biryani,price:Rs.325","chicken biryani,price:Rs.275","egg biryani,price:Rs.225","chicken 65 biryani,price:Rs.320","kaadai biryani,price:360"],"chettinad special":["chettinad kozhi masala,price:Rs.295","chettinad kozhi varuval,price:Rs.283"],"Breads":["naan","parotta"],"rating":5},
                       {"name":"salemrr","recommened":"chicken biryani,price:Rs.275","staters":["muton kola,price:Rs.70/perpc","mutton sukka varuval,price:Rs.310","chicken lolipop,price:288","Anjappar poricha kozhi,price:325","kadai 65,price:Rs.222"],"Briyani variety":["mutton biryani,price Rs.325","chicken biryani,price Rs.275","Egg briyani,price:Rs.225","chicken 65 biryani,price:Rs.320","kaadai biryani,price:360"],"chettinad special":["chettinad kozhi masala,price:Rs.295","chettinad kozhi varuval,price:Rs.283"],"Breads":["naan","parotta"],"rating":5},
                       {"name":"buhari","recommened":"chicken biryani,price:Rs.275","staters":["muton kola,price:Rs.70/perpc","mutton sukka varuval,price:Rs.310","chicken lolipop,price:288","Anjappar poricha kozhi,price:325","kadai 65,price:Rs.222"],"Briyani variety":["mutton biryani,price Rs.325","chicken biryani,price Rs.275","Egg briyani,price:Rs.225","chicken 65 biryani,price:Rs.320","kaadai biryani,price:360"],"chettinad special":["chettinad kozhi masala,price:Rs.295","chettinad kozhi varuval,price:Rs.283"],"Breads":["naan","parotta"],"rating":5},
                        {"name":"house","recommened":"chicken biryani,price:Rs.275","staters":["muton kola,price:Rs.70/perpc","mutton sukka varuval,price:Rs.310","chicken lolipop,price:288","Anjappar poricha kozhi,price:325","kadai 65,price:Rs.222"],"Briyani variety":["mutton biryani,price Rs.325","chicken biryani,price Rs.275","Egg briyani,price:Rs.225","chicken 65 biryani,price:Rs.320","kaadai biryani,price:360"],"chettinad special":["chettinad kozhi masala,price:Rs.295","chettinad kozhi varuval,price:Rs.283"],"Breads":["naan","parotta"],"rating":5},
                        {"name":"thupakii","recommened":"chicken biryani,price:Rs.275","staters":["muton kola,price:Rs.70/perpc","mutton sukka varuval,price:Rs.310","chicken lolipop,price:288","Anjappar poricha kozhi,price:325","kadai 65,price:Rs.222"],"Briyani variety":["mutton biryani,price Rs.325","chicken biryani,price Rs.275","Egg briyani,price:Rs.225","chicken 65 biryani,price:Rs.320","kaadai biryani,price:360"],"chettinad special":["chettinad kozhi masala,price:Rs.295","chettinad kozhi varuval,price:Rs.283"],"Breads":["naan","parotta"],"rating":5},
                        {"name":"bhai","recommened":"chicken biryani,price:Rs.275","staters":["muton kola,price:Rs.70/perpc","mutton sukka varuval,price:Rs.310","chicken lolipop,price:288","Anjappar poricha kozhi,price:325","kadai 65,price:Rs.222"],"Briyani variety":["mutton biryani,price Rs.325","chicken biryani,price Rs.275","Egg briyani,price:Rs.225","chicken 65 biryani,price:Rs.320","kaadai biryani,price:360"],"chettinad special":["chettinad kozhi masala,price:Rs.295","chettinad kozhi varuval,price:Rs.283"],"Breads":["naan","parotta"],"rating":5},
                        {"name":"aarthy","recommened":"chicken biryani,price:Rs.275","staters":["muton kola,price:Rs.70/perpc","mutton sukka varuval,price:Rs.310","chicken lolipop,price:288","Anjappar poricha kozhi,price:325","kadai 65,price:Rs.222"],"Briyani variety":["mutton biryani,price Rs.325","chicken biryani,price Rs.275","Egg briyani,price:Rs.225","chicken 65 biryani,price:Rs.320","kaadai biryani,price:360"],"chettinad special":["chettinad kozhi masala,price:Rs.295","chettinad kozhi varuval,price:Rs.283"],"Breads":["naan","parotta"],"rating":5}]}]
for i in restaurants:
    if i["nonveg"][0]["rating"]>=4:
            if i["nonveg"][0]["name"] == "Dindigul Thalapakathi":
                print("\nDindigul Thalapakathi:")
                print("Starters:")
                print(restaurants[0]["nonveg"][0]["starters"])
                print("\nBiryani Variety:")
                print(restaurants[0]["nonveg"][0]["Biryani variety"])
                print("\nRecommened Food:")
                print(restaurants[0]["nonveg"][0]["recommened"])

                
for i in restaurants:
    if i["nonveg"][1]["rating"]>=4:
            if i["nonveg"][1]["name"] == "Anjappar":
                print("\nAnjappar:")
                print("Starters:")
                print(restaurants[0]["nonveg"][1]["starters"])
                print("\nBiryani Variety:")
                print(restaurants[0]["nonveg"][1]["Briyani variety"])
                print("\nChettinad Special:")
                print(restaurants[0]["nonveg"][1]["chettinad special"])
                print("\nRecommened Food:")
                print(restaurants[0]["nonveg"][1]["recommened"])

                
for i in restaurants:
    if i["nonveg"][2]["rating"]>=4:
            if i["nonveg"][2]["name"] == "Buhari":
                print("\nBuhari:")
                print("Starters:")
                print(restaurants[0]["nonveg"][2]["starters"])
                print("\nBiryani Variety:")
                print(restaurants[0]["nonveg"][2]["Briyani variety"])
                print("\nRecommened Food:")
                print(restaurants[0]["nonveg"][2]["recommened"])

                
for i in restaurants:
    if i["nonveg"][3]["rating"]>=4:
            if i["nonveg"][3]["name"] == "Pandian":
                print("\nPandian:")
                print("Starters:")
                print(restaurants[0]["nonveg"][3]["starters"])
                print("\nBiryani Variety:")
                print(restaurants[0]["nonveg"][3]["Briyani variety"])
                print("\nRecommened Food:")
                print(restaurants[0]["nonveg"][3]["recommened"])

for i in restaurants:
    if i["nonveg"][4]["rating"]>=4:
            if i["nonveg"][4]["name"] == "Crescent":
                print("\nCrescent:")
                print("Starters:")
                print(restaurants[0]["nonveg"][4]["starters"])
                print("\nBiryani Variety:")
                print(restaurants[0]["nonveg"][4]["Briyani variety"])
                print("\nRecommened Food:")
                print(restaurants[0]["nonveg"][4]["recommened"])


        
                                                                                                 
