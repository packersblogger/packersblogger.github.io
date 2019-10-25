
    $('h2').each(function(){
      const scores = $(this).text()
      
      var strArray = scores.match(/(\d+)/g);
      const difference = parseInt(strArray[0])-parseInt(strArray[1]);
      if (typeof(difference) ==="number"){
        console.log(difference);
        $(this).after($('<h4></h4>').text(`Actual Difference: ${difference}`));  
      } 
      
    })
