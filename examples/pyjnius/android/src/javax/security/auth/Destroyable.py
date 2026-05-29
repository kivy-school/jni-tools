from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Destroyable"]

class Destroyable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/Destroyable"
    isDestroyed = JavaMethod("()Z")
    destroy = JavaMethod("()V")