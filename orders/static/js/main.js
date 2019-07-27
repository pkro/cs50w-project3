document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.addCartButton').forEach(button=> {
        button.onclick = () => {
            let toppings_required = button.dataset.toppings;
            document.querySelector('#toppings_required_disp').innerText = toppings_required;
        }
    })
});