import pytest
import rpy2
import rpy2.robjects as robjects

print(rpy2.__version__)
print(rpy2.__path__)


robjects.r['source']("2024/03/main.R")

part1 = robjects.r['part1']
part2 = robjects.r['part2']
input = robjects.r['input']

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
