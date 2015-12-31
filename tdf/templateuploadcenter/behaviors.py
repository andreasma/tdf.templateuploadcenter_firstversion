from zope.interface import implements
from tdf.templateuploadcenter.interfaces import INameForRelease


class NameForRelease(object):
    """ Adapter to INameFromTitle
    """

    implements(INameForRelease)

    def __init__(self, context):
        self.context = context

    def __new__(cls, context):
        releasenumber = context.releasenumber
        title = u'%s' % (releasenumber)
        releasename = super(NameForRelease, cls).__new__(cls)
        releasename.title = title
        return releasename
