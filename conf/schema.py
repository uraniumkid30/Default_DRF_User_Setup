from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from conf.authentication import JWTAuthentication


class SimpleJWTTokenUserScheme(OpenApiAuthenticationExtension):
    target_class = JWTAuthentication
    name = 'JWT Authentication'

    def get_security_definition(self, auto_schema):        
        return build_bearer_security_scheme_object("Authorization", "Bearer")