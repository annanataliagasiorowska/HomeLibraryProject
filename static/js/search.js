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
        if (result['title'] != null){
        li.textContent = result['title']} else
        {li.textContent = result['author']}
        resultsList.appendChild(li);
    }
}


function getTitle() {
    let titleToFind = inputTitle.value;
    console.log(titleToFind);
    searchAuthorOrTitle(`/api/search?title=${titleToFind}`)
}

function getAuthor() {
    let authorToFind = inputAuthor.value;
    console.log(authorToFind);
    searchAuthorOrTitle(`/api/search?author=${authorToFind}`)
}

searchAuthorOrTitle(url = "/api/search?title=a")



const inputTitle = document.getElementById("input-title");
console.log(inputTitle.value);
inputTitle.addEventListener("input", getTitle);
const inputAuthor = document.getElementById("input-author");
console.log(inputAuthor.value)
inputAuthor.addEventListener("input", getAuthor);