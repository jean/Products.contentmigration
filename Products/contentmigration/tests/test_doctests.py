import unittest

from zope.testing.doctest import ELLIPSIS

from Testing.ZopeTestCase import ZopeDocFileSuite

from Products.contentmigration.tests.cmtc import ContentMigratorTestCase

def test_suite():
    suites = (
        ZopeDocFileSuite(
            '../inplace.txt',
            '../translocate.txt',
            '../archetypes.txt',
            package='Products.contentmigration.tests',
            optionflags=ELLIPSIS,
            test_class=ContentMigratorTestCase),
        )

    from unittest import TestSuite
    return TestSuite(suites)

if __name__ == "__main__":
    unittest.main(defaultTest='test_suite')