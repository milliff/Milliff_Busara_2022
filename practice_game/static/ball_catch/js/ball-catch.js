var trayID;
var interval = 41; //the lower the value, the quicker ball falls.
var ballDelay = 1071; //the lower the value, the more balls.
var nCol = 4;
var score = 50; // starting endowment
var catches = 0; // "hits"
var time = 61;
var prize = -5; // per hit penalty
var lives = 10; // "lives" remember to set down in line 116


$(document).ready(function(){
    $("#waterfall").fadeTo("slow", 0.33);
    $("#startbutton").click(function(){
        timer();
        startNewGame();
    });
});

/**
 * Main function to start the game.
 */
function startNewGame() {
    $("#waterfall").fadeTo("slow", 1);
    $(".stats").fadeIn();
    $("#startbutton").hide();

    createballs();
    createtray();
    updateStats();
    /*
     $(document).keydown(function(e) {
     if(e.keyCode == 37) {
     leftArrow();
     } else if(e.keyCode == 39) {
     rightArrow();
     }
     });
     */
    $("#clickleft").click(function(){
        leftArrow();
    })
    $("#clickright").click(function(){
        rightArrow();
    })
}

/**
 * Created a single ball.
 */
function createball() {
    var newball = document.createElement("div");
    $(newball).attr("class", "fallingball");
    $(newball).css("position","absolute");
    var tempId = "ball" + Math.floor(Math.random()*30003);
    $(newball).attr("id", tempId);

    var leftMargin = (Math.floor(Math.random() * nCol)) / nCol;
    leftMargin *= ($("#waterfall").width() - 60);

    $(newball).css("margin-left", leftMargin + 73 + "px" );

    $(newball).appendTo("#waterfall");

    ballFall(tempId);
}

/**
 * Created a flow of balls.
 */

function createballs() {
    var control = setInterval(function(){
        if (time == 0){
            clearInterval(control);
        }
        else if (score < 1){
            clearInterval(control);
            alert("Game Over. Click Next to See your Score.");
        }
        createball();
    }, ballDelay);
}

/**
 * Animates a ball falling and checks whether the ball was caught
 */
function ballFall(id) {
    var ball = $("#" + id);

    var fall = setInterval(function(){
        var topMargin = ball.css("margin-top");
        topMargin = parseInt(topMargin);
        if (topMargin < $("#waterfall").height() - ball.height()){
            topMargin += 5;
            ball.css("margin-top", topMargin + 'px' );
        }
        else {
            ball.effect('puff');
            clearInterval(fall);
        }
    }, interval);

    /**
     * * Called when a ball was caught.
     * * Score goes up .
     * */
    var caught = setInterval(function(){
        if (parseInt(ball.css("margin-top")) < parseInt($(".tray").css("margin-top"))
            && parseInt(ball.css("margin-top")) == parseInt($(".tray").css("margin-top")) - 40
            && parseInt(ball.css("margin-left")) == parseInt($(".tray").css("margin-left")) + 13
            && score >= 1){ // still can't get the break conditions figured out yet.
            score -= prize;
            catches += 1;
            lives -= 1;


            ball.effect('explode');
            clearInterval(fall);
            clearInterval(caught);

            updateStats();
        }
        else if (time == 0){
            clearInterval(fall);
            clearInterval(caught);
        }
        else if (score == 0){
            clearInterval(fall);
            clearInterval(caught);
//            alert("Game Over. Click Next to See your Score.");
        }
    }, interval);

}

function createtray() {
    var tray = document.createElement("div");
    $(tray).attr("class", "tray");
    $(tray).css("position", "absolute");
    trayID = "tray0";
    $(tray).attr("id", trayID);
    $(tray).css("margin-left", 60 + "px" );
    var topMargin = $("#waterfall").height() - 30;
    $(tray).css("margin-top", topMargin + "px" );
    $(tray).appendTo("#waterfall");
}

function leftArrow() {
    var leftMargin = $("#" + trayID).css("margin-left");
    leftMargin = parseFloat(leftMargin);
    var step = ($("#waterfall").width() - 60) / nCol;
    if (leftMargin > step){
        leftMargin -= step;
    }
    $("#" + trayID).css("margin-left", leftMargin + "px" );
}


function rightArrow() {
    var leftMargin = $("#" + trayID).css("margin-left");
    leftMargin = parseFloat(leftMargin);
    var step = ($("#waterfall").width() - 60) / nCol;
    if (leftMargin < step * (nCol - 1) + 30 ) {
        leftMargin += step;
    }
    $("#" + trayID).css("margin-left", leftMargin + "px" );
}

/**
 * * Needed to update all the current stats.
 * */
function updateStats(){
    $("#scorestats").html(score);
    $("#catchesstats").html(catches);
    $("#livesstats").html(lives);

    $('#catches').val(catches);
    $('#lives').val(lives);
    $('#score').val(score);
}

function timer() {
    function pad(val){
        return val> 9 ? val : "0" + val;
    }
    var x = setInterval (function(){
        $("#clock").html(Math.floor(--time / 60) + ":" + pad(time % 60));
        if (time == 0){
            clearInterval (x);
            updateStats();

        }
        else if (score == 0){
            clearInterval (x);
//            alert("Game Over. Click Next to See your Score.")
        }
    },1000);

    updateStats();
}

