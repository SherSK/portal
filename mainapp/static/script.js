$(document).ready(() => {
        var form = $('#form');
        console.log(form);
        var csrf_token=$("input[name='csrfmiddlewaretoken']").val()
        console.log(csrf_token)

        setInterval(() => {
             $.ajax({
                url:'',
                type:'post',
                data: {
                    text: $(this).text(),
                    csrfmiddlewaretoken:csrf_token
                },
            success: function(response){
                // console.log(response);
                 $.each(response,(objId,el)=>{
                     for (var key in el){
                         param=key;
                         parValue=String(el[key])
                         sign=parValue.indexOf(',')
                         if (sign<0){
                             realValue=parValue;
                         } else{
                             realValue=parValue.substring(0,sign)
                         }
                        if (parValue.indexOf('up')>0) {
                           $(`#${objId}>.${param}`).removeClass('bg-warning').addClass('bg-danger')
                        }   
                        if (parValue.indexOf('down')>0) {
                            $(`#${objId}>.${param}`).removeClass('bg-danger').addClass('bg-warning')
                        }
                        if (parValue.indexOf(',')<0){
                            $(`#${objId}>.${param}`).removeClass('bg-primary').removeClass('bg-danger');
                        }  
                        $(`#${objId}>.${param}`).text(realValue)                                   
                  
                     }  
                    })
            }  //succes
            }) //ajax           
        }, 2000);//interval

        
    });



