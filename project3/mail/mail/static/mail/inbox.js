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
  document.querySelector('#email').style.display = 'none';

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
  document.querySelector('#email').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // create grid structure for email info and archive button
  const div_email_info = document.createElement('div');
  const div_archive_btn = document.createElement('div');
  div_email_info.setAttribute('class', 'div_email_info');
  div_archive_btn.setAttribute('class', 'div_archive_btn');

  document.querySelector('#emails-view').append(div_email_info);
  document.querySelector('#emails-view').append(div_archive_btn);



  // get data
  fetch(`emails/${mailbox}`)
  .then(response => {
    return response.json();
  })
  .then(json => {
    console.log(json);
    json.forEach(ele => {
      let div = document.createElement('div');
      div.setAttribute('class', 'email_div');

      if(ele.read){
        div.style.backgroundColor = 'grey';
      }

      let emailData = `<p class="ptag"><span class="sender">${ele.sender}</span> ${ele.subject} <span class="timestamp">${ele.timestamp}</span></p>`;
      div.innerHTML = emailData;
      div.addEventListener('click', function() {
        console.log(`clicked: ${ele.id} div`);
        // mark email as read
        if(!ele.read) {
          mark_as_read(ele);
        }
        // show email
        show_email(ele);
      });

      div_email_info.append(div);

      let archive_btn = document.createElement('button');
      archive_btn.setAttribute('class', 'btn btn-sm btn-outline-primary');
      archive_btn.innerText = "Archive";
      archive_btn.addEventListener('click', () => {
        console.log('archive button clicked!');
      });

      div_archive_btn.append(archive_btn);

    });
  })
  .catch(error => console.log(error));
  
}

function mark_as_read(ele) {
  requestOptions = {
    method: 'put',
    body: JSON.stringify({
      read: true
    })
  };

  fetch(`emails/${ele.id}`, requestOptions)
  .then(response => {
    if (!response.ok) {
      throw new Error(response.status);
    }
  })
  .catch(error => console.log(error));

}

function show_email(ele){
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email').style.display = 'block';

  const email_div = document.querySelector('#email');
  email_div.innerHTML = '';

  fetch(`emails/${ele.id}`)
  .then(response => response.json())
  .then(json => {
    console.log(json);
  })
  .catch(error => console.log(error))

  // show email
  let emailData = document.createElement('div');
  let emailBody = document.createElement('div');
  emailData.setAttribute('class', 'email-data');
  emailBody.setAttribute('class', 'email-body');

  let from_ = `<p><span>From:</span> ${ele.sender}</p>`;
  let to_ = '';
  ele.recipients.forEach(recipient => {
    to_ += `${recipient}, `;
  });
  to_ = '<p><span>To:</span> ' + to_.slice(0, -2) + '</p>' // remove last two char from to list (', ')
  let subject_ = `<p><span>Subject:</span> ${ele.subject}</p>`;
  let timestamp_ = `<p><span>Timestamp:</span> ${ele.timestamp}</p>`;
  let replybutton = '<button class="btn btn-sm btn-outline-primary" id="reply-button">Reply</button>'
  let body_ = `<p>${ele.body}</p>`;

  emailData.innerHTML = '<hr>' + from_ + to_ + subject_ + timestamp_ + replybutton + '<hr>';
  emailBody.innerHTML = body_;

  email_div.append(emailData);
  email_div.append(emailBody);

  document.querySelector('#reply-button').addEventListener('click', () => {
    console.log('reply button was clicked!');
  });

}