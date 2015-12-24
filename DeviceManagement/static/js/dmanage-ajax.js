$(document).ready(function(){
$(".return-btn").click(function(event)
{
	var sn;
	sn = $(this).attr("data-sn");
	$.get('/return_device/',{sn:sn},function(data,status){
		if ( status == 'success')
		{
			alert('success')
		}
		else
		{
		 alert('Return device failed.Error: '+ data)
		}
	})})
})