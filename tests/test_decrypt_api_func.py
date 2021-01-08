import re
import json
import azure.functions as func
from decrypt_api_func import main


def test_decrypt_01():
    """
    correct input and response
    """

    test_req = func.HttpRequest(
        method="POST",
        url="",
        body="",
        params={
            "vc": "85b3d231de13e9a261a4584e761eda8331f7c4caedf3c0c8e59d0ab6bfba9ed0a3165ca684cbc0230daec738c9ba3c9d7c973929266270b143db175eb0347bdca582d757e4521baba78104bb14fd5488b96d49ddd43744aa72e8c8f5f8f51db05189754945ca232392e234e6a9c61f0900ced6e3d576fffc8ca7602e743ccbbfa39ce6a466c274abf90bc9722867ac71500c94fcd74444d862a1ebbd79d25c0f4307b95be3b07ea7dcceb83f1ec382e1510856ea24ef27522ab81da21fb4e4f96e519dd992a0144d9d5847584d18f4b83b3292273540fb5972e35906fbebd777a7a4d763742fb3e6f4280023d759106464aa7582dc2a4b6bda6f0e95b2b009ea06422190a76a52efec801f2bdba1e840e2e6f0b4559d893ffd946b6a2f67ff5a22cbfa2732c5c72e4c2ce7a0659e4fab51c608fa69ea21348a625be9a6548db2254539f00e0aa00537cf1c037e361ab6316d31ba800a2693d23730ae2e6b90129ba24eebdc6419f5a7e2d411cba0bea92a2a559d6820d88e132667da53e1d5135f16ec81527fcf2d2282d27ddf1183b9a1fb223d36e8ee4527a3fdbd69a6509274193084117a9fa3179d38d32aa5dfc662801aa8517e543bf4ecd76901f0cbd9d1c3868167bd55034798ade5dfef7dbec70f06ea95e0eed2f5c999911d5dd14b94e2db8769a15bd9b49f15e2f91e572c51bd9474d3f556d8ddab4d57ea23ef6e0ed30f1a592ed698277de32b8e8c6dded69c20c0dd6cd3b1890bb54967df3025a4354976c5cd9614fc4241d498ae4ffb7ef4680acbaef93574c120cb776e703249645f191b24e3645b5772eabf3fe897f57f2db7db34bd1e77f2f0e76014affb54689f98252200c9655b5fbc6b2cee93043021135ce29e2334711173ac7dedc89c769ae123c44108cf2f89320e15aead7373954ffffdcab64f6d1c19195a3e0dc6760adc9c7902b0dbb0f58eea955813f01e6d04a2909903ca1421047dfbfb0d1e2b4735dc125d3406e145cace3879860a0caebf3b91c1fdb30c082911e7d227cbfd467ee72bf4eaddb53bedc5593ef2dd1e0561a3e1a54dc8b3e2825fedf32de8df5eef7cf5eb95155ff4b931f25d920cc271c4df",
            "SymmetricKey": "sush123sush123sush123sush123sush",

        }
    )
    ret = main(test_req)
    assert ret.status_code == 200
    vc = json.loads(ret.get_body().decode())
    assert vc["credentialSubject"]["given_names"]["value"] == "John"
    assert vc["credentialSubject"]["surname"]["value"] == "Smith"


def test_decrypt_02():
    """
    abnormal input due to incomplete params
    """

    test_req = func.HttpRequest(
        method="POST",
        url="",
        body="",
        params={
            "vc": "xxxx"
        }
    )
    ret = main(test_req)
    assert ret.status_code == 400
    assert re.search(
        r"invalid input", ret.get_body().decode()
    ) is not None


def test_decrypt_03():
    """
    abnormal input due to invalid length of AES key
    """

    test_req = func.HttpRequest(
        method="POST",
        url="",
        body="",
        params={
            "vc": "xxxx",
            "SymmetricKey": "sush12",
        }
    )
    ret = main(test_req)
    assert ret.status_code == 500
    assert re.search(
        r"internal error", ret.get_body().decode()
    ) is not None
