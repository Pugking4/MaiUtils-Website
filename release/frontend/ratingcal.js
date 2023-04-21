const calculateBtn = document.querySelector("#calculate-btn");
const scoreInput = document.querySelector("#score");
const difficultyInput = document.querySelector("#constant");
const ratingInput = document.querySelector("#rating");
const dataTable = document.querySelector("#data-table");

calculateBtn.addEventListener("click", () => {
  const score = scoreInput.value || 0;
  const constant = difficultyInput.value || 13.9;
  const rating = ratingInput.value || 0;

  const url = `/calculate?score=${score}&constant=${constant}&rating=${rating}`;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const ranks = ["S", "S+", "SS", "SS+", "SSS", "SSS+"];
      const customScore = data.customScore;

      // Fill in rating data
      const ratingRow = dataTable.rows[1];
      const ratingCells = ratingRow.cells;
      ratingCells[7].textContent = customScore;

      if (rating !== "") {
        const ratingIndex = ranks.indexOf(rating.toUpperCase());
        if (ratingIndex >= 0) {
          ratingCells[ratingIndex + 1].textContent = customScore;
        }
      }

      // Fill in difficulty data
      const difficulties = data.difficulties;
      const difficultyRow = dataTable.rows[2];
      const difficultyCells = difficultyRow.cells;
      difficulties.forEach((d, i) => {
        difficultyCells[i + 1].textContent = d;
      });
    })
    .catch(error => console.error(error));
});
