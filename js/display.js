$(document).ready(function(){
	var quotes = ['<p class="quoteText">Do or do not, there is no try</p>', 
		'<p class="quoteText">Life is too short to remove USB safely</p>',
		'<p class="quoteText">With great power comes great electricity bill</p>',
		'<p class="quoteText">Robots will rules one day..</p>',
		'<p class="quoteText">#Yolo</p>',
		'<p class="quoteText">$wagu</p>',
		'<p class="quoteText">Dont feed gremlins after midnight</p>',
		'<p class="quoteText">Go hang a salami Im a lasagna hog</p>',
		'<p class="quoteText">Do you even data bro?</p>',
		'<p class="quoteText">Respect my authoritay!</p>'
		];
	
	$("body").fadeIn(1000);
	
	//$("#bigTitle").effect('slide', 2000);
	$(".heading").each( function(key, value){
		$(value).effect('slide', 2000);
	});
	
	$("#mascot").effect('slide', {direction: 'right'}, 2000);
		
	$('#mascot').mouseover( function(){
		$('#quoteContainer').empty();
		
		var num = (Math.floor(Math.random() * 10));
			
		var quote = quotes[num];
			
		$('<p/>', {
			'class': 'speech',
			'html': quote
		}).appendTo('#quoteContainer');
	});
		
	$('#mascot').mouseleave(function(){
		$('#quoteContainer').empty();
	});
	
	//On form submit handler
	$('#botFindForm').submit(function(event) {
		
		$('#resultContainer').empty();
		
		var items = [];
		
		//Get value from form
		var req = '<p class="req">' + $('#botInput').val() + '</p>';
		var info = '<p class="info">Life Hack Bot Found: blank for request:</p> ' + req;
		
		items.push(info);
		
		$.getJSON("/get_hack?hack=" + req, function(data){
			//make results div
			var results = $('<div/>', {
				'text': info
			}).appendTo('#resultContainer');
		});
		
		$('<div/>', {
			'html': items.join(""),
			'class': 'resultText'
		}).appendTo('#resultContainer');
		
		event.preventDefault();
		
	});
	
		$('#botMakeForm').submit(function(event) {
		
			$('#resultContainer').empty();
			
			items.push(info);
			
			$.getJSON("/build_hack?hack=" + req, function(data){
				//make results div
				var results = $('<div/>', {
					'text': info
				}).appendTo('#resultContainer');
			});
			
			$('<div/>', {
				'html': items.join(""),
				'class': 'resultText'
			}).appendTo('#resultContainer');
			
			event.preventDefault();
			
	});
	
	
});