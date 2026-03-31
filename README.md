<div align="center">
  
# 🚀 Mini Sistema de Gestão de Tarefas
**Um projeto de portfólio focado em performance, lógica e design fora da curva.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

</div>

---

## 💡 Sobre o Projeto
Este Mini Sistema de Gestão de Tarefas foi desenvolvido como um projeto de aprendizado prático e intensivo. O objetivo principal é consolidar conhecimentos em **Backend com Python**, **manipulação de banco de dados relacional (CRUD)** e construção de uma **interface Web moderna e responsiva**.

Fugindo do básico, a aplicação conta com um design exclusivo em *Dark Mode*, categorização inteligente e sistema de prioridades, refletindo um padrão de código limpo, variáveis padronizadas em português e foco absoluto em usabilidade.

---

## ⚡ Funcionalidades (Features)
- **Criação de Tarefas (Create):** Formulário interativo para registrar novas tarefas com título, descrição, categoria, prioridade e data limite.
- **Leitura Dinâmica (Read):** Listagem automática das tarefas ordenadas por status de conclusão e proximidade do prazo.
- **Atualização de Status (Update):** Sistema de marcação de conclusão com um clique, aplicando feedback visual instantâneo (texto riscado e opacidade).
- **Remoção Segura (Delete):** Exclusão permanente de registros direto do banco de dados.
- **Categorização Visual:** Etiquetas dinâmicas para classificar demandas (Desenvolvimento, Estudos, Pessoal, Projetos).
- **UI/UX Premium:** Interface moderna com transições suaves, sombras dinâmicas e paleta de cores focada em conforto visual.

---

## 🔄 Fluxo de Funcionamento da Aplicação

O diagrama abaixo ilustra a arquitetura simples, porém robusta, da comunicação entre o Cliente (Frontend), o Servidor (Flask) e o Banco de Dados (SQLite):

```mermaid
graph TD
    A[🧑 Usuário] -->|Interage com a Interface| B(Interface Web - HTML/CSS)
    B -->|Envia/Solicita Dados| C{Rotas Flask - app.py}
    
    C -->|GET / | D[(Leitura - SQLite)]
    C -->|POST /adicionar| E[(Inserção - SQLite)]
    C -->|GET /concluir| F[(Atualização - SQLite)]
    C -->|GET /excluir| G[(Deleção - SQLite)]
    
    D --> H[Renderiza index.html atualizado]
    E --> H
    F --> H
    G --> H
    
    H -->|Resposta| B
