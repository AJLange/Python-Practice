

function closeBox()
{
    var box = document.getElementById("cookiebox");
    box.remove();
}



function alertme()
{
    alert('Loading weather report...');
}

async function getAPIData(city, units)
{
    var lat, lon;
    if(city == "Burbank"){
        lat = 34.18
        lon = -118.3
    }
    else if(city == "Chicago"){
        lat = 41.88
        lon = -87.623
    }
    else if(city == "Dallas"){
        lat = 32.77
        lon = -96.809
    }
    
    weather = await getWeatherData(lat, lon, units)
    document.getElementById("hightemp0").innerText = weather.main.temp_max;
    document.getElementById("lowtemp0").innerText = weather.main.temp_min;
    document.getElementById("weathercaption").innerText = weather.weather[0].description;
    document.getElementById("thisCity").innerText = weather.name;

}


async function getWeatherData(lat, lon, units) {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var APIkey = "mykeygoeshere"
    var response = await fetch("http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid="+ APIkey + "&units=" + units);
    // We then need to convert the data into JSON format.
    var coderData = await response.json();
    return coderData;
}



function convertTemps(ele){
    console.log(`Convert to ${ele.value}`);
    
        if(ele.value === 'C'){
            units = "metric";
            
    }
        else if(ele.value === 'F'){
            units = "imperial";
        }

}
