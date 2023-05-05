import pandas
friends_names=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\friend_names.xls",sheet_name="Sheet1")
print(friends_names)
sty_fil=friends_names[friends_names['Quality']=='style']
print(sty_fil)
fun_fil=friends_names[friends_names['Quality']=='funny']
print(fun_fil)


import pandas
family_members=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\family_members.xls",sheet_name="Sheet1")
print(family_members)
#bro_sis_fil=family_members[(family_members['Relation']=='brother') | (family_members['Relation']=='sister')]
#print(bro_sis_fil)
#pare_fil=family_members[(family_members['FamilyMemberName']=='anwar') |(family_members['FamilyMemberName']=='fathima')]
#print(pare_fil)
pare_fil=family_members[family_members['FamilyMemberName']!="father"]
print(pare_fil)


import pandas
veg_foods=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\Vegfood_items.xlsx",sheet_name='Sheet1')
print(veg_foods)
#soup_fil=veg_foods[(veg_foods['VegFoodName']=="vegsoup") | (veg_foods['VegFoodName']=="tomatosoup")]
#print(soup_fil)
#friedrice=veg_foods[veg_foods['VegFoodName']=='vegfriedrice']
#print(friedrice)
#manchuria=veg_foods[veg_foods['VegFoodName']=='vegmanchuria']
#print(manchuria)
fried_manu_fil=veg_foods[(veg_foods['VegFoodName']=="vegmanchuria") | (veg_foods['VegFoodName']=="vegfriedrice")]
print(fried_manu_fil)

import pandas
non_veg_foods=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\NonVegfood_items.xlsx",sheet_name="Sheet")
print(non_veg_foods)
#chicken_fil=non_veg_foods[non_veg_foods["NonVegFoodName"]==(["chickenbiryani","chicken65","chickenmanchuria","chickenfriedrice","chickenoddles"])]
#print(chicken_fil)
#mutton_fil=non_veg_foods[non_veg_foods['NonVegFoodName']=='muttonbiryani']
#print(mutton_fil)
chic_mutt_fil=non_veg_foods[(non_veg_foods['NonVegFoodName']=='chickenbiryani') | (non_veg_foods['NonVegFoodName']=='muttonbiryani')]
print(chic_mutt_fil)

import pandas
month_details=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\month_names.xlsx",sheet_name="Sheet1")
print(month_details)
#win_mon_fil=month_details[month_details['Season']=="Winter Season"]
#print(win_mon_fil)
#summ_fil=month_details[month_details['Season']=="Summer Season"]
#print(summ_fil)
#man_fil=month_details[month_details['Season']=="Monsoon Season"]
#print(man_fil)
#sum_win_fil=month_details[(month_details['Season']=="Summer Season") | (month_details['Season']=="Winter Season")]
#print(sum_win_fil)
win_man_fil=month_details[(month_details['Season']=="Winter Season") | (month_details['Season']=="Monsoon Season")]
print(win_man_fil)




