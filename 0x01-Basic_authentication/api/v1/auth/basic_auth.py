#!/usr/bin/env python3
"""BasicAuth class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """deifne class"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """base64"""
        if (not authorization_header or type(authorization_header) != str
            or authorization_header.startswith('Basic ')):
            return None
        return authorization_header[6:]
