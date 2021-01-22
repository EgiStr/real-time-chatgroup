
const roomName = JSON.parse(document.getElementById('room-name').textContent);
const username = JSON.parse(document.getElementById('username').textContent);

const chatSocket = new ReconnectingWebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

//-- No use time. It is a javaScript effect.
function insertChat(who, massage,timestamp ){

    var control = "";

    if (who.username == username){

        control = `<li style="list-style-type: none;">
                        <div class="d-flex justify-content-end mb-4">
                        <p class="">${who.username}</p>
                        <div class="msg_cotainer_send">
                            ${massage}
                            <span class="msg_time_send h-50">${timestamp}</span>
                        </div>
                        <div class="img_cont_msg">
                            <img src="${who.profil}" class="rounded-circle user_img_msg">
                        </div>
                        </div>
                    </li>`;                    
    }else{
        control = `<li style="list-style-type: none;">
                        <div class="d-flex justify-content-start mb-4">
                        <p class="">${who.username}</p>
                        <div class="img_cont_msg">
                            <img src="${who.profil}" class="rounded-circle user_img_msg">
                        </div>
                        <div class="msg_cotainer">
                            ${massage}
                            <span class="msg_time">${timestamp}</span>
                        </div>
                        </div>
                    </li>`;
    }
    setTimeout(
        function(){                        
            $(".penampung").append(control).scrollTop($(".penampung").prop('scrollHeight'));
        }, 100);
    }

function resetChat(){
    $("ul").empty();
}

// $(".type_msg").on("keydown", function(e){
//     if (e.which == 13){
//         var text = $(this).val();
//         if (text !== ""){
//             insertChat(username, text);              
//             $(this).val('');
//         }
//     }
// });


chatSocket.onmessage = function(e) {
    let data = JSON.parse(e.data);
    data = data.message

    data.forEach( (e) => {
        insertChat(e.user,e.message,e.timestamp)
    })
};

chatSocket.onclose = function(e) {
    console.error(e)
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('.type_msg').focus();
document.querySelector('.type_msg').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('.send_btn').click();
    }
};

window.addEventListener("load", function(){
    chatSocket.send(JSON.stringify({
        'username':username,
        'message': '',
        'command':'get_lates'
    }));
});

document.querySelector('.send_btn').onclick = function(e) {
    const messageInputDom = document.querySelector('.type_msg');
    const message = messageInputDom.value;
    
    if (message !== ""){
        chatSocket.send(JSON.stringify({
            'username':username,
            'message': message,
            'command':'send_massage'
        }));
    }
    
    messageInputDom.value = '';
};