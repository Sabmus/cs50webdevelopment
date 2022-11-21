document.addEventListener('DOMContentLoaded', () => {
    document.querySelector("#form_post").onsubmit = function(event) {
        event.preventDefault();

        const content = document.querySelector("#content").value;
        
        const formData = new FormData();
        formData.append('content', content);
        formData.append('csrfmiddlewaretoken', '{{ csrf_token  }}');
        console.log(formData);
        
 
        fetch('create_post', {
            method: 'post',
            body: formData //JSON.stringify(requestOptions)
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error(response.status);
            }
        })
        .then(json => console.log(json))
        .catch(error => console.log(error));
   
    };

});
