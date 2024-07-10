var state = {
    nextUrl: ""
}

/**
 * 
 * @param {string} nextUrl 
 */
const fetchNewsList = (nextUrl) => {
    const listElement = $('#news-list');
    const moreElement = $('#more');

    const url = '/api/v1/news'
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

const updateNotification = () => {
    const url = "/news";
    const socket = new WebSocket(url);

    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);

        if (data.updated) {
            $('#toast').toast('show');
        }
    };
}

$(document).ready(() => {
    // init: hide more button
    const moreElement = $('#more');
    moreElement.hide();

    // init: news list update notification
    updateNotification();

    // init: populate list
    fetchNewsList(null);

    // click: fetch more
    fetchMore();
});