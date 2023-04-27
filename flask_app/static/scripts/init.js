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