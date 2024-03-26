"""
example:
python jwt_token_generator.py \
-secret_key="<secret key>" \
-claim_key="<claim key>" \
-claim_key_name="iss" \
-set_expiration_token="Yes" \
-expiration_token_age_in_days="1"
"""


import argparse
import datetime
import json
import jwt


def handle_args() -> list[str]:
    """
    handle the program arguments.

    arguments:
        - secret_key: confidential secret key
        - claim_key: who singned the token
        - claim_key_name: field on the payload that we can check who signed the token
        - set_expiration_token: if set to yes the token will expire
        - expiration_token_age_in_days: the time in days the token will expire
    """
    parser = argparse.ArgumentParser(description='JWT Token Generator')
    parser.add_argument('-secret_key', help='Confidencial secret key')
    parser.add_argument('-claim_key',
                        help='who singned the token')
    parser.add_argument('-claim_key_name',
                        help='field on the payload that we can check who signed the token')
    parser.add_argument('-set_expiration_token',
                        required=True,
                        choices=['Yes', 'No'],
                        help='if set to yes the token will expire')
    parser.add_argument('-expiration_token_age_in_days',
                        help='the time in days the token will expire')
    return parser.parse_args()


if __name__ == '__main__':
    args = handle_args()
    SECRET_KEY = args.secret_key
    KEY_CLAIM = args.claim_key
    KEY_CLAIM_NAME = args.claim_key_name
    SET_EXPIRATION_TOKEN = args.set_expiration_token.upper()

    payload = {
        KEY_CLAIM_NAME: KEY_CLAIM,
    }
    if SET_EXPIRATION_TOKEN == 'YES':
        EXPIRATION_TOKEN_AGE_IN_DAYS = float(args.expiration_token_age_in_days)
        payload["exp"] = datetime.datetime.now(datetime.UTC) + datetime.timedelta(
            days=EXPIRATION_TOKEN_AGE_IN_DAYS)

    header = {
        "alg": "HS256",
        "typ": "JWT",
    }

    print(
        json.dumps({
            'token': jwt.encode(
                payload=payload,
                key=SECRET_KEY,
                algorithm="HS256",
                headers=header
            )
        })
    )
