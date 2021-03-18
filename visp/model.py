#!/usr/bin/env python
import uuid


class Model():

    def __init__(self):
        pass


class Stakeholder:
    def __init__(self,
                 name,
                 description,
                 role,
                 organization):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description
        self.role = role
        self.organization = organization

    def __repr__(self):
        return "<Stakeholder: name=%s, description=%s, role=%s, organization:%s>" % (self.name, self.description, self.role, self.organization)


class Need:
    def __init__(self,
                 name,
                 description,
                 stakeholder,
                 category):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description
        self.stakeholder = stakeholder
        self.category = category

    def __repr__(self):
        return "<Need: name=%s, description=%s, stakeholder:%s, category:%s, uuid:%s>" % (self.name, self.description, self.stakeholder, self.category, self.uuid)


class NeedCategory:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<NeedCategory: name=%s, description=%s>" % (self.name, self.description)


class ValueDriver:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ValueDriver: name=%s, description=%s>" % (self.name, self.description)


class Designsolution:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Designsolution: name=%s, description=%s>" % (self.name, self.description)


class FunctionalRequirement:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<FunctionalRequirement: name=%s, description=%s>" % (self.name, self.description)


class Constraint:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Constraint: name=%s, description=%s>" % (self.name, self.description)


class ProductProject:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ProductProject: name=%s, description=%s>" % (self.name, self.description)


class ConfigurableComponent:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ConfigurableComponent: name=%s, description=%s>" % (self.name, self.description)


class Parameter:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Parameter: name=%s, description=%s>" % (self.name, self.description)


class Interaction:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Interaction: name=%s, description=%s>" % (self.name, self.description)


class Platform:
    def __init__(self,
                 name,
                 description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Platform: name=%s, description=%s>" % (self.name, self.description)


def main():
    pass


if __name__ == "__main__":
    main()
