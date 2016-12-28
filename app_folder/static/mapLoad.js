var numStores=0;
var stores=[];
var currStore = null;
localStorage.currStore=null;

function storeInfo(id, name, lat, long,address){
    this.id=id;
    this.name=name;
    this.lat=lat;
    this.long=long;
    this.address=address;
}

function loadStores(page) {
  var script = document.createElement('script');
  script.src = 'http://lcboapi.com/stores?per_page=100;where_not=is_dead;page='+page+';callback=loadMore';
  script.async = true;
  document.head.appendChild(script);
}

function loadMore(response){
  for(var i=0; i< response.pager.current_page_record_count; i++){
    var r = response.result[i];
    var c = new storeInfo(r.id, r.name, r.latitude, r.longitude,r.address_line_1);
    stores.push(c);
  }

  numStores+= response.pager.current_page_record_count;
  
  if(!response.pager.is_final_page){
    loadStores(response.pager.current_page+1);
  }
  else
  {
    var script = document.createElement('script');
    script.src = 'https://maps.googleapis.com/maps/api/js?callback=initMap';
    script.async = true;
    document.head.appendChild(script);
  }
}

function saveFavourite(){
  if(currStore!=null){
  alert('change from '+ localStorage.store+' to '+currStore.id);
  localStorage.store = currStore.id;
}
}

loadStores(1);