from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BuildConfig"]

class BuildConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/BuildConfig"
    __javaconstructor__ = [("()V", False)]
    DEBUG = JavaStaticField("Z")
    LIBRARY_PACKAGE_NAME = JavaStaticField("Ljava/lang/String;")
    BUILD_TYPE = JavaStaticField("Ljava/lang/String;")