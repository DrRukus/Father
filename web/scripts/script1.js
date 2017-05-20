var hexDigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];

function convert() {

    var num = Number(document.getElementById("decNum").value);
    var select = document.querySelector('input[name="select"]:checked').value;
    document.getElementById("binNum").innerHTML = "";

    var result = "";
    if (select === 'binary') {
        for (var i = 1; i < 17; i++) {
    	    if (num / Math.pow(2, (16 - i)) >= 1) {
	        result = result + "1";
                num = num - Math.pow(2, (16 - i));
	    } else { result = result + "0";	}
        }
    } else if (select === 'hexadecimal') {
        for (var j = 1; j < 5; j++) {
	    var powSixt = Math.pow(16, (4 - j));
    	    var hDg = Math.floor(num / powSixt);
    	    if (num / powSixt >= 1) {
	        result = result + hexDigits[hDg - 1];
                num = num - powSixt * hDg;
	    } else { result = result + "0";	}
	}
    }
    //result - "40"
    document.getElementById("binNum").innerHTML += result;
}
