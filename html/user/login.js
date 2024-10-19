const cards = document.querySelectorAll('.avaliacao-card');
const indicatores = document.querySelectorAll('.indicator');
let currentCard = 0;

function showNextCard() {
    cards[currentCard].classList.remove('active');
    indicatores[currentCard].classList.remove('active');
    currentCard = (currentCard + 1) % cards.length;
    cards[currentCard].classList.add('active');
    indicatores[currentCard].classList.add('active');
}

setInterval(showNextCard, 4000);

document.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const submitButton = document.getElementById('submit');
    const emailError = document.getElementById('emailErro');
    const emailNaoEncontrado = document.getElementById('emailNaoEncontrado');
    const passwordErro = document.getElementById('passwordErro');

    const usuariosCadastrados = {
        'ana@teste.com': '123',
        'tiago@teste.com': '456'
    };

    function validateEmail(email) {
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return emailPattern.test(email);
    }

    function checkEmailCadastrado(email) {
        return email in usuariosCadastrados;
    }

    function checkPassword(email, password) {
        return usuariosCadastrados[email] === password;
    }

    emailInput.addEventListener('input', () => {
        emailError.textContent = '';
        emailNaoEncontrado.textContent = '';

        if (!validateEmail(emailInput.value)) {
            emailError.textContent = 'Formato de email inválido';
        } else {
            if (!checkEmailCadastrado(emailInput.value)) {
                emailNaoEncontrado.textContent = 'Não existe uma conta com esse email';
            }
        }
        passwordErro.textContent = '';
    });

    passwordInput.addEventListener('input', () => {
        if (checkEmailCadastrado(emailInput.value)) {
            passwordErro.textContent = checkPassword(emailInput.value, passwordInput.value) ? '' : 'Senha incorreta';
        }
    });

    document.querySelector('form').addEventListener('input', () => {
        submitButton.disabled = !(validateEmail(emailInput.value) &&
        checkEmailCadastrado(emailInput.value) &&
        checkPassword(emailInput.value, passwordInput.value));
    });
});