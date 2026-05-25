from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DevicePolicyResources"]

class DevicePolicyResources(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/DevicePolicyResources"
    UNDEFINED = JavaStaticField("Ljava/lang/String;")