function getBooksData(url) {
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            fillBooksTable(data);
        })
}


let url = new URL(window.location.href);
let page = url.searchParams.get('page');
if (page === null ) {
    page = 1;
}
getBooksData(`/api/books?page=${page}`)


function fillBooksTable(data) {
    let tableBody = document.getElementById("books-data");
    tableBody.innerHTML = "";
    for (let i = 0; i < data.length; i++) {
        const row = tableBody.insertRow();
        const columns = ['title', 'author', 'release_year',
            'rating', 'internal_rating', ]
        for (const column of columns) {
            let dataText = data[i][column];
            let cell = row.insertCell();
            cell.innerText = dataText;
        }
    }
}

