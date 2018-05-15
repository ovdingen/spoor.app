let currentStation;

function getStopData(station) {
    // if stopcode matches valid thingy idk, for example: 50529210
    let queryString = "https://dvs.ovdingen.nl/v2/station/" + station.toUpperCase();
    currentStation = station;
    getData(queryString);
}

function startLoop(time, station) {
    currentStation = station;
    getStopData(currentStation);
    intervalId = setInterval(function() {getStopData(currentStation)}, time);
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

function getData(query) {
    // fetch helper function
    fetch(query)
    .then((response) => {
        return response.json();
    }).then((items) => {
        renderItems(items.vertrektijden);
    }).catch((err) => {
        console.log("something failed: ", err);
    });
    // once there is a result, render items with it
}
function renderItems(items) {
    let container = document.querySelector("#stationscontainer");
    container.innerHTML = ""
    console.log("Rendering items: ")
    console.log(items);
    // takes in a template for the html it needs
    // generates the appropriate html and renders each item
    
    items.forEach(item => {
        container.innerHTML += toElement(item);
    });
}

function toElement(item) {
    let dd = new Date(item.vertrek);
    let ds = checkTime(dd.getHours()) + ":" + checkTime(dd.getMinutes());

    let opmerkingen = "";
    for (var i = 0; i < item.opmerkingen.length; i++) {
        opmerkingen = opmerkingen + '<p class="red-text">' + item.opmerkingen[i] + "</p>";
    }
    let tips = "";
    for (var i = 0; i < item.tips.length; i++) {
        tips = tips + '<i>' + item.tips[i] + "</i>";
    }
    let template =
    `
  <div class="vertrek">
    <div class="col s12 m6 l4">
      <div class="card card-vertrek">
        <a href="/train/today/${item.treinNr}" class="black-text"><div class="card-content">
        <span class="card-title yellow-text text-darken-4"><b>${ds}</b> | spoor: <b class="right-align">${item.spoor}</b></span>
          <span class="card-title">(${item.soortAfk}) ${item.bestemming}</span>
          <p>${item.opgeheven == false && item.via ? "via " + item.via + "<br>": ""}
          ${opmerkingen}
          ${tips}</p>
        </div></a>
      </div>
    </div>
  </div>
    `;
    return template;
}
