 /*
	This is where we request and receive the data from the API
 */

function store(){
	var v = document.getElementById('num').value;
	var script = document.createElement('script');
  script.src = 'http://lcboapi.com/stores/'+v+'?callback=loadStore';
  script.async = true;
  document.head.appendChild(script);
  }

 function initialStoreLoad(id) {
  var script = document.createElement('script');
  script.src = 'http://lcboapi.com/stores/'+id+'?callback=loadStore';
  script.async = true;
  document.head.appendChild(script);
}

function loadProductsAtStore(id, page){

  var script = document.createElement('script');
  script.src = 'http://lcboapi.com/products?store_id='+id+';where=has_limited_time_offer;order=price_in_cents.asc;callback=loadProduct;page='
  + page+';per_page=100';
  script.async = true;
  document.head.appendChild(script);
}

//for(var i=0;i<654;i++){loadStore(i);}

function start(){
if(localStorage.currStore!= "null"){
    document.getElementById('num').value=parseInt(localStorage.currStore);
  initialStoreLoad(localStorage.currStore);
}
else if(localStorage.store!="null"){
  initialStoreLoad(localStorage.store);
  document.getElementById('num').value=localStorage.store;
}
else{
initialStoreLoad(510);
}}

window.onload= start;