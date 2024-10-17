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
    const confirmEmailInput = document.getElementById('confirmEmail');
    const passwordInput = document.getElementById('password');
    const submitButton = document.getElementById('submit');
    const emailError = document.getElementById('emailErro');
    const confirmError = document.getElementById('emailConfirmErro');
    const passwordStrength = document.getElementById('passwordSt');

    function validateEmail(email) {
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return emailPattern.test(email);
    }

    function checkPasswordStrength(password) {
        if (password.length < 8) {
            return 'Senha muito fraca';
        } else if (!/[A-Z]/.test(password)) {
            return 'Adicione uma letra maiúscula';
        } else if (!/[0-9]/.test(password)) {
            return 'Adicione um número';
        }
        return 'Senha forte';
    }

    emailInput.addEventListener('input', () => {
        emailError.textContent = validateEmail(emailInput.value) ? '' : 'Formato de email inválido';
        confirmError.style.display = 'none';
    });

    confirmEmailInput.addEventListener('input', () => {
        confirmError.style.display = emailInput.value !== confirmEmailInput.value ? 'inline' : 'none';
    });

    passwordInput.addEventListener('input', () => {
        passwordStrength.textContent = checkPasswordStrength(passwordInput.value);
    });

    document.querySelector('form').addEventListener('input', () => {
        submitButton.disabled = !(validateEmail(emailInput.value) &&
            emailInput.value === confirmEmailInput.value &&
            checkPasswordStrength(passwordInput.value) === 'Senha forte');
    });
});