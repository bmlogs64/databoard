async function carregarDados() {
    const tbody = document.querySelector("#tabela tbody");
    tbody.innerHTML = "";

    try {
        const resposta = await fetch("http://127.0.0.1:8000/dados");
        const resultado = await resposta.json();

        if(resultado.status === "sucesso") {
            resultado.dados.forEach(item => {
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
        } else {
            mostrarErroNaTabela("Erro ao carregar dados: " + resultado.mensagem);
        }
    } catch (error) {
        console.error(error);
        mostrarErroNaTabela("Erro ao conectar com a API.");
    }
}

function mostrarErroNaTabela(mensagem) {
    const tbody = document.querySelector("#tabela tbody");
    const tr = document.createElement("tr");
    const td = document.createElement("td");
    td.colSpan = 5;
    td.style.textAlign = "center";
    td.style.color = "red";
    td.textContent = mensagem;
    tr.appendChild(td);
    tbody.appendChild(tr);
}

window.onload = carregarDados;

setInterval(carregarDados, 30000);