from plone.app.content.interfaces import INameFromTitle

class INameForRelease(INameFromTitle):

    def title():
        """Return a custom title for a release"""



class INameForLinkedRelease(INameFromTitle):

    def title():
        """Return a custom title for a linked release"""
