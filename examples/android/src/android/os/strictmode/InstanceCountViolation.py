from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstanceCountViolation"]

class InstanceCountViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/InstanceCountViolation"
    getNumberOfInstances = JavaMethod("()J")