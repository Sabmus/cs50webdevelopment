document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#profile').style.display = 'none';
    
    document.querySelector('#profile-page').addEventListener('click', () => {
        document.querySelector('#profile').style.display = 'block';
        
    });
});