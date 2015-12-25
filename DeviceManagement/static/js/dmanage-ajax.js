$(document).ready(function(){
$(".return-btn").click(function(event)
{
	var sn;
	sn = $(this).attr("data-sn");
	$.get('/return_device/',{sn:sn},function(data,status){
		if ( status == 'success')
		{
			window.location.reload()
		}
		else
		{
		 alert('Return device failed.Error: '+ data)
		}
	})
	}
);
$(".borrow-btn").click(function(event)
{
	var sn;
	sn = $(this).attr("data-sn");
	$.get('/borrowDeviceForm/',{sn:sn},function(data,status){
	})
	})

})