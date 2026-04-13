import os
import secrets

class Config:
    # Use a secure random secret key in production
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
    
    # Security Headers Configuration
    SECURITY_HEADERS = {
        'Content-Security-Policy': "default-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:;",
        'X-Frame-Options': 'DENY',
        'X-Content-Type-Options': 'nosniff',
        'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
        'Referrer-Policy': 'strict-origin-when-cross-origin'
    }
