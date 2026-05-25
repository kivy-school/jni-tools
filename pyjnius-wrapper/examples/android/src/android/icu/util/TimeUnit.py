from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeUnit"]

class TimeUnit(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/TimeUnit"
    values = JavaStaticMethod("()[Landroid/icu/util/TimeUnit;")