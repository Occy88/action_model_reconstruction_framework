import os
import pathlib
from abc import abstractmethod


class DataGenerator:
    @classmethod
    @abstractmethod
    def generate_data(cls, *args, **kwargs):
        ...


class GridWorldGenerator(DataGenerator):

    @staticmethod
    def generate_data(output_dir: str,
                      no_states: int = 100,
                      x_scale: int = 5,
                      y_scale: int = 5,
                      keys: int = 10,
                      num_key_lock_variations: int = 5,
                      locks=10, p_key_in_goal: int = 100):
        pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

        path = os.getcwd()
        os.chdir(f'{os.path.dirname(__file__)}')
        for i in range(0, no_states):
            print("generating states: ", i, "/", no_states)
            cmd = f"./grid " \
                  f"-x {x_scale} " \
                  f"-y {y_scale} " \
                  f"-t {num_key_lock_variations} " \
                  f"-k {keys} " \
                  f"-l {locks} " \
                  f"-p {p_key_in_goal} " \
                  f"> {output_dir}/state_{i}"
            os.popen(cmd).read()  # nosec
        os.chdir(path)
