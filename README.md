# 📊 Databoard

Este projeto é uma aplicação **fullstack** para visualização de dados.
🔗 [Acesse a aplicação aqui](https://bmlogs64.github.io/databoard/)

O **backend** foi desenvolvido em **Python com FastAPI** e está hospedado no **Render**.
O **frontend** é uma página estática em **HTML, CSS e JavaScript**, hospedada no **GitHub Pages**, que consome os dados da API e os exibe em uma tabela dinâmica com filtros e paginação.

📄 Documentação do processo: [Google Docs](https://docs.google.com/document/d/1o9cLmsYfJeH0-UL6Spf1cMiDNIebFa3NTWBGvk8wGOo/edit?usp=sharing)

📄 Documentação das funções: [Google Docs](https://docs.google.com/document/d/1XPJUXPYPjHPgPcg9WMjFoiFcrOEd6uxkuodSZPrViDQ/edit?usp=sharing)

## 🖥️ Funcionalidades do Frontend

Tabela Dinâmica → exibição dos dados retornados pela API.

Filtros em tempo real → busca por nome, telefone, e-mail e CPF.

Paginação → controle de registros por página, com botões de navegação e opção de ir direto para uma página específica.

Mensagens de erro amigáveis → caso não haja registros ou a API esteja fora do ar.

Atualização Automática → os dados são recarregados a cada 30 segundos, garantindo que as informações exibidas estejam sempre atualizadas.

## ⚙️ Decisões Técnicas

FastAPI foi escolhido pelo desempenho e facilidade de construir APIs modernas e performáticas.

O CORS foi configurado para permitir apenas o frontend hospedado no GitHub Pages e também localhost para testes locais.

O backend foi publicado no Render, que oferece deploy rápido de APIs em containers.

O frontend foi hospedado no GitHub Pages, permitindo distribuição estática gratuita e integração contínua com o repositório.

A tabela no frontend foi feita com JavaScript puro, com suporte a filtros, paginação e atualização automática.

O projeto foi estruturado de forma modular, separando serviços (data_service) e configuração principal (main.py) no backend.

⚠️ Como o Render está no plano gratuito, o servidor pode “hibernar” após algum tempo de inatividade. Nesse caso, preciso religar manualmente o serviço.
👉 Se você estiver testando e a API retornar erro ou carregar infinitamente, me avise para que eu religue o servidor.
