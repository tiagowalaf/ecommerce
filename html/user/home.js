let tempoTotal = 4 * 60 * 60;
const reiniciarNumero = num => num < 10 ? '0' + num : num;
const iniciarTimer = () => {
    if (tempoTotal <= 0) {
        clearInterval(intervalo);
        return;
    }

    const horas = Math.floor(tempoTotal / 3600);
    const minutos = Math.floor((tempoTotal % 3600) / 60);
    const segundos = Math.floor(tempoTotal % 60);

    document.getElementById('hours').textContent = reiniciarNumero(horas);
    document.getElementById('minutes').textContent = reiniciarNumero(minutos);
    document.getElementById('seconds').textContent =  reiniciarNumero(segundos);
    tempoTotal--;
};

const intervalo = setInterval(iniciarTimer, 1000);
const modalE = document.getElementById("modalEndereco");
const endereco = document.getElementById("endereco");
const fecharModal = document.querySelector(".fechar")
const enderecoUserInput = document.getElementById("enderecoUser");
const numeroInput = document.getElementById("numero");
const cepInput = document.getElementById("cep");
let enderecoUser = "Brasil, SP, São Paulo";

endereco.onclick = () => {
    modalE.style.display = "block";
    enderecoUserInput.value = enderecoUser;
    numeroInput.value = '';
};

fecharModal.onclick = () => {
    modalE.style.display = "none";
};

window.onclick = event => {
    if (event.target === modalE) {
        modalE.style.display = "none";
    }
};

document.getElementById("buscarCep").addEventListener("click", () => {
    const cep = cepInput.value.replace(/\D/g, '');
    if (cep.length === 8) {
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(response => response.json())
        .then(data => {
            if (!data.erro) {
                enderecoUser = `Brasil, ${data.uf}, ${data.localidade}, ${data.bairro}, ${data.logradouro}`;
                enderecoUserInput.value = enderecoUser;
            }
        })
        .catch(console.error);
    }
});

document.getElementById("salvarEndereco").addEventListener("click", () => {
    const numero = numeroInput.value.trim();
    if (numero) {
        enderecoUser = `${enderecoUser}, ${numero}`;
        endereco.textContent = enderecoUser.split(',')[0] + ', ' + enderecoUser.split(',')[1];
        modalE.style.display = "none";
        enderecoUserInput.value = '';
        numeroInput.value = '';
        cepInput.value = '';
    }
});