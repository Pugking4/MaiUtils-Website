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
      const headerRow = document.createElement('tr');
      headerRow.innerHTML = `
          <th></th>
          <th>Title</th>
          <th>Type</th>
          <th>Difficulty</th>
          <th>Score</th>
          <th>Combo</th>
          <th>Sync</th>
          <th>Place</th>
          <th>P2</th>
          <th>Time</th>
          <th>Track</th>
        `;
      table.appendChild(headerRow);
      for (const item of response) {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>
          <div class="img-container">
            <img id="myImage" class="hoverable-img" src="${item.img_link}">
          </div>
        </td>
        <td>${item.title ? item.title : ''}</td>
        <td>${item.type ? item.type.toUpperCase() : ''}</td>
        <td>${item.difficulty ? item.difficulty : ''}</td>
        <td>${item.score ? item.score : ''}</td>
        <td>${item.combo ? item.combo : ''}</td>
        <td>${item.sync ? item.sync : ''}</td>
        <td>${item.place ? item.place : ''}</td>
        <td>${item.player2 ? item.player2 : ''}</td>
        <td>${item.time ? item.time : ''}</td>
        <td>${item.track ? item.track : ''}</td>
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

  // get all rows in the table
  const rows = document.querySelectorAll('tr');

  // loop through each row
  rows.forEach(row => {
    // get the difficulty cell in the current row
    const difficultyCell = row.querySelector('td:nth-child(3)');
    console.log(difficultyCell.textContent.trim().toLowerCase());

    // check if the difficulty is "expert"
    if (difficultyCell.textContent.trim().toLowerCase() === "expert") {
      // add a CSS class to the row that applies a red outline
      row.classList.add('expert-row');
    }
  });

});
