function changeQuantity(foodId, change) {
    const quantityInput = document.getElementById(`quantityInput${foodId}`);
    let currentQuantity = parseInt(quantityInput.value);
    currentQuantity = Math.max(currentQuantity + change, 0); // Ensure quantity doesn't go below 0
    quantityInput.value = currentQuantity;
    updateTotal(foodId);
}

function updateTotal(foodId) {
    const quantity = parseInt(document.getElementById(`quantityInput${foodId}`).value);
    const unitPrice = parseFloat(document.getElementById(`price${foodId}`).textContent);
    const totalPrice = (quantity * unitPrice).toFixed(2);
    document.getElementById(`totalPrice${foodId}`).textContent = totalPrice;
    updateGrandTotal();
}

// Initial calculation for all items


function updateGrandTotal() {
    let grandTotal = 0;
    document.querySelectorAll('[id^="totalPrice"]').forEach(element => {
        grandTotal += parseFloat(element.textContent);
    });
    const deliveryCharge = 20

    // Conditionally apply delivery charge
    const hasProducts = grandTotal > 0;
    const effectiveDeliveryCharge = hasProducts ? deliveryCharge : 0;
   

    // Calculate grand total with fixed amount and delivery charge
    const grandTotalWithFixed = (grandTotal + effectiveDeliveryCharge).toFixed(2);

    document.getElementById('grandTotal').textContent = grandTotal.toFixed(2);
    document.getElementById('deliveryCharge').textContent = effectiveDeliveryCharge.toFixed(2);
    document.getElementById('grandTotalWithFixed').textContent = grandTotalWithFixed;
    document.getElementById('grandTotalWithFixed2').textContent = grandTotalWithFixed;
}

document.querySelectorAll('[id^="quantityInput"]').forEach(input => {
    const foodId = input.id.replace('quantityInput', '');
    updateTotal(foodId);
});