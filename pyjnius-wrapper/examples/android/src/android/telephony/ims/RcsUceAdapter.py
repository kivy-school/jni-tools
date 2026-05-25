from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RcsUceAdapter"]

class RcsUceAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/RcsUceAdapter"
    isUceSettingEnabled = JavaMethod("()Z")