document.getElementById('iaForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o envio do formulário

    // Captura os valores dos campos
    const nome = document.getElementById('nome').value;
    const descricao = document.getElementById('descricao').value;
    const plano = document.getElementById('plano').value;
    const categoriasSelect = document.getElementById('categorias');
    const categorias = Array.from(categoriasSelect.selectedOptions).map(option => option.value);

    // Cria o objeto de dados
    const data = { nome, descricao, plano, categorias };

    // Envia os dados para a API
    fetch('/add_modelo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Modelo IA registrado com sucesso!');
        } else {
            alert('Erro ao registrar o modelo IA: ' + data.message);
        }
        console.log('Response:', data);
    })
    .catch((error) => {
        alert('Erro ao registrar o modelo IA.');
        console.error('Error:', error);
    });
});

const canvas = document.getElementById('background');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const colors = ['#e11b39', '#ffca3a', '#8ac926', '#1982c4', '#550cb5', '#21e4eb', '#b61be1', '#e1851b'];
const particlesArray = [];
const numberOfParticles = 500; // Aumentado para mais partículas
class Particle {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 7 + 1; // Diferentes tamanhos
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.weight = Math.random() * 1 - 0.5;
        this.directionX = Math.random() * 2 - 1;
        this.directionY = Math.random() * 2 - 1;
    }

    update() {
        this.x += this.directionX;
        this.y += this.directionY;
        if (this.size > 0.2) this.size -= 0.1;
        if (this.x < 0 || this.x > canvas.width || this.y < 0 || this.y > canvas.height) {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 7 + 1; // Diferentes tamanhos
            this.weight = Math.random() * 1 - 0.5;
            this.directionX = Math.random() * 2 - 1;
            this.directionY = Math.random() * 2 - 1;
        }
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
        ctx.fillStyle = this.color;
        ctx.fill();
    }
}

function init() {
    for (let i = 0; i < numberOfParticles; i++) {
        particlesArray.push(new Particle());
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < particlesArray.length; i++) {
        particlesArray[i].update();
        particlesArray[i].draw();
    }
    requestAnimationFrame(animate);
}

init();
animate();

window.addEventListener('resize', function() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});