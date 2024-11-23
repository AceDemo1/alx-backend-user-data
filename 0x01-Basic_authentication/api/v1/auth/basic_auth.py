#!/usr/bin/env python3
"""BasicAuth class"""
import base64
from models.user import User
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """deifne class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """base64"""
        if (not authorization_header
                or not isinstance(authorization_header, str)
                or not authorization_header.startswith('Basic ')):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode"""
        if (not base64_authorization_header
                or not isinstance(base64_authorization_header, str)):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extract"""
        if (not decoded_base64_authorization_header
                or not isinstance(decoded_base64_authorization_header, str)
                or ':' not in decoded_base64_authorization_header):
            return (None, None)
        tuple_res = decoded_base64_authorization_header.split(':')
        return (tuple_res[0], tuple_res[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user obj"""
        if (not isinstance(user_email, str)
                or not isinstance(user_pwd, str)):
            return None
        try:
            users = User.search({'email': user_email})
            if not users:
                return None
            user = users[0]
            if not user.is_valid_password(user_pwd):
                return None
            return user
        except BaseException:
            return None
