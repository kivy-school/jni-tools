from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceNotAssociatedException"]

class DeviceNotAssociatedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/DeviceNotAssociatedException"