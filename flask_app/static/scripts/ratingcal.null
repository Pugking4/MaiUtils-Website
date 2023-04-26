// Add a click event listener to the Calculate button
document.getElementById('calculate-btn').addEventListener('click', () => {
  // Get the values of the input fields
  const constant = document.getElementById("constant").value;
  const achievement = document.getElementById("achievement").value;
  const rating = document.getElementById("rating").value;

  // Send an AJAX request to the server with the input values
  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://pugking4.me/calculate');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onload = () => {
    // Update the header element with the response text
    const header = document.getElementById('header');
    header.textContent = xhr.responseText;
  };
  xhr.send(`constant=${constant}&achievement=${achievement}&rating=${rating}`);
});
