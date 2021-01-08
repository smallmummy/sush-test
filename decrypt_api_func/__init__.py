import logging

import azure.functions as func
from lib.decrypt import (
    validate_decrypt_params, decrypt_content
)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('trigger decrypt API endpoint...')

    try:
        # validate and fetch params
        (
            vc, symmetric_key, err_msg
        ) = validate_decrypt_params(req.params)

        if err_msg is not None:
            return func.HttpResponse(
                f"invalid input, detail: {err_msg}",
                status_code=400
            )

        decrypted_vc = decrypt_content(vc, symmetric_key)
        return func.HttpResponse(
                decrypted_vc,
                mimetype="application/json"
            )
    except Exception as e:
        logging.error(f"unexcept error in decrypt, detail: {str(e)}")
        return func.HttpResponse(
            f"internal error, detail: {str(e)}",
            status_code=500
        )
