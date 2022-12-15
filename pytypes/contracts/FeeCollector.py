from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.core import Contract, Library, Address, Wei, Account, ChainInterface
from woke.testing.internal import TransactionRevertedError
from woke.testing.transactions import LegacyTransaction

from enum import IntEnum
from woke.testing.pytypes_generator import RequestType

from pytypes.openzeppelin.contracts.token.ERC20.IERC20 import IERC20
from pytypes.openzeppelin.contracts.proxy.utils.Initializable import Initializable



class FeeCollector(Initializable):
    _abi = {b'\x19\xabE<': {'inputs': [{'internalType': 'contract IERC20', 'name': '_token', 'type': 'address'}], 'name': 'init', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfc\x0cTj': {'inputs': [], 'name': 'token', 'outputs': [{'internalType': 'contract IERC20', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _deployment_code = "608060405234801561001057600080fd5b5061048e806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c806319ab453c1461003b578063fc0c546a14610057575b600080fd5b610055600480360381019061005091906102ab565b610075565b005b61005f6101ed565b60405161006c9190610337565b60405180910390f35b60008060019054906101000a900460ff161590508080156100a65750600160008054906101000a900460ff1660ff16105b806100d357506100b530610213565b1580156100d25750600160008054906101000a900460ff1660ff16145b5b610112576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610109906103d5565b60405180910390fd5b60016000806101000a81548160ff021916908360ff160217905550801561014f576001600060016101000a81548160ff0219169083151502179055505b81600060026101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080156101e95760008060016101000a81548160ff0219169083151502179055507f7f26b83ff96e1f2b6a682f133852f6798a09c465da95921460cefb384740249860016040516101e0919061043d565b60405180910390a15b5050565b600060029054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006102668261023b565b9050919050565b60006102788261025b565b9050919050565b6102888161026d565b811461029357600080fd5b50565b6000813590506102a58161027f565b92915050565b6000602082840312156102c1576102c0610236565b5b60006102cf84828501610296565b91505092915050565b6000819050919050565b60006102fd6102f86102f38461023b565b6102d8565b61023b565b9050919050565b600061030f826102e2565b9050919050565b600061032182610304565b9050919050565b61033181610316565b82525050565b600060208201905061034c6000830184610328565b92915050565b600082825260208201905092915050565b7f496e697469616c697a61626c653a20636f6e747261637420697320616c72656160008201527f647920696e697469616c697a6564000000000000000000000000000000000000602082015250565b60006103bf602e83610352565b91506103ca82610363565b604082019050919050565b600060208201905081810360008301526103ee816103b2565b9050919050565b6000819050919050565b600060ff82169050919050565b600061042761042261041d846103f5565b6102d8565b6103ff565b9050919050565b6104378161040c565b82525050565b6000602082019050610452600083018461042e565b9291505056fea2646970667358221220a829a2ec5f1a960bf8cdd43ca957f22aa1b35882c5327a59dad7a0601d62995864736f6c63430008110033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[ChainInterface] = None) -> FeeCollector:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[ChainInterface] = None) -> LegacyTransaction[FeeCollector]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[ChainInterface] = None) -> Union[FeeCollector, LegacyTransaction[FeeCollector]]:
        return cls._deploy([], return_tx, FeeCollector, from_, value, gas_limit, {}, chain)

    @classmethod
    def deployment_code(cls) -> bytes:
        return cls._get_deployment_code({})

    @overload
    def token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> IERC20:
        ...

    @overload
    def token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[IERC20]:
        ...

    def token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[IERC20, LegacyTransaction[IERC20]]:
        """
        Returns:
            contract IERC20
        """
        return self._transact("fc0c546a", [], return_tx, request_type, IERC20, from_, to, value, gas_limit) if not request_type == 'call' else self._call("fc0c546a", [], return_tx, IERC20, from_, to, value, gas_limit)

    @overload
    def init(self, _token: IERC20, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> None:
        ...

    @overload
    def init(self, _token: IERC20, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[None]:
        ...

    def init(self, _token: IERC20, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[None, LegacyTransaction[None]]:
        """
        Args:
            _token: contract IERC20
        """
        return self._transact("19ab453c", [_token], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("19ab453c", [_token], return_tx, type(None), from_, to, value, gas_limit)

