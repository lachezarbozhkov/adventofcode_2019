from collections import defaultdict
import fileinput
import re

PATTERN = re.compile(r'(\d+) (\w+)')
MAX = 1_000_000_000_000


def parse(lines):
    rules = {}
    for line in lines:
        srcs, last = {}, None
        for match in PATTERN.finditer(line):
            if last is not None:
                key, n = last
                srcs[key] = n
            last = match.group(2), int(match.group(1))
        key, n = last
        rules[key] = n, srcs
    return rules


def produce(rules, quantity):
    mats = defaultdict(int)
    mats['FUEL'] = quantity
    try:
        while True:
            key, n = next(
                (key, n) for key, n in mats.items() if key != 'ORE' and n > 0)
            m, srcs = rules[key]
            x = (n + m - 1) // m
            mats[key] -= m * x
            for k, v in srcs.items():
                mats[k] += x * v
    except StopIteration as e:
        pass
    return mats['ORE']

def part2(rules):
    good, bad = MAX // produce(rules, 1), None
    while bad is None or good < bad - 1:
        quantity = 2 * good if bad is None else (good + bad) // 2
        ores = produce(rules, quantity)
        if ores < MAX:
            good = quantity
        elif ores > MAX:
            bad = quantity
        else:
            return mid
    return good


lines = """164 ORE => 2 TLJL
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
3 JZWH => 1 TZND""".splitlines()


print(produce(parse(lines), 1))
print(part2(parse(lines)))

