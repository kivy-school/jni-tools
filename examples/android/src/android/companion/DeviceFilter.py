from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceFilter"]

class DeviceFilter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/DeviceFilter"