from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntentReceiverLeakedViolation"]

class IntentReceiverLeakedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/IntentReceiverLeakedViolation"