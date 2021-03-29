#!/usr/bin/env python
import uuid


class Model():

    def __init__(self):
        pass


class Stakeholder:
    def __init__(self,
                 name: str,
                 description: str = None,
                 role: str = None,
                 organization: str = None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description
        self.role = role
        self.organization = organization

    def __repr__(self):
        return "<Stakeholder: name=%s, description=%s, role=%s, organization=%s>" % (self.name, self.description, self.role, self.organization)


class Expectation:
    def __init__(self,
                 name,
                 description=None,
                 stakeholder=None,
                 category=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description
        self.stakeholder = stakeholder
        self.category = category

    def __repr__(self):
        return "<Expectation: name=%s, description=%s, stakeholder=%s, category=%s, uuid=%s>" % (self.name, self.description, self.stakeholder, self.category, self.uuid)


class Need:
    def __init__(self,
                 name,
                 description=None,
                 stakeholder=None,
                 category=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description
        self.stakeholder = stakeholder
        self.category = category

    def __repr__(self):
        return "<Need: name=%s, description=%s, stakeholder=%s, category=%s, uuid=%s>" % (self.name, self.description, self.stakeholder, self.category, self.uuid)


class NeedCategory:
    def __init__(self,
                 name,
                 description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<NeedCategory= name=%s, description=%s>" % (self.name, self.description)


class ValueDriver:
    def __init__(self,
                 name,
                 description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ValueDriver: name=%s, description=%s>" % (self.name, self.description)


class DesignSolution:
    def __init__(self,
                 name,
                 description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<DesignSolution: name=%s, description=%s>" % (self.name, self.description)


class FunctionalRequirement:
    def __init__(self,
                 name,
                 description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<FunctionalRequirement: name=%s, description=%s>" % (self.name, self.description)


class Constraint:
    def __init__(self,
                 name,
                 description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Constraint: name=%s, description=%s>" % (self.name, self.description)


class ProductProject:
    def __init__(self,
                 name,
                 description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ProductProject: name=%s, description=%s>" % (self.name, self.description)


class ConfigurableComponent:
    def __init__(self,
                 name,
                 description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ConfigurableComponent: name=%s, description=%s>" % (self.name, self.description)


class Parameter:
    def __init__(self,
                 name,
                 description=None,
                 parameter_type=None,
                 min=None,
                 max=None,
                 value=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description
        self.parameter_type = parameter_type,
        self.min = min,
        self.max = max,
        self.value = value

    def __repr__(self):
        return "<Parameter: name=%s, description=%s>" % (self.name, self.description)


class Interaction:
    def __init__(self,
                 category,
                 origin,
                 target):
        self.uuid = uuid.uuid4()
        self.category = category
        self.origin = origin
        self.target = target

    def __repr__(self):
        return "<Interaction: category=%s, origin=%s, target=%s>" % (self.category, self.origin, self.target)


class Platform:
    def __init__(self,
                 name,
                 description=None):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Platform: name=%s, description=%s>" % (self.name, self.description)


def main():
    pass


if __name__ == "__main__":
    main()
