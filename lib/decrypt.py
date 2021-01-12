from lib.aes import AesEncryption


def validate_decrypt_params(req_params):
    err_msg = None

    vc = req_params.get('vc')
    symmetric_key = req_params.get('SymmetricKey')

    if any([
        vc is None,
        symmetric_key is None
    ]) is True:
        err_msg = "Both of vc & SymmetricKey cannot be None"

    return vc, symmetric_key, err_msg


def decrypt_content(vc, symmetric_key):
    aes = AesEncryption(symmetric_key)
    decrypted_vc = aes.decrypt(vc)
    return decrypted_vc
