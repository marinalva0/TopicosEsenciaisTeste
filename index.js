//questão1 vale  nota
var calculadora

function calculadora(num1, num2, operação) {
    let resultado;
    if (operação === 'soma')
        resultado = num1 + num2;

}
if (operação === 'subtração') {
    resultado = num1 - num2;

} else if (operação === 'multiplicação')
    resultado = num1 * num2;

else if (operação === 'multiplicação') {
    resultado = num1 * num2;

} else if (operação === 'divisão') {
    if (num2 !== 0) {
        resultado = num1 / num2;
    } else {
        return 'erro: operaçao invalida use soma, subtração, multiplicação, ou divisão';
    }
    return resultado;
}
console.log(calculadora(2, 5, 'soma'));
console.log(calculadora(10, 2, "subtração"));
console.log(calculadora(2, 10, "multiplicação"));
console.log(calculadora(10, 2, "divisão"));
console.log(calculadora(10, 0, "divisao"));
console.log(calculadora(3, 10, "modulo"));