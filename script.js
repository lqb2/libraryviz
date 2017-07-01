

// console.log('jQuery', $)

function handleResponse(response){
	console.log('response',response)
}

$.ajax({
  url: 'http://www.goodreads.com/review/list/61877628-lawrence?shelf=read',
  success: handleResponse,
});

