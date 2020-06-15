function query(movie) {
  var url = "cgi-bin/question.py" + movie;
  console.log(url);
  standart(url, fill);
}

function fill(data) {
  //var table = "<table id='demo'>";
  //for (let dat in data) {
  console.log(dat);
}

function standart(url, callback) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      //tablae = JSON.parse(this.responseText);
      //console.log(this.responseText);
      //console.log(tablae);
      callback(this.responseText);
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}
