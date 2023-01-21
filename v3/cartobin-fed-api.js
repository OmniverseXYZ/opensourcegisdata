// this script pulls all of the federal sources from gis-server.cartobin.com api 
// then based on the request from the html doc it cleans the data to only display what is requested
// then renders the data into cards in line with the bootstrap theme

// HOW TO USE:
// <div id="restServices"></div>
// <script src="js/cartobin-fed-api.js" reqFederal=""></script>

// variable that contains the requested data from the html
var reqFederal = document.currentScript.getAttribute("reqFederal")
var fedAPIURL = 'https://gis-servers.cartobin.com/federal/'
// array used to store all of the data from the api
var serverArray = []
// array used to store the cleaned data containing only the requested items
var reqServerArray = []

// fetch the json data from the api 
// call append function to add the data to the state html doc
fetch(fedAPIURL)
    .then(function (response) {
        return response.json()
    })
    .then(function (data) {
        serverArray = [...data.servers]
        cleanData(serverArray, reqFederal);
        console.log(reqServerArray)
        appendData(reqServerArray);
    })
    .catch(function (err) {
        console.log('ERROR: ' + err);
    });

//return an array of values that match on a certain key
function getValues(obj, key) {
    var objects = []
    for (var i in obj) {
        if (!obj.hasOwnProperty(i)) continue
        if (typeof obj[i] == 'object') {
            objects = objects.concat(getValues(obj[i], key));
        } else if (i == key) {
            objects.push(obj[i])
        }
    }
    return objects
}

// this function finds all of the values from the "server_owner" key that include the requested string
function cleanData(data, reqFederal) {
    // loop to iterate through the entire json object 
    for (var i = 0; i < data.length; i++) {
        // variable that contains the value of "server_owner" for object  
        var serverOwner = getValues(data[i], "server_owner")
        // check if the "serverOwner" variable contains the requested string
        if (serverOwner[0].includes(reqFederal)) {
            // add the entire element to a new global array
            reqServerArray.push(serverArray[i])
        } else {
            //console.log("reqFederal Not Found")
        }
    }
}

// renders data into divs on the federal agency html page
function appendData(data) {
    var mainContainer = document.getElementById("restServices");
    for (var i = 0; i < data.length; i++) {
        // create main card div element
        var div = document.createElement("div");
        //div.className = "card w-auto";

        // create nested card body element
        var div2 = document.createElement('div');
        //div2.className = "card-body"
        div.appendChild(div2);

        // create nested h5 element
        var h5title = document.createElement('h3');
        //h5title.className = "card-title";
        div2.appendChild(h5title);

        // create nested p element
        var p = document.createElement('p');
        //p.className = "card-text";
        div2.appendChild(p);

        // create nested a element
        var a = document.createElement('a');
        a.className = 'btn btn-primary';
        a.setAttribute('href', data[i]["server_url"]);
        a.setAttribute('target', "_blank");
        a.setAttribute('rel', 'nofollow noopener');
        div2.appendChild(a);

        // render content inside of created elements
        h5title.innerHTML = (data[i]["server_owner"]);
        p.innerHTML = data[i]["server_url"];
        a.innerHTML = "Rest Service Index"
        mainContainer.appendChild(div);
    }
}