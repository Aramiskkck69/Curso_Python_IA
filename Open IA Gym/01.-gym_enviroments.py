from gym import envs

env_names = [env.id for env in envs.registry.all()]



f = open ('juegos_gym.txt','w')
for name in sorted(env_names):
        f.write(name +'\n')

f.close()