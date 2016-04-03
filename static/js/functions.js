function sortTableBy(sorting) {
  $("table").trigger("sorton",[sorting]);
}

function checkLastSort() {
  var cookie=getCookie("lastSort");
  if (cookie != "") {
    if (cookie == "school") {
      var sorting = [[2,0],[1,0],[0,0]];
      sortTableBy(sorting);
    }
    else if (cookie == "name") {
      var sorting = [[0,0]];
      sortTableBy(sorting);
    }
    else if (cookie == "level") {
      var sorting = [[1,0]];
      sortTableBy(sorting);
    }
  }
}

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + "; " + expires;
}
function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0)==' ') c = c.substring(1);
    if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
  }
  return "";
}
