import json
import os

from typing import List, Tuple


# definition of an action
class FFToActionParser:
    """
    Parses oiutput (modified with sed command) from ff
    to a list of actions (plan traces that can be interpreted for
    ML.
    """

    def _clean(self, text: str):
        """
        removes step and final line from:
        step    0: MOVE-B-TO-T B2 B1
        1: MOVE-B-TO-T B3 B10
        ....
        10: MOVE-T-TO-B B6 B3


        time spent:    0.00 seconds instantiating 1200 easy, 0 hard action templates

        """
        # for now ignore this, take care of parsing properly in parse_line...
        return text

    def _parse_line(self, line: str) -> Tuple[str, List[str]]:
        arr = line.split(":")
        if len(arr) <= 1:
            raise ValueError(f'Unexpected arg: "{line}" when parsing FF output to action_traces.')

        if "step" in arr[0] or int(arr[0]):
            text = arr[1].strip().split(" ")
            return text[0], text[1:]

    def _parse(self, text: str) -> List[Tuple[str, List[str]]]:
        """
        returns list of actions.
        """
        text = self._clean_text(text)
        trace = [self._parse_line(line) for line in text.split('\n')]
        return trace

    def convert_ffx_plan_traces_to_actions(self, state_dir: str, output_dir: str):
        """
        writes output to json saves each output into a new state file.
        """
        for name in os.listdir(state_dir):
            f = open(f'{state_dir}/{name}')
            text = f.read()
            f.close()
            parsed = self._parse(text)
            f = open(f"{output_dir}/{name}", "w+")
            f.write(json.dumps(parsed))
            f.close()
