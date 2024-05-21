# Executando o Projeto Teleop Turtlebot

Este projeto permite controlar um robô Turtlebot de forma remota através do teclado e inclui uma funcionalidade de parada de emergência.

## Pré-requisitos

Antes de iniciar, verifique se você tem os seguintes requisitos instalados em seu sistema:

- ROS 2 (Foxy Fitzroy ou superior)
- Python 3
- Pynput (Python library)
- Turtlebot3 ROS 2 Packages

## Instruções de Instalação

1. Instale o ROS 2 em seu sistema, seguindo as instruções fornecidas na [documentação oficial do ROS 2](https://index.ros.org/doc/ros2/Installation/).

2. Instale a biblioteca `pynput` utilizando `pip install pynput`

3. Clone este repositório! `git clone https://github.com/Gabrielle-Cartaxo/Turtlebot3-Teleoperado.git`

## Executando o Projeto

Siga estas etapas para executar o projeto:

1. Abra a pasta desse repositório no seu terminal

2. Compile o código utilizando `colcon build`

3. Inicie o ros 2 com `source install/local_setup.bash`

4. Inicie os nós com o comando: `ros2 launch control_turtlebot3 teleop_launch.py start_client:=true`

5. Use as teclas do teclado para mover o robô (w para frente, s para trás, a para esquerda, d para direita).

6. Para acionar a parada de emergência, pressione a tecla 'q'. Isso irá interromper imediatamente o movimento do robô.

7. Para encerrar o programa, pressione Ctrl+C ou feche o terminal onde o nó `control.py` está sendo executado.

## Vídeo de execução

Acesse o vídeo [aqui!](https://youtu.be/Vg6_H0a8pco)

<iframe width="560" height="315" src="https://youtu.be/Vg6_H0a8pco" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
