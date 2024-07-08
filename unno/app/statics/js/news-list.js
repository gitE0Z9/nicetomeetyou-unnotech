var state = {
    nextUrl: ""
}


// const url = "ws://localhost:8000/api/v1/news";
// const socket = new WebSocket(url);

// socket.onopen((event) => {

// });

// socket.onmessage((event) => {

// });

// socket.onerror((event) => {

// });

// socket.onclose((event) => {

// });

/**
 * 
 * @param {string} nextUrl 
 */
const fetchNewsList = (nextUrl) => {
    const listElement = $('#news-list');
    const moreElement = $('#more');

    const url = 'http://localhost:8000/api/v1/news'
    $.getJSON(nextUrl ?? url, function (response) {
        const data = response.results;
        for (const item of data) {
            const rowElement = `<li class="list-group-item"><a href="/news/${item.id}">${item.title}</a></li>`;
            listElement.append(rowElement);
        }

        if (response.next) {
            state.nextUrl = response.next;
            moreElement.show();
        }
        else {
            moreElement.hide();
        }
    }).fail((err) => {
        console.error(err);
    });
}


const fetchMore = () => {
    const moreElement = $('#more');

    moreElement.click(function () {
        fetchNewsList(state.nextUrl);
    });
}

$(document).ready(() => {
    // init: hide more button
    const moreElement = $('#more');
    moreElement.hide();

    // init: populate list
    fetchNewsList(null);

    // click: fetch more
    fetchMore();
});