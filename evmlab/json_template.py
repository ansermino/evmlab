HEX_FORMAT = '#0x'


def get_json(bytecode, start_gas, end_gas, test_name, input_data=0x00, return_val="0x"):
    return {
      test_name : {
        "_info" : {
          "comment" : "",
          "filledwith" : "cpp-1.3.0+commit.6e0ce939.Linux.g++",
          "lllcversion" : "Version: 0.4.18-develop.2017.9.25+commit.a72237f2.Linux.g++",
          "source" : "src/VMTestsFiller/vmArithmeticTest/add1Filler.json",
          "sourceHash" : "f21647f7464e6af98c7a9817d45d0665345edc8837011bfbdd2190da3ac83d1c"
        },
        "callcreates" : [
        ],
        "env" : {
          "currentCoinbase" : "0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba",
          "currentDifficulty" : "0x0100",
          "currentGasLimit" : "0x0f4240",
          "currentNumber" : "0x00",
          "currentTimestamp" : "0x01"
        },
        "exec" : {
          "address" : "0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6",
          "caller" : "0xcd1722f2947def4cf144679da39c4c32bdc35681",
          "code" : '0x' + bytecode,
          "data" : input_data,
          "gas" : format(start_gas, HEX_FORMAT),
          "gasPrice" : "0x5af3107a4000",
          "origin" : "0xcd1722f2947def4cf144679da39c4c32bdc35681",
          "value" : "0x00"
        },
        "gas" : format(end_gas, HEX_FORMAT),
        "logs" : "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "out" : "0x0000000000000000000000000000000000000000000000000000000000000001" if return_val is True else "0x0000000000000000000000000000000000000000000000000000000000000000",
        "post" : {
          "0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6" : {
            "balance" : format(end_gas, HEX_FORMAT),
            "code" : '0x' + bytecode,
            "nonce" : "0x00",
            "storage" : {}
          }
        },
        "pre" : {
          "0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6" : {
            "balance" : format(start_gas, HEX_FORMAT),
            "code" : '0x' + bytecode,
            "nonce" : "0x00",
            "storage" : {}
          }
        }
      }
    }