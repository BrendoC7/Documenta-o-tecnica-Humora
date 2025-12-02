# 📘 **HUMORA – Aplicativo de Suporte Emocional com IA**
### *Chatbot emocional inteligente para bem-estar, acolhimento e produtividade*

---

## 🎯 **Descrição do Projeto**

O **HUMORA** é um aplicativo mobile desenvolvido em **Flutter**, com backend em **Flask/Python**, criado para oferecer **suporte emocional rápido, acessível e humanizado** através de um chatbot inteligente alimentado pela **IA Google Gemini**.

O projeto surgiu da necessidade de um espaço seguro, gratuito e prático para:

- desabafar  
- organizar emoções  
- melhorar produtividade  
- ter conversas acolhedoras com IA  
- criar hábitos saudáveis  

Tudo dentro de uma interface leve, amigável e cheia de personalidade — com elementos visuais inspirados em humor, nuvens e mascotes ilustrados.

---

## 💡 **Motivação e Justificativa**

O crescente aumento de estresse, ansiedade e sobrecarga emocional reforça a necessidade de ferramentas acessíveis e eficazes. O HUMORA vem como resposta a:

✔ Falta de acesso rápido a apoio emocional  
✔ Aplicativos caros e pouco humanizados  
✔ Chatbots confusos e com baixa precisão  
✔ Falta de integração entre produtividade e saúde mental  
✔ Necessidade de um espaço seguro e gratuito  

### **Por que Google Gemini?**

- 100% gratuito  
- API simples e moderna  
- Excelente performance em linguagem natural  
- Ideal para chatbots emocionais  
- Reduz custos e complexidade no TCC

---

## 🧠 **Principais Funcionalidades**

- 🤖 Chatbot emocional inteligente (Google Gemini)
- 🗨️ Sistema de chat com balões personalizados
- 🌤️ Interface acolhedora e ilustrada
- 🧩 Hacks de produtividade integrados
- 🎮 Tela de introdução gamificada
- 🔌 Backend Flask preparado para expansão (histórico, autenticação etc.)
- 📱 Design responsivo, intuitivo e leve

---

## 🛠️ **Metodologia de Desenvolvimento**

### **SCRUM**

- **Sprint Planning:** definição de funcionalidades (chat, UI, backend)  
- **Sprints:** desenvolvimento modular e incremental  
- **Daily Meetings:** revisão de progresso entre membros  
- **Sprint Review:** testes no emulador e ajustes  

### **KANBAN**

Quadro utilizado para organizar tarefas:

- **TO DO:** telas, API, fluxos  
- **DOING:** código em desenvolvimento  
- **TESTES:** funcionalidades validadas  
- **DONE:** entregas finalizadas  

### **Trello**

Usado para:

- gestão visual  
- distribuição de tarefas  
- registro de bugs  
- controle de prazos  

---

## 🧰 **Tecnologias e Ferramentas**

| Stack | Descrição |
|------|-----------|
| **Flutter / Dart** | Desenvolvimento mobile |
| **Python / Flask** | Backend, API e integração |
| **Google Gemini API** | IA para o chatbot |
| **VS Code** | IDE principal |
| **Figma** | Prototipação UI |
| **Canva** | Artes e elementos gráficos |
| **Miro** | Mapa mental inicial |
| **GitHub** | Versionamento |

---

## 📱 **Estrutura de Pastas (Flutter)**# Documenta-o-tecnica-Humora
lib/
├── main.dart

├── screens/

│   ├── intro_screen.dart

│   ├── chat_screen.dart

│   ├── produtos_screen.dart

│   └── loading_screen.dart

├── widgets/

│   ├── custom_button.dart

│   ├── chat_bubble.dart

│   └── humora_cloud.dart

├── models/

│   └── message_model.dart

├── services/

│   └── gemini_service.dart

└── utils/

  └── app_colors.dart
    

## 🤖 **Integração com o Google Gemini**

A classe `GeminiService` realiza:

1. Envio da mensagem do usuário à API  
2. Recebimento e tratamento da resposta  
3. Exibição no chat com estilização própria  

Esse fluxo garante diálogos mais humanos, positivos e éticos — essenciais para suporte emocional.

---

## 🎯 **Resultado Final Esperado**

O HUMORA deve entregar:

- Chat emocional funcional  
- Respostas motivacionais e acolhedoras  
- Hacks e rotinas de produtividade  
- Interface totalmente responsiva  
- Backend preparado para futuras expansões:
  - registro de humor  
  - histórico de conversas  
  - autenticação  
  - sistema de progresso  

---

## 🌍 **Impacto do Projeto**

O HUMORA contribui para:

✨ Saúde mental preventiva  
✨ Acessibilidade emocional gratuita  
✨ Apoio rápido e humanizado  
✨ Melhor organização pessoal  
✨ Desenvolvimento de IA ética e útil  

E pode ser expandido para:

- plataformas educacionais  
- programas institucionais de apoio emocional  
- soluções corporativas  
- iniciativas de bem-estar  

---

## 🧩 **Problemas Resolvidos pelo HUMORA**

| Problema | Solução |
|---------|---------|
| Falta de espaço seguro para desabafar | Chatbot acolhedor com IA |
| Dificuldade de gerenciar emoções | Reflexões e exercícios emocionais |
| Baixa produtividade | Hacks simples e aplicáveis |
| Apps caros de IA | Integração com Google Gemini (gratuito) |
| Baixa acessibilidade | App leve, gratuito e intuitivo |

---

## 🏁 **Conclusão Geral**

O **HUMORA** é um projeto:

✔ Tecnologicamente viável  
✔ Socialmente relevante  
✔ Inovador  
✔ Bem documentado  
✔ Adequado academicamente para TCC  

Ele integra de forma harmoniosa:

- Flutter  
- Flask  
- IA (Gemini)  
- Design emocional  
- Produtividade  
- Experiência do usuário  

Um aplicativo moderno, útil e com impacto real na vida das pessoas.
