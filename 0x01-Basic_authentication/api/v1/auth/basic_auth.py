#!/usr/bin/env python3
"""BasicAuth class"""
from api.v1.auth.auth import Auth


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
