import os
from abc import ABC
from abc import abstractmethod


class BaseSolver(ABC):

    @classmethod
    def solve_problem_dir(cls, domain_file: str, problem_dir: str, output_dir):
        """
        Solves each problem in a directory and outputs solutions with the same file names into
        a newly specified directory.
        :param domain:
        :param problem_dir:
        :param output_dir:
        :return:
        """
        problems = os.listdir(problem_dir)
        for p in problems:
            cls.solve(domain_file, f'{problem_dir}/{p}', f'{output_dir}/{p}')

    @classmethod
    @abstractmethod
    def solve(cls, domain_file: str, problem_path: str, output_path: str):
        ...

    @staticmethod
    def exec_os_command(cmd: str):
        os.popen(cmd).read()  # nosec


class FFXSolver(BaseSolver):
    @classmethod
    def solve(cls, domain_file: str, problem_path: str, output_path: str):
        ff_path = f'{os.path.dirname(__file__)}/ffx/'
        cmd = f'{ff_path}ff -o  {domain_file}  -f {problem_path}| sed -n "/step/,/time/p" > {output_path}'
        cls.exec_os_command(cmd)


class CloudSolver(BaseSolver):
    @classmethod
    def solve(cls, domain_file: str, problem_path: str, output_path: str):
        cloud_solver_dir = f'{os.getcwd()}/opesource/cloud-solver'
        cmd = f'exec "$(dirname "$0")"/siw-then-bfsf --domain {domain_file} --problem {problem_path} --output {output_path}'
        cls.exec_os_command(cmd)
