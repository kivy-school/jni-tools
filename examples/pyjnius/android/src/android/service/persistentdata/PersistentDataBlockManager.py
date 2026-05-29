from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PersistentDataBlockManager"]

class PersistentDataBlockManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/persistentdata/PersistentDataBlockManager"
    isFactoryResetProtectionActive = JavaMethod("()Z")