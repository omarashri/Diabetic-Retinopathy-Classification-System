var img ;
function readURL(input) {

if (input.files && input.files[0]) {
  var reader = new FileReader();

  reader.onload = function(e) {
    $('#upload_prieview').attr('src', e.target.result);
    img = e.target.result;
  }

  reader.readAsDataURL(input.files[0]);
}
}

$("#imgInp").change(function() {
readURL(this);
});





//var formData = new FormData();
//formData.append("file", img);
//$.ajax({  
    //url: '/chat/send_voice/', //url of the model
    //type:"POST",
    //data: img,
    //processData: false,
    //contentType: false,
    //success:function(data) { //return model result and number of class
      //$("#class"+data).show() 
      //},
    //error: function(xhr, status, error)
      //{
        //console.log(status);
        //alert(status+ xhr.responseText + error);
      //}
   //});