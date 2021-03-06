import logging

import azure.functions as func
from lib.encrypt import (
    validate_encrypt_params, encrypt_content
)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('trigger encrypt API endpoint...')

    try:
        # validate and fetch params
        (
            subject_claims, symmetric_key, subject_id, err_msg
        ) = validate_encrypt_params(req.params)

        if err_msg is not None:
            return func.HttpResponse(
                f"invalid input, detail: {err_msg}",
                status_code=400
            )

        encrypted_vc = encrypt_content(
            subject_claims, symmetric_key, subject_id
        )
        return func.HttpResponse(
                encrypted_vc
            )
    except Exception as e:
        logging.error(f"unexcept error in encrypt, detail: {str(e)}")
        return func.HttpResponse(
            f"internal error, detail: {str(e)}",
            status_code=500
        )
