
class TreeConstraintException(Exception):
    """When tree constraints are violated"""
    def __init__(self, obj, fault_msg):
        msg = "'%s' violates tree constraint" % obj.__class__.__name__
        if fault_msg:
            msg += " due to '%s'" % fault_msg
            self.message = "%s." % msg

    def __str__(self):
        return self.message


class TreeCyclicException(TreeConstraintException):
    """When cycle is detect in tree"""
    def __init__(self, root, node, fault_msg=None):
        self.fault_msg = fault_msg
        if not self.fault_msg:
            self.fault_msg = "Non-cyclic constraint violated when attempting \
                              to add '%s' to tree rooted at '%s'" % (node, root)
        super().__init__(obj=node, fault_msg=fault_msg)
