document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // submit form
  document.querySelector('#compose-form').onsubmit = function() {
    
    // form data
    let formData = {
      recipients: document.querySelector('#compose-recipients').value,
      subject: document.querySelector('#compose-subject').value,
      body: document.querySelector('#compose-body').value
    };

    // sent to Django API
    fetch('emails', {
      method: 'post',
      body: JSON.stringify(formData)
    })
    .then(response => {
      if (response.ok){
        return response.json();
      } else {
        throw new Error(response.status);
      }
    })
    .then(json => {
      console.log(json);
      load_mailbox('sent');
    })
    .catch(error => console.log(error));

    // do not submit the form
    return false;
  };

}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // get data
  user_ = document.querySelector('h2').value;

  fetch(`emails/${mailbox}`, {user: user_})
  .then(response => {
    return response.json();
  })
  .then(json => {

    console.log(json);
    json.forEach(ele => {
      let emailData = `<p class="ptag"><span class="sender">${ele.sender}</span> <a class="email" href="emails/${ele.id}">${ele.subject}</a> <span class="timestamp">${ele.timestamp}</span></p>`;
      let div = document.createElement('div');
      div.setAttribute('class', 'email_div')
      div.innerHTML = `${emailData}`;
      document.querySelector('#emails-view').append(div);
    });

  })
  .catch(error => console.log(error));
  
}