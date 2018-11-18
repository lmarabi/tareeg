/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
function exportForm() {

var rEmail = document.getElementById("email").value;
    if (rEmail === '') {
        alert('Email filed is empty');
        return;
    }

    if (!validateemail(rEmail)){
	alert("email is invalied");
	return;
    }


    if (boxCoords === null) {
        alert('No area has been chosen!');
        return;
    }


var coords = document.getElementById("boxC").value.split(',');
    var latmax = coords[0];
    var latmin = coords[1];
    var lonmax = coords[2];
    var lonmin = coords[3];
    var area = ((lonmax-lonmin)*(lonmax-lonmin));
    //alert(latmax + '\n' + lonmax + '\n' + latmin + '\n' + lonmin); //////// write here 
    //alert(area)

    if(area > 997.0005035400418){
        alert("area selected is larg kindly select a smaller area!");
        return;
    }


var e = document.getElementById("type");
    var type = e.options[e.selectedIndex].text;

var commaname = document.getElementById("name").value;
var spacename = commaname.replace(",","_");
var rName = spacename.replace(" ","_");
    if (rName === '') {
        alert('Name filed is empty');
        return;
    }

if(type == null){
       alert("select spatial Data type");
       return;
}


request = new XMLHttpRequest();
    request.onreadystatechange = respond_export;
    request.open("POST", "control.php", true /* asynchronous? */)
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    request.send("action=coords&coords=" + document.getElementById("boxC").value +
            "&type=" + type+
            "&rName=" + rName +
            "&rEmail=" + rEmail           
            );
  
    alert("your request of extracting "+type+" has been received you will recieve the result via email to "+rEmail+"  within the next 10 minutes")
    document.getElementById("email").value = "";


}

function validateemail(email) 
{
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}


function respond_export() {
}
function submit_view() {
}
function respond_view() {

}
