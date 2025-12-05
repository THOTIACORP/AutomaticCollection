**Módulo de Coleta Automática de Imagens Extraorais com câmeras reutilizáveis**

* fluxo técnico
* objetivos clínicos
* pipeline com **align-face**
* integração com **fer.py**
* padronização fotográfica
* uso para prontuários odontológicos

Componente Open Source do Ecossistema Escudo Orofacial

Este módulo foi desenvolvido para permitir a coleta automática, padronizada e reprodutível de imagens extraorais, utilizando câmeras reutilizáveis, webcams convencionais ou sistemas de captura conectados. Seu objetivo é facilitar a documentação clínica em odontologia, harmonização orofacial, estetica e pesquisa científica.

O módulo combina:

- detecção facial em tempo real
- alinhamento automático (align-face)
- reconhecimento de expressões com fer.py
- validação geométrica da pose (frontal / perfil direito / perfil esquerdo)
- captura automatizada sem intervenção humana
- reutilização de setups fotográficos existentes (clínicas, hospitais, universidades, SUS)

Ele nasce como uma iniciativa open source que reúne inovação tecnológica e impacto social através da parceria entre:
**IGEos, Fundação Banco do Brasil, UFPEL, UFR, UNEMAT**

Criando um padrão nacional de documentação orofacial acessível, científica e interoperável.

🎯 1. Objetivos Clínicos

✔️ Criar um protocolo padronizado nacional de documentação facial extraoral
✔️ Reduzir erros de rotação, inclinação e distância
✔️ Padronizar fotografias clínicas para:

prontuários odontológicos
harmonização orofacial
perícias judiciais
ensino universitário
pesquisa científica


✔️ Usar equipamentos de baixo custo e câmeras reutilizáveis, promovendo acesso em unidades públicas de saúde
✔️ Permitir comparações temporais confiáveis (antes / depois / acompanhamento clínico)

🧠 2. Fluxo Técnico Completo
flowchart TD
A[📷 Câmera Reutilizável / Webcam] --> B[🔍 Detecção de Face (dlib/mediapipe)]
B --> C[📐 Align-Face (correção de rotação, pitch, yaw)]
C --> D{Modo solicitado?}

D -->|Neutro| E[🎯 Avaliar posição: frontal / dir / esq]
E --> F{Posição válida?}
F -->|Sim| G[📸 Captura Automática Neutra]
F -->|Não| A

D -->|Expressão| H[😃 Análise da expressão com fer.py]
H --> I{Expressão corresponde ao alvo?}
I -->|Sim| J[📸 Captura Automática da Expressão]
I -->|Não| A

📐 3. Pipeline de Posição — Align Face

O align-face corrige automaticamente:
rotação lateral (yaw)
inclinação vertical (pitch)
rotação axial (roll)
centralização
distância padrão da câmera

Parâmetros usados para considerar a imagem válida:
Frontal neutra
roll < 3°
pitch ~ 0°
yaw < 5°
distância entre olhos dentro da faixa ideal
simetria entre os lados da face

Perfil direito
olho direito 100% visível
o olho esquerdo parcialmente ou não visível
nariz projetado
queixo alinhado ao plano

Perfil esquerdo
mesma lógica espelhada

Se todos os parâmetros forem aprovados → captura automática (sem clique do usuário).

😃 4. Pipeline de Expressões — fer.py

Usamos o FER (Facial Expression Recognition) para reconhecer automaticamente:

neutral
happy (sorriso)
surprise
angry
sad
disgust
fear

Regra de captura:
expressão detectada ≥ 3 frames consecutivos
confiança > 0.85
rosto alinhado
iluminação aceitável

🖼️ 5. Padronização Fotográfica Clínica
Parâmetros adotados:

✔️ fundo neutro
✔️ distância fixa paciente–câmera (80–120 cm)
✔️ iluminação frontal difusa
✔️ alinhamento pelo tragus–pupila
✔️ ISO e exposição automáticos
✔️ captura automática sem interação humana

Conjunto final de imagens geradas:
frontal_neutra.jpg
perfil_direito.jpg
perfil_esquerdo.jpg
expressao_sorriso.jpg
expressao_surpresa.jpg
expressao_neutra.jpg
expressao_tristeza.jpg

🏛️ 6. Uso em Prontuários Odontológicos e Médicos

As imagens seguem padrões aceitos em:

prontuários clínicos
documentação de ortodontia
harmonização orofacial
avaliações faciais
perícias judiciais
programas de ensino em saúde
teleatendimento
pesquisa científica


Cada imagem é salva com:
timestamp
parâmetros biométricos
JSON de metadados
condição da captura (pose, expressão, alinhamento)

🧩 7. Por que Câmeras Reutilizáveis?

Este módulo é desenhado para equipamentos já existentes, como:

câmeras USB antigas
webcams reutilizadas de laboratórios
câmeras de consultórios
sistemas de captura de universidades

Isso reduz custos → ideal para:

clínicas públicas
centros de ensino
hubs de inovação
projetos sociais

🌍 8. Open Source e Impacto Social (IGEos, Fundação BB, UFPEL, UFR, UNEMAT)

Este módulo nasce dentro de um ecossistema de inovação aberta, com objetivo de criar um padrão brasileiro de documentação facial acessível e auditável.

🤝 Parcerias envolvidas:
IGEos — Instituto de Gestão e Estratégia e Organização Social Sustentáveis
o I-GEOS tem se dedicado a implementar projetos e programas que fomentam o empreendedorismo inovador, a justiça social, e a geração de emprego e renda, sempre alinhado às necessidades e aspirações da comunidade
Fornece governança, padronização e direcionamento - Consultória Científica

💛 Fundação Banco do Brasil
Apoia iniciativas de tecnologia social e inovação para impacto nacional
Premiações Subvenções 

🏛️ UFPEL — Universidade Federal de Pelotas
Contribui com expertise científica em:
análise facial
pesquisa aplicada

🏥 UFR — Universidade Federal de Rondonópolis
Colabora com validação de softwares 

🎓 UNEMAT — Universidade do Estado de Mato Grosso
Apoia pesquisa, extensão e uso comunitário do sistema

🚀 9. Objetivo do Open Source
Criar um padrão nacional livre e auditável para documentação facial extraoral:

✔️ reduzir desigualdades tecnológicas
✔️ permitir uso em clínicas privadas e públicas
✔️ incorporar em plataformas SUS
✔️ permitir auditoria científica
✔️ interoperar com prontuários eletrônicos

📦 10. Como executar
pip install opencv-python dlib fer numpy
python auto_capture.py