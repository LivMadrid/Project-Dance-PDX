// Create the script tag, set the appropriate attributes
const script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyC389BQpOUF3nQFHc7qky-pJoVMkdJo2Vo&callback=initMap';
script.async = true;

// Attach your callback function to the `window` object
window.initMap = function() {
  // JS API is loaded and available
};

// Append the 'script' element to 'head'
document.head.appendChild(script);
      
AIzaSyC389BQpOUF3nQFHc7qky-pJoVMkdJo2Vo



// let map;

// function initMap() {
//   map = new google.maps.Map(document.getElementById("map"), {
//     center: { lat: -34.397, lng: 150.644 },
//     zoom: 8,
//   });
// }



//Initialize and add the map
function initMap() {
  // The location of PDX
  const portland_or = { lat:  45.523064, lng: -122.676483 };
  // The map, centered at Portland, OR
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: portland_or,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: portland_or,
    map: map,
    icon: " "
  });
}


// GROUP HANDLER FUNCTIONS !

const button = document.querySelector('#joingroup');

button.addEventListener('click', () => {
  alert('You are now a group member');
});


$('#joingroup').on('click', () => {
  console.log("you clicked the button!")
})

