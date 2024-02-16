# coding: utf-8
# New TOML-only structure
import json
import os
import tomllib
from cached import CacheMgr

cache = CacheMgr()


class ProblemManager:

    def get_problem_list(self):
        # just list the problems dir and get the names of the problems
        l = os.listdir("./problems.toml/")
        result = []
        l.sort()
        for toml_filename in l:
            i = toml_filename.split(".")[0]
            sdata = self.get_problem_solve_data(i)
            result.append({
                "id": int(i),
                "title": self.get_problem_meta(i)['title'],
                "solved": sdata[0],
                "unsolved": sdata[1]
            })

        result.sort(key=lambda x: x['id'])
        return result

    def get_problem_meta(self, problem_id):
        problem_id = str(problem_id)
        with open("./problems/%s.toml" % (problem_id, ), "rb") as f:
            return tomllib.load(f)

    def get_problem_solve_data(self, problem_id):
        with open("./users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        problem_id = int(problem_id)
        result = [0, 0, {}]
        for ip, solved in data.items():
            solved: int
            if solved >= problem_id:
                result[0] += 1
            else:
                result[1] += 1
            result[2][ip] = solved >= problem_id
        return result

    @cache.cached_deco(5)
    def get_problem_description(self, problem_id: str | int):
        with open("./problems/%s.toml" % (str(problem_id), ), "rb") as f:
            return tomllib.load(f)['descriptions']
