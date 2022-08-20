function total() {
    var tot = document.getElementById('qt');
    tot.addEventListener('change',total)
    var soma = document.querySelector('#preço1').innerHTML;
    var soma2 = tot.value
    var add = document.getElementById('preço');
    add.innerHTML=soma*soma2
}
