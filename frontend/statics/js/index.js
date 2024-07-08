const url = "ws://localhost:8000/api/v1/news";
const socket = new WebSocket(url);

socket.onopen((event) => {

});

socket.onmessage((event) => {

});

socket.onerror((event) => {

});

socket.onclose((event) => {

});

$(document).ready(() => {
    const listElement = $('news-list');

    const url = 'http://localhost:8000/api/v1/news'
    $.getJSON(url, function (response) {
        const data = response.data;
        for (const item of data) {
            const rowElement = `<li class="list-group-item"><a href="/news/${item.id}">${item.title}</a></li>`;
            listElement.append(rowElement);
        }
    }).fail((err) => {
        console.error(err);
    });
});