document.addEventListener('DOMContentLoaded', () => {

    // add event listener to nav a tags
    // TODO

    const posts = document.querySelector("#posts");

    // fetch post data
    fetch('posts/all')
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error(response.status);
        }
    })
    .then(json => {
        json.forEach(element => {
            let post_div = document.createElement('div');
            post_div.setAttribute('class', 'post_div');

            let author_link = document.createElement('a');
            author_link.setAttribute('class', 'post_author');
            author_link.setAttribute('href', `profile/${element.author}`);
            author_link.innerText = element.author;

            let ptag_content = document.createElement('p');
            ptag_content.setAttribute('class', 'ptag_post');
            ptag_content.innerText = element.content;

            let ptag_datetime = document.createElement('p');
            ptag_datetime.setAttribute('class', 'ptag_datetime');
            ptag_datetime.innerText = element.created_at;

            let separator = document.createElement('hr');
            separator.setAttribute('class', 'separator');

            let footer_div = document.createElement('div');
            footer_div.setAttribute('class', 'fotter_post');

            let like_div = document.createElement('div');
            like_div.setAttribute('class', 'like_section');

            /*let svg_image = `<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-suit-heart-fill" viewBox="0 0 18 18">
                <path d="M4 1c2.21 0 4 1.755 4 3.92C8 2.755 9.79 1 12 1s4 1.755 4 3.92c0 3.263-3.234 4.414-7.608 9.608a.513.513 0 0 1-.784 0C3.234 9.334 0 8.183 0 4.92 0 2.755 1.79 1 4 1z"/>
            </svg>`*/

            let svg_image = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
            svg_image.setAttribute('width', '25');
            svg_image.setAttribute('height', '25');
            svg_image.setAttribute('fill', 'currentColor');
            svg_image.setAttribute('class', 'bi bi-suit-heart-fill');
            svg_image.setAttribute('viewBox', '0 0 18 18');

            let svg_path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            svg_path.setAttribute('d', 'M4 1c2.21 0 4 1.755 4 3.92C8 2.755 9.79 1 12 1s4 1.755 4 3.92c0 3.263-3.234 4.414-7.608 9.608a.513.513 0 0 1-.784 0C3.234 9.334 0 8.183 0 4.92 0 2.755 1.79 1 4 1z');
            svg_image.appendChild(svg_path);
            
            let span_tag = document.createElement('span');
            span_tag.setAttribute('class', 'likes');
            span_tag.textContent = element.like_count;

            let reply_div = document.createElement('div');
            reply_div.innerHTML = '<a href="#">Reply</a>';


            post_div.appendChild(author_link);
            post_div.appendChild(ptag_content);
            post_div.appendChild(ptag_datetime);
            post_div.appendChild(separator);
            post_div.appendChild(footer_div);
            footer_div.appendChild(like_div);
            like_div.appendChild(svg_image);
            like_div.appendChild(span_tag);
            footer_div.appendChild(reply_div);


            // eventListener to like a post
            svg_image.addEventListener('click', () => {
                let lastChild = like_div.lastElementChild;
                like_a_post(lastChild, element.id);
            });
            
            posts.appendChild(post_div);

        });
    })
    .catch(error => console.log(error));

});


function like_a_post(last_child, post_id) {
    // console.log(last_child);

    fetch(`liked_post/${post_id}`)
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error(response.status);
        }
    })
    .then(json => {
        // console.log(json);
        last_child.textContent = json.likes;
    })
    .catch(error => console.log(error));
}
