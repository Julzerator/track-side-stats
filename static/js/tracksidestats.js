// Player assignment Functions

$(function() {
    $( ".home_player" ).draggable({revert:true});
    $( ".home_player" ).draggable({
        start: function( event, ui ) {
            $( ".away_position" ).droppable( "disable" );
            $( ".home_position" ).droppable( "enable" );
        }
    });
    $( ".home_position" ).droppable({
      drop: function( event, ui ) {
        var player_id = ui.helper.data().playerid;
        var name = ui.helper.data().name;
        var number = ui.helper.data().number;
        var player = ui.helper.children('.roster').html();
        $( 'input[value="'+player_id+'"]').siblings('.player_pos').html('');
        $( 'input[value="'+player_id+'"]').attr('value', '');
        $( this ).children('.pos').attr('value', player_id );
        $( this ).children('.player_pos').html(player);

        }
    });
});
$(function() {
    $( ".away_player" ).draggable({revert:true});
    $( ".away_player" ).draggable({
        start: function( event, ui ) {
            $( ".home_position" ).droppable( "disable" );
            $( ".away_position" ).droppable( "enable" );
        }
    });
    $( ".away_position" ).droppable({
      drop: function( event, ui ) {
        var player_id = ui.helper.data().playerid;
        var name = ui.helper.data().name;
        var number = ui.helper.data().number;
        var player = ui.helper.children('.roster').html();
        $( 'input[value="'+player_id+'"]').siblings('.player_pos').html('');
        $( 'input[value="'+player_id+'"]').attr('value', '');
        $( this ).children('.pos').attr('value', player_id );
        $( this ).children('.player_pos').html(player);
        }
    });
});

// Action assignment Functions
// Timers for screen.
window.onload = function() {
    var jamtimer_up = Tock({
        interval: 100,
        callback: function () {
            $('#clockface').html(jamtimer_up.msToTime(jamtimer_up.lap()));
        }
    });
    $(document).ready( function () {
        jamtimer_up.start($('#clockface').html());
    });

    var jamtimer_down = Tock({
        interval: 100,
        countdown: true,
        callback: function () {
            $('#jamtimer').html(jamtimer_down.msToTime(jamtimer_down.lap()));
        },
        complete: function () {
            $('#timeranout').show();
        }
    });
    $(document).ready( function () {
        jamtimer_down.start($('#jamtimer').html());
    });
};

// Drag/Drop functionality to send actions.
$(function() {
    $( ".player" ).draggable({revert:true});
    $( ".player" ).draggable({
        start: function( event, ui ) {
            var here = $( this ).parent().attr('id');
            var there = '#' + here + '_actions';
            var there_class = $( there ).parent().attr('class');
            if (there_class == 'control blocker') {
                $("<div class='driveout' data-play='driveout'>Drive Out</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='knockdown' data-play='knockdown'>Knock Down</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='screen' data-play='screen'>Screen</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='whip' data-play='whip'>Whip</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='blockassist' data-play='blockassist'>Block Assist</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='penalty' data-play='penalty'>Penalty</div>").droppable(dropActions).appendTo( $(there) );
            } else if (there_class == 'control jammer') {
                $("<div class='leadjam' data-play='leadjam'>Lead Jammer</div>").droppable(dropActions).appendTo ( $(there) );
                $("<div class='initialpass' data-play='initialpass'>Initial Pass</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='calloff' data-play='calloff'>Call Off Jam</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='points' data-play='points'>Points</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='penalty' data-play='penalty'>Penalty</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='starpass' data-play='starpass'>Star Pass</div>").droppable(dropActions).appendTo( $(there) );
            };

        }
    });
    var dropActions = {
        drop: function( event, ui ) {
            var player_id = $( this ).parent().parent().data().playerid;
            var play = $( this ).data().play;
            console.log(player_id);
            console.log(play);
            if ($( this ).hasClass('starpass')) {
                // put starpass actions here HARDEST THING
                $.post( '/action', { 
                    player_id : player_id,
                    play : play
                    })
                    .done(function( result ) {
                        $('#message').html(result).show().fadeOut( 3000 );
                    })
                    .fail(function() {
                        $('#message').html('Action was not processed').show().fadeOut( 3000 );
                    });
            } else if ($( this ).hasClass('leadjam')) {
                // put leadjam actions here
                $.post( '/action', { 
                    player_id : player_id,
                    play : play
                    })
                    .done(function( result ) {
                        $('#message').html(result).show().fadeOut( 3000 );
                    })
                    .fail(function() {
                        $('#message').html('Action was not processed').show().fadeOut( 3000 );
                    });
                $( this ).parent().parent().addClass("leadjammer");
            } else if ($( this ).hasClass('calloff')) {
                // put calloff actions here
                $.post( '/action', { 
                    player_id : player_id,
                    play : play
                    })
                    .done(function( result ) {
                        $('#message').html(result).show().fadeOut( 3000 );
                    })
                    .fail(function() {
                        $('#message').html('Action was not processed').show().fadeOut( 3000 );
                    });
            } else if ($( this ).hasClass('points')) {
                // put points actions here
                // first, show a dialog to choose number of points 0-5

                // var points = 
                var jammer_type = $( this ).parent().parent().attr('id')
                $.post( '/action', { 
                    player_id : player_id,
                    play : play,
                    points : points,
                    jammer_type : jammer_type
                    })
                    .done(function( result ) {
                        $('#message').html(result).show().fadeOut( 3000 );
                    })
                    .fail(function() {
                        $('#message').html('Action was not processed').show().fadeOut( 3000 );
                    });
            } else {
                $.post( '/action', { 
                    player_id : player_id,
                    play : play
                    })
                    .done(function( result ) {
                        $('#message').html(result).show().fadeOut( 3000 );
                    })
                    .fail(function() {
                        $('#message').html('Action was not processed').show().fadeOut( 3000 );
                    });
            };
            $( this ).parent().empty();
        } 
    };
  });
