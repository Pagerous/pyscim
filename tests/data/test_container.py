import pytest

from src.data.container import AttrRep, Missing, SCIMDataContainer


@pytest.mark.parametrize(
    ("attr_rep", "expected"),
    (
        (AttrRep(attr="id"), "2819c223-7f76-453a-919d-413861904646"),
        (
            AttrRep(schema="urn:ietf:params:scim:schemas:core:2.0:User", attr="userName"),
            "bjensen@example.com",
        ),
        (
            AttrRep(attr="userName"),
            "bjensen@example.com",
        ),
        (
            AttrRep(attr="meta", sub_attr="resourceType"),
            "User",
        ),
        (
            AttrRep(attr="name", sub_attr="givenName"),
            "Barbara",
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:core:2.0:User",
                attr="name",
                sub_attr="familyName",
            ),
            "Jensen",
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:core:2.0:User",
                attr="name",
                sub_attr="familyName",
            ),
            "Jensen",
        ),
        (
            AttrRep(
                attr="emails",
                sub_attr="type",
            ),
            ["work", "home"],
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
                attr="employeeNumber",
            ),
            "1",
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
                attr="manager",
                sub_attr="displayName",
            ),
            "John Smith",
        ),
    ),
)
def test_value_from_scim_data_container_can_be_retrieved(attr_rep, expected, user_data_dump):
    actual = SCIMDataContainer(user_data_dump)[attr_rep]

    assert actual == expected


@pytest.mark.parametrize(
    ("attr_rep", "value", "expected"),
    (
        (
            AttrRep(attr="id"),
            "2819c223-7f76-453a-919d-413861904646",
            {"id": "2819c223-7f76-453a-919d-413861904646"},
        ),
        (
            AttrRep(schema="urn:ietf:params:scim:schemas:core:2.0:User", attr="userName"),
            "bjensen@example.com",
            {"userName": "bjensen@example.com"},
        ),
        (
            AttrRep(attr="userName"),
            "bjensen@example.com",
            {"userName": "bjensen@example.com"},
        ),
        (
            AttrRep(attr="meta", sub_attr="resourceType"),
            "User",
            {"meta": {"resourceType": "User"}},
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:core:2.0:User",
                attr="meta",
                sub_attr="resourceType",
            ),
            "User",
            {"meta": {"resourceType": "User"}},
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:core:2.0:User",
                attr="emails",
                sub_attr="type",
            ),
            ["work", "home"],
            {"emails": [{"type": "work"}, {"type": "home"}]},
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:core:2.0:User",
                attr="emails",
                sub_attr="type",
            ),
            [Missing, "home"],
            {"emails": [{}, {"type": "home"}]},
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
                attr="employeeNumber",
                extension=True,
            ),
            "701984",
            {
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                    "employeeNumber": "701984"
                }
            },
        ),
        (
            AttrRep(
                schema="urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
                attr="manager",
                sub_attr="displayName",
                extension=True,
            ),
            "John Smith",
            {
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                    "manager": {"displayName": "John Smith"}
                }
            },
        ),
    ),
)
def test_value_can_be_inserted_to_scim_data_container(attr_rep, value, expected):
    container = SCIMDataContainer()

    container[attr_rep] = value

    assert container.to_dict() == expected


def test_attr_value_in_container_can_be_reassigned():
    container = SCIMDataContainer()
    container["key"] = 123

    container["KEY"] = 456

    assert container["key"] == 456


def test_sub_attr_value_in_container_can_be_reassigned():
    container = SCIMDataContainer()
    container["key.subkey"] = 123

    container["KEY.SUBKEY"] = 456

    assert container["key.subkey"] == 456


def test_sub_attr_bigger_list_value_in_container_can_be_reassigned():
    container = SCIMDataContainer()
    container["key.subkey"] = [1, 2]

    container["KEY.SUBKEY"] = [4, 5, 6]

    assert container["key.subkey"] == [4, 5, 6]


def test_sub_attr_smaller_list_value_in_container_can_be_reassigned():
    container = SCIMDataContainer()
    container["key.subkey"] = [1, 2, 3]

    container["KEY.SUBKEY"] = [4, 5]

    assert container["key.subkey"] == [4, 5, 3]


def test_assigning_sub_attr_to_non_complex_attr_fails():
    container = SCIMDataContainer()
    container["key"] = 1

    with pytest.raises(KeyError, match=r"can not assign \(subkey, \[1, 2, 3\]\) to 'key'"):
        container["key.subkey"] = [1, 2, 3]
