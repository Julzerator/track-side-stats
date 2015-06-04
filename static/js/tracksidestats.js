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

// Set the background of things to the team color.
$(function() {
    var home_color = $( '#home_team_info').data().color;
    var away_color = $('#away_team_info').data().color;
    console.log(home_color);
    console.log(away_color);
    $('.home').css('background', home_color);
    $('.away').css('background', away_color);
});

// Drag/Drop functionality to send actions.
$(function() {
    $( ".player" ).draggable({revert:true});
    $( ".player" ).draggable({
        start: function( event, ui ) {
            $( this ).css('width', '50px');
            $( this ).css('height', '50px');
            var here = $( this ).parent().attr('id');
            var there = '#' + here + '_actions';
            var there_class = $( there ).parent().attr('class');
            if (there_class == 'control home blocker') {
                $("<div class='driveout dropmehere' data-play='driveout'>Drive Out</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='knockdown dropmehere' data-play='knockdown'>Knock Down</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='screen dropmehere' data-play='screen'>Screen</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='whip dropmehere' data-play='whip'>Whip</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='blockassist dropmehere' data-play='blockassist'>Block Assist</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='penalty dropmehere' data-play='penalty'>Penalty</div>").droppable(dropActions).appendTo( $(there) );
                console.log("blocker buttons made");
            } else if (there_class == 'control home jammer' || there_class == 'control away jammer') {
                $("<div class='leadjam dropmehere' data-play='leadjam'>Lead Jammer</div>").droppable(dropActions).appendTo ( $(there) );
                $("<div class='initialpass dropmehere' data-play='initialpass'>Initial Pass</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='calloff dropmehere' data-play='calloff'>Call Off Jam</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='points dropmehere' data-play='points'>Points</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='penalty dropmehere' data-play='penalty'>Penalty</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='starpass dropmehere' data-play='starpass'>Star Pass</div>").droppable(dropActions).appendTo( $(there) );
                console.log("jammer buttons made");
            };

        }
    });
    $( ".player" ).draggable({
        stop: function( event, ui ) {
            $( this ).css('width', '100px');
            $( this ).css('height', '100px');
            $( '.actions' ).empty();
        }
    })
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
                $( '#points_jammer' ).attr('value', player_id);
                $( '#points-modal' ).modal({
                    keyboard: false
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

// Points recording and submission
$('.points_number').on('click', function(){
    var points = $( this ).text();
    var player_id = $( '#points_jammer' ).attr('value');
    console.log('points - ' + points);
    console.log('player id - ' + player_id);
    $.post( '/action', { 
        player_id : player_id,
        play : 'points',
        points : points
        })
        .done(function( result ) {
            $('#message').html(result).show().fadeOut( 3000 );
        })
        .fail(function() {
            $('#message').html('Action was not processed').show().fadeOut( 3000 );
    });
    $('#points-modal').modal('hide')
});
