import pytest
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector

packnames = ("tidyverse")

utils = rpackages.importr("utils")
utils.chooseCRANmirror(ind=12)
names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
if len(names_to_install) > 0:
    utils.install_packages(StrVector(names_to_install))


robjects.r["source"]("2024/03/main.R")

part1 = robjects.r["part1"]
part2 = robjects.r["part2"]
input = robjects.r["input"]


@pytest.mark.benchmark
def test_3p1_R():
    assert part1(input)[0] == 159833790


@pytest.mark.benchmark
def test_3p2_R():
    assert part2(input)[0] == 89349241


@pytest.mark.benchmark
def test_3_R():
    assert part1(input)[0] == 159833790
    assert part2(input)[0] == 89349241
