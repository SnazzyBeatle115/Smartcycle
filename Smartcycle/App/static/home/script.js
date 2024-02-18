// function to add a new category to the categories list
function addCategory(title) {
  const category = document.createElement("a");
  category.classList.add("category");
  const categoryText = document.createElement("p");
  categoryText.innerText = title;
  category.appendChild(categoryText);
  document.querySelector(".categories").appendChild(category);
}

addCategory("Plastic Bottle");
