/*
* Landing javascript files
*/

var redirect_to = function() {
    $('#explorer-panel-transparent-bgd').show();
    $('#explore-panel-loading').show();
}

/*
* on ready
*/
$(function() {
  $("#btn_explore_view").on("click", redirect_to);
});
