import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werzkeug.security import check_password_hash, generate_password

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

