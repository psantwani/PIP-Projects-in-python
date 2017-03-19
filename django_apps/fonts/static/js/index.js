document.getElementById("submit").onclick = function(event){
	spans = document.getElementsByClassName( "spans" );
	text = document.getElementById("user_input").value;
	[].slice.call( spans ).forEach(function ( span ) {
		span.innerHTML = text;
	});
}