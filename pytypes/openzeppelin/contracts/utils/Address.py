from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.core import Contract, Library, Address, Wei, Account, ChainInterface
from woke.testing.internal import TransactionRevertedError
from woke.testing.transactions import LegacyTransaction

from enum import IntEnum



class Address(Library):
    _abi = {}
    _deployment_code = "60566050600b82828239805160001a6073146043577f4e487b7100000000000000000000000000000000000000000000000000000000600052600060045260246000fd5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600080fdfea26469706673582212201456f7767f46f239da11f81368573b480f6d8de2e2a321dadf5bcd65d1c39d7564736f6c63430008110033"

    _library_id = b'd\x04s\x7f\xbb\xa1\xba\x11k;kc\x93w\x8a\xfb\x0b'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[ChainInterface] = None) -> Address:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[ChainInterface] = None) -> LegacyTransaction[Address]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[ChainInterface] = None) -> Union[Address, LegacyTransaction[Address]]:
        return cls._deploy([], return_tx, Address, from_, value, gas_limit, {}, chain)

    @classmethod
    def deployment_code(cls) -> bytes:
        return cls._get_deployment_code({})

