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

from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IERC20 import IERC20



class IERC20MintableBurnable(IERC20):
    _abi = {b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9d\xc2\x9f\xac': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'burn', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'@\xc1\x0f\x19': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'mint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _deployment_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[ChainInterface] = None) -> IERC20MintableBurnable:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[ChainInterface] = None) -> LegacyTransaction[IERC20MintableBurnable]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[ChainInterface] = None) -> Union[IERC20MintableBurnable, LegacyTransaction[IERC20MintableBurnable]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def deployment_code(cls) -> bytes:
        raise Exception("Cannot get deployment code of an interface")

    @overload
    def mint(self, to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> None:
        ...

    @overload
    def mint(self, to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[None]:
        ...

    def mint(self, to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[None, LegacyTransaction[None]]:
        """
        Args:
            to_: address
            amount: uint256
        """
        return self._transact("40c10f19", [to_, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("40c10f19", [to_, amount], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def burn(self, from__: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> None:
        ...

    @overload
    def burn(self, from__: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[None]:
        ...

    def burn(self, from__: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[None, LegacyTransaction[None]]:
        """
        Args:
            from__: address
            amount: uint256
        """
        return self._transact("9dc29fac", [from__, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("9dc29fac", [from__, amount], return_tx, type(None), from_, to, value, gas_limit)

