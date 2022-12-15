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



class IERC20(Contract):
    _abi = {b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _deployment_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[ChainInterface] = None) -> IERC20:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[ChainInterface] = None) -> LegacyTransaction[IERC20]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[ChainInterface] = None) -> Union[IERC20, LegacyTransaction[IERC20]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def deployment_code(cls) -> bytes:
        raise Exception("Cannot get deployment code of an interface")

    @dataclass
    class Transfer:
        """
        Attributes:
            from__ (Address): indexed address
            to_ (Address): indexed address
            value_ (int): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}
        selector = b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef'

        from__: Address
        to_: Address
        value_: int


    @dataclass
    class Approval:
        """
        Attributes:
            owner (Address): indexed address
            spender (Address): indexed address
            value_ (int): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}
        selector = b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%'

        owner: Address
        spender: Address
        value_: int


    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> int:
        ...

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[int]:
        ...

    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[int, LegacyTransaction[int]]:
        """
        Returns:
            uint256
        """
        return self._transact("18160ddd", [], return_tx, request_type, int, from_, to, value, gas_limit) if not request_type == 'call' else self._call("18160ddd", [], return_tx, int, from_, to, value, gas_limit)

    @overload
    def balanceOf(self, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> int:
        ...

    @overload
    def balanceOf(self, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[int]:
        ...

    def balanceOf(self, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[int, LegacyTransaction[int]]:
        """
        Args:
            account: address
        Returns:
            uint256
        """
        return self._transact("70a08231", [account], return_tx, request_type, int, from_, to, value, gas_limit) if not request_type == 'call' else self._call("70a08231", [account], return_tx, int, from_, to, value, gas_limit)

    @overload
    def transfer(self, to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def transfer(self, to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[bool]:
        ...

    def transfer(self, to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[bool, LegacyTransaction[bool]]:
        """
        Args:
            to_: address
            amount: uint256
        Returns:
            bool
        """
        return self._transact("a9059cbb", [to_, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("a9059cbb", [to_, amount], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def allowance(self, owner: Union[Account, Address], spender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> int:
        ...

    @overload
    def allowance(self, owner: Union[Account, Address], spender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[int]:
        ...

    def allowance(self, owner: Union[Account, Address], spender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[int, LegacyTransaction[int]]:
        """
        Args:
            owner: address
            spender: address
        Returns:
            uint256
        """
        return self._transact("dd62ed3e", [owner, spender], return_tx, request_type, int, from_, to, value, gas_limit) if not request_type == 'call' else self._call("dd62ed3e", [owner, spender], return_tx, int, from_, to, value, gas_limit)

    @overload
    def approve(self, spender: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def approve(self, spender: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[bool]:
        ...

    def approve(self, spender: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[bool, LegacyTransaction[bool]]:
        """
        Args:
            spender: address
            amount: uint256
        Returns:
            bool
        """
        return self._transact("095ea7b3", [spender, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("095ea7b3", [spender, amount], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def transferFrom(self, from__: Union[Account, Address], to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def transferFrom(self, from__: Union[Account, Address], to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[bool]:
        ...

    def transferFrom(self, from__: Union[Account, Address], to_: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[bool, LegacyTransaction[bool]]:
        """
        Args:
            from__: address
            to_: address
            amount: uint256
        Returns:
            bool
        """
        return self._transact("23b872dd", [from__, to_, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("23b872dd", [from__, to_, amount], return_tx, bool, from_, to, value, gas_limit)

