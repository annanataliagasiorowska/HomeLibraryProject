function searchAuthorOrTitle(url) {
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            showSearchResults(data);
        })
}

function showSearchResults(data) {
    let resultsList = document.getElementById("results-list");
    resultsList.innerHTML = "";
    for (const result of data) {
        const li = document.createElement('li');
        li.textContent = result['title'];
        resultsList.appendChild(li);
    }
}


function getParameters() {
    let titleToFind = inputTitle.value;
    console.log(titleToFind);
    searchAuthorOrTitle(`/api/search?title=${titleToFind}`)
}

searchAuthorOrTitle(url = "/api/search?title=a")


// const inputAuthor = document.getElementById("input-author");
// console.log(inputAuthor.value)
// inputAuthor.addEventListener("input", getParameters);
const inputTitle = document.getElementById("input-title");
console.log(inputTitle.value);
inputTitle.addEventListener("input", getParameters);