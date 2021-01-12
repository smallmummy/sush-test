import json
from copy import deepcopy
from lib.common import CREDENTIAL_TEMPLATE
from lib.aes import AesEncryption


def validate_encrypt_params(req_params):

    err_msg = None

    subject_claims = req_params.get('subject_claims')
    symmetric_key = req_params.get('SymmetricKey')
    subject_id = req_params.get('Subjectid')

    if any([
        subject_claims is None,
        symmetric_key is None,
        subject_id is None
    ]) is True:
        err_msg = "all of subject_claims & SymmetricKey & Subjectid cannot be None"
        return subject_claims, symmetric_key, subject_id, err_msg

    try:
        subject_claims = json.loads(subject_claims)
    except Exception:
        subject_claims = None
        err_msg = "value of subject_claims must be JSON string"
        return None, symmetric_key, subject_id, err_msg

    return subject_claims, symmetric_key, subject_id, err_msg


def construct_vc_content(subject_id, subject_claims):
    vc = deepcopy(CREDENTIAL_TEMPLATE)
    vc["id"] = vc["id"].format(guid=subject_id)

    for key, val in subject_claims.items():
        vc["credentialSubject"][key] = {"value": val}

    return json.dumps(vc)


def encrypt_content(subject_claims, symmetric_key, subject_id):

    vc = construct_vc_content(subject_id, subject_claims)

    aes = AesEncryption(symmetric_key)
    encrypted_vc = aes.encrypt(vc)

    return encrypted_vc
