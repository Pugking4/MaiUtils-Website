// Get references to the input fields and table cells
const constantInput = document.getElementById('constant');
const achievementInput = document.getElementById('achievement');
const ratingInput = document.getElementById('rating');
const sCell = document.querySelector('#data-table tr:nth-child(2) td:nth-child(2)');
const splusCell = document.querySelector('#data-table tr:nth-child(2) td:nth-child(3)');
const ssCell = document.querySelector('#data-table tr:nth-child(2) td:nth-child(4)');
const ssplusCell = document.querySelector('#data-table tr:nth-child(2) td:nth-child(5)');
const sssCell = document.querySelector('#data-table tr:nth-child(2) td:nth-child(6)');
const sssplusCell = document.querySelector('#data-table tr:nth-child(2) td:nth-child(7)');
const customCell = document.querySelector('#data-table tr:nth-child(2) td:nth-child(8)');

// Add a click event listener to the Calculate button
document.getElementById('calculate-btn').addEventListener('click', () => {
  // Get the values of the input fields
  const constant = constantInput.value;
  const achievement = achievementInput.value;
  const rating = ratingInput.value;

  // Send an AJAX request to the server with the input values
  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'release\backend\ratingcal.py');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onload = () => {
    // Parse the response JSON
    const { s_rating, splus_rating, ss_rating, ssplus_rating, sss_rating, sssplus_rating, custom_rating } = JSON.parse(xhr.responseText);

    // Update the table cells with the response values
    sCell.textContent = s_rating;
    splusCell.textContent = splus_rating;
    ssCell.textContent = ss_rating;
    ssplusCell.textContent = ssplus_rating;
    sssCell.textContent = sss_rating;
    sssplusCell.textContent = sssplus_rating;
    customCell.textContent = custom_rating;
  };
  xhr.send(`constant=${constant}&achievement=${achievement}&rating=${rating}`);
});
