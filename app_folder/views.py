from flask import render_template
from flask import request

from __init__ import app
import ast
pagenum = 1
dataset = []
b = 0
productinfo = open("/home/TilTin/LCBOw/Backup-LCBO/app_folder/ProductInfo.txt")
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
    secondaryitems = open("/home/TilTin/LCBOw/Backup-LCBO/app_folder/Preloaded/{}.txt".format(secondarycat))
    lst = secondaryitems.readlines()

    for line in lst:
        items.append(ast.literal_eval(line))

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
    secondaryitems = open("/home/TilTin/LCBOw/Backup-LCBO/app_folder/Preloaded/{}.txt".format(secondarycat))
    if type(secondaryitems[0]) != "2":
        return render_template("search.html",
                           title='Home',
                           user=user,
                           items=items,
                           test=test,
                        desiredamount = desiredamount)
    for line in secondaryitems:
        items.append(ast.literal_eval(line))



    return render_template("search.html",
                           title='Home',
                           user=user,
                           items=items,
                           test=test,
                           desiredamount = desiredamount)
