/**
 * Fetch news detail from api server
 * @param {number} postId 
 * @param {callback} callback 
 */
const getNewsDetail = async (postId, callback) => {
    const url = 'http://localhost:8000/api/v1/news/'
    $.getJSON(url + postId, function (response) {
        const data = response;
        callback(data);
    }).fail((err) => {
        console.error(err);
    });
}

// main

$(document).ready(() => {
    const postId = new URL(document.URL).pathname.replace('/news/', '');
    getNewsDetail(postId, (data) => {
        $('title').text(data.title + $('title').text());
        $('h1').text(data.title);
        $('#news-detail-container img').attr('src', data.img);
        $('#news-detail-container img').attr('alt', data.title);
        $('#news-detail-container p').text(data.content);
    });
});