import os
from abc import ABC
from abc import abstractmethod


class BaseSolver(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def solve(self, domain_file: str, problem_path: str, output_path: str):
        """solves a problem given a domain.

        :param domain_file: path to domain file
        :param problem_path: path to problem
        :param output_path: path to output directory
        :return:
        """
        pass

    @staticmethod
    def exec_os_command(cmd: str):
        os.popen(cmd).read()


class FFXSolver(BaseSolver):
    def solve(self, domain_file: str, problem_path: str, output_path: str):
        command = f'./ff -o  {domain_file}  -f {problem_path}| sed -n "/step/,/time/p" > {output_path}'
        self.exec_os_command(command)


class CloudSolver(BaseSolver):
    def solve(self, domain_file: str, problem_path: str, output_path: str):
        cmd = f'exec "$(dirname "$0")"/siw-then-bfsf --domain {domain_file} --problem {problem_path} --output {output_path}'
        self.exec_os_command(cmd)
