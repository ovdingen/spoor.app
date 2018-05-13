function getStopData(lat, lon) {
    // if stopcode matches valid thingy idk, for example: 50529210
    let queryString = "https://stations.ovdingen.nl/nearest/?lat=" + lat + "&lon=" + lon;
    console.log(queryString);
    getData(queryString);
}

function getData(query) {
    // fetch helper function
    fetch(query)
    .then((response) => {
        return response.json();
    }).then((items) => {
        renderItems(items.stations);
    }).catch((err) => {
        console.log("something failed: ", err);
    });
    // once there is a result, render items with it
}
function renderItems(items) {
    let container = document.querySelector(".stations");
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
    let template =
    `<li class="collection-item"><a href="/station/${item.code}/">${item.name_long}</a> <div class="secondary-content">${item.distance.toFixed(1)} km</div></li>
    `;
    return template;
}