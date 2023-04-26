// get the form and input elements
const form = document.getElementById('date-form');
const dateInput = document.getElementById('date-input');

// add event listener to form submission
form.addEventListener('submit', (e) => {
  e.preventDefault(); // prevent the form from submitting normally
  const date = dateInput.value; // get the value of the input field
  const url = `http://127.0.0.1:5000/view-records-search`; // construct the URL for the API endpoint
  const xhr = new XMLHttpRequest(); // create a new XMLHttpRequest object
  xhr.open('POST', url); // configure the request method and URL
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // set the request header
  xhr.onload = function () {
    if (xhr.status === 200) {
      const response = JSON.parse(xhr.responseText); // parse the JSON response
      // update the UI with the response data
      const table = document.querySelector('table');
      table.innerHTML = ''; // clear the existing table data
      for (const item of response) {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${item.title}</td>
          <td>${item.difficulty}</td>
          <td>${item.score}</td>
          <td>${item.deluxe_score}</td>
          <td>${item.type}</td>
          <td>${item.time}</td>
          <td>${item.track}</td>
          <td><img src="${item.img_link}"></td>
          <td>${item.combo}</td>
          <td>${item.sync}</td>
          <td>${item.place}</td>
          <td>${item.players}</td>
        `;
        table.appendChild(row);
      }
    } else {
      console.error(xhr.statusText);
    }
  };
  xhr.onerror = function () {
    console.error('An error occurred while sending the request.');
  };
  xhr.send(`date=${date}`); // send the request with the form data
});