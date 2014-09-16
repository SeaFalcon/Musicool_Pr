function sleep (milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}







function getArticle(number) {
	var EndArticle = false;
	$.ajax({
		url:'/more',
		dataType: 'JSON',
		data: {
			number: number


		},
		success: function(data) {
			if(Number(data.id) < 1){
				var string = "<div class='well' id='article_" + data.id +"'><h1>마지막 글입니다.</h1></div>";
				$("#results").append(string);
				$("#morebtn").fadeout('slow');
				EndArticle = true;
			} else {
				var string = "<div class='well' id = 'article_" + data.id +"'><h1><a href='/article/detail/" + data.id + "'>" + data.title + "</a></h1><h3>" + data.author + "</h3><h6>" + data.date_created + "</h6><p>" + data.content
				+"</p></div>";
				$('#results').append(string);
			}
		},
		error: function(status){
				var string = "<div clss='well' id='bug'><h1>일시적인 서버 에러가 발생했습니다... 새로고침을 해주시기 바랍니다.</h1></div>";
				$("#results").append(string);
				$("#morebtn").fadeOut('slow');

		}
	});
	return true;
}

$(document).ready(function () {
	var number = 0;

	$.ajax({
		url:"/rows",
		dataType: 'JSON',
		success: function(data) {
			number = data.rows - 4;
		}
	});

$('#load_more_button').click(function() {
	for(var i = 0; i < 5; i ++) {
		sleep(200);
		number --;
		getArticle(number);
		if(number < 1) {
			break;
		}
		
	}
	return false;
});
});