// Get all the rows in the table
const rows = document.querySelectorAll('tr');

// Loop through each row and attach a click event listener
rows.forEach(row => {
  row.addEventListener('click', (event) => {
    event.preventDefault();

    console.log('clicked');

    // Get the values for the "Time", "Title", and "Type" columns for the clicked row
    const time = row.cells[9].textContent;
    const title = row.cells[1].textContent;
    const type = row.cells[2].textContent;

    console.log(time, title, type);

    // Create a new form element
    const form = document.createElement('form');

    // Set the attributes for the form
    form.setAttribute('method', 'POST');
    form.setAttribute('action', '/test');
    form.setAttribute('target', '_blank');

    // Create three hidden input elements for the "Time", "Title", and "Type" values
    const timeInput = document.createElement('input');
    timeInput.setAttribute('type', 'hidden');
    timeInput.setAttribute('name', 'time');
    timeInput.setAttribute('value', time);

    const titleInput = document.createElement('input');
    titleInput.setAttribute('type', 'hidden');
    titleInput.setAttribute('name', 'title');
    titleInput.setAttribute('value', title);

    const typeInput = document.createElement('input');
    typeInput.setAttribute('type', 'hidden');
    typeInput.setAttribute('name', 'type');
    typeInput.setAttribute('value', type);

    // Append the input elements to the form
    form.appendChild(timeInput);
    form.appendChild(titleInput);
    form.appendChild(typeInput);

    // Serialize the form data
    const formData = new FormData(form);
    const formDataString = new URLSearchParams(formData).toString();

    // Submit the form to send the data via POST
    fetch('/test', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: formDataString
    })
    .then(response => response.json())
    .then(data => {
      // Open a new page at "/display-test" with the received data
      const params = new URLSearchParams(data);
      window.open(`/display-test?${params.toString()}`);
    })
    .catch(error => console.error(error));

    // Reset the form for next click event
    //form.reset();
  });
});



function addCustomDifficultyRows(table) {
  const rows = table.querySelectorAll('tr');
  rows.forEach(row => {
    const difficultyCell = row.querySelector('td:nth-child(4)');
    if (difficultyCell) {
      const difficulty = difficultyCell.textContent.trim().toLowerCase();
      const classToAdd = `${difficulty}-row`;
      row.classList.add(classToAdd);
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const table = document.querySelector('table');
  addCustomDifficultyRows(table);
});

// get the form and input elements
const form = document.getElementById('date-form');
const dateInput = document.getElementById('date-input');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const date = dateInput.value;
  const url = `http://127.0.0.1:5000/view-records-search`;
  const xhr = new XMLHttpRequest();
  xhr.open('POST', url);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onload = function () {
    if (xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      const table = document.querySelector('table');
      table.innerHTML = '';
      const headerRow = document.createElement('tr');
      headerRow.innerHTML = `
          <th></th>
          <th>Title</th>
          <th>Type</th>
          <th>Difficulty</th>
          <th>Score</th>
          <th style="width: 3%">Combo</th>
          <th style="width: 3%">Sync</th>
          <th style="width: 3%">Place</th>
          <th style="width: 11%">P2</th>
          <th>Time</th>
          <th>Track</th>
        `;
      table.appendChild(headerRow);
      for (const item of response) {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td><img src="${item.img_link}"></td>
        <td style="width: 30%">${item.title ? item.title : ''}</td>
        <td>${item.type ? item.type.toUpperCase() : ''}</td>
        <td>${item.difficulty ? item.difficulty : ''}</td>
        <td>${item.score ? item.score : ''}</td>
        <td style="width: 3%">${item.combo ? item.combo : ''}</td>
        <td style="width: 3%">${item.sync ? item.sync : ''}</td>
        <td style="width: 3%">${item.place ? item.place : ''}</td>
        <td style="width: 11%">${item.player2 ? item.player2 : ''}</td>
        <td>${item.time ? item.time : ''}</td>
        <td>${item.track ? item.track : ''}</td>
      `;      
        table.appendChild(row);
        const difficultyCell = row.querySelector('td:nth-child(4)');
        if (difficultyCell.textContent.trim().toLowerCase() === "remaster") {
          row.classList.add('remaster-row');
        
        }
        if (difficultyCell.textContent.trim().toLowerCase() === "master") {
          row.classList.add('master-row');
        
        }
        if (difficultyCell.textContent.trim().toLowerCase() === "expert") {
          row.classList.add('expert-row');
        
        }
        if (difficultyCell.textContent.trim().toLowerCase() === "advanced") {
          row.classList.add('advanced-row');
        
        }
        if (difficultyCell.textContent.trim().toLowerCase() === "basic") {
          row.classList.add('basic-row');
        
        }
      }
    } else {
      console.error(xhr.statusText);
    }
  };
  xhr.onerror = function () {
    console.error('An error occurred while sending the request.');
  };
  xhr.send(`date=${date}`);
  
});
