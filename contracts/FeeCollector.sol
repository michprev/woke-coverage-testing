// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";


contract FeeCollector is Initializable {
    IERC20 public token;

    function init(IERC20 _token) initializer public {
        token = _token;
    }

}