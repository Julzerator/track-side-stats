// Action buttons for Track Side Stats

function showButtons () {

};

function hideButtons () {

};

$(function() {
  	$( ".player" ).draggable({revert:true});
    $( ".player" ).draggable({
    	start: function( event, ui ) {
       		$( ".actions" ).siblings( ".control" ).show();
    	}
    });
    $( ".home_position" ).droppable({
      drop: function( event, ui ) {
      	var player_id = ui.helper.data().playerid;
      	var name = ui.helper.data().name;
      	var number = ui.helper.data().number;
      	var player = ui.helper.children('.player').html();
      	$( 'input[value="'+player_id+'"]').siblings('.player').html('');
      	$( 'input[value="'+player_id+'"]').attr('value', '');
        $( this ).children('.pos').attr('value', player_id );
        $( this ).children('.player').html(player);

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
      	var player = ui.helper.children('.player').html();
      	$( 'input[value="'+player_id+'"]').siblings('.player').html('');
      	$( 'input[value="'+player_id+'"]').attr('value', '');
        $( this ).children('.pos').attr('value', player_id );
        $( this ).children('.player').html(player);
	    }
    });
  });