"""
Definition of models using Pydantic.
"""

import json
from typing import List, Optional
from pydantic import BaseModel, UUID4


class Parameter(BaseModel):
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        parameter_type: Optional[str] = None,
        min: Optional[float] = None,
        max: Optional[float] = None,
        value: Optional[float] = None,
    ):
        self.uuid: UUID4
        self.name = name
        self.description = description
        self.parameter_type = (parameter_type,)
        self.min = (min,)
        self.max = (max,)
        self.value = value

    def __repr__(self):
        return "<Parameter: name=%s, description=%s>" % (self.name, self.description)


class Stakeholder(BaseModel):
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        role: Optional[str] = None,
        organization: Optional[str] = None,
    ):
        self.uuid: UUID4
        self.name = name
        self.description = description
        self.role = role
        self.organization = organization

    def __repr__(self):
        """docstring"""
        return "<Stakeholder: name=%s, description=%s, role=%s, organization=%s>" % (
            self.name,
            self.description,
            self.role,
            self.organization,
        )


class Expectation(BaseModel):
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        stakeholder: Optional[str] = None,
        category: Optional[str] = None,
        parameter: Optional[Parameter] = None,
    ):
        self.uuid: UUID4
        self.name = name
        self.description = description
        self.stakeholder = stakeholder
        self.category = category
        self.parameter = parameter

    def __repr__(self):
        return (
            "<Expectation: name=%s, description=%s, stakeholder=%s, category=%s, uuid=%s>"
            % (self.name, self.description, self.stakeholder, self.category, self.uuid)
        )


class Need(BaseModel):
    def __init__(self, name, description=None, stakeholder=None, category=None):
        self.uuid: UUID4
        self.name = name
        self.description = description
        self.stakeholder = stakeholder
        self.category = category

    def __repr__(self):
        return (
            "<Need: name=%s, description=%s, stakeholder=%s, category=%s, uuid=%s>"
            % (self.name, self.description, self.stakeholder, self.category, self.uuid)
        )


class NeedCategory(BaseModel):
    def __init__(self, name, description=None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<NeedCategory= name=%s, description=%s>" % (self.name, self.description)


class ValueDriver(BaseModel):
    def __init__(self, name, description=None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ValueDriver: name=%s, description=%s>" % (self.name, self.description)


class DesignSolution(BaseModel):
    def __init__(self, name, description=None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<DesignSolution: name=%s, description=%s>" % (
            self.name,
            self.description,
        )


class FunctionalRequirement(BaseModel):
    def __init__(self, name, description=None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<FunctionalRequirement: name=%s, description=%s>" % (
            self.name,
            self.description,
        )


class Constraint(BaseModel):
    def __init__(self, name, description=None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Constraint: name=%s, description=%s>" % (self.name, self.description)


class ProductProject(BaseModel):
    def __init__(self, name, description=None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ProductProject: name=%s, description=%s>" % (
            self.name,
            self.description,
        )


class ConfigurableComponent(BaseModel):
    def __init__(self, name, description=None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<ConfigurableComponent: name=%s, description=%s>" % (
            self.name,
            self.description,
        )


class Interaction(BaseModel):
    def __init__(self, category, origin, target):
        self.uuid: UUID4
        self.category = category
        self.origin = origin
        self.target = target

    def __repr__(self):
        return "<Interaction: category=%s, origin=%s, target=%s>" % (
            self.category,
            self.origin,
            self.target,
        )


class Platform(BaseModel):
    def __init__(self, name: str, description: Optional[str] = None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Platform: name=%s, description=%s>" % (self.name, self.description)


class Product(BaseModel):
    def __init__(self, name: str, description: Optional[str] = None):
        self.uuid: UUID4
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Product: name=%s, description=%s>" % (self.name, self.description)

def main() -> None:
    """Main function."""

    # Read data from a JSON file
    with open("./data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        # print(books)
        print(books[0])
        # print(books[0].dict(exclude={"price"}))
        # print(books[1].copy())


if __name__ == "__main__":
    main()
