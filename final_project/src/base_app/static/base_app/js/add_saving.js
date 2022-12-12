document.addEventListener("DOMContentLoaded", () => {

    document.querySelector("#message").innerHTML = "";

    document.querySelector("#add_saving_form").addEventListener('submit', event => {
        event.preventDefault();

        const csrftoken = getCookie('csrftoken');

        let formData = {
            name: document.querySelector("#id_name").value,
            amount: document.querySelector("#id_amount").value,
            currency: document.querySelector("#id_currency").value,
        };

        const request = new Request(
            `/budget/add_saving`,
            {
                method: 'POST',
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin', // Do not send CSRF token to another domain.
                body: JSON.stringify(formData)
            }
        );

        fetch(request)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error(response.status);
            }
        })
        .then(json => {
            document.querySelector("#add_saving_form").reset();
            console.log(json);
            document.querySelector("#message").innerHTML = "Saving added!";
        })
        .catch(error => console.log(error));

    });
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
