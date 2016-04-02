$(document).ready(function(){
	
	$('#mascot').mouseover( function(){
		$('#quoteContainer').empty();
		
		var quotes = ['<p class="quoteText">Do or do not, there is no try</p>', 
		'<p class="quoteText">Life is short to remove USB safely</p>',
		'<p class="quoteText">With great power comes great electricity bill</p>',
		'<p class="quoteText">Robots will rules one day..</p>',
		'<p class="quoteText">Yolo</p>',
		'<p class="quoteText">$wagu</p>',
		'<p class="quoteText">Dont feed gremlin after midnight</p>'
		];
		
		var num = (Math.floor(Math.random() * 7));
			
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
		
		/*$.getJSON("/get_hacks?hack=" + req, function(data){
			//make results div
			var results = $('<div/>', {
				'text': info
			}).appendTo('#resultContainer');
		});*/
		
		$('<div/>', {
			'html': items.join(""),
			'class': 'resultText'
		}).appendTo('#resultContainer');
		
		event.preventDefault();
		
	});
});