# 💰 Sistema Bancário em Python

Este é um projeto simples de um sistema bancário desenvolvido em Python como exercício de lógica de programação e controle de fluxo. O sistema permite **depósitos**, **saques** e a **visualização de extrato bancário**, com algumas regras de negócio aplicadas para os saques.

## ✨ Funcionalidades

- 📥 **Depósito**: Permite depositar qualquer valor positivo.
- 💸 **Saque**:
  - Limite de **R$ 500,00 por saque**
  - Máximo de **3 saques diários**
  - Não permite saque com saldo insuficiente
- 📄 **Extrato**:
  - Exibe todos os depósitos e saques realizados
  - Mostra o saldo atual

## 🔒 Regras do Sistema

- O saldo inicia em **R$ 0,00**
- Não é possível realizar saques com valor superior ao saldo disponível
- Saques acima de **R$ 500,00** são bloqueados
- Só é possível fazer **até 3 saques por dia**
- O extrato mostra as operações realizadas na sessão atual

## 🛠 Tecnologias

- Python 3.x

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Adriano-Silva92/desafio-bancario-Dio.git
   cd desafio-bancario-Dio
