from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemFonts"]

class SystemFonts(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/SystemFonts"
    getAvailableFonts = JavaStaticMethod("()Ljava/util/Set;")