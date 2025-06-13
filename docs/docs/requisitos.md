---
sidebar_position: 2
title : "Requsitos do Projeto"
---

# Detalhes Técnicos do Drone Multiespectral Autônomo

## Estrutura Física

Tipo de Drone: Modular (quadricóptero ou hexacóptero, dependendo da aplicação).

Materiais: Fibra de carbono para braços e suportes, alumínio aeronáutico para estrutura central.

Montagem: Sistema de encaixe e parafusamento para facilitar manutenção e upgrades.

Proteções: Carenagens contra intempéries e choque.

## Sensoriamento

Câmera Multiespectral: RGB + Infravermelho (IR) + NDVI.

Sensores de Navegação:

GPS + RTK para posicionamento preciso.

LIDAR para mapeamento de obstáculos e altimetria.

IMU para orientação inercial (giroscópio, acelerômetro, magnetômetro).

Ultrassônicos para proximidade em ambientes internos.

## Sistema de Controle

Placa Controladora: Pixhawk (compatível com PX4 e ArduPilot).

Firmware: ArduPilot (preferencial) ou PX4, com suporte a voo autônomo e rotas pré-definidas.

Modos de Operação:

Manual (via rádio controle).

Semi-autônomo (waypoints definidos).

Totalmente autônomo (decisão baseada em dados processados).

Software Embarcado

Processamento Local: Raspberry Pi ou Jetson Nano como companion computer.

Linguagens:

Python (controle de missão, visão computacional, IA leve).

C++ (firmware, tempo real).

Frameworks e Bibliotecas:

OpenCV (processamento de imagem).

DroneKit ou MAVSDK (interface de voo).

ROS (Robot Operating System) para integração modular.

Comunicações

Telemetria: Rádio 915 MHz para comunicação com estação base.

Streaming: Wi-Fi para envio de imagens ao vivo.

Backup de Comunicação: Módulo 4G/LTE para redundância em locais remotos.

Energia

Bateria: LiPo 6S com sistema de gerenciamento inteligente (BMS).

Autonomia Esperada: 25 a 40 minutos dependendo da carga útil.

Capacidade de Decisão Autônoma

Entrada Inicial: Mapeamento manual ou waypoint.

Processamento de Dados: Extração de padrões geográficos e estruturais.

Execução de Tarefa: Escolha de rota e sensores com base no tipo de operação necessário.

Expansibilidade

Suporte a novos sensores (termográficos, gás, ambientais).

Integração com servidores externos para processamento em nuvem.

Atualizações OTA (Over-the-Air) do sistema embarcado.

