CREDENTIAL_TEMPLATE = {
    "@context": [
        "https://www.w3.org/2018/credentials/v1",
        "https://www.example.nz/2020/credentials/v1"
    ],
    "id": " https://ics.example.nz/credentials/{guid}",
    "type": ["VerifiableCredential", "IdentityCredential"],
    "issuer": "https://ics.example.nz",
    "issuanceDate": "2010-01-01T19:73:24Z",
    "credentialSubject": {
        "id": "did:id:subjectid",
        "proof": {
            "type": "RsaSignature2018",
            "created": "2020-11-29T21:19:10Z",
            "proofPurpose": "assertionMethod",
            "verificationMethod": "identity_key",
            "jws": "eyJhbGciOiJSUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..TCYt5XsITJX1CxPCT8yAV-TVkIEq_PbChOMqsLfRoPsnsgw5WEuts01mq-pQy7UJiN5mgRxD-WUcX16dUEMGlv50aqzpqh4Qktb3rk-BuQy72IFLOqV0G_zS245-kronKb78cPN25DGlcTwLtjPAYuNzVBAh4vGHSrQyHUdBBPM"
        }
    }
}

SUPPORTABLE_AES_KEY_LEN = [32]
AES_CFB_IV = "8E5EC1AC8E5EC1AC".encode()
