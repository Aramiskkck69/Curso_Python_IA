import gym

enviroement = gym.make("CartPole-v0")
enviroement.reset() #Limpiar el entorno para tomar desiciones

for _ in range(2000): #iteraciones
    enviroement.render() #Pintar acciones
    enviroement.step(enviroement.action_space.sample()) #Tomamos una desicion aleatoria del conjunto de las diponibles

enviroement.close()

