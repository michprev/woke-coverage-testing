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



class ConstAddressDeployer(Contract):
    _abi = {b'J\xf6?\x02': {'inputs': [{'internalType': 'bytes', 'name': 'bytecode', 'type': 'bytes'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'deploy', 'outputs': [{'internalType': 'address', 'name': 'deployedAddress_', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcfMd2': {'inputs': [{'internalType': 'bytes', 'name': 'bytecode', 'type': 'bytes'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'init', 'type': 'bytes'}], 'name': 'deployAndInit', 'outputs': [{'internalType': 'address', 'name': 'deployedAddress_', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc2\xb1\x04\x1c': {'inputs': [{'internalType': 'bytes', 'name': 'bytecode', 'type': 'bytes'}, {'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'deployedAddress', 'outputs': [{'internalType': 'address', 'name': 'deployedAddress_', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _deployment_code = "608060405234801561001057600080fd5b5061090e806100206000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c80634af63f0214610046578063c2b1041c14610076578063cf4d6432146100a6575b600080fd5b610060600480360381019061005b9190610507565b6100d6565b60405161006d91906105a4565b60405180910390f35b610090600480360381019061008b919061064b565b610112565b60405161009d91906105a4565b60405180910390f35b6100c060048036038101906100bb91906106bf565b610190565b6040516100cd91906105a4565b60405180910390f35b600061010a8333846040516020016100ef92919061075e565b60405160208183030381529060405280519060200120610275565b905092915050565b600080838360405160200161012892919061075e565b604051602081830303815290604052805190602001209050308187876040516101529291906107b7565b604051809103902060405160200161016c93929190610890565b6040516020818303038152906040528051906020012060001c915050949350505050565b60006101c48533866040516020016101a992919061075e565b60405160208183030381529060405280519060200120610275565b905060008173ffffffffffffffffffffffffffffffffffffffff1684846040516101ef9291906107b7565b6000604051808303816000865af19150503d806000811461022c576040519150601f19603f3d011682016040523d82523d6000602084013e610231565b606091505b505090508061026c576040517f4f77232300000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b50949350505050565b600080835114156102b2576040517f21744a5900000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b818351602085016000f59050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415610325576040517f4102e83a00000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff168284805190602001207f27b8e3132afa95254770e1c1d214eafde52bc47d1b6e1f5dfcbb380c3ca3f53260405160405180910390a492915050565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6103de82610395565b810181811067ffffffffffffffff821117156103fd576103fc6103a6565b5b80604052505050565b6000610410610377565b905061041c82826103d5565b919050565b600067ffffffffffffffff82111561043c5761043b6103a6565b5b61044582610395565b9050602081019050919050565b82818337600083830152505050565b600061047461046f84610421565b610406565b9050828152602081018484840111156104905761048f610390565b5b61049b848285610452565b509392505050565b600082601f8301126104b8576104b761038b565b5b81356104c8848260208601610461565b91505092915050565b6000819050919050565b6104e4816104d1565b81146104ef57600080fd5b50565b600081359050610501816104db565b92915050565b6000806040838503121561051e5761051d610381565b5b600083013567ffffffffffffffff81111561053c5761053b610386565b5b610548858286016104a3565b9250506020610559858286016104f2565b9150509250929050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061058e82610563565b9050919050565b61059e81610583565b82525050565b60006020820190506105b96000830184610595565b92915050565b600080fd5b600080fd5b60008083601f8401126105df576105de61038b565b5b8235905067ffffffffffffffff8111156105fc576105fb6105bf565b5b602083019150836001820283011115610618576106176105c4565b5b9250929050565b61062881610583565b811461063357600080fd5b50565b6000813590506106458161061f565b92915050565b6000806000806060858703121561066557610664610381565b5b600085013567ffffffffffffffff81111561068357610682610386565b5b61068f878288016105c9565b945094505060206106a287828801610636565b92505060406106b3878288016104f2565b91505092959194509250565b600080600080606085870312156106d9576106d8610381565b5b600085013567ffffffffffffffff8111156106f7576106f6610386565b5b610703878288016104a3565b9450506020610714878288016104f2565b935050604085013567ffffffffffffffff81111561073557610734610386565b5b610741878288016105c9565b925092505092959194509250565b610758816104d1565b82525050565b60006040820190506107736000830185610595565b610780602083018461074f565b9392505050565b600081905092915050565b600061079e8385610787565b93506107ab838584610452565b82840190509392505050565b60006107c4828486610792565b91508190509392505050565b600081905092915050565b7fff00000000000000000000000000000000000000000000000000000000000000600082015250565b60006108116001836107d0565b915061081c826107db565b600182019050919050565b60008160601b9050919050565b600061083f82610827565b9050919050565b600061085182610834565b9050919050565b61086961086482610583565b610846565b82525050565b6000819050919050565b61088a610885826104d1565b61086f565b82525050565b600061089b82610804565b91506108a78286610858565b6014820191506108b78285610879565b6020820191506108c78284610879565b60208201915081905094935050505056fea26469706673582212204aacc10a2f3ab798e559a6ebec1f333425a30857ce7cd60cef3c0b35614a944f64736f6c63430008090033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[ChainInterface] = None) -> ConstAddressDeployer:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[ChainInterface] = None) -> LegacyTransaction[ConstAddressDeployer]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[ChainInterface] = None) -> Union[ConstAddressDeployer, LegacyTransaction[ConstAddressDeployer]]:
        return cls._deploy([], return_tx, ConstAddressDeployer, from_, value, gas_limit, {}, chain)

    @classmethod
    def deployment_code(cls) -> bytes:
        return cls._get_deployment_code({})

    @dataclass
    class EmptyBytecode(TransactionRevertedError):
        _abi = {'inputs': [], 'name': 'EmptyBytecode', 'type': 'error'}
        selector = b'!tJY'



    @dataclass
    class FailedDeploy(TransactionRevertedError):
        _abi = {'inputs': [], 'name': 'FailedDeploy', 'type': 'error'}
        selector = b'A\x02\xe8:'



    @dataclass
    class FailedInit(TransactionRevertedError):
        _abi = {'inputs': [], 'name': 'FailedInit', 'type': 'error'}
        selector = b'Ow##'



    @dataclass
    class Deployed:
        """
        Attributes:
            bytecodeHash (bytearray): indexed bytes32
            salt (bytearray): indexed bytes32
            deployedAddress (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'bytecodeHash', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'deployedAddress', 'type': 'address'}], 'name': 'Deployed', 'type': 'event'}
        selector = b"'\xb8\xe3\x13*\xfa\x95%Gp\xe1\xc1\xd2\x14\xea\xfd\xe5+\xc4}\x1bn\x1f]\xfc\xbb8\x0c<\xa3\xf52"

        bytecodeHash: bytearray
        salt: bytearray
        deployedAddress: Address


    @overload
    def deploy_(self, bytecode: Union[bytearray, bytes], salt: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def deploy_(self, bytecode: Union[bytearray, bytes], salt: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[Address]:
        ...

    def deploy_(self, bytecode: Union[bytearray, bytes], salt: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[Address, LegacyTransaction[Address]]:
        """
        Args:
            bytecode: bytes
            salt: bytes32
        Returns:
            address
        """
        return self._transact("4af63f02", [bytecode, salt], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("4af63f02", [bytecode, salt], return_tx, Address, from_, to, value, gas_limit)

    @overload
    def deployAndInit(self, bytecode: Union[bytearray, bytes], salt: Union[bytearray, bytes], init: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def deployAndInit(self, bytecode: Union[bytearray, bytes], salt: Union[bytearray, bytes], init: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[Address]:
        ...

    def deployAndInit(self, bytecode: Union[bytearray, bytes], salt: Union[bytearray, bytes], init: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='default') -> Union[Address, LegacyTransaction[Address]]:
        """
        Args:
            bytecode: bytes
            salt: bytes32
            init: bytes
        Returns:
            address
        """
        return self._transact("cf4d6432", [bytecode, salt, init], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("cf4d6432", [bytecode, salt, init], return_tx, Address, from_, to, value, gas_limit)

    @overload
    def deployedAddress(self, bytecode: Union[bytearray, bytes], sender: Union[Account, Address], salt: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def deployedAddress(self, bytecode: Union[bytearray, bytes], sender: Union[Account, Address], salt: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType='default') -> LegacyTransaction[Address]:
        ...

    def deployedAddress(self, bytecode: Union[bytearray, bytes], sender: Union[Account, Address], salt: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[Address, LegacyTransaction[Address]]:
        """
        Args:
            bytecode: bytes
            sender: address
            salt: bytes32
        Returns:
            address
        """
        return self._transact("c2b1041c", [bytecode, sender, salt], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("c2b1041c", [bytecode, sender, salt], return_tx, Address, from_, to, value, gas_limit)

