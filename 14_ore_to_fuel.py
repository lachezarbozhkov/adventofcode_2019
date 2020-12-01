from collections import defaultdict
from math import ceil 
import re


class Solution():
    def __init__(self, solution, qty, ingredients):
        self.solution = solution
        self.qty = qty
        self.ingredients = ingredients

    def __hash__(self):
        return hash(self.solution)
        
    def __repr__(self):
        return f"{self.qty} {self.solution} <= {self.ingredients}"

def parse(line):
    ingredients = re.findall(r"(\d+) (\w+)", line)
    ingredients = [(int(q), e) for q, e in ingredients]
    qty, sol = ingredients.pop(-1)
    return sol, Solution(sol, qty, ingredients)

def calc(el_name, qty):
    solution = recept[el_name]

    qty -= surplus[el_name]
    surplus[el_name] = 0

    qty = qty / solution.qty
    ceil_qty = ceil(qty)
    if ceil_qty != qty:
        surplus[el_name] = (ceil_qty - qty) * solution.qty

    qty = ceil_qty
    total = 0
    for q, el in solution.ingredients:
        if el == "ORE":
            return q * qty
        else:
            res = calc(el, q * qty)
            total += res
    return total


recept = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

surplus = defaultdict(int)
lines = recept.splitlines()
fuel_line = [l for l in lines if "FUEL" in l][0]
recept = dict(parse(line) for line in lines)
assert(calc("FUEL", 1) == 165)


recept = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

surplus = defaultdict(int)
lines = recept.splitlines()
fuel_line = [l for l in lines if "FUEL" in l][0]
recept = dict(parse(line) for line in lines)
assert(calc("FUEL", 1) == 13312)

recept = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""

surplus = defaultdict(int)
lines = recept.splitlines()
fuel_line = [l for l in lines if "FUEL" in l][0]
recept = dict(parse(line) for line in lines)
assert(calc("FUEL", 1) == 2210736)


recept = """164 ORE => 2 TLJL
2 VKMKW => 4 DTCB
2 VKMKW, 16 ZKMXZ, 2 TSVN => 3 TSVQX
2 NFJKN, 2 LMVCD, 5 DSQLK => 1 RNRPB
3 NFJKN, 3 TSVQX, 6 VKMKW => 7 FBFQZ
7 ZKMXZ, 1 PVQLR => 4 MBWVZ
3 SHMGH => 4 ZKMXZ
2 MSZWL => 4 QSDC
3 DGFK => 9 TSVN
21 DTCB, 1 DSQLK => 8 DGDGS
1 DGFK, 1 SXNZP, 1 GCHL => 9 JZWH
1 DSQLK, 4 WFDK, 1 BVSL, 1 TZND, 15 HVPMK, 1 NSKX => 3 DSFDZ
1 ZDVCH, 2 PVQLR, 7 VLNX, 4 JTZM, 1 MVLHV, 1 RDBR, 11 MBWVZ => 7 ZTXQ
9 JZWH, 4 BVSL, 2 NFJKN, 26 LMVCD, 3 MKFDR, 2 TGMNG, 1 NTMRX, 12 DGDGS => 4 PBRZF
25 RNRPB => 6 MKFDR
27 ZKMXZ, 4 NFJKN, 1 DTCB => 5 RDBR
2 ZXTQ, 13 KHRFD => 7 JQJGR
3 WFDVM, 18 QSLKV => 5 NSBN
2 ZXTQ, 6 NTMRX => 4 WFDK
1 VKMKW, 14 TSVQX, 10 ZKMXZ => 6 NFJKN
1 NVDL, 1 ZKMXZ, 9 NSKX => 5 ZDVCH
7 QSDC, 1 BVSL => 4 GCHL
1 QSLKV, 13 XRBKF => 5 NTMRX
11 GDPLN => 8 KHRFD
15 VCJSD => 7 LSLP
4 PCHC, 1 SXNZP, 1 JQJGR => 9 KPBPL
18 TGMNG => 4 HVPMK
1 XRBKF, 26 LVLV => 6 WFDVM
9 VCJSD, 14 SXNZP => 4 TGMNG
22 WFDK, 20 FBFQZ => 6 LHJBH
195 ORE => 7 SHMGH
2 VCJSD, 1 XRBKF => 8 QSLKV
8 ZTXNJ, 4 TLJL => 2 MSZWL
2 LMVCD, 9 PVQLR => 4 NSKX
2 TLJL, 1 GJDPC, 8 ZXTQ => 8 PCHC
6 NSBN, 4 JVJV => 9 ZCDZ
155 ORE => 1 GDPLN
1 GDPLN => 4 VKMKW
1 KPBPL => 8 LVLV
30 NSBN, 20 MVLHV => 1 JVJV
1 LVLV => 1 DGFK
7 TSVQX => 6 LMVCD
7 TLJL, 16 MSZWL, 5 KHRFD => 2 ZXTQ
55 MBWVZ, 61 KHRFD, 16 DSFDZ, 40 LHJBH, 6 ZTXQ, 28 JZWH, 1 PBRZF => 1 FUEL
5 JQJGR, 20 VCJSD => 5 MVLHV
1 SHMGH, 1 ZTXNJ => 4 GJDPC
3 XRBKF, 9 QSLKV, 2 WFDK => 5 JTZM
5 GJDPC => 6 VCJSD
1 GJDPC, 7 XRBKF => 4 PVQLR
11 BVSL => 6 SXNZP
104 ORE => 3 ZTXNJ
3 JZWH, 9 HVPMK, 2 GCHL => 6 VLNX
1 LSLP => 6 XRBKF
1 TLJL => 5 BVSL
5 HVPMK => 9 DSQLK
6 FBFQZ, 22 PVQLR, 4 ZCDZ => 1 NVDL
3 JZWH => 1 TZND"""

surplus = defaultdict(int)
lines = recept.splitlines()
fuel_line = [l for l in lines if "FUEL" in l][0]
recept = dict(parse(line) for line in lines)
print(calc("FUEL", 1))
