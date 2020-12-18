function timeConverter(timestamp){
    var a = new Date(timestamp * 1000);
    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    var year = a.getFullYear();
    //var month = months[a.getMonth()];
    var month = a.getMonth() + 1;
    var date = a.getDate();
    var hour = a.getHours();
    var min = a.getMinutes();
    if(min>=0 && min<=9){
        var time = date + '-' + month + '-' + year + ' ' + hour + ':0' + min ;
    }
    else{
        var time = date + '-' + month + '-' + year + ' ' + hour + ':' + min ;
    }
    return time;
  }

  function getName(object){
    var name = Object.keys(object)
      return name
  }
  

window.addEventListener("load", evt => {
    evt.preventDefault();
    
    function loadProductDetails() {
        fetch('http://localhost:3002/data')
            .then(response => {
                response.json()
                    .then(data => {
                        var dataTest = data[1].dataTest
                        console.log(dataTest);
                        console.log(dataTest[0]);
                        var date = new Date(dataTest[0].marteau[0].timestamp*1000);
                        console.log(timeConverter(dataTest[0].marteau[1].timestamp));

                        var ctx = document.getElementById('myChart').getContext('2d');
                        var chart = new Chart(ctx, {
                            // The type of chart we want to create
                            type: 'line',

                            // The data for our dataset
                            data: {
                                labels: [timeConverter(dataTest[0].marteau[0].timestamp), timeConverter(dataTest[0].marteau[1].timestamp), timeConverter(dataTest[0].marteau[2].timestamp), timeConverter(dataTest[0].marteau[3].timestamp), timeConverter(dataTest[0].marteau[4].timestamp), timeConverter(dataTest[0].marteau[5].timestamp), timeConverter(dataTest[0].marteau[6].timestamp)],
                                datasets: [{
                                    label: "Prix en €",
                                    backgroundColor: 'rgb(255, 99, 132)',
                                    borderColor: 'rgb(255, 99, 132)',
                                    data: [dataTest[0].marteau[0].price, dataTest[0].marteau[1].price, dataTest[0].marteau[2].price, dataTest[0].marteau[3].price, dataTest[0].marteau[4].price, dataTest[0].marteau[5].price, dataTest[0].marteau[6].price]
                                }]
                            },

                            // Configuration options go here
                            options: {
                                title: {
                                    display: true,
                                    text: "Parfum BOSS"
                                }
                            }
                        });

                        for(var i=0;i<dataTest[0].length;i++){

                        }
                    });
            })
            .catch(console.error);
    }
     
    loadProductDetails();
})