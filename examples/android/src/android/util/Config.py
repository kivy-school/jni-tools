from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Config"]

class Config(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Config"
    DEBUG = JavaStaticField("Z")
    LOGD = JavaStaticField("Z")
    LOGV = JavaStaticField("Z")
    PROFILE = JavaStaticField("Z")
    RELEASE = JavaStaticField("Z")