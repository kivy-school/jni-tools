from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellLocation"]

class CellLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellLocation"
    __javaconstructor__ = [("()V", False)]
    getEmpty = JavaStaticMethod("()Landroid/telephony/CellLocation;")
    requestLocationUpdate = JavaStaticMethod("()V")