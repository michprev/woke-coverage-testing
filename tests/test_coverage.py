from typing import List

from woke.testing import default_chain
from woke.testing.campaign import Campaign
from woke.testing.decorators import *
from woke.testing.random import *

from pytypes.contracts.FeeCollector import FeeCollector
from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.ConstAddressDeployer import ConstAddressDeployer
from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.test.ERC20MintableBurnable import ERC20MintableBurnable


class Sequence:
    _deployer: ConstAddressDeployer
    _fee_collectors: List[FeeCollector]

    def __init__(self) -> None:
        self._fee_collectors = []

        default_chain.default_account = random_address()

        self._deployer = ConstAddressDeployer.deploy()

    @flow
    def flow_deploy_fee_collector(self):
        salt = random_bytes(32, 32)
        collector = FeeCollector(self._deployer.deploy_(FeeCollector.deployment_code(), salt))
        self._fee_collectors.append(collector)

        name = random_string(0, 32)
        symbol = random_string(3, 3)
        erc20 = ERC20MintableBurnable.deploy(name, symbol, 18)

        collector.init(erc20)


def test_coverage(coverage):
    default_chain.gas_price = 0

    campaign = Campaign(Sequence)
    campaign.run(1000, 50, coverage=coverage)
