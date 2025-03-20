document.getElementById('calculate-btn').addEventListener('click', function() {
    const initialAmount = parseFloat(document.getElementById('initial-amount').value);
    const annualRate = parseFloat(document.getElementById('annual-rate').value) / 100;
    const years = parseInt(document.getElementById('years').value);

    if (isNaN(initialAmount) || isNaN(annualRate) || isNaN(years)) {
        document.getElementById('result').textContent = 'Пожалуйста, заполните все поля.';
        return;
    }

    const finalAmount = initialAmount * Math.pow(1 + annualRate, years);
    const profit = finalAmount - initialAmount;

    document.getElementById('result').textContent = `Итоговая сумма: ${finalAmount.toFixed(2)} руб. Прибыль: ${profit.toFixed(2)} руб.`;
});