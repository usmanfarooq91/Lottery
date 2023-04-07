from scripts.helpful_scripts import (
    get_account,
    get_contract,
    start_lottery,
    enter_lottery,
    end_lottery,
)
from brownie import config, network, Lottery


def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("varify", False),
    )
    print("Lottry deployed!!!")
    return lottery


def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
