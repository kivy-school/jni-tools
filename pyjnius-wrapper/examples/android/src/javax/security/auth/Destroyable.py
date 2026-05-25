from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Destroyable"]

class Destroyable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/Destroyable"
    destroy = JavaMethod("()V")
    isDestroyed = JavaMethod("()Z")