#!/usr/bin/env python3
"""
Encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    uses random salt to hash data
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    if data isencrypted return hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
