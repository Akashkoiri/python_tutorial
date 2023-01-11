let url = `ws://${window.location.host}/socket/`;
let username = document.getElementById('username').innerText
// Doing this because in username we are getting extra text
username = username.split('\n')[0]

// Getting backend data through the socket
const chatSocket = new WebSocket(url);
chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);

    if (data.type === 'chat_message') {
        let chatbox = document.querySelector('.chatbox')
        if (data.author == username) {
            chatbox.insertAdjacentHTML('beforeend',
                `<div class="message my_message">
                    <p>${data.message}<br><span>12:15</span></p>
                </div>`)
        }

        else {
            chatbox.insertAdjacentHTML('beforeend',
                `<div class="message frnd_message">
                    <p>${data.message}<br><span>12:16</span></p>
                </div>`)
        }
    }
}

// Sending form data to socket
let form = document.getElementById('form')
form.addEventListener('submit', (e) => {
    e.preventDefault()
    let message = e.target.message.value;
    if (validateForm(message)) {
        chatSocket.send(JSON.stringify({
            'message': message,
            'username': username
        }))
    }
    form.reset()
})


function validateForm(msg) {
    if (!!msg) {
        for (let i in msg) {
            // console.log(msg[i])
            if (msg[i] != ' ') {
                return true
            }
        }
        return false
    }
}

