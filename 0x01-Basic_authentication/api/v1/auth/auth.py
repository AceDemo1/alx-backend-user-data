#!/usr/bin/env python3
"""class to manage the API authentication"""
import flask
import request
from typing import List, TypeVar


class Auth:
    """define class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """define class"""
        return False

    def authorization_header(self, request=None) -> str:
        """define class"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """deine class"""
        return None
