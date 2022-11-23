document.addEventListener('DOMContentLoaded', () => {

    // add event listener to form post request
    document.querySelectorAll(".like_btn").forEach(button => {
        let counter = 0;
        button.addEventListener('click', event => {
            counter++;
            const element = event.target;
            element.innerHTML = "likes: " + counter.toString();
            console.log("like btn clicked!");
        });
    });

    document.querySelectorAll(".bi-suit-heart-fill").forEach(heart => {
        heart.addEventListener('click', event => {
            const element = event.target;
            
        });
    });

});

/*
function create_post(ev) {
    ev.preventDefault();

    const div_posts = document.querySelector("#posts");
    div_posts.innerHTML = "";
    const form = document.querySelector("#form_post");
    const formData = new FormData(form);

    const content = document.querySelector("#content");
    
    fetch('create_post', {
        method: 'post',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            content.value = "";  // reset textarea value
            return response.json();
        } else {
            throw new Error(response.status);
        }
    })
    .then(json => {
        json.forEach(element => {
            let ptag = document.createElement("p");
            ptag.innerHTML = element.content;

            div_posts.appendChild(ptag);
        });
    })
    .catch(error => console.log(error));
}*/