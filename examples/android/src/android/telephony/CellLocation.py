from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellLocation"]

class CellLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellLocation"
    __javaconstructor__ = [("()V", False)]
    requestLocationUpdate = JavaStaticMethod("()V")
    getEmpty = JavaStaticMethod("()Landroid/telephony/CellLocation;")