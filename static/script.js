var socket = io.connect('http://127.0.0.1:5000');
socket.on('connect', function () {

    socket.send('Connected  ');

    socket.emit('custom event', {data: 'User Connected'});
    var form = $('form').on('submit', function (e) {
        e.preventDefault();
        let user_name = $('input.username').val();
        let user_input = $('input.message').val();
        socket.emit('custom event', {
            user_name: user_name,
            message: user_input
        });
        $('input.message').val('').focus();
    });

    socket.on( 'my response', function( msg ) {
  console.log( msg );
  if( typeof msg.user_name !== 'undefined' ) {
    $( 'h3' ).remove()
    $( 'div.message_holder' ).append('<div><b style="color:             #000">'+msg.user_name+'</b>'+': ' +msg.message+'</div>' )
  }
});
    /*
    socket.on('from flask', function (msg) {
        alert(msg['extension']);
    });

    socket.on('message', function (msg) {
        alert(msg);

    });
    */

});


