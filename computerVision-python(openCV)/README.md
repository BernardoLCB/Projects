# 🛬 Detecção de Base de Pouso para Drones
Um sistema em Python utilizando OpenCV para detectar formas geométricas específicas (quadrados, círculos e cruzes) em imagens ou via câmera, com suporte à filtragem de cores (amarelo e azul). O principal objetivo é integrar essa funcionalidade a um drone, permitindo a identificação precisa de bases de pouso.

- Base de pouso 1: https://github.com/BernardoLCB/Projects/blob/main/computerVision-python(openCV)/inputs/chosen/Base_comum.png
  
- Base de pouso 2: https://github.com/BernardoLCB/Projects/blob/main/computerVision-python(openCV)/inputs/chosen/Base_de_Takeoff.png

## 📌 Descrição
Este projeto utiliza processamento de imagem e visão computacional para detectar padrões específicos que representam uma base de pouso. Ele pode ser usado tanto com imagens estáticas quanto com transmissões ao vivo de uma câmera.

## 🛠️ Funcionalidades


- **Detecção de Formas Geométricas**: Detecta quadrados, círculos e cruzes em imagens.
  
- **Filtragem de Cores**: Suporte para filtrar as cores amarelo e azul nas imagens.
  
- **Integração com Drone**: Permite que a detecção de formas seja usada para guiar o drone em direção às bases de pouso.
  
- **Trabalho com Imagens Estáticas ou Ao Vivo**: Permite trabalhar tanto com imagens estáticas (carregadas do disco) quanto com transmissões ao vivo (via câmera), proporcionando flexibilidade no uso do sistema em diferentes cenários.
  
- **Sliders**: Permitem a alteração em tempo real de diversos parâmetros dentro do programa, como:
    - Aplicar filtros de suavização na imagem.
    - Aplicar filtros de morfologia na imagem.
    - Ajustar a dimensão da matriz do elemento estruturante (referente aos filtros de morfologia).
    - Ajustar o brilho da imagem.
    - Aplicar limiarização (threshold) na imagem.
    - Filtrar para detectar somente a cor amarela ou azul na imagem.
    - Controlar a detecção das formas com base em um valor de área.
 

## 📖 História do Projeto

O presente sistema foi desenvolvido como parte do Projeto Prático de Controle e Sistemas Embarcados, no contexto do processo de treinamento para ingressar na Equipe de Robótica Aérea (EDRA) da Universidade de Brasília (UnB). O objetivo principal é adquirir a experiência necessária e se preparar para atuar na área de Controle e Sistemas Embarcados (C&SE), buscando a vaga e a oportunidade de contribuir com inovações e soluções tecnológicas no campo.

A escolha de trabalhar com o tema de Visão Computacional foi motivada pela relevância crescente dessa área na atualidade, que tem se tornado fundamental em diversas aplicações, desde a automação industrial até sistemas de segurança, veículos autônomos, e drones. Embora o projeto não integre diretamente inteligência artificial avançada, como o YOLO (You Only Look Once), ele se baseia em técnicas de processamento de imagem e análise visual, com o objetivo de detectar, interpretar e responder a informações visuais de maneira eficiente.


## 🗂️ Fontes de Pesquisa
Este projeto foi desenvolvido com base em diversas fontes de pesquisa, sendo principalmente fundamentado na leitura da documentação oficial da biblioteca OpenCV, além de fóruns de ajuda e vídeos tutoriais disponíveis no YouTube. Essas fontes foram essenciais para adquirir o conhecimento necessário e garantir a aplicação adequada das ferramentas e técnicas utilizadas no desenvolvimento do sistema.

## 📋 Requisitos

- Python 3.7+
- OpenCV 4.11.0
- NumPy 2.2.3


👉 Download [Python](https://www.python.org/downloads/)
```bash
pip install numpy  # Para instalar o NumPy
pip install opencv-python  # Para instalar o OpenCV
```



## Como Baixar Este Repositório

### Clonar usando Git
Se você tem o Git instalado, pode clonar este repositório com o seguinte comando:

```bash 
git clone https://github.com/BernardoLCB/Projects.git 
```

## 📧 Contato
Se tiver alguma dúvida ou sugestão, entre em contato via email: bernardoleinig@gmail.com.
