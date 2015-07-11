var item = document.getElementById('some-item');
$(document).ready( function(){ 
	console.log("fires me !!!");
	$(".button-collapse").sideNav();
	$("#foodForm").hide();
	$("#clothForm").hide();
	$("#moneyForm").hide();
	$("#bookForm").hide();
	$("#addForm").hide();
	$( "#foodForm" ).submit(function( event ) {
		var foodName = $("#foodName").val();
		var foodQ = $("#foodQ").val();
		var foodVeg = $("#foodVeg").val();
		var foodLong = $("#foodLong").val();
		if(!foodName || foodQ.isNaN())
		{

		} else{

		}
	  event.preventDefault();
	});
	$( "#clothForm" ).submit(function( event ) {
		var male = $("#male").val();
		var female = $("#female").val();
		var clothOption = $("#clothOption").val();
		var clothQ = $("#clothQ").val();
		var size = $("#size").val();
	  event.preventDefault();
		if (male=="male" || female=="female" || clothOption.isNaN() || clothQ.isNaN() || size.isNaN())
		{

		}else{

		}
	});
	$( "#moneyForm" ).submit(function( event ) {
		var moneyQ = $("#moneyQ").val();
		if(moneyQ.isNaN())
		{

		}else{

		}
	  event.preventDefault();
	});
	$( "#bookForm" ).submit(function( event ) {
		var bookOption = $("#bookOption").val();
		var bookQ = $("#bookQ").val();
		if(bookOption.isNaN() || bookQ.isNaN())
		{

		} else{

		}
	  event.preventDefault();
	});
	$( "#addForm" ).submit(function( event ) {
		var first_name = $("#first_name").val();
		var last_name = $("#last_name").val();
		var emailSU = $("#emailSU").val();
		var passwordSU = $("#passwordSU").val();
		var admin = $("#admin").val();
		if(!first_name || !last_name || !emailSU || !passwordSU)
		{

		}else{

		}
	  event.preventDefault();
	});

	$("#food" ).click(function() {
		console.log("yolo2");
		$( "#foodForm" ).show();
		$(".collection").hide();
	});
	$("#backF").click(function(){
		$("#foodForm").hide();
		$(".collection").show();
	});
	$("#cloth" ).click(function() {
		$( "#clothForm" ).show();
		$(".collection").hide();
	});
	$("#backC").click(function(){
		$("#clothForm").hide();
		$(".collection").show();
	});
	$("#money" ).click(function() {
		$( "#moneyForm" ).show();
		$(".collection").hide();
	});
	$("#backM").click(function(){
		$("#moneyForm").hide();
		$(".collection").show();
	});
	$("#book" ).click(function() {
		$( "#bookForm" ).show();
		$(".collection").hide();
	});
	$("#backB").click(function(){
		$("#bookForm").hide();
		$(".collection").show();
	});
	$("#add" ).click(function() {
		$( "#addForm" ).show();
		$(".collection").hide();
	});
	$("#backSU").click(function(){
		$("#addForm").hide();
		$(".collection").show();
	});
	
	// login logic --> applies to : index.html
	console.log("Over login_b");
	$("#login_b").click( 
		function(){
			console.log("setting up login");
			var login_packet ={
				"_id": $("#email").val(),
				"pass": $("#password").val()
			};
			console.log(login_packet);
			var xhr = new XMLHttpRequest({mozSystem:true});
			xhr.open("POST", "http://localhost:5000/api/login", false);
			// xhr.setRequestHeader("Access-Control-Allow-Origin","*");
			xhr.send(JSON.stringify(login_packet));
			var x= JSON.parse(xhr.responseText) ;
			if(x.loggedIn == true){
				console.log("Login successful, redirecting to home.html");
				//console.log(xhr.responseText);
				localStorage.setItem("uid",$("#email").val());
				localStorage.setItem("token", x.token);
				//console.log('hey'+localStorage.getItem('username'));
				window.location = "choices.html";
			}
			else{
				console.log("Login unsuccessful, show the message");
				$('#login').append("Login not successful, Please try again.");
				$('#email').addClass('invalid');
				$('#password').addClass('invalid');
			}
		}); 
});
