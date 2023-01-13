// this script pulls state data from gis-server.cartobin.com api 
// then renders the data into cards in line with the bootstrap theme

// HOW TO USE:
// <div id="restServices"></div>
// <script src="js/cartobin-state-api.js" reqState=""></script>

// concatenate api request url from state html page
var reqState = document.currentScript.getAttribute("reqState");
var stateAPIURL = 'https://gis-servers.cartobin.com/state/';
var stateURL = stateAPIURL + reqState;

// fetch the json data from the api 
// call append function to add the data to the state html doc
fetch(stateURL)
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        appendData(data);
    })
    .catch(function (err) {
        console.log('error: ' + err);
    });

// renders json data into divs on the state html page
function appendData(data) {
    var mainContainer = document.getElementById("restServices");
    for (var i = 0; i < data.servers.length; i++) {
        // create main card div element
        var div = document.createElement("div");
        div.className = "card w-auto";

        // create nested card body element
        var div2 = document.createElement('div');
        div2.className = "card-body"
        div.appendChild(div2);

        // create nested h5 element
        var h5title = document.createElement('h5');
        h5title.className = "card-title";
        div2.appendChild(h5title);

        // create nested p element
        var p = document.createElement('p');
        p.className = "card-text";
        div2.appendChild(p);

        // create nested a element
        var a = document.createElement('a');
        a.className = 'btn btn-primary';
        a.setAttribute('href', data.servers[i]["server_url"]);
        a.setAttribute('target', "_blank");
        a.setAttribute('rel', 'nofollow noopener');
        div2.appendChild(a);

        // render content inside of created elements
        // conditional that renders the title of the card with the org, county or city
        // concatenation needs some work, only concats county, want to render "City of " for cities
        h5title.innerHTML = (data.servers[i]["server_owner"] || data.servers[i]["government_town"] || data.servers[i]["government_county"] + " County");
        p.innerHTML = data.servers[i]["server_url"];
        a.innerHTML = "Rest Service Index"
        mainContainer.appendChild(div);
    }
}