#!/usr/bin/env python3
"""class to manage the API authentication"""
import flask
import requests
from typing import List, TypeVar


class Auth:
    """define class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """define class"""
        if not path or not excluded_paths:
            return True
        new_path = path if path[-1] == '/' else path + '/'
        new_excluded_paths = [i if i[-1] == '/' else i + '/'
                              for i in excluded_paths]
        if new_path in new_excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """define class"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """deine class"""
        return None
