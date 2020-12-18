var flag = 0;
const productsDiv = document.querySelector('#products');
const chooseProductForm = document.querySelector('#choose-product-form');

if(navigator.serviceWorker) {
    navigator.serviceWorker
        .register('sw.js')
}

function loadProductDetails() {
    fetch('http://localhost:3001/data')
        .then(response => {
            response.json()
                .then(productTest => {
                    console.log(productTest.length);
                    const allProducts = productTest.map(p => `
                    <a href="objet1.php?id=${p.ID}" style="color:black;" onmouseover="this.style.color='#FFFFFF';" onmouseout="this.style.color='#000000';">
                    <div class="card" style="display: inline-block;width:75%; margin-bottom:3px;">
                        <div class="card-body">
                        <h5 class="card-title">${p.Nom}</h5>
                        <p class="card-text">Site marchand : ${p.marchand}</p>
                        <p class="card-text">Prix : ${p.Prix}€</p>
                        <p class="card-text">Frais de port : ${p.Frais}€</p>
                        </div>
                    </div>
                    </a>`)
                            .join('');
            
                    productsDiv.innerHTML = allProducts; 
                });
        })
        .catch(console.error);
}

function changeFlag(){
    if(flag == 0){
        flag = 1
        loadProductDetails();
    }
    else{
        flag = 0
    }
}


if(flag == 1){        
    loadProductDetails();
}