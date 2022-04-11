# -*- coding: utf-8 -*-
"""Openlab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZleMvBPZnrNuRczie48BkPTMx_tgqnzA
"""
#Instalando bibliotecas
#pip install paho-mqtt

import paho.mqtt.client as mqtt
import pandas as pd
import time
from datetime import datetime
import os
#import sys
#sys.path.append("/scrapy")
#import scrapy as i

# Pegando dado da variavel do arquivo do Robô do site
resposta = i.pegatexto

# Pegando dado do modo de jogo do arquivo do Robô do site
modoJogo = i.mode_element

# Pegando valor do contador
cont = i.cont

print(f"Respostas: {resposta}")
print(f"Modo de jogo: {modoJogo}")
print(f"Contador: {cont}")


user = "grupo1-bancadaB4"
passwd = "L@Bdygy1B4"

Broker = "labdigi.wiseful.com.br"   # Endereco do broker
Port = 80                           # Porta utilizada (firewall da USP exige 80)
KeepAlive = 60                      # Intervalo de timeout (60s)

E = []
S = []

for i in range(7):
    E.append(user+"/E"+str(i))
    S.append(user+"/S"+str(i))

# Quando conectar na rede (Callback de conexao)
def on_connect(client, userdata, flags, rc):

    for topicE in E:
        client.subscribe(topicE, qos=0)
    
    for topicS in S:
        client.subscribe(topicS, qos=0)
    
# Quando receber uma mensagem (Callback de mensagem)
def on_message(client, userdata, msg):
    global dados_pollock_payload
    global occurrence_time
    
    client.newmsg = True    
    client.topic = msg.topic
    client.msg = msg.payload.decode("utf-8")
    
    #if client.msg == "1" and client.topic == user+"/S2":
               



client = mqtt.Client()                      # Criacao do cliente MQTT
client.on_connect = on_connect              # Vinculo do Callback de conexao
client.on_message = on_message              # Vinculo do Callback de mensagem recebida
client.username_pw_set(user, passwd)        # Apenas para coneccao com login/senha
client.connect(Broker, Port, KeepAlive)     # Conexao do cliente ao broker


"""client.loop_start()
time.sleep(1)
client.publish(user+"/led", "1")
time.sleep(1)
client.publish(user+"/led", "0")"""

#Modo de jogo
"""
if modoJogo == 'showDoMilhao':
    while cont <= 16:
        print("PASSANDO NO SHOW DO MILHAO")
        print("Modo: Show do Milhão")
        client.loop_start()
        #Inserindo modo de jogo
        client.publish(user+"/E7", "1")
        #Iniciando o circuito
        print("Iniciando...")
        client.publish(user+"/E2", "1")
        time.sleep(1)
        client.publish(user+"/E2", "0")
        time.sleep(1)

            # Realizando Validacao da resposta
        if resposta == 2:
            print("Acertou")
            client.loop_start()
            time.sleep(1)
            client.publish(user+"/E6", "1")
            time.sleep(1)
            client.publish(user+"/E6", "0")
        else:
            print("Errou")
            client.loop_start()
            time.sleep(1)
            client.publish(user+"/E1", "1")
            time.sleep(1)
            client.publish(user+"/E1", "0")

elif modoJogo == 'highScore':
    while cont <= 20:
        print("PASSANDO NO HIGHSCORE")
        print("Modo: HighScore")
        client.loop_start()
        time.sleep(1)
        #Inserindo modo de jogo
        client.publish(user+"/E7", "0")
        #Iniciando o circuito
        print("Iniciando...")
        client.publish(user+"/E2", "1")
        time.sleep(1)
        client.publish(user+"/E2", "0")
        time.sleep(1)

            # Realizando Validacao da resposta
        if resposta == 2:
            print("Acertou")
            client.loop_start()
            time.sleep(1)
            client.publish(user+"/E6", "1")
            time.sleep(1)
            client.publish(user+"/E6", "0")
        else:
            print("Errou")
            client.loop_start()
            time.sleep(1)
            client.publish(user+"/E1", "1")
            time.sleep(1)
            client.publish(user+"/E1", "0")

"""
   


  
"""
def aaa():

    client = mqtt.Client()                      # Criacao do cliente MQTT
    client.on_connect = on_connect              # Vinculo do Callback de conexao
    client.on_message = on_message              # Vinculo do Callback de mensagem recebida
    client.username_pw_set(user, passwd)        # Apenas para coneccao com login/senha
    client.connect(Broker, Port, KeepAlive)  
    


    if alternativa == "A":
        client.publish(user+"/E1", "1")
        time.sleep(1)
        client.publish(user+"/E1", "0")
"""
    
  
  
  
  
  
  
  