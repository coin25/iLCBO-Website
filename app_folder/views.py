from flask import render_template
from flask import request

from app_folder import app
import time
import ast
pagenum = 1
dataset = []
b = 0
productinfo = open("ProductInfo.txt")
for line in productinfo:
    dataset.append(line)
datasetfresh = []

for i in range(len(dataset) - 1):
    str1 = dataset[i]
    datasetfresh.append(str1[:-2])






def searchabv(dol_per_eth_desired,dict_abv_dollar):
    temp = []
    for productid, dol_per_eth in dict_abv_dollar.items():
        if dol_per_eth == dol_per_eth_desired:
            temp.append(productid)
    return temp

def database():
    iddatabase = {}
    for k in datasetfresh:
        for i in ast.literal_eval(k)["result"]:
            iddatabase[i["id"]] = i
    return iddatabase


@app.route('/')
@app.route('/lcbo.html')
def index():
    return render_template("lcbo.html")

@app.route('/map.html')
def googleMap():
    return render_template("map.html")
@app.route('/stores.html')
def stores():
    return render_template("stores.html")
@app.route('/products.html')
def products():
    return render_template("products.html")

'''
@app.route('/V', defaults={'path': ''})
@app.route('/<path:secondarycat>',methods=['GET', 'POST'])
'''

@app.route('/search.html')
def searchfor():
    desiredamount = 1


    items =[]
    ids = []
    prev = 0
    dict_cont = {}
    dict_abv_dollar = {}
    test = [2]
    user = {'nickname': 'Austin'}

    if request.args.get('secondarycat') == None:
        return render_template("search.html",
                           title='Home',
                           user=user,
                           items=items,
                           test=test,
                               desiredamount = desiredamount)
    else:
        secondarycat = str(request.args.get('secondarycat'))
    if request.method == 'POST':
        if request.form.get('sort-by-cheapest'):
            return render_template("products.html")
    for l in datasetfresh:
        l = ast.literal_eval(l)
        for i in l["result"]:
            if i["secondary_category"] == secondarycat or i["primary_category"] == secondarycat:
                dict_cont[i["id"]] = [i["alcohol_content"], i["price_in_cents"], i["package_unit_volume_in_milliliters"]]

    for i in range(len(dict_cont)):
        if dict_cont[list(dict_cont.keys())[i]][0] != 0 and dict_cont[list(dict_cont.keys())[i]][2] != 0:
            dict_abv_dollar[list(dict_cont.keys())[i]] = (float(dict_cont[list(dict_cont.keys())[i]][1]) / 100) / ((float(dict_cont[list(dict_cont.keys())[i]][0]) / 10000) * float(dict_cont[list(dict_cont.keys())[i]][2]))
    #print(dict_abv_dollar)

    sorted_abv_dollar = sorted(list(dict_abv_dollar.values()))
    #print(sorted_abv_dollar)
    sorted_abv_dollar = sorted_abv_dollar[:50]
    for v in sorted_abv_dollar:
        if v != prev:
            for productid in searchabv(v,dict_abv_dollar):
                ids.append(productid)
        prev = v

    current_database = database()
    for productid in ids:
        items.append(current_database[productid])
    #for i in items:



        #sort by price, get fucked ratio, binary search



    return render_template("search.html",
                           title='Home',
                           user=user,
                           items=items,
                           test=test,
                           desiredamount = desiredamount)

@app.route('/search.html', methods=['POST'])
def searchforPOST():
    desiredamount = 1
    if request.form.get('text') != None:
        desiredamount = request.form.get('text')

    items =[]
    ids = []
    prev = 0
    dict_cont = {}
    dict_abv_dollar = {}
    test = [2]
    user = {'nickname': request.args.get('secondarycat')}

    if request.args.get('secondarycat') == None:
        return render_template("search.html",
                           title='Home',
                           user=user,
                           items=items,
                           test=test,
                        desiredamount = desiredamount)
    else:
        secondarycat = str(request.args.get('secondarycat'))
    if request.method == 'POST':
        if request.form.get('sort-by-cheapest'):
            return render_template("products.html")
    for l in datasetfresh:
        l = ast.literal_eval(l)
        for i in l["result"]:
            if i["secondary_category"] == secondarycat or i["primary_category"] == secondarycat:
                dict_cont[i["id"]] = [i["alcohol_content"], i["price_in_cents"], i["package_unit_volume_in_milliliters"]]

    for i in range(len(dict_cont)):
        if dict_cont[list(dict_cont.keys())[i]][0] != 0 and dict_cont[list(dict_cont.keys())[i]][2] != 0:
            dict_abv_dollar[list(dict_cont.keys())[i]] = (float(dict_cont[list(dict_cont.keys())[i]][1]) / 100) / ((float(dict_cont[list(dict_cont.keys())[i]][0]) / 10000) * float(dict_cont[list(dict_cont.keys())[i]][2]))
    #print(dict_abv_dollar)

    sorted_abv_dollar = sorted(list(dict_abv_dollar.values()))
    #print(sorted_abv_dollar)
    sorted_abv_dollar = sorted_abv_dollar[:50]
    for v in sorted_abv_dollar:
        if v != prev:
            for productid in searchabv(v,dict_abv_dollar):
                ids.append(productid)
        prev = v

    current_database = database()
    for productid in ids:
        items.append(current_database[productid])
    #for i in items:



        #sort by price, get fucked ratio, binary search



    return render_template("search.html",
                           title='Home',
                           user=user,
                           items=items,
                           test=test,
                           desiredamount = desiredamount)
