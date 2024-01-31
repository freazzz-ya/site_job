let isFullDescriptionVisible = false;

function toggleDescription() {
  if (isFullDescriptionVisible) {
    document.getElementById("shortDescription").style.display = "block";
    document.getElementById("fullDescription").style.display = "none";
    isFullDescriptionVisible = false;
  } else {
    document.getElementById("shortDescription").style.display = "none";
    document.getElementById("fullDescription").style.display = "block";
    isFullDescriptionVisible = true;
  }
}