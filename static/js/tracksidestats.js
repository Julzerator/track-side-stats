// Player assignment Functions

$(function() {
    $( ".home_player" ).draggable({revert:true});
    $( ".home_player" ).draggable({
        helper: 'clone',
        appendTo: 'body',
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
        var player = ui.helper.children('.roster_player').html();
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
        helper: 'clone',
        appendTo: 'body',
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
        var player = ui.helper.children('.roster_player').html();
        $( 'input[value="'+player_id+'"]').siblings('.player_pos').html('');
        $( 'input[value="'+player_id+'"]').attr('value', '');
        $( this ).children('.pos').attr('value', player_id );
        $( this ).children('.player_pos').html(player);
        }
    });
});

// Action assignment Functions
// Timers for screen.
$(document).ready( function() {
    var jamtimer_up = Tock({
        interval: 100,
        callback: function () {
            $('#clockface').html(jamtimer_up.msToTime(jamtimer_up.lap()));
        }
    });

    jamtimer_up.start($('#clockface').html());

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
    jamtimer_down.start($('#jamtimer').html());
});

// Set the background of things to the team color.
$(function() {
    var home_color = $( '#home_team_info').data().color;
    var away_color = $('#away_team_info').data().color;
    console.log(home_color);
    console.log(away_color);
    $('.home').css('background', home_color);
    $('.away').css('background', away_color);
    $('.home_position').css('border-color', home_color);
    $('.away_position').css('border-color', away_color);
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
                $("<div class='driveout dropmehere' data-play='driveout'>Drive<br>Out</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='knockdown dropmehere' data-play='knockdown'>Knock<br>Down</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='screen dropmehere' data-play='screen'>Screen</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='whip dropmehere' data-play='whip'>Whip</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='blockassist dropmehere' data-play='blockassist'>Block<br>Assist</div>").droppable(dropActions).appendTo( $(there) );
                $("<div class='penalty dropmehere' data-play='penalty'>Penalty</div>").droppable(dropActions).appendTo( $(there) );
            } else if (there_class == 'control home jammer' || there_class == 'control away jammer') {
                $("<div class='penalty dropmehere' data-play='penalty'>Penalty</div>").droppable(dropActions).appendTo( $(there) );
                if ( !$( this ).hasClass("starpass")) {
                    $("<div class='starpass dropmehere' data-play='starpass'>Star<br>Pass</div>").droppable(dropActions).appendTo( $(there) );
                };
                // Lead Jammer or Initial Pass buttons available with bonus call off.
                if ( !$('#jammer_player').hasClass("leadjammer") && !$('#away_jammer_player').hasClass("leadjammer")) {
                    if ( !$( this ).hasClass('penalty') && !$( this ).hasClass("starpass") ) {
                        $("<div class='leadjam dropmehere' data-play='leadjam'>Lead<br>Jammer</div>").droppable(dropActions).appendTo ( $(there) );
                    } else if (!$( this ).hasClass('initialpass')) {
                        $("<div class='initialpass dropmehere' data-play='initialpass'>Initial Pass</div>").droppable(dropActions).appendTo( $(there) );
                    }
                } else if ($( this ).hasClass('leadjammer')) {
                    $("<div class='calloff dropmehere' data-play='calloff'>Call Off Jam</div>").droppable(dropActions).appendTo( $(there) );
                } else if (!$( this ).hasClass('initialpass')) {
                    $("<div class='initialpass dropmehere' data-play='initialpass'>Initial Pass</div>").droppable(dropActions).appendTo( $(there) );
                };
                // Points drop available
                if ( $( this ).hasClass('leadjammer') || $( this ).hasClass('initialpass')) {
                    $("<div class='points dropmehere' data-play='points'>Points</div>").droppable(dropActions).appendTo( $(there) );
                }
                console.log("jammer buttons made");
            };

        }
    });
    $( ".player" ).draggable({
        cursor: "move", cursorAt: { top: 26, left: 26 }
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
            console.log('jammer id = ' + player_id);
            console.log(play);
            if ($( this ).hasClass('starpass')) {
                // get pivot id associated with this jammer
                var pivot_id = $( this ).parent().siblings('.pivot').data().playerid;
                console.log('pivot id = ' + pivot_id)
                // put starpass actions here
                $.post( '/action', { 
                    player_id : player_id,
                    play : play,
                    pivot_id : pivot_id
                    })
                    .done(function( result ) {
                        // First set a variable with what the id of the jammer and pivot are:
                        var jammer_dom = $("div[data-playerid='" + player_id +"']").attr('id');
                        jammer_dom = "#" + jammer_dom;
                        var pivot_dom = $("div[data-playerid='" + pivot_id +"']").attr('id');
                        pivot_dom = "#" + pivot_dom;

                        // Set new Jammer in DOM:
                        $(jammer_dom).find('.player_name').html(result.new_jammer.name);
                        console.log(result.new_jammer.name);
                        $(jammer_dom).find('.player_number').html(result.new_jammer.number);
                        console.log(result.new_jammer.number);
                        $(jammer_dom).attr('data-playerid', result.new_jammer.id);

                        // Set new Pivot:
                        $(pivot_dom).find('.player_name').html(result.new_pivot.name);
                        $(pivot_dom).find('.player_number').html(result.new_pivot.number);
                        $(pivot_dom).find('.position').html('Blocker');
                        $(pivot_dom).attr('data-playerid', result.new_pivot.id);

                        // Flash message:
                        $('#message').html(result.message).show().fadeOut( 3000 );
                    })
                    .fail(function() {
                        $('#message').html('Action was not processed').show().fadeOut( 3000 );
                    });
                $( this ).parent().parent().children('.player').addClass("starpass");
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
                $( this ).parent().parent().children('.player').addClass("leadjammer");
            } else if ($( this ).hasClass('calloff')) {
                // put calloff actions here
                $.post( '/action', { 
                    player_id : player_id,
                    play : play
                    })
                    .done(function( result ) {
                        $('#message').html(result).show().fadeOut( 3000 );
                        $('#calledbyjammer').show();
                        $('#calledbyjammer').click();
                    })
                    .fail(function() {
                        $('#message').html('Action was not processed').show().fadeOut( 3000 );
                    });

            } else if ($( this ).hasClass('initialpass')) {
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
                $( this ).parent().parent().children('.player').addClass("initialpass");
            } else if ($( this ).hasClass('penalty')) {
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
                $( this ).parent().parent().children('.player').addClass("penalty");
            } else if ($( this ).hasClass('points')) {
                // put points actions here
                // first, show a dialog to choose number of points 0-5
                player_id = $( this ).parent().parent().data().playerid;
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
            $('#message').html(result.message).show().fadeOut( 3000 );
            $('#home_score').html("<h2>" + result.home_score + "</h2>");
            $('#away_score').html("<h2>" + result.away_score + "</h2>");
        })
        .fail(function() {
            $('#message').html('Action was not processed').show().fadeOut( 3000 );
    });
    $('#points-modal').modal('hide')
});

$('#start_jam_button').on('click', function(){
    $('#start_jam').click();
    $('#points-modal').modal('hide');
});

// Remove player:
$('.removeplayer').on('click', removePlayer);

function removePlayer(evt) {
    var rospla_id = this.dataset.rosplaid;
    console.log(this.parentNode);
    this.parentNode.remove();
    $.post( "/change_roster/remove/" + rospla_id );
    console.log(this.dataset.rosplaid);
};

// Add player: 
$('.addplayer').on('click', addPlayer);

function addPlayer(evt) {
    alert('I clicked you to add! Woot!');
};

// Search for player:
$('.searchplayer').on('click', searchPlayer);

function searchPlayer(evt) {
    alert('I want to search for the right player!');
}
