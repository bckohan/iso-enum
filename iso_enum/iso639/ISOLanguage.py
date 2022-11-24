"""The standard enum type for ISO 639-1 common languages"""
from enum_properties import (
    EnumProperties,
    s
)


class ISOLanguage(
    EnumProperties,
    s('english', case_fold=True),
    s('french', case_fold=True),
    s('indigenous', case_fold=True)
):
    """
    An enumeration for ISO 639-1 language codes.
    """

    AB = "ab", ["Abkhazian", "Abkhaz", ], ["abkhaze", "abkhazien", ], ["apsua byszwa", ]
    OM = "om", ["Afan Oromo", "Oromo", "Galla", ], ["oromo", "afan oromo", "galla", ], ["(afan) oromo", ]
    AA = "aa", ["Afar", ], ["afar", ], ["afar", ]
    AF = "af", ["Afrikaans", ], ["afrikaans", ], ["Afrikaans", ]
    # pylint: disable=C0303
    @property
    def en(self):
        """The most common english name for this language"""
        return self.english[0]

    @property
    def fr(self):
        """The most common french name for this language"""
        return self.french[0]

    @property
    def ind(self):
        """The most common indigenous name for this language"""
        return self.indigenous[0]

    @property
    def identifier(self):
        """An alias for the alpha-2 code"""
        return self.value

    @property
    def code(self):
        """An alias for the alpha-2 code"""
        return self.value

    def __str__(self):
        """
        The string representation of this enum is its alpha-2 language code
        """
        return self.value
