function getAuthorsData(url) {
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            fillAuthorsTable(data);
        })
}


let url = new URL(window.location.href);
let page = url.searchParams.get('page');
if (page === null ) {
    page = 1;
}
getAuthorsData(`/api/authors?page=${page}`)


function fillAuthorsTable(data) {
    let tableBody = document.getElementById("authors-data");
    tableBody.innerHTML = "";
    for (let i = 0; i < data.length; i++) {
        const row = tableBody.insertRow();
        const columns = ['author', 'birthday', 'origin']
        for (const column of columns) {
            let dataText = data[i][column];
            let cell = row.insertCell();
            cell.innerText = dataText;
        }
    }
}

