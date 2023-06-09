from .attributes import (
    Attribute,
    AttributeIssuer,
    AttributeMutability,
    AttributeReturn,
    AttributeUniqueness,
    ComplexAttribute,
)
from ..attributes import type as at
from src.parser.attributes.validators import validate_single_primary_value


user_name = Attribute(
    name="userName",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=True,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.SERVER,
)

_name__formatted = Attribute(
    name="formatted",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_name__family_name = Attribute(
    name="familyName",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_name__given_name = Attribute(
    name="givenName",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_name__middle_name = Attribute(
    name="middleName",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_name__honorific_prefix = Attribute(
    name="honorificPrefix",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_name__honorific_suffix = Attribute(
    name="honorificSuffix",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: warn if "formatted" does not contain information from all the other sub-attributes
name = ComplexAttribute(
    sub_attributes=[
        _name__formatted,
        _name__family_name,
        _name__given_name,
        _name__middle_name,
        _name__honorific_prefix,
        _name__honorific_suffix,
    ],
    name="name",
    issuer=AttributeIssuer.BOTH,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: warn if 'displayName' does not match any of: 'userName', 'name' (any of its sub-attributes)
display_name = Attribute(
    name="displayName",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: warn if 'nickName' is equal to 'username'
nick_name = Attribute(
    name="nickName",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

profile_url = Attribute(
    name="profileUrl",
    issuer=AttributeIssuer.BOTH,
    type_=at.ExternalReference,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

title = Attribute(
    name="title",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

user_type = Attribute(
    name="userType",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: write proper validator for this field according to: https://www.rfc-editor.org/rfc/rfc7231#section-5.3.5
preferred_language = Attribute(
    name="preferredLanguage",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: write proper validator for this field according to: https://www.rfc-editor.org/rfc/rfc7231#section-5.3.5
locale = Attribute(
    name="locale",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: write proper validator for this field according to: https://www.rfc-editor.org/rfc/rfc6557 ("Olson")
timezone = Attribute(
    name="locale",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

active = Attribute(
    name="locale",
    issuer=AttributeIssuer.BOTH,
    type_=at.Boolean,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: make password preparation according to https://www.rfc-editor.org/rfc/rfc7644#section-7.8
password = Attribute(
    name="password",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.WRITE_ONLY,
    returned=AttributeReturn.NEVER,
    uniqueness=AttributeUniqueness.NONE,
)

_email_value = Attribute(
    name="value",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_email_display = Attribute(
    name="display",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_email_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    canonical_values=["work", "home", "other"],
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_email_primary = Attribute(
    name="primary",
    issuer=AttributeIssuer.BOTH,
    type_=at.Boolean,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

emails = ComplexAttribute(
    sub_attributes=[
        _email_value,
        _email_type,
        _email_display,
        _email_primary,
    ],
    name="emails",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
    validators=[validate_single_primary_value],
)

# TODO: make proper validation (warn) according to RFC3966 https://datatracker.ietf.org/doc/html/rfc3966
_phone_number_value = Attribute(
    name="value",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_phone_number_display = Attribute(
    name="display",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_phone_number_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    canonical_values=["work", "home", "mobile", "fax", "pager", "other"],
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_phone_number_primary = Attribute(
    name="primary",
    issuer=AttributeIssuer.BOTH,
    type_=at.Boolean,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

phone_numbers = ComplexAttribute(
    sub_attributes=[
        _phone_number_value,
        _phone_number_type,
        _phone_number_display,
        _phone_number_primary,
    ],
    name="phoneNumbers",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
    validators=[validate_single_primary_value],
)

# TODO: warn if value contain whitespaces and isn't lowercase
_ims_value = Attribute(
    name="value",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_ims_display = Attribute(
    name="display",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# no canonical values included, as those presented in RFC 7643 are obsolete and does not contain modern tools
_ims_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_ims_primary = Attribute(
    name="primary",
    issuer=AttributeIssuer.BOTH,
    type_=at.Boolean,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

ims = ComplexAttribute(
    sub_attributes=[
        _ims_value,
        _ims_type,
        _ims_display,
        _ims_primary,
    ],
    name="ims",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
    validators=[validate_single_primary_value],
)

_photos_value = Attribute(
    name="value",
    issuer=AttributeIssuer.BOTH,
    type_=at.ExternalReference,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_photos_display = Attribute(
    name="display",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_photos_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    canonical_values=["photo", "thumbnail"],
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_photos_primary = Attribute(
    name="primary",
    issuer=AttributeIssuer.BOTH,
    type_=at.Boolean,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

photos = ComplexAttribute(
    sub_attributes=[
        _photos_value,
        _photos_type,
        _photos_display,
        _photos_primary,
    ],
    name="photos",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
    validators=[validate_single_primary_value],
)

_addresses_formatted = Attribute(
    name="formatted",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_addresses_street_address = Attribute(
    name="streetAddress",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_addresses_locality = Attribute(
    name="locality",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_addresses_region = Attribute(
    name="region",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_addresses_postal_code = Attribute(
    name="postalCode",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: validate according to ISO 3166-1 "alpha-2"
_addresses_country = Attribute(
    name="country",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_addresses_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    canonical_values=["work", "home", "other"],
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

addresses = ComplexAttribute(
    sub_attributes=[
        _addresses_formatted,
        _addresses_locality,
        _addresses_street_address,
        _addresses_region,
        _addresses_postal_code,
        _addresses_country,
        _addresses_type,
    ],
    name="addresses",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

# TODO: make validation of correct group id here
_groups_value = Attribute(
    name="value",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_ONLY,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_groups_ref = Attribute(
    name="$ref",
    issuer=AttributeIssuer.BOTH,
    type_=at.SCIMReference,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_ONLY,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_groups_display = Attribute(
    name="display",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_ONLY,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_groups_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    canonical_values=["direct", "indirect"],
    multi_valued=False,
    mutability=AttributeMutability.READ_ONLY,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

groups = ComplexAttribute(
    sub_attributes=[
        _groups_value,
        _groups_ref,
        _groups_display,
        _groups_type,
    ],
    name="groups",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_entitlements_value = Attribute(
    name="value",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_entitlements_display = Attribute(
    name="display",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_entitlements_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_entitlements_primary = Attribute(
    name="primary",
    issuer=AttributeIssuer.BOTH,
    type_=at.Boolean,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

entitlements = ComplexAttribute(
    sub_attributes=[
        _entitlements_value,
        _entitlements_display,
        _entitlements_type,
        _entitlements_primary,
    ],
    name="entitlements",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
    validators=[validate_single_primary_value],
)

_roles_value = Attribute(
    name="value",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_roles_display = Attribute(
    name="display",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_roles_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_roles_primary = Attribute(
    name="primary",
    issuer=AttributeIssuer.BOTH,
    type_=at.Boolean,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

roles = ComplexAttribute(
    sub_attributes=[
        _roles_value,
        _roles_display,
        _roles_type,
        _roles_primary,
    ],
    name="roles",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
    validators=[validate_single_primary_value],
)

_x509_certificates_value = Attribute(
    name="value",
    issuer=AttributeIssuer.BOTH,
    type_=at.Binary,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_x509_certificates_display = Attribute(
    name="display",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_x509_certificates_type = Attribute(
    name="type",
    issuer=AttributeIssuer.BOTH,
    type_=at.String,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

_x509_certificates_primary = Attribute(
    name="primary",
    issuer=AttributeIssuer.BOTH,
    type_=at.Boolean,
    required=False,
    case_exact=False,
    multi_valued=False,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
)

x509_certificates = ComplexAttribute(
    sub_attributes=[
        _x509_certificates_value,
        _x509_certificates_display,
        _x509_certificates_type,
        _x509_certificates_primary,
    ],
    name="x509_certificates",
    issuer=AttributeIssuer.BOTH,
    required=False,
    case_exact=False,
    multi_valued=True,
    mutability=AttributeMutability.READ_WRITE,
    returned=AttributeReturn.DEFAULT,
    uniqueness=AttributeUniqueness.NONE,
    validators=[validate_single_primary_value],
)
