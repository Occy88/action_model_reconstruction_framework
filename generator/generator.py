import os

gen_dir = "./generator/"


class Generator:
    def __init__(self):
        pass

    def gen_problem_states(self, problem, no_states, flags: str):
        os.chdir(gen_dir + problem)
        os.popen("rm -rf states; mkdir states")  # nosec
        for i in range(0, no_states):
            print("generating states: ", i, "/", no_states)
            # time.sleep(0.2)
            cmd = "./" + problem + " " + flags + " > states/state_" + str(i)
            os.popen(cmd).read()  # nosec
        os.chdir("../../")
