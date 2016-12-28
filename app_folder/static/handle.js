
function loadStore(response) {
        var el = document.getElementById('store_name');
        var days = ["sunday_open","sunday_close","monday_open","monday_close","tuesday_open","tuesday_close","wednesday_open",
        "wednesday_close","thursday_open","thursday_close","friday_open","friday_close","saturday_open","saturday_close"];

        // //var deprecated = response.result.is_dead;
        var d = new Date();
        var open = response.result[days[d.getDay()*2]];
        var close = response.result[days[d.getDay()*2+1]];

        // // Resets the html so it does not interfere with previous models
        el.innerHTML=  response.result.name +  '<br>';
        el.innerHTML +='Open from '+ time((open/60 >> 0),(open%60))+
        ' to '+ time((close/60 >> 0),(close%60))+ '<br>';

        loadProductsAtStore(response.result.id, 1);
}

function loadProduct(response){
        var el = document.getElementById('product');
        var p = response.pager.records_per_page;
        for(var i=0;i<p;i++){
          var n = response.result[i].name;
          if(n.toLowerCase().indexOf('gold')!=-1)
          { 
        var img = response.result[i].image_url;
        el.innerHTML = "Specialty Products: <br><img src='"+img+"'>";
          }
        }
}

function allInfo (reponse) {
        var obj = Object.keys(response.result);
        var count = obj.length;
        var it=Iterator(obj);

        // Last one is store number which is deprecated
         for(var i=0; i<count-1; i++){
          var current = it.next();
          var str = current[1];
          //el.append(str +"= "+response.result[str] +"<br>");
          el.innerHTML=el.innerHTML+ str +"= "+response.result[str] +"<br>";
         }
}

function loadStores(response){
      var el = document.getElementById('stores');
      el.innerHTML = response.result[2];
     var count = Object.keys(response.result[1]).length;
}

function time(n,m){
 var s = n +":";
 if(m>=10){
  s+=m;
 }
 else{
  s+="0" +m;
 }
 return s;
}