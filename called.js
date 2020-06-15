function standart(table) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      //tablae = JSON.parse(this.responseText);
      console.log(this.responseText);
      console.log(tablae);
      //fill(table);
    }
  };
  xhttp.open("GET", "cgi-bin/question.py", true);
  xhttp.send();
}
function fill(data) {
  //var table = "<table id='demo'>";
  for (let dat in data) {
    console.log(dat);
  }
}
