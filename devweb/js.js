let displayValue = '';

document.getElementById('search').addEventListener('input', function() {
    const inputValue = this.value;
    const calculator = document.getElementById('calculator');

    // Mostra a calculadora quando começar a digitar
    if (!isNaN(inputValue)) { // Verifica se o valor digitado é um número
        calculator.style.display = 'block';
    } else {
        calculator.style.display = 'none'; // Oculta a calculadora se não for um número
    }
});

function appendToDisplay(value) {
    displayValue += value;
    document.getElementById('display').value = displayValue;
}

function clearDisplay() {
    displayValue = '';
    document.getElementById('display').value = displayValue;
}

function calculateResult() {
    try {
        const result = eval(displayValue);
        document.getElementById('display').value = result;
    } catch (error) {
        document.getElementById('display').value = 'Erro';
    }
}
