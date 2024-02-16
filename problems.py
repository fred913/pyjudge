# coding: utf-8
# legacy JSON&MD structure
import os
import json
from threading import Lock
from typing import Hashable, TypedDict
from cached import CacheMgr

cache = CacheMgr()


class LockPool:

    def __init__(self) -> None:
        self.locks = {}

    def getlock(self, id_: Hashable):
        try:
            return self.locks[id_]

        except KeyError:
            self.locks[id_] = Lock()
            return self.locks[id_]


lpool = LockPool()


class ProblemMetaDict(TypedDict):
    title: str
    cases: list[list[str]]
    timeout: int
    descriptions: str


class ProblemManager:

    def get_problem_list(self):
        # just list the problems dir and get the names of the problems
        l = os.listdir("./problems/")
        result = []
        for i in l:
            sdata = self.get_problem_solve_data(i)
            result.append({
                "id": int(i),
                "title": self.get_problem_meta(i)['title'],
                "solved": sdata[0],
                "unsolved": sdata[1]
            })

        result.sort(key=lambda x: x['id'])  # type: ignore
        return result

    def get_problem_meta(self, problem_id: str | int) -> ProblemMetaDict:
        problem_id = int(problem_id)
        with lpool.getlock((problem_id, 0)):
            with open("./problems/%s/info.json" % (problem_id, ),
                      "r",
                      encoding="utf-8") as f:
                return json.load(f)

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
    def get_problem_description(self, problem_id):
        with lpool.getlock((problem_id, 1)):
            with open("./problems/%s/description.md" % (str(problem_id), ),
                      "r",
                      encoding="utf-8") as f:
                return f.read()
