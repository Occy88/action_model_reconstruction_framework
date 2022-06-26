import os
import shutil
import uuid
from abc import ABC
from abc import abstractmethod

from parser.ff_to_action import FFToActionParser


class BaseSolver(ABC):

    @classmethod
    def solve_problem_dir(cls, domain_file: str, problem_dir: str, output_dir):
        """
        Solves each problem in a directory and outputs solutions with the same file names into
        a newly specified directory.
        :param domain_file:
        :param problem_dir:
        :param output_dir:
        :return:
        """
        problems = os.listdir(problem_dir)
        for p in problems:
            cls.solve(domain_file, f'{problem_dir}/{p}', f'{output_dir}/{p}')
        cls.post_process_results(problem_dir=problem_dir)

    @classmethod
    @abstractmethod
    def solve(cls, domain_file: str, problem_path: str, output_path: str):
        ...

    @classmethod
    @abstractmethod
    def post_process_results(cls, problem_dir: str):
        pass

    @staticmethod
    def exec_os_command(cmd: str):
        os.popen(cmd).read()  # nosec


class FFXSolver(BaseSolver):
    ff_output_parser: FFToActionParser = FFToActionParser

    @classmethod
    def solve(cls, domain_file: str, problem_path: str, output_path: str):
        ff_path = f'{os.path.dirname(__file__)}/ffx/'
        cmd = f'{ff_path}ff -o  {domain_file}  -f {problem_path}| sed -n "/step/,/time/p" > {output_path}'
        cls.exec_os_command(cmd)

    @classmethod
    def post_process_results(cls, problem_dir: str):
        cls.ff_output_parser.convert_ffx_plan_traces_to_actions(state_dir=problem_dir, output_dir=problem_dir)


class CloudSolver(BaseSolver):
    @classmethod
    def solve(cls, domain_file: str, problem_path: str, output_path: str):
        cloud_solver_dir = f'{os.getcwd()}/opesource/cloud-solver'
        cmd = f'exec "$(dirname "$0")"/siw-then-bfsf --domain {domain_file} --problem {problem_path} --output {output_path}'
        cls.exec_os_command(cmd)
