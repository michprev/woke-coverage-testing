from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.core import Contract, Library, Address, Wei, Account, ChainInterface
from woke.testing.internal import TransactionRevertedError
from woke.testing.transactions import LegacyTransaction

from enum import IntEnum



class Initializable(Contract):
    _abi = {}
    _deployment_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[ChainInterface] = None) -> Initializable:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[ChainInterface] = None) -> LegacyTransaction[Initializable]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[ChainInterface] = None) -> Union[Initializable, LegacyTransaction[Initializable]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def deployment_code(cls) -> bytes:
        raise Exception("Cannot get deployment code of an abstract contract")

    @dataclass
    class Initialized:
        """
        Attributes:
            version (int): uint8
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint8', 'name': 'version', 'type': 'uint8'}], 'name': 'Initialized', 'type': 'event'}
        selector = b'\x7f&\xb8?\xf9n\x1f+jh/\x138R\xf6y\x8a\t\xc4e\xda\x95\x92\x14`\xce\xfb8G@$\x98'

        version: int


