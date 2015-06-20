$(document).ready( function(){
	$("#foodForm").hide();
	$("#clothForm").hide();
	$("#moneyForm").hide();
	$("#bookForm").hide();
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
});
