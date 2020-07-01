import gym
import sys

argv = []


def run_gym_environment(argv):
    environment = gym.make(argv[1])
    environment.reset()
    for _ in range(int(argv[2])):
        environment.render()
        environment.step(environment.action_space.sample())
    environment.close()
    
#next_state     ->Object
#reward         ->Float
#done           ->Boolean
#info           -> Dctionary

if __name__ == "__main__":
    run_gym_environment(sys.argv)
