from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVOIRONMENTS,
    fund_with_link,
    get_account,
)
from brownie import network, accounts
import pytest
from scripts.deploy_lottery import deploy_lottery
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVOIRONMENTS:
        pytest.skip()
    account = get_account()
    lottery = deploy_lottery()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    fund_with_link(lottery)
    tx = lottery.endLottery({"from": account})
    print("Wait started....")
    time.sleep(120)
    print("Wait ended....")
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
