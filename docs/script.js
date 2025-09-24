let dados = [];
let paginaAtual = 1;
const registrosPorPagina = 10;

async function carregarDados() {
    const tbody = document.querySelector("#tabela tbody");
    tbody.innerHTML = "<tr><td colspan='5' style='text-align:center'>Carregando...</td></tr>";

    try {
        const resposta = await fetch("https://databoard-backend.onrender.com/dados");
        const resultado = await resposta.json();

        if (resultado.status === "sucesso" && Array.isArray(resultado.dados)) {
            dados = resultado.dados;
            paginaAtual = 1;
            atualizarTabela();
        } else {
            dados = [];
            mostrarErroNaTabela("Erro ao carregar dados: " + (resultado.mensagem || "Formato inválido"));
}
    } catch (error) {
        console.error(error);
        mostrarErroNaTabela("Erro ao conectar com a API.");
    }
}

function mostrarErroNaTabela(mensagem) {
    const tbody = document.querySelector("#tabela tbody");
    tbody.innerHTML = "";
    const tr = document.createElement("tr");
    const td = document.createElement("td");
    td.colSpan = 5;
    td.style.textAlign = "center";
    td.style.color = "red";
    td.textContent = mensagem;
    tr.appendChild(td);
    tbody.appendChild(tr);
}

function aplicarFiltros(dados) {
    const filtroNome = document.getElementById("filtro-nome").value.toLowerCase();
    const filtroTelefone = document.getElementById("filtro-telefone").value.toLowerCase();
    const filtroEmail = document.getElementById("filtro-email").value.toLowerCase();
    const filtroCpf = document.getElementById("filtro-cpf").value.toLowerCase();

    return dados.filter(item => 
        item.nome.toLowerCase().includes(filtroNome) &&
        item.numero.toLowerCase().includes(filtroTelefone) &&
        item.email.toLowerCase().includes(filtroEmail) &&
        item.cpf.toLowerCase().includes(filtroCpf)
    );
}

function atualizarTabela() {
    const tbody = document.querySelector("#tabela tbody");
    tbody.innerHTML = "";

    const dadosFiltrados = aplicarFiltros(dados);
    const totalPaginas = Math.ceil(dadosFiltrados.length / registrosPorPagina);
    if (paginaAtual > totalPaginas) paginaAtual = totalPaginas || 1;

    const inicio = (paginaAtual - 1) * registrosPorPagina;
    const fim = inicio + registrosPorPagina;
    const paginaDados = dadosFiltrados.slice(inicio, fim);

    if (paginaDados.length === 0) {
        mostrarErroNaTabela("Nenhum registro encontrado.");
        document.getElementById("info-pagina").textContent = `Página 0 de 0`;
        document.getElementById("total-registros").textContent = `Total de registros: 0`;
        return;
    }

    paginaDados.forEach(item => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${item.nome}</td>
            <td>${item.numero}</td>
            <td>${item.email}</td>
            <td>${item.cpf}</td>
            <td>${item.data_formatada}</td>
        `;
        tbody.appendChild(tr);
    });

    document.getElementById("info-pagina").textContent = `Página ${paginaAtual} de ${totalPaginas}`;
    document.getElementById("total-registros").textContent = `Total de registros: ${dadosFiltrados.length}`;

    // Habilita/desabilita botões
    document.getElementById("prev").disabled = paginaAtual === 1;
    document.getElementById("next").disabled = paginaAtual === totalPaginas;
}

document.getElementById("prev").addEventListener("click", () => {
    if (paginaAtual > 1) {
        paginaAtual--;
        atualizarTabela();
    }
});

document.getElementById("next").addEventListener("click", () => {
    const dadosFiltrados = aplicarFiltros(dados);
    const totalPaginas = Math.ceil(dadosFiltrados.length / registrosPorPagina);
    if (paginaAtual < totalPaginas) {
        paginaAtual++;
        atualizarTabela();
    }
});

document.getElementById("go").addEventListener("click", () => {
    const dadosFiltrados = aplicarFiltros(dados);
    const totalPaginas = Math.ceil(dadosFiltrados.length / registrosPorPagina);
    const inputPagina = parseInt(document.getElementById("input-pagina").value);

    if (isNaN(inputPagina) || inputPagina < 1 || inputPagina > totalPaginas) {
        mostrarErroNaTabela(`Página inválida! Digite entre 1 e ${totalPaginas}.`);
        return;
    }

    paginaAtual = inputPagina;
    atualizarTabela();
});

document.querySelectorAll("#filtro-nome, #filtro-telefone, #filtro-email, #filtro-cpf")
    .forEach(input => input.addEventListener("input", () => {
        paginaAtual = 1;
        atualizarTabela();
    }));

window.onload = carregarDados;


setInterval(carregarDados, 30000);