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



class ERC20(IERC20):
    _abi = {'constructor': {'inputs': [{'internalType': 'string', 'name': 'name_', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol_', 'type': 'string'}, {'internalType': 'uint8', 'name': 'decimals_', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'1<\xe5g': {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa4W\xc2\xd7': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'9P\x93Q': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _deployment_code = "60a06040523480156200001157600080fd5b50604051620011e6380380620011e683398181016040528101906200003791906200030b565b82600390805190602001906200004f92919062000080565b5081600490805190602001906200006892919062000080565b508060ff1660808160ff16815250505050506200040a565b8280546200008e90620003d4565b90600052602060002090601f016020900481019282620000b25760008555620000fe565b82601f10620000cd57805160ff1916838001178555620000fe565b82800160010185558215620000fe579182015b82811115620000fd578251825591602001919060010190620000e0565b5b5090506200010d919062000111565b5090565b5b808211156200012c57600081600090555060010162000112565b5090565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b62000199826200014e565b810181811067ffffffffffffffff82111715620001bb57620001ba6200015f565b5b80604052505050565b6000620001d062000130565b9050620001de82826200018e565b919050565b600067ffffffffffffffff8211156200020157620002006200015f565b5b6200020c826200014e565b9050602081019050919050565b60005b83811015620002395780820151818401526020810190506200021c565b8381111562000249576000848401525b50505050565b6000620002666200026084620001e3565b620001c4565b90508281526020810184848401111562000285576200028462000149565b5b6200029284828562000219565b509392505050565b600082601f830112620002b257620002b162000144565b5b8151620002c48482602086016200024f565b91505092915050565b600060ff82169050919050565b620002e581620002cd565b8114620002f157600080fd5b50565b6000815190506200030581620002da565b92915050565b6000806000606084860312156200032757620003266200013a565b5b600084015167ffffffffffffffff8111156200034857620003476200013f565b5b62000356868287016200029a565b935050602084015167ffffffffffffffff8111156200037a57620003796200013f565b5b62000388868287016200029a565b92505060406200039b86828701620002f4565b9150509250925092565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b60006002820490506001821680620003ed57607f821691505b60208210811415620004045762000403620003a5565b5b50919050565b608051610dc06200042660003960006103fa0152610dc06000f3fe608060405234801561001057600080fd5b50600436106100a95760003560e01c80633950935111610071578063395093511461016857806370a082311461019857806395d89b41146101c8578063a457c2d7146101e6578063a9059cbb14610216578063dd62ed3e14610246576100a9565b806306fdde03146100ae578063095ea7b3146100cc57806318160ddd146100fc57806323b872dd1461011a578063313ce5671461014a575b600080fd5b6100b6610276565b6040516100c39190610a1e565b60405180910390f35b6100e660048036038101906100e19190610ad9565b610304565b6040516100f39190610b34565b60405180910390f35b61010461031b565b6040516101119190610b5e565b60405180910390f35b610134600480360381019061012f9190610b79565b610321565b6040516101419190610b34565b60405180910390f35b6101526103f8565b60405161015f9190610be8565b60405180910390f35b610182600480360381019061017d9190610ad9565b61041c565b60405161018f9190610b34565b60405180910390f35b6101b260048036038101906101ad9190610c03565b6104ba565b6040516101bf9190610b5e565b60405180910390f35b6101d06104d2565b6040516101dd9190610a1e565b60405180910390f35b61020060048036038101906101fb9190610ad9565b610560565b60405161020d9190610b34565b60405180910390f35b610230600480360381019061022b9190610ad9565b6105fe565b60405161023d9190610b34565b60405180910390f35b610260600480360381019061025b9190610c30565b610615565b60405161026d9190610b5e565b60405180910390f35b6003805461028390610c9f565b80601f01602080910402602001604051908101604052809291908181526020018280546102af90610c9f565b80156102fc5780601f106102d1576101008083540402835291602001916102fc565b820191906000526020600020905b8154815290600101906020018083116102df57829003601f168201915b505050505081565b600061031133848461063a565b6001905092915050565b60025481565b600080600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff81146103e1576103e0853385846103db9190610d00565b61063a565b5b6103ec8585856107c3565b60019150509392505050565b7f000000000000000000000000000000000000000000000000000000000000000081565b60006104b0338484600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020546104ab9190610d34565b61063a565b6001905092915050565b60006020528060005260406000206000915090505481565b600480546104df90610c9f565b80601f016020809104026020016040519081016040528092919081815260200182805461050b90610c9f565b80156105585780601f1061052d57610100808354040283529160200191610558565b820191906000526020600020905b81548152906001019060200180831161053b57829003601f168201915b505050505081565b60006105f4338484600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020546105ef9190610d00565b61063a565b6001905092915050565b600061060b3384846107c3565b6001905092915050565b6001602052816000526040600020602052806000526040600020600091509150505481565b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614806106a15750600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16145b156106d8576040517f6d187b2800000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b80600160008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925836040516107b69190610b5e565b60405180910390a3505050565b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16148061082a5750600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16145b15610861576040517f6d187b2800000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b61086c838383610980565b806000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546108ba9190610d00565b92505081905550806000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461090f9190610d34565b925050819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040516109739190610b5e565b60405180910390a3505050565b505050565b600081519050919050565b600082825260208201905092915050565b60005b838110156109bf5780820151818401526020810190506109a4565b838111156109ce576000848401525b50505050565b6000601f19601f8301169050919050565b60006109f082610985565b6109fa8185610990565b9350610a0a8185602086016109a1565b610a13816109d4565b840191505092915050565b60006020820190508181036000830152610a3881846109e5565b905092915050565b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000610a7082610a45565b9050919050565b610a8081610a65565b8114610a8b57600080fd5b50565b600081359050610a9d81610a77565b92915050565b6000819050919050565b610ab681610aa3565b8114610ac157600080fd5b50565b600081359050610ad381610aad565b92915050565b60008060408385031215610af057610aef610a40565b5b6000610afe85828601610a8e565b9250506020610b0f85828601610ac4565b9150509250929050565b60008115159050919050565b610b2e81610b19565b82525050565b6000602082019050610b496000830184610b25565b92915050565b610b5881610aa3565b82525050565b6000602082019050610b736000830184610b4f565b92915050565b600080600060608486031215610b9257610b91610a40565b5b6000610ba086828701610a8e565b9350506020610bb186828701610a8e565b9250506040610bc286828701610ac4565b9150509250925092565b600060ff82169050919050565b610be281610bcc565b82525050565b6000602082019050610bfd6000830184610bd9565b92915050565b600060208284031215610c1957610c18610a40565b5b6000610c2784828501610a8e565b91505092915050565b60008060408385031215610c4757610c46610a40565b5b6000610c5585828601610a8e565b9250506020610c6685828601610a8e565b9150509250929050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b60006002820490506001821680610cb757607f821691505b60208210811415610ccb57610cca610c70565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b6000610d0b82610aa3565b9150610d1683610aa3565b925082821015610d2957610d28610cd1565b5b828203905092915050565b6000610d3f82610aa3565b9150610d4a83610aa3565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115610d7f57610d7e610cd1565b5b82820190509291505056fea2646970667358221220efe6ff7099028e00ff8a8c723752a6fdad616f3f4ecd654450da76f98b854ac664736f6c63430008090033"

    @overload
    @classmethod
    def deploy(cls, name_: str, symbol_: str, decimals_: int, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[ChainInterface] = None) -> ERC20:
        ...

    @overload
    @classmethod
    def deploy(cls, name_: str, symbol_: str, decimals_: int, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[ChainInterface] = None) -> LegacyTransaction[ERC20]:
        ...

    @classmethod
    def deploy(cls, name_: str, symbol_: str, decimals_: int, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[ChainInterface] = None) -> Union[ERC20, LegacyTransaction[ERC20]]:
        """
        Args:
            name_: string
            symbol_: string
            decimals_: uint8
        """
        return cls._deploy([name_, symbol_, decimals_], return_tx, ERC20, from_, value, gas_limit, {}, chain)

    @classmethod
    def deployment_code(cls) -> bytes:
        return cls._get_deployment_code({})

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> int:
        ...

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[int]:
        ...

    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[int, LegacyTransaction[int]]:
        """
        Args:
            key0: address
        Returns:
            uint256
        """
        return self._transact("70a08231", [key0], return_tx, request_type, int, from_, to, value, gas_limit) if not request_type == 'call' else self._call("70a08231", [key0], return_tx, int, from_, to, value, gas_limit)

    @overload
    def allowance(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> int:
        ...

    @overload
    def allowance(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[int]:
        ...

    def allowance(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[int, LegacyTransaction[int]]:
        """
        Args:
            key0: address
            key1: address
        Returns:
            uint256
        """
        return self._transact("dd62ed3e", [key0, key1], return_tx, request_type, int, from_, to, value, gas_limit) if not request_type == 'call' else self._call("dd62ed3e", [key0, key1], return_tx, int, from_, to, value, gas_limit)

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
    def name(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> str:
        ...

    @overload
    def name(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[str]:
        ...

    def name(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[str, LegacyTransaction[str]]:
        """
        Returns:
            string
        """
        return self._transact("06fdde03", [], return_tx, request_type, str, from_, to, value, gas_limit) if not request_type == 'call' else self._call("06fdde03", [], return_tx, str, from_, to, value, gas_limit)

    @overload
    def symbol(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> str:
        ...

    @overload
    def symbol(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[str]:
        ...

    def symbol(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[str, LegacyTransaction[str]]:
        """
        Returns:
            string
        """
        return self._transact("95d89b41", [], return_tx, request_type, str, from_, to, value, gas_limit) if not request_type == 'call' else self._call("95d89b41", [], return_tx, str, from_, to, value, gas_limit)

    @overload
    def decimals(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> int:
        ...

    @overload
    def decimals(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[int]:
        ...

    def decimals(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[int, LegacyTransaction[int]]:
        """
        Returns:
            uint8
        """
        return self._transact("313ce567", [], return_tx, request_type, int, from_, to, value, gas_limit) if not request_type == 'call' else self._call("313ce567", [], return_tx, int, from_, to, value, gas_limit)

    @overload
    def transfer(self, recipient: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def transfer(self, recipient: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[bool]:
        ...

    def transfer(self, recipient: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[bool, LegacyTransaction[bool]]:
        """
        Args:
            recipient: address
            amount: uint256
        Returns:
            bool
        """
        return self._transact("a9059cbb", [recipient, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("a9059cbb", [recipient, amount], return_tx, bool, from_, to, value, gas_limit)

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
    def transferFrom(self, sender: Union[Account, Address], recipient: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def transferFrom(self, sender: Union[Account, Address], recipient: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[bool]:
        ...

    def transferFrom(self, sender: Union[Account, Address], recipient: Union[Account, Address], amount: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[bool, LegacyTransaction[bool]]:
        """
        Args:
            sender: address
            recipient: address
            amount: uint256
        Returns:
            bool
        """
        return self._transact("23b872dd", [sender, recipient, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("23b872dd", [sender, recipient, amount], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def increaseAllowance(self, spender: Union[Account, Address], addedValue: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def increaseAllowance(self, spender: Union[Account, Address], addedValue: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[bool]:
        ...

    def increaseAllowance(self, spender: Union[Account, Address], addedValue: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[bool, LegacyTransaction[bool]]:
        """
        Args:
            spender: address
            addedValue: uint256
        Returns:
            bool
        """
        return self._transact("39509351", [spender, addedValue], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("39509351", [spender, addedValue], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def decreaseAllowance(self, spender: Union[Account, Address], subtractedValue: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def decreaseAllowance(self, spender: Union[Account, Address], subtractedValue: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[bool]:
        ...

    def decreaseAllowance(self, spender: Union[Account, Address], subtractedValue: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[bool, LegacyTransaction[bool]]:
        """
        Args:
            spender: address
            subtractedValue: uint256
        Returns:
            bool
        """
        return self._transact("a457c2d7", [spender, subtractedValue], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("a457c2d7", [spender, subtractedValue], return_tx, bool, from_, to, value, gas_limit)

