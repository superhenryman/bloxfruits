const products = [
    { id: 1, name: "Laptop", price: 999, image: "laptop.png" },
    { id: 2, name: "Headphones", price: 199, image: "headphones.png" },
];

let cart = [];
let email = "";

// Display products
function displayProducts() {
    const productList = document.getElementById('product-list');
    productList.innerHTML = ''; // Clear any existing products first
    products.forEach(product => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        productCard.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>$${product.price}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productCard);
    });
}

// Add item to the cart
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (!cart.includes(product)) {
        cart.push(product);
    }
    updateCart();
}

// Remove item from the cart
function removeFromCart(productId) {
    cart = cart.filter(p => p.id !== productId);
    updateCart();
}

// Update the cart display
function updateCart() {
    const cartItems = document.getElementById('cart-items');
    cartItems.innerHTML = "";
    cart.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `${item.name} - $${item.price} <button onclick="removeFromCart(${item.id})">Remove</button>`;
        cartItems.appendChild(li);
    });
}

// Handle login
document.getElementById('login-btn').addEventListener('click', () => {
    email = document.getElementById('email-input').value;
    if (!email) {
        alert('Please enter a valid email!');
        return;
    }
    
    // Hide the login modal after successful login
    document.getElementById('email-modal').style.display = 'none';
    
    // Show the cart and products
    document.querySelector('main').style.display = 'block';
});

// Navigation functionality
document.getElementById('home-link').addEventListener('click', () => {
    document.getElementById('product-list').style.display = 'grid';
    document.getElementById('cart').style.display = 'none';
    displayProducts();
});

document.getElementById('cart-link').addEventListener('click', () => {
    document.getElementById('cart').style.display = 'block';
    document.getElementById('product-list').style.display = 'none';
});

// Handle checkout
document.getElementById('checkout-btn').addEventListener('click', () => {
    if (cart.length === 0) {
        alert("Your cart is empty!");
        return;
    }

    // Show loading spinner
    const checkoutButton = document.getElementById('checkout-btn');
    checkoutButton.disabled = true;
    checkoutButton.textContent = 'Processing...';

    const cartData = {
        discord: email,
        items: cart.map(item => ({
            name: item.name,
            price: item.price,
            quantity: 1
        }))
    };

    const jsonData = JSON.stringify(cartData);

    fetch('https://web-production-d652a.up.railway.app/checkout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => response.json())
    .then(data => {
        alert("Checkout successful!");
        cart = [];
        updateCart();
        checkoutButton.disabled = false;
        checkoutButton.textContent = 'Checkout';
    })
    .catch(error => {
        alert("An error occurred during checkout.");
        console.error('Error:', error);
        checkoutButton.disabled = false;
        checkoutButton.textContent = 'Checkout';
    });
});

// Initialize
displayProducts();

// Show the login modal initially
window.onload = function() {
    document.getElementById('email-modal').style.display = 'flex';
};
