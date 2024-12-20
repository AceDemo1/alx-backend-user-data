#!/usr/bin/env python3
"""hassh password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is valid"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
