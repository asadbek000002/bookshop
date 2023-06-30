
////////Header-1 icons
searchForm = document.querySelector('.search-form');
document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
}

window.onscroll = () => {
    searchForm.classList.remove('active');
    if(window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    }else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

window.onload = () => {
    if(window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    }else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

///////////////login form container//
let loginForm = document.querySelector('.login-form-container');

document.querySelector('#login-btn').onclick = () => {
    loginForm.classList.toggle('active');
}
document.querySelector('#close-login-btn').onclick = () => {
    loginForm.classList.remove('active');
}

//////////////////////////////////button onclick//
function send () {
    alert("Xabar Jo'natildi")
}
function error() {
    alert("Xaridingiz bekor qilindi")
}




///////////CART Savat
let cartIcon = document.querySelector('#cart-icon')
let cart = document.querySelector('.cart')
let closeCart = document.querySelector('#close-cart')
//////////////// open cart
cartIcon.onclick = () => {
    cart.classList.add("active")
};  
 /////////////close cart
closeCart.onclick = () => {
    cart.classList.remove("active")
};   

//////////CARD WARKING JS
if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", ready);
} else {
    ready();
}

// ////////////Making Funcsion
 function ready() {
    //////Reomve Items From Cart
    var reomveCartButtons = document.getElementsByClassName('cart-remove')
    console.log(reomveCartButtons);
    for(var i = 0; i < reomveCartButtons.length; i++) {
        var button = reomveCartButtons[i]
        button.addEventListener('click', removeCartItem)
    }
    ////////////////Quantity Changes
    var quantityInputs = document.getElementsByClassName('cart-quantity');
    for (var i = 0; i < quantityInputs.length; i++) {
        var input = quantityInputs[i];
        input.addEventListener('change', quantityChanged)
    }
    
    
    ///////////aDD tO  Card
    var addCart = document.getElementsByClassName("add-cart");
    for (var i = 0; i < addCart.length; i++) {
        var button = addCart[i];
        button.addEventListener("click", addCartClicked)
    }
    
 }
 
 
 
//  //////////Reomve Item From Cart
 function removeCartItem(event) {
    var buttonClicked = event.target
    buttonClicked.parentElement.remove();
    updatetotal();
 }
 
//  ////////////////Quantity Changes
 function quantityChanged(event) {
    var input = event.target
    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }
    updatetotal();
 }
 

 
 
 
 
//  //////////////Add to Cart
 function  addCartClicked(event) {
    var button = event.target;
    var shopProducts = button.parentElement;
    var title = shopProducts.getElementsByClassName("product-title")[0].innerText;  
    var price = shopProducts.getElementsByClassName("price")[0].innerText;  
    var productImg = shopProducts.getElementsByClassName("product-img")[0].src;
    addProductToCart (title, prise, productImg);
    updatetotal();
 }






 
 function addProductToCart(title, prise, productImg) {
    var cartShopBox = document.createElement("div")
    cartShopBox.classList.add("cart-box")
    var cartItem = document.getElementsByClassName("cart-content")[0]
    var cartItemsNames = cartItems.getElementsByClassName("cart-product-title");
    for (var i = 0; i < cartItemsNames.length; i++) {
        alert("You have already add this item to cart")
         return;
    }
   
}

    
    var cartBoxContent =`
                        <img src="./img/book7.png" alt="" class="cart-img">
                            <div class="detail-box">
                                <div class="cart-product-title">Earbuds</div>
                                <div class="cart-price">$25</div>
                                <input type="number" value="1" class="cart-quantity">
                            </div>
                            <!-- -----Remove Cart------ -->
                            <i class="fa-solid fa-trash cart-remove"></i>`;
// //////cart shop box
cartShopBox.innerHYML = cartBoxContent
cartItems.append(cartShopBox)
cartShopBox.getElementsByClassName('cart-remove')[0].addEventListener('click', removeCartItem)
cartShopBox.getElementsByClassName('cart-quantity')[0].addEventListener('change', quantityChanged)
 
 
 
 
 ///////////Update Total
 function updatetotal() {
    var cartContent = document.getElementsByClassName("cart-content")[0]
    var cartBoxes = cartContent.getElementsByClassName("cart-box");
    var toral = 0;
    for (var i = 0; i < cartBoxes.length; i++) {
        var cartBox = cartBoxes[i]
        var priceElement = cartBox.getElementsByClassName("cart-price")[0]
        var quantityElement = cartBox.getElementsByClassName('cart-quantity')[0]
        var price = parseFloat(priceElement.innerText.replase("$", ""))
        var quantity = quantityElement.value;
        total = total + price * quantity;
        
        ////////////If price Contain some Cents Value
        total = Math.round(total * 100) / 100;
        
        document.getElementsByClassName("total-price")[0].innerText = "$" + total;
    }
 }

/*
    SignUP
*/
const close = document.querySelector(".message-close");
const message = document.querySelector(".messages");

if (close && message){
    //Close Error/Success Message
    close.addEventListener("click", () =>{
        message.style.display = "none";
    })

}

//Form Validation
const signupForm = document.getElementById("signup-form");

signupForm.addEventListener("submit", (e) =>{

    const title = document.querySelector(".message-title");
    const messageParagraph = document.querySelector(".message-paragraph");
    const password1 = document.getElementById("password1").value;
    const password2 = document.getElementById("password2").value;

    if (password1 != password2){
        e.preventDefault();
        message.style.display = "flex";
        title.textContent = "Invalid Password!";
        messageParagraph.textContent = "Make sure to confirm your password."
    }

})


 
 
 
