# SafeBank IDOR Lab 🚀

Bem-vindo ao laboratório de IDOR (Insecure Direct Object Reference) do SafeBank! Este projeto simula um ambiente bancário para estudo e demonstração de vulnerabilidades do tipo IDOR, com interface moderna e automação total do ambiente.

## ⚡️ Como executar

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repo>
   cd www
   ```
2. **Execute o laboratório:**
   ```bash
   python3 build.py
   ```
   - O script `build.py` cria um ambiente virtual isolado, instala as dependências e inicia o servidor Flask automaticamente.
   - Ao encerrar (Ctrl+C), o ambiente virtual é removido para garantir limpeza e segurança.

3. **Acesse o sistema:**
   - Abra o navegador e acesse: [http://localhost:5000](http://localhost:5000)

## 🛡️ O que o código faz

- **Ambiente Virtual Automático:** O `build.py` garante que todas as dependências sejam instaladas em um ambiente isolado, sem afetar seu sistema.
- **Servidor Flask:** O `app.py` simula um banco digital, com autenticação JWT, dashboard de usuário, páginas institucionais e uma API com vulnerabilidade IDOR.
- **Limpeza Segura:** Ao sair do laboratório, todo o ambiente virtual é removido automaticamente.
- **Didático e Profissional:** Interface moderna, endpoints realistas e documentação clara para uso em treinamentos, CTFs e estudos.

## 🧑‍💻 Usuários de exemplo

| Usuário  | Senha   | Perfil   |
|----------|---------|----------|
| lukao    | 1234    | Cliente  |
| admin    | admin   | Admin/CTF|
| user     | user    | Cliente  |
| guest    | guest   | Visitante|

## 📚 Páginas institucionais
- `/seguranca`: Explica IDOR, LGPD e boas práticas.
- `/sobre`: Informações sobre o SafeBank, missão, visão e valores.

## ⚠️ Aviso de Segurança
> **Este laboratório é apenas para fins educacionais!**
> Não utilize em ambientes de produção ou com dados reais.

---

Feito com 💙 para a comunidade de segurança!
